---
title: "選擇權 Greeks 希臘字母"
category: "操作策略"
created: 2026-05-24
---

# 選擇權 Greeks 希臘字母

> Greeks 是選擇權的「操控面板」——不懂 Greeks 等於蒙著眼睛開跑車

## 核心概念

選擇權的 Greeks（希臘字母）是一組衡量選擇權價格敏感度的指標，每一個希臘字母代表一個影響選擇權價格的風險因子。理解 Greeks 是選擇權交易者的基本功，就像開車必須懂油門、煞車、方向盤。

### 選擇權定價的五個變數

選擇權價格（權利金）由五個變數決定：

1. **標的物價格（S）**→ 衡量指標：**Delta**
2. **履約價（K）**→ 衡量指標：Delta 的特例（到期機率）
3. **到期時間（T）**→ 衡量指標：**Theta**
4. **波動率（σ）**→ 衡量指標：**Vega**
5. **無風險利率（r）**→ 衡量指標：**Rho**（影響最小）

## 五大 Greeks 詳解

### 一、Delta（δ）— 方向敏感度

**Delta = 選擇權價格變動量 ÷ 標的物價格變動量**

- 買權（Call）：Delta 介於 0 ~ 1
- 賣權（Put）：Delta 介於 −1 ~ 0
- **深價內**：Delta 趨近 ±1（跟著標的物幾乎 1:1 變動）
- **價平**：Delta ≈ ±0.5（一半的敏感度）
- **深價外**：Delta 趨近 0（幾乎不動）

**三種解讀**：

1. **方向敏感度**：Delta = 0.5 表示標的漲 1 元，選擇權漲 0.5 元
2. **到期機率的近似值**：Delta = 0.3 大約代表到期時價內的機率約 30%
3. **避險比例**：Delta = 0.5 代表要持有 0.5 張現貨才能對沖 1 口選擇權的風險

**Delta 中性（Delta Neutral）**：
- 總 Delta = 0 的組合，不受標的物漲跌影響
- 詳見 [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利與Delta Neutral策略]]

### 二、Gamma（γ）— Delta 的變化率

**Gamma = Delta 變動量 ÷ 標的物價格變動量**

- Gamma 是 Delta 的「加速度」
- **價平選擇權 Gamma 最大**：Delta 變化最劇烈
- **深價內/深價外 Gamma 最小**：Delta 已趨近穩定
- **到期時 Gamma 急速放大**（特別是價平選擇權）

**實戰意義**：
- Gamma 放大代表 Delta 在快速變化，避險需要更頻繁調整
- 買方的 Gamma 為正（站在加速度這一邊），賣方為負（被加速度傷害）
- Gamma 是選擇權賣方最大的風險來源

**Gamma Squeeze**：
- 當選擇權買盤大量增加，自營商必須買現貨避險（Delta hedge）
- 買越多 → Gamma 越大 → 避險買越多 → 股價越漲 → 正循環
- 詳見 [[逼券商拉抬Gamma-Squeeze兩手策略|逼券商拉抬Gamma Squeeze]]

### 三、Theta（Θ）— 時間衰減

**Theta = 選擇權價格變動量 ÷ 時間流逝（通常以每天計算）**

- Theta 永遠是負數（時間流逝會消耗權利金）
- **價平選擇權 Theta 最大**：時間價值最高，衰減最快
- **到期越近，衰減越快**：最後 30 天 Time Decay 加速
- **買方被時間傷害，賣方靠時間賺錢**

**Theta 的實戰規律**：

| 時間到到期 | Theta 影響 | 實戰意義 |
|-----------|-----------|---------|
| > 60 天 | 衰減緩慢 | 買方時間成本可接受 |
| 30~60 天 | 衰減加速 | 賣方 theta 開始明顯獲利 |
| < 30 天 | 衰減急速 | 買方最危險的時期，賣方黃金期 |
| < 7 天 | 衰減暴烈 | 每天時間價值大量消失（週選賣方天堂） |

詳見 [[Theta時間價值衰退與選擇權賣方策略|Theta時間價值衰退與選擇權賣方策略]]

### 四、Vega（ν）— 波動率敏感度

**Vega = 選擇權價格變動量 ÷ 波動率變動 1%**

- Vega 永遠是正數（波動率上升，選擇權權利金增加）
- **價平選擇權 Vega 最大**
- **長天期選擇權 Vega 大**：到期時間越長，波動率的影響越大
- **買方賭波動率上升，賣方賭波動率下降**

**波動率對選擇權的影響**：

| 情境 | 隱含波動率 | 買方 | 賣方 |
|------|-----------|------|------|
| 波動率上升 | IV ↑ | 權利金增加（賺） | 權利金增加（虧） |
| 波動率下降 | IV ↓ | 權利金減少（虧） | 權利金減少（賺） |

詳見 [[隱含波動率IV與歷史波動率HV實戰判讀|隱含波動率IV與歷史波動率HV實戰判讀]]

