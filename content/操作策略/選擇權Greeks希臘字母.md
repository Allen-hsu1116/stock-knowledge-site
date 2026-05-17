# 選擇權Greeks希臘字母

> 選擇權的「風險儀表板」——Delta是時速表、Gamma是加速度、Theta是漏油量、Vega是路況，看懂這四個字母才能從盲目賭博變成精準操作

## 核心概念

Greeks（希臘字母）是選擇權定價模型（BSM Model）算出來的風險參數，量化選擇權策略對不同風險的曝險程度。搞懂 Greeks 讓交易策略從單一維度（只看漲跌）提升到多維度（方向+時間+波動率+加速度），交易機會更多、風險控制更好。

### Delta：時速表（方向敏感度）

- **定義**：標的價格變動 1 單位，選擇權價格變動 Delta 單位
- **範圍**：Call 0~+1，Put -1~0
- **實戰判讀**：
  - 深價外 (OTM) Delta ≈ 0.1：大盤漲 100 點，權利金只漲 10 點，像騎腳踏車
  - 價平 (ATM) Delta ≈ 0.5：大盤漲 100 點，權利金漲 50 點，一般轎車
  - 深價內 (ITM) Delta ≈ 1.0：大盤漲 100 點，權利金漲 100 點，跟期貨同步
- **Delta 也是 ITM 機率**：Delta 0.75 ≈ 75% 機率到期時在價內
- **四大基本策略 Delta**：
  - Buy Call：正 Delta，看多
  - Buy Put：負 Delta，看空
  - Sell Call：負 Delta，看空
  - Sell Put：正 Delta，看多

### Gamma：加速度（Delta 的變化率）

- **定義**：標的價格變動 1 單位，Delta 變動 Gamma 單位
- **特性**：ATM Gamma 最大；越接近到期日 Gamma 越大
- **買方 (Long Gamma)**：看對方向，Gamma 幫你踩油門，Delta 從 0.5→0.6→0.7，賺錢速度越來越快
- **賣方 (Short Gamma)**：看錯方向，Gamma 加速虧損，賠錢速度像失速列車
- **Gamma Squeeze**：GameStop 事件就是散戶利用 Gamma Squeeze 讓機構爆倉
- **到期風險**：接近到期日時 Gamma 急速放大（6天到期 Gamma 可達 35天到期的 2.7 倍），通常在到期前 14 天平倉降低 Gamma 風險

### Theta：漏油量（時間衰減）

- **定義**：每過一天，選擇權價值衰減多少
- **方向**：買方 Theta 永遠為負（時間是敵人），賣方 Theta 永遠為正（時間是朋友）
- **衰減特性**：
  - 90 天以上到期：Theta 衰減緩慢
  - 30 天以下到期：Theta 衰減加速
  - 越接近到期日扣血越快，特別是價平選擇權
- **實戰**：賣方通常賣 30 天左右到期的選擇權，讓 Theta 衰減夠快獲利了結

### Vega：路況（波動率敏感度）

- **定義**：隱含波動率 (IV) 變動 1%，權利金變動 Vega 單位
- **特性**：到期日越遠，Vega 越大
- **高低 IV 影響**：
  - SPY（IV 19%）ATM Call 價值 $9.38
  - MDB（IV 55%）ATM Call 價值 $34.50
  - 同樣價位的標的，IV 越高權利金越貴
- **實戰方向**：
  - Buy options：正 Vega，IV 擴張時獲利
  - Sell options：負 Vega，IV 收縮時獲利

## 實戰應用

### Greeks 四大策略曝險對照表

| 策略 | Delta | Gamma | Vega | Theta |
|------|-------|-------|------|-------|
| Buy Call | + | + | + | - |
| Buy Put | - | + | + | - |
| Sell Call | - | - | - | + |
| Sell Put | + | - | - | + |

### 買方 vs 賣方 Greeks 建議

