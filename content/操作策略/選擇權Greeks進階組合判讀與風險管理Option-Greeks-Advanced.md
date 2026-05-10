# 選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced

> 單看 Greeks 只是一維風險，組合判讀才是多維雷達——Delta-Gamma 看加速度、Vega-Theta 看時間與波動對賭、四大 Greeks 矩陣選策略、風險限額控管活下來

## 核心概念

Greeks 進階不是學更多公式，而是**把四個字母放在一起看**，理解它們之間的交互作用。單一 Greek 告訴你「一個維度的風險」，組合判讀告訴你「整體部位的風險輪廓」。

### Delta-Gamma 二維判讀

Delta 告訴你「現在的敏感度」，Gamma 告訴你「敏感度正在怎麼變化」。

**關鍵公式**：新 Delta ≈ 舊 Delta + Gamma × 價格變動量

- 大盤 20000，ATM Call Delta=0.5, Gamma=0.005
- 大盤漲 100 點 → 新 Delta ≈ 0.5 + 0.005×100 ≈ 0.55
- 這就是「Delta 跑起來了」——買方越賺越快，Gamma 幫你踩油門

**Delta-Gamma 矩陣**：

| 位置 | Delta | Gamma | 解讀 |
|------|-------|-------|------|
| 深價內 | ≈1.0 | 極小 | 像期貨，方向確定但加速空間有限 |
| 價平 | ≈0.5 | 最大 | 加速最快，方向不確定但爆發力最強 |
| 深價外 | ≈0.1 | 極小 | 便宜但需要大波動才能啟動 |

### Delta-Theta 對沖思維

Delta 和 Theta 是選擇權最核心的「付費 vs 收租」對抗：

- **正 Delta + 負 Theta**：買方策略——方向對賺價差、時間流逝扣成本
- **負 Delta + 正 Theta**：賣方策略——收時間價值但方向錯虧價差
- **Delta Neutral + 正 Theta**：中性賣方——不管漲跌只收時間價值
- **Delta Neutral + 負 Theta**：中性買方——賭波動率擴張

**Theta/Gamma 比值是賣方生存指標**：
- 比值 > 1：賣方有利，時間價值收入 > Gamma 風險
- 比值 < 1：賣方不利，Gamma 風險 > Theta 收入
- 高 IV 環境 Theta 夠大足以覆蓋 Gamma 風險，這就是賣方偏好高 IV 的原因

### Vega-Theta 共同判讀

Vega 和 Theta 同源於時間價值，是一體兩面：

- **IV 擴張**：Vega 正的部位獲利，但 Theta 同時扣時間價值
- **IV 收縮**：Vega 正的部位虧損，Theta 也加速扣時間價值——雙殺
- **賣方甜蜜點**：IV 收縮 + 時間衰減，Vega 和 Theta 雙賺

**IV Percentile 導向策略**：

| IV Percentile | 策略方向 | Vega | Theta | 說明 |
|--------------|---------|------|-------|------|
| > 70%（高） | 賣方策略 | 負 | 正 | IV收縮+時間衰減雙賺 |
| 30-70%（中） | 組合策略 | 視方向 | 視策略 | 需要方向判斷輔助 |
| < 30%（低） | 買方策略 | 正 | 負 | 低IV買權利金便宜，賭IV擴張 |

### 四大 Greeks 組合策略矩陣

| 策略 | Delta | Gamma | Vega | Theta | 適用情境 |
|------|-------|-------|------|-------|---------|
| 買 ATM Call | +0.5 | + | + | - | 看多+波動率低 |
| 買 ATM Put | -0.5 | + | + | - | 看空+波動率低 |
| 賣 ATM Call | -0.5 | - | - | + | 看空+波動率高 |
| 賣 ATM Put | +0.5 | - | - | + | 看多+波動率高 |
| 買 Straddle | 0 | ++ | ++ | -- | 不看方向+波動率低 |
| 賣 Straddle | 0 | -- | -- | ++ | 不看方向+波動率高 |
| 鐵兀鷹 | 0 | -- | -- | + | 不看方向+波動率高+限風險 |
| 買日曆價差 | 0 | + | + | + | 不看方向+低IV+收Theta |

## 實戰應用

### Delta Neutral 動態調整

Delta Neutral 不是設好就忘，需要持續 Rebalance：

1. **觸發調整條件**：|Portfolio Delta| > 門檻值（通常為總部位風險的 5-10%）
2. **調整方式**：
   - 買/賣標的（期貨或現貨）——最直接，只影響 Delta
   - 買/賣選擇權——同時影響其他 Greeks
   - 調整履約價或到期日——結構性調整
3. **調整頻率**：越頻繁手續費越高但風險越低

