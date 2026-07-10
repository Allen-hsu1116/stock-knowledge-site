---
title: "愛爾德安全區停損 Elder's SafeZone Stop"
tags: [操作策略, 停損系統, Alexander Elder, 動態停損, 波動率停損]
created: 2026-07-10
---

# 愛爾德安全區停損 Elder's SafeZone Stop

> Alexander Elder 設計的波動率驅動停損系統，用最近N期「被觸發的穿透幅度」平均值來設定停損——不是用全部波動（像 ATR），而是只用「真正刺穿了近期極值的那部分」，讓停損設在噪音之外的安全區。

## 核心概念

**Elder's SafeZone Stop** 是 Alexander Elder 在《Trading for a Living》和《Come Into My Trading Room》中提出的動態停損方法。Elder 認為傳統的固定百分比停損太過粗糙——不同股票波動特性完全不同，用同一個百分比去套所有股票等於蒙眼開槍。

### 解決什麼問題

Elder 觀察到市場價格有兩種波動：
1. **噪音波動（Noise）**：盤中的正常起伏，不代表趨勢改變
2. **穿透波動（Penetration）**：價格刺穿近期高點或低點，代表方向性力量

傳統的 [[ATR平均真實波幅-Average-True-Range|ATR]] 停損把兩種波動都算進去，導致停損距離可能設得太大。SafeZone Stop 只計算「真正穿透了近期極值的那部分幅度」，用這個平均值來設定停損——讓停損剛好設在噪音區之外，不被正常波動掃掉，但也不會設得太遠。

### 與其他停損方法的差異

- **固定百分比停損**：簡單但不考慮個股波動特性，高波動股和低波動股用同樣百分比
- **ATR 停損**（[[停損設定方法Stop-Loss-Placement]]）：用全部波動幅度，可能設太遠
- **[[Chandelier-Exit吊燈出場指標|Chandelier Exit]]**：ATR 版的追蹤停損，從最高點往下掛
- **[[Chande-Kroll-Stop錢德克羅停損指標|Chande Kroll Stop]]**：雙重 ATR 過濾的進階停損
- **SafeZone Stop**：只看穿透幅度，停損更貼合實際風險

## 計算公式

### 多頭停損（做多時的下方保護）

**Step 1：找出最近N期的低點**

回看過去 N 期（預設 N=10 或 N=20），找出每期的低點。

**Step 2：識別「被穿透」的期數**

對每一期 i，如果 $Low_i < Low_{i-1}$（當期低點比前一期低點更低），這一期就是「被穿透」的——空方力量刺穿了前一期低點。

**Step 3：計算穿透幅度**

$$Penetration_i = Low_{i-1} - Low_i \quad (\text{if } Low_i < Low_{i-1})$$

只記錄被穿透期的幅度，未被穿透的期數不算。

**Step 4：計算平均穿透幅度**

$$\bar{Penetration} = \frac{\sum Penetration_i}{\text{count of penetrated bars}}$$

只除以被穿透的期數，不是全部 N 期。

**Step 5：設定停損**

$$Stop = Low_{today} - (Multiplier \times \bar{Penetration})$$

Multiplier 通常設 2~3 倍，跟 ATR 停損的倍數概念類似。

### 空頭停損（做空時的上方保護）

邏輯完全對稱：

**Step 1-2**：找出被穿透的期數（$High_i > High_{i-1}$ 為被穿透）

**Step 3**：$Penetration_i = High_i - High_{i-1}$

**Step 4**：計算平均穿透幅度

**Step 5**：$Stop = High_{today} + (Multiplier \times \bar{Penetration})$

### 計算範例

假設做多某股票，過去 10 期的低點如下：

| 期數 | 低點 | 前期低點 | 被穿透？ | 穿透幅度 |
|------|------|----------|----------|----------|
| 1 | 100 | — | — | — |
| 2 | 102 | 100 | 否 | — |
| 3 | 99 | 102 | 是 | 3 |
| 4 | 101 | 99 | 否 | — |
| 5 | 97 | 101 | 是 | 4 |
| 6 | 98 | 97 | 否 | — |
| 7 | 95 | 98 | 是 | 3 |
| 8 | 96 | 95 | 否 | — |
| 9 | 93 | 96 | 是 | 3 |
| 10 | 94 | 93 | 否 | — |

被穿透期數 = 4 次
穿透幅度合計 = 3 + 4 + 3 + 3 = 13
平均穿透幅度 = 13 / 4 = 3.25

停損 = 94 - (2 × 3.25) = 94 - 6.5 = **87.5**

對比如果用 ATR（全部波動平均），假設 ATR = 5，停損 = 94 - (2 × 5) = 84。

SafeZone Stop（87.5）比 ATR 停損（84）更近，因為它只計算方向性穿透的幅度而非全部波動。

## 實戰應用

### 優勢場景

**場景 1：趨勢追蹤策略**

SafeZone Stop 最適合趨勢追蹤——在趨勢中，價格會持續創新高（多頭）或新低（空頭），「穿透」的方向一致，平均穿透幅度穩定，停損距離合理。

搭配 [[趨勢追蹤策略Trend-Following|趨勢追蹤策略]] 或 [[海龜交易法則|海龜交易法則]] 使用效果最佳。

**場景 2：高波動個股**