### 五、Rho（ρ）— 利率敏感度

**Rho = 選擇權價格變動量 ÷ 利率變動 1%**

- Rho 對短天期選擇權影響極小，實戰中通常可忽略
- 利率上升 → Call 權利金微漲、Put 權利金微跌
- 長天期 LEAPS 選擇權才需要考慮 Rho

## Greeks 的交互關係

### Gamma-Theta 拔河

- **買方**：正 Gamma + 負 Theta（方向有利但時間不利）
- **賣方**：負 Gamma + 正 Theta（方向不利但時間有利）
- 這是選擇權最核心的矛盾：**方向槓桿 vs 時間成本**

### Delta-Gamma 關係

- Delta 告訴你「現在站在哪裡」
- Gamma 告訴你「站在那裡的角度有多陡」
- 高 Gamma = Delta 變化快 = 方向槓桿加速

### Vega-Theta 抵消

- 遠月選擇權：Vega 大、Theta 小（波動率影響大，時間影響小）
- 近月選擇權：Vega 小、Theta 大（波動率影響小，時間影響大）
- 這就是為什麼**近月賣方靠 Theta 賺錢，遠月要靠波動率判斷**

## Greeks 在不同部位的展現

### 單一部位 Greeks

| 部位 | Delta | Gamma | Theta | Vega |
|------|-------|-------|-------|------|
| 買 Call | + | + | − | + |
| 買 Put | − | + | − | + |
| 賣 Call | − | − | + | − |
| 賣 Put | + | − | + | − |

詳見 [[選擇權四大基本策略|選擇權四大基本策略]]

### 常見組合 Greeks

| 組合 | Delta | Gamma | Theta | Vega |
|------|-------|-------|-------|------|
| 跨式（Long Straddle） | ≈0 | ++ | −− | ++ |
| 勒式（Long Strangle） | ≈0 | + | − | + |
| 鐵兀鷹（Iron Condor） | ≈0 | − | + | − |

詳見 [[跨式Straddle與勒式Strangle|跨式與勒式]]、[[選擇權組合策略|選擇權組合策略]]

## 實戰應用

### 1. 選擇策略的 Greeks 思維

- **看好大漲**：買 Call（正 Delta + 正 Gamma）
- **看好小漲**：賣 Put（正 Theta + 正 Delta）
- **認為盤整**：賣 Straddle/Strangle（正 Theta + 負 Vega）
- **認為將大波動但方向不定**：買 Straddle（正 Gamma + 正 Vega）

### 2. 避險 Delta 中性

- 組合總 Delta = 0 不受方向影響
- 靠 Theta 或 Vega 變化獲利
- 詳見 [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利與Delta Neutral策略]]

### 3. 選擇權賣方的 Greeks 管理

- 賣方最怕 Gamma（方向加速傷害）和 Vega（波動率上升傷害）
- 賣方賺 Theta（時間流逝獲利）
- 避險方式：調整 Delta、控制 Gamma、設定停損

詳見 [[選擇權賣方收租策略Option-Seller-Rent-Collection|選擇權賣方收租策略]]

## 注意事項

1. **Greeks 是瞬時敏感度**，只告訴你「此刻」的變化，標的物大幅波動後 Greeks 會改變
2. **到期附近的 Gamma 極度不穩定**，Delta 中性策略需要頻繁調整
3. **波動率變化會同時影響所有 Greeks**，不能只看 Delta 忽略 Vega
4. **Greeks 不能告訴你方向**，只能告訴你「如果某個因素變化，價格會怎麼動」

## 相關主題

- [[選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|選擇權Greeks進階組合判讀]] - Greeks組合分析的進階技巧
- [[選擇權四大基本策略|選擇權四大基本策略]] - 買Call賣Call買Put賣Put
- [[選擇權賣方收租策略Option-Seller-Rent-Collection|選擇權賣方收租策略]] - Theta收入策略
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利與Delta Neutral]] - Delta中性策略
- [[跨式Straddle與勒式Strangle|跨式與勒式]] - 波動率交易策略
- [[選擇權Convexity凸性與非對稱收益Option-Convexity|選擇權Convexity]] - Greeks的高階延伸
- [[波動率微笑曲線與偏態Volatility-Smile-and-Skew|波動率微笑與偏態]] - 波動率結構
- [[隱含波動率IV與歷史波動率HV實戰判讀|IV與HV實戰判讀]] - 波動率實戰
- [[逼券商拉抬Gamma-Squeeze兩手策略|Gamma Squeeze]] - Gamma避險的正回饋迴圈
- [[Theta時間價值衰退與選擇權賣方策略|Theta時間衰退]] - 時間價值實戰
- [[VIX恐慌指數實戰判讀|VIX恐慌指數]] - 波動率的恐懼指標

## 來源

- 未標註原始素材；需後續回溯補齊。
