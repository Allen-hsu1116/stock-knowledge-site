---
title: Theta時間價值衰退與選擇權賣方策略
tags:
  - 操作策略
  - 選擇權
  - Theta
  - 時間價值
---

# Theta時間價值衰退與選擇權賣方策略

> 選擇權買方每天與時間為敵，賣方每天坐享時間流逝——Theta是選擇權賣方最可靠的盟友，但Gamma是它永不分離的影子敵人。

## 核心概念

### Theta是什麼

Theta（θ）是選擇權希臘字母之一，衡量選擇權價值隨時間流逝的衰減速率：

**Θ = ∂V/∂t**（選擇權價格對時間的偏微分）

白話文：每過一天，其他條件不變，選擇權價格會變動多少。

- **選擇權買方**：Theta為負值，每天都在虧損時間價值
- **選擇權賣方**：Theta為正值，每天坐享時間價值流逝

### 選擇權價值組成

**選擇權價值 = 內在價值（Intrinsic Value）+ 時間價值（Extrinsic Value）**

- 內在價值：現在立刻結算可以拿到的價值
- 時間價值：因為還沒到期，未來可能變成價內的機率價值

所有選擇權到期時，時間價值歸零——這就是Theta的戰場。

### 比喻：漏沙的卡車

選擇權的時間價值就像一輛裝滿河沙的卡車，開往目的地的途中不斷將沙子漏在地上。買方握著這輛車，沙子越漏越少；賣方撿起地上漏掉的沙子，每一粒都是利潤。

## Theta衰退三大特性

### 1. 非線性加速：越接近到期衰退越快

Theta衰退不是等速的，而是**加速的**：

| 距到期時間 | Theta衰退速度 | 體感 |
|-----------|-------------|------|
| 300天→299天 | 極慢 | 幾乎無感 |
| 60天→59天 | 中等 | 開始有感覺 |
| 30天→29天 | 快 | 明顯衰退 |
| 7天→6天 | 很快 | 價值快速蒸發 |
| 2天→1天 | 極快 | 時間價值可能腰斬 |

**比喻**：像融化的冰塊，越接近消失融化越快。

**賣方啟示**：最後30天是Theta衰退的「黃金收割期」，但Gamma風險也最大。

### 2. 價平（ATM）選擇權Theta最大

- **ATM（價平）**：Theta絕對值最大，因為不確定性最高
- **ITM（價內）**：Theta較小，大部分價值已是內在價值
- **OTM（價外）**：Theta較小，時間價值本身就不多

**賣方啟示**：賣ATM選擇權收取最多時間價值，但Delta風險也最大。

### 3. 週選 vs 月選的Theta差異

| 類型 | Theta特徵 | 適合策略 |
|------|----------|---------|
| 週選 | 最後幾天Theta衰退極快 | 短線賣方、快進快出 |
| 月選 | Theta衰退較平緩 | 中長線賣方、穩定收租 |

**實務建議**：賣方選擇30-45天到期的選擇權，平衡Theta收益與Gamma風險。

## Theta與其他Greeks的交互關係

### Theta vs Gamma：時間與波動的對價

這是選擇權最重要的對價關係：

| 部位 | Gamma | Theta | 本質 |
|------|-------|-------|------|
| Long Option | Long（賺波動） | Short（賠時間） | 買波動、賣時間 |
| Short Option | Short（賠波動） | Long（賺時間） | 賣波動、買時間 |

**白話文**：你付的權利金，本質上就是在「買Gamma、賣Theta」。賣方收的權利金，就是在「賣Gamma、買Theta」——用承擔波動風險換取時間價值。

### Theta vs Vega：時間與波動率的拉扯

- **離到期日越遠**：Vega影響力大，Theta影響力小
- **離到期日越近**：Theta影響力大，Vega影響力小

實務啟示：
- 買方在遠月選擇權主要對抗Vega風險
- 賣方在近月選擇權主要收割Theta收益
- **30天左右是Theta和Vega影響力的甜蜜點**

### Convexity的本質

Long Option的收益曲線是凸的（convex）——「賺的時候越賺越多，賠的時候越賠越少」。這個不對稱收益的代價就是Theta衰退。

- Long Option = Long Convexity = Long Gamma = 付出權利金 + 承受時間衰退
- Short Option = Short Convexity = Short Gamma = 收取權利金 + 承受波動風險

## 實戰應用