對於波動大的股票（如 AI 概念股、小型股），固定百分比停損要麼設太近被天天掃、要麼設太遠風險太大。SafeZone Stop 自動適應個股的穿透特性，給出合理的停損距離。

**場景 3：多時間框架停損**

日線用日線 SafeZone Stop，週線用週線 SafeZone Stop，兩者共振時停損更可靠。參考 [[多時間框架分析|多時間框架分析]]。

### 劣勢場景

**盤整市不適用**

盤整時價格在區間內來回，穿透方向不一致（有上有下），平均穿透幅度會偏小，停損可能設得太近容易被掃。盤整市應該用 [[盤整市綜合操作策略Consolidation-Market-Strategy|盤整策略]] 或 [[網格交易Grid-Trading|網格交易]]。

**跳空缺口風險**

SafeZone Stop 跟所有波動率停損一樣，無法防範 [[跳空缺口風險Gap-Risk|跳空缺口]]。如果收盤 100、停損 95，隔天開盤 88，停損會在 88 成交而非 95。解法是搭配 [[保護性賣權與Collar避險策略Protective-Put-and-Collar|Protective Put]] 做硬性保護。

### 與 Elder 系統整合

SafeZone Stop 是 Elder 交易系統中的「防守組件」：

- **方向判斷**：[[Elder-Ray牛熊力量指標|Elder-Ray]] Bull/Bear Power
- **力道確認**：[[Force-Index力量指標|Force Index]]
- **進場時機**：[[Elder-Impulse-System艾爾德衝擊系統|Elder Impulse System]]
- **停損保護**：SafeZone Stop
- **資金管理**：[[Elder-2%與6%雙重法則|Elder 2%與6%法則]]
- **波動感測**：[[愛爾德溫度計Elder-Thermometer|Elder's Thermometer]]

### 參數調校建議

- **回看期數 N**：日線交易用 N=10~20，週線用 N=8~13。太短則樣本不足，太長則反應太慢
- **倍數 Multiplier**：保守用 2.5~3 倍，積極用 1.5~2 倍。倍數越大停損越遠、被掃機率越低但單筆虧損越大
- **搭配 2% 法則**：不管 SafeZone Stop 算出多少，單筆最大虧損不超過總資金 2%（[[部位控制2%法則Position-Sizing-2-Percent-Rule|2% 法則]]）

## 台股實戰注意事項

- **除權息調整**：除權息日產生的跳空會人為放大穿透幅度，計算 SafeZone Stop 時應使用還原股價
- **漲跌停限制**：漲停鎖死時高點不會再往上穿透，SafeZone Stop 的空頭停損可能偏小；跌停鎖死時同理
- **當沖不適用**：SafeZone Stop 用日線高低點計算，當沖需要用分鐘K線重新計算
- **融資維持率**：停損距離算出來後，要確認不會觸發 [[融資維持率與斷頭|融資追繳]]。如果 SafeZone Stop 的停損價會讓維持率跌破 130%，應該縮小部位而非放寬停損

## 優缺點總結

**優點：**
- 自動適應個股波動特性，不同股票不同停損距離
- 只計算穿透波動而非全部波動，停損比 ATR 更貼合實際風險
- 與 Elder 交易系統無縫整合
- 多空對稱，做多做空都能用
- 計算比 ATR 簡單，只需高低點數據

**缺點：**
- 盤整市效果差，穿透方向不一致導致停損距離失真
- 無法防範跳空缺口，需要搭配選擇權保護
- 樣本量要求：回看期數太短則平均穿透幅度不穩定
- 參數選擇缺乏學術驗證，過度依賴經驗
- 被穿透期數可能為零（強趨勢中很少回檔），需要備用方案

## 總結

SafeZone Stop 的核心智慧是「只看真正的方向性穿透，忽略噪音波動」。這讓它比 ATR 停損更精準——在同樣的保護效果下停損距離更近，代表單筆虧損更小、風報比更好。但它不是萬能的：盤整市會失靈、跳空防不住、參數要調校。最佳用法是把它當成 Elder 交易系統的一環，與方向判斷、力道確認、資金管理組合使用，而不是單獨依賴。

## 相關筆記

- [[ATR平均真實波幅-Average-True-Range]] — 全波動率停損的基礎
- [[Chandelier-Exit吊燈出場指標]] — ATR 版追蹤停損
- [[Chande-Kroll-Stop錢德克羅停損指標]] — 雙重 ATR 進階停損
- [[停損設定方法Stop-Loss-Placement]] — 停損設定通用方法
- [[移動停利停損Trailing-Stop]] — 移動停損通用框架
- [[愛爾德溫度計Elder-Thermometer]] — Elder 系統的波動感測器
- [[Elder-Ray牛熊力量指標]] — Elder 系統的多空力量指標
- [[Force-Index力量指標]] — Elder 系統的量價力道指標
- [[Elder-Impulse-System艾爾德衝擊系統]] — Elder 系統的進出場時機
- [[Elder-2%與6%雙重法則]] — Elder 系統的資金管理
- [[部位控制2%法則Position-Sizing-2-Percent-Rule]] — 2% 法則
- [[跳空缺口風險Gap-Risk]] — 跳空風險基礎
- [[趨勢追蹤策略Trend-Following]] — 趨勢追蹤策略
- [[盤整市綜合操作策略Consolidation-Market-Strategy]] — 盤整市策略