**Gamma Scalping 本質**：在 Delta Neutral 基礎上利用 Gamma 獲利
- 跌時 Buy（Delta 變負）→ 漲時 Sell（Delta 變正）→ 自動低買高賣
- 前提：Gamma 夠大（ATM 或接近到期）+ 波動率夠高
- 詳見 [[Gamma-Scalping波動率利潤引擎]]

### Greeks 風險限額設定

| 參數 | 建議限額 | 計算方式 |
|------|---------|---------|
| Delta | ≤ 帳戶淨值 5% | Delta × 點值 |
| Gamma | 當日最大虧損 ≤ 2% | Gamma × (3%波動)² |
| Vega | ≤ 帳戶淨值 10% | Vega × IV變動5% |
| Theta | 日收入目標 0.5-1% | Theta / 帳戶淨值 |

### 壓力測試情境

| 情境 | 檢查項目 |
|------|---------|
| 標的漲跌 3% | Delta + Gamma 損益 |
| IV 突增 20% | Vega 損益 |
| IV 突降 20% | Vega 損益（反向） |
| 跳空缺口 | Gamma 損益（非連續價格） |
| 黑天鵝（漲跌 10%+） | 全部 Greeks 極端損益 |

### Greeks 對沖優先序

1. **Delta 優先**：方向風險最大，先歸零 Delta
2. **Gamma 其次**：非線性風險，超過門檻必須處理
3. **Vega 第三**：波動率風險，用遠月對沖成本較低
4. **Theta 最後**：時間衰減是可預期的，不需要「對沖」

### 不同市況的 Greeks 策略選擇

| 市況 | 最佳策略 | 最差策略 |
|------|---------|---------|
| 低波動+緩漲 | 買 Call（+Delta,+Vega） | 賣 Put（Vega風險） |
| 低波動+緩跌 | 買 Put（-Delta,+Vega） | 賣 Call（Vega風險） |
| 低波動+盤整 | 買 Straddle（0,+Vega） | 賣 Straddle（0,-Vega） |
| 高波動+急漲 | 賣 Put+買 Call | 買 Put（Vega虧損） |
| 高波動+急跌 | 賣 Call+買 Put | 買 Call（Vega虧損） |
| 高波動+盤整 | 賣 Iron Condor | 買 Straddle（Theta虧損） |

## 進階觀念

### Vanna 和 Charm：二階 Greeks

- **Vanna** = ∂Delta/∂IV = ∂Vega/∂S：IV 變動對 Delta 的影響
  - IV 上升 → 價外 Delta 變大，價內 Delta 變小
  - 暴跌時 Put Delta 加速變大（IV飆升 + 價格下跌雙重效果）

- **Charm** = ∂Delta/∂t：時間流逝對 Delta 的影響
  - 價內 Delta → 1，價外 Delta → 0
  - 賣價外選擇權最後幾天特別安穩的原因

### Greeks 時間演化

| Greek | 趨近到期 | 實戰意義 |
|-------|---------|---------|
| Delta | 價內→1，價外→0 | 越接近到期越兩極化 |
| Gamma | 價平急速放大 | 到期前 Gamma 爆炸 |
| Theta | 價平加速衰減 | 賣方最後幾天 Theta 最大 |
| Vega | 逐漸縮小 | 遠月 Vega 大，近月 Vega 小 |

## 注意事項

1. **Greeks 是瞬時值**：每一秒都在變化，不是靜態數字，需要持續監控和調整
2. **Greeks 交互作用**：Delta 影響 Gamma，Gamma 影響 Delta，Vega 影響 Theta，不能獨立看
3. **理論假設的侷限**：BSM 模型假設連續交易、無跳空、波動率恆定，現實市場充滿斷層
4. **跳空缺口是 Greeks 失效區**：Gap 發生時 Delta 和 Gamma 計算全部失準，壓力測試必須包含極端情境
5. **流動性風險**：Greeks 再漂亮，流動性不足時無法調整部位，理論止損可能無法執行
6. **手續費侵蝕**：頻繁 Rebalance 的手續費可能吃掉 Gamma Scalping 的利潤
7. **模型風險**：Greeks 基於 BSM 模型計算，模型假設與現實的偏差就是風險來源

## 相關主題

- [[選擇權Greeks希臘字母]]
- [[Theta時間衰減實戰]]
- [[逼券商拉抬Gamma-Squeeze兩手策略]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[隱含波動率IV與歷史波動率HV實戰判讀]]
- [[VIX恐慌指數系統性風險監控]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[Black-Scholes定價模型]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[鐵兀鷹Iron-Condor]]
- [[選擇權組合策略]]
- [[選擇權四大基本策略]]
- [[選擇權Convexity凸性與非對稱收益Option-Convexity]]

## 來源

- [選擇權Greeks進階組合判讀與風險管理](../raw/2026-05-10/選擇權Greeks進階組合判讀與風險管理.md)