### 四種Theta收割策略

#### 1. Covered Call掩護性買權

最保守的Theta策略：持有現股 + 賣出Call

- 收取權利金，降低持股成本
- 股價不漲或小跌：賺權利金
- 股價大漲：股票被叫走，少賺上漲但權利金落袋
- **風險**：股價大跌的下行風險仍在

#### 2. Cash-Secured Put現金擔保賣出

想買股票但想便宜買：

- 賣出Put收取權利金
- 股價維持在履約價之上：權利金全收
- 股價跌破履約價：以較低價格買入股票（扣掉權利金後成本更低）

#### 3. Iron Condor鐵兀鷹

中性策略，同時賣出Call Spread和Put Spread：

- 四個腿都是賣方，Theta收益最大
- 預期股價在區間內盤整時最適合
- **定義風險**：最大虧損是履約價差減去權利金

#### 4. 對角價差Diagonal Spread

垂直價差 + 時間價差的混合體：

- 買遠月ATM/ITM選擇權（Theta影響小）
- 賣近月OTM選擇權（Theta衰退快）
- 同時賺取近月的Theta衰退和遠月的Vega差
- Rolling策略是殺手鐧：近月到期後再賣下一期

### Theta判讀五要點

1. **看Theta絕對值**：Theta=-5代表每天虧5點（買方）或賺5點（賣方）
2. **看Theta/Gamma比值**：比值高代表時間價值收益占優勢
3. **看時間價值佔比**：時間價值佔權利金比例高的，Theta衰退絕對金額大
4. **週選賣方黃金期**：最後5天Theta衰退最猛烈，但Gamma風險同步放大
5. **月選賣方穩定收割**：30-45天到期是甜蜜點

## 注意事項

### 四大風險管理

1. **Gamma風險——Theta的影子敵人**
   - 賣方賺Theta，但承擔Gamma風險
   - 股價大幅波動時，Gamma讓Delta急速變化，虧損可能遠超權利金
   - **解法**：到期前14天左右平倉，避開Gamma風險最大的最後兩週

2. **波動率風險（Vega）**
   - IV突然飆升（財報、重大事件），選擇權價值暴漲
   - **解法**：避開財報日前後、重大事件前賣出選擇權

3. **被指派風險**
   - 賣出選擇權可能被提前指派
   - 除息前的Call容易被提前指派
   - **解法**：注意除息日，避免在除息前賣深度價內Call

4. **部位控制**
   - 賣方獲利有限（最多收權利金），虧損可能無限
   - **解法**：單一交易風險不超過帳戶的2-5%

### 常見誤區

| 誤區 | 正確理解 |
|------|---------|
| 賣方穩賺不賠 | Theta是盟友但Gamma是敵人，大波動會讓賣方虧損遠超權利金 |
| 選擇權買方一定虧 | 如果波動率大幅上升，買方可以獲利超過Theta損失 |
| 越接近到期Theta越大越好 | Theta大的同時Gamma也大，最後幾天的賣方面臨巨大Gamma風險 |
| 賣OTM選擇權最安全 | OTM的Theta金額小，真正大波動來臨時Delta會迅速變化 |

## 相關主題

- [[選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]
- [[選擇權賣方收租策略Option-Seller-Rent-Collection]]
- [[選擇權Greeks希臘字母]]
- [[鐵兀鷹Iron-Condor]]
- [[對角價差Diagonal-Spread]]
- [[隱含波動率IV與歷史波動率HV實戰判讀]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[逼券商拉抬Gamma-Squeeze兩手策略]]

## 來源

- [深入了解選擇權中的Theta：時間對選擇權價值的影響](../raw/2026-05-10/Theta時間價值衰退與選擇權賣方策略.md)
- [Theta for Option Sellers: Why Time Decay is the Ultimate Friend - Passive Seeds](https://www.passiveseeds.com/stock-and-options/theta-for-option-sellers-why-time-decay-is-the-ultimate-friend/)
- [選擇權的定價與避險參數 - Anton Cheng](https://medium.com/defi-taiwan/%E9%82%A3%E4%BA%9B%E5%B9%B4-%E6%B2%92%E5%AD%B8%E5%A5%BD%E7%9A%84%E9%81%B8%E6%93%87%E6%AC%8A-2-6934483b2f78)
- [Option Greeks for Beginners - SlashTraders](https://slashtraders.com/en/blog/option-greeks/)