| 希臘字母 | 買方建議 | 賣方建議 |
|---------|---------|---------|
| Delta | 不要選太價外（Delta 太小跑不快） | Delta 中性避險 |
| Gamma | 享受貼背感（方向對加速獲利） | 最怕 Gamma！需嚴控風險 |
| Theta | 速戰速決（時間是敵人） | 跟時間做朋友 |
| Vega | IV 由小變大時獲利 | IV 大時保費貴但小心翻車 |

### 多維度策略範例：時間價差

市場判斷：短期看不跌、長期看跌
策略：相同履約價賣出短期 Put、買入長期 Put
Greeks 效果：正 Gamma + 正 Vega + 正 Theta，Delta = 0（不判斷方向）

兩種思考模式：
1. **價格角度**：Sell Put 短線不跌破履約價賺保證金，Buy Put 長線跌破賺價差
2. **Greeks 角度**：短期 IV 下降 Theta 偏賺、Vega 偏虧但損益不明顯；中期暴跌時 Vega + Theta 雙賺

### 賣 Strangle 篩選條件

- DTE > 30（安全的 Theta 衰減）
- IV Percentile > 67%（IV 偏高有收縮空間，Vega 有利）
- Open Interest > 100,000（流動性好）
- Market Cap > $10B（避免被操控）
- Squeeze = False（避免 IV 即將擴張）
- Strangle BP < $1000（分散風險）

## 注意事項

1. **Delta 不是概率**：雖然 Delta 可以近似 ITM 機率，但這只是理論值，實際機率受波動率和時間影響
2. **Gamma 是賣方的死神**：Short Gamma 在劇烈波動時虧損呈非線性放大，賣方必須嚴格控制 Gamma 風險
3. **Theta 衰減非線性**：越接近到期日衰減越快，買方拖到最後一刻等於把時間價值全部浪費掉
4. **Vega 和 Theta 是一體兩面**：賣方收的權利金本質上是「承擔 Vega 風險的補償」，Theta 越大 = Vega 風險越大
5. **Greeks 隨時在變**：Greeks 不是固定數字，會隨標的價格、時間、IV 變化而動態調整
6. **忽略 Rho**：利率變化對選擇權定價影響極小，實戰中通常忽略
7. **接近到期 Gamma 爆炸**：到期前最後幾天 Gamma 急速放大，6天到期的 Gamma 可能是 35天的 2.7 倍，必須提前平倉

## 相關主題

- [[選擇權四大基本策略]]
- [[選擇權組合策略]]
- [[選擇權Greeks希臘字母]]
- [[選擇權Greeks希臘字母]]
- [[隱含波動率IV判讀]]
- [[VIX恐慌指數實戰判讀]]
- [[時間價差Calendar-Spread]]
- [[選擇權Greeks希臘字母]]
- [[Theta時間衰減實戰]]
- [[Black-Scholes定價模型]]
- [[選擇權Convexity凸性與非對稱收益Option-Convexity]]

## 來源

- [OP凱文-選擇權Greeks風險儀表板](../raw/2026-04-30/OP凱文-選擇權Greeks風險儀表板.md)
- [BlockTempo-Greeks多維度策略](../raw/2026-04-30/BlockTempo-Greeks多維度策略.md)
- [SlashTraders-Greeks風險管控](../raw/2026-04-30/SlashTraders-Greeks風險管控.md)
- [OP凱文-Greeks風險儀表板(2026-05-10)](../raw/2026-05-10/Greeks基礎-Delta-Gamma-Vega-Theta開車比喻.md)
- [SlashTraders-Greeks風險管控(2026-05-10)](../raw/2026-05-10/Greeks基礎-Delta-Gamma-Vega-Theta斜槓投資達人.md)
- [Anton Cheng-選擇權的定價與避險參數](../raw/2026-05-10/Greeks進階-選擇權定價與避險參數.md)
- [BlockTempo-Greeks多維度策略(2026-05-10)](../raw/2026-05-10/Greeks多維度策略與實戰範例.md)