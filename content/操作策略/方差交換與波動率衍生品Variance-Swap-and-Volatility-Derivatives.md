---
title: "方差交換與波動率衍生品 Variance Swap & Volatility Derivatives"
category: "操作策略"
---

# 方差交換與波動率衍生品 Variance Swap & Volatility Derivatives

> 波動率不再是隱含在選擇權裡的副產品——方差交換把「波動率本身」變成可以直接交易的商品

## 核心概念

方差交換（Variance Swap）是場外交易（OTC）的金融衍生品，讓投資人可以直接對標的資產的**已實現波動率（Realized Variance）**進行投機或避險。它跟選擇權不同——選擇權的波動率曝險是副產品（透過Vega），方差交換的標的就是波動率本身。

### 基本結構

一份方差交換包含三個核心要素：

- **方差履約價 Variance Strike**：簽約時約定的固定波動率水準（以方差單位計價）
- **已實現方差 Realized Variance**：契約期間標的資產日對數報酬的樣本方差
- **Vega名義本金 Vega Notional**：每1個波動率點的損益金額

損益公式：

```
損益 = (已實現方差 − 履約方差) × Vega名義本金
```

如果已實現波動率 > 履約波動率，買方獲利；反之賣方獲利。

### 為什麼不直接用選擇權

理論上方差交換可以用選擇權的delta-neutral部位複製（下面會講），但實務上：

- 選擇權部位的 Vega 隨股價變化而變，需要不斷調整delta
- 選擇權有履約價離散問題——只有特定履約價可選
- 方差交換是純波動率曝險，沒有delta/gamma維護負擔

## 定價與複製

### 靜態複製

方差交換可以用一籃子選擇權靜態複製。關鍵發現：**對數報酬平方的期望值可以用所有履約價的選擇權價格積分表示**。

複製組合：

- 買入每個履約價 K 的買權與賣權，權重 = 1/K²
- 所有履約價從 0 到 ∞ 的連續積分
- 實務上用離散履約價近似

這個組合的損益只依賴已實現波動率，跟標的價格路徑無關。

### 公允方差

由複製組合推導，公允方差（fair variance）等於：

```
σ² fair = (2/T) × ∫₀∞ Q(K)/K² dK
```

其中 Q(K) 是履約價 K 的 out-of-the-money 選擇權價格。實務上從選擇權市場反推，相關頁面 [[Black-Scholes定價模型]]、[[隱含波動率IV與歷史波動率HV實戰判讀]]。

這個公式顯示方差交換的定價依賴**整條波動率微笑曲線**——不只是ATM的IV。相關頁面 [[波動率微笑曲線與偏態Volatility-Smile-and-Skew]]。

## 相關工具

### Volatility Swap

方差交換的兄弟——直接交易波動率（標準差）而非方差：

```
損益 = (已實現波動率 − 履約波動率) × Vega名義本金
```

方差是波動率平方，兩者有凸性關係。Volatility Swap 比 Variance Swap 難定價，因為波動率本身沒有靜態複製組合（需要動態調整），流動性較差。

### VIX 指數

CBOE 的 VIX 指數就是用 S&P 500 選擇權計算的 30 天隱含方差開根號：

```
VIX = 100 × √(σ² 30天)
```

相關頁面 [[VIX恐慌指數實戰判讀]]。VIX 期貨與選擇權讓散戶也能交易方差，不需要 OTC 方差交換。

### Gamma Swap

方差Swap的改良版——權重隨股價調整，避免標的下跌時權重過大，讓曝險更平穩。

## 實戰用途

### 1. 波動率投機

機構用方差交換對整體市場波動率下注：

- **做多方差**：預期事件驅動（財報、選舉、政策）會讓波動率跳升，買方差交換
- **做空方差**：預期市場平靜，賣出方差交換收權利金

### 2. 避險

長期投資組合可以用方差交換避險：

- 股票組合買入方差交換，當市場大跌波動率飆升時，方差交換獲利抵消組合虧損
- 比 Protective Put 便宜，因為沒有 delta 成分
- 相關頁面 [[尾部風險對沖Tail-Risk-Hedging]]、[[保護性賣權與Collar避險策略Protective-Put-and-Collar]]

### 3. 相對價值

方差交換與選擇權組合可以做相對價值套利：

- 隱含方差 vs 已實現方差的利差——賣隱含買實現（或反向）
- 不同到期日的方差交換利差——方差曲線套利
- 相關頁面 [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]、[[波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution]]

### 4. 離散度交易

方差交換是離散度交易的基石，相關頁面 [[離散度交易Dispersion-Trading]]。

## 風險

### 跳空風險

方差交換的損益在跳空時非線性——單日大跌的方差貢獻遠大於連續小跌。相關頁面 [[跳空缺口風險Gap-Risk]]。

### 流動性風險

OTC 方差交換沒有公開市場，平倉需要跟對手協商。相關頁面 [[流動性風險Liquidity-Risk]]。

### 交易對手風險

OTC 衍生品的對手可能違約。相關頁面 [[交易對手風險Counterparty-Risk]]。2008 年金融危機中許多方差交換買方因對手破產而損失。

### 模型風險

定價依賴 Black-Scholes 假設，但真實世界有肥尾、跳空、波動率叢聚。相關頁面 [[模型風險Model Risk]]、[[GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting]]。

## 台股適用性

台股沒有官方的方差交換市場，但可以用：

- **台指選 TXO 組合靜態複製**：買入不同履約價的Call/Put組合模擬方差Swap
- **台指VIX 期貨**：期交所正在規劃，尚未上路
- **個股選擇權組合**：針對個股用 Call/Put 組合複製方差曝險

相關頁面 [[選擇權組合策略]]、[[選擇權Greeks希臘字母]]。

## 總結

方差交換是現代波動率交易的基石——它把波動率從選擇權的副產品變成獨立可交易的資產類別。核心價值：

- **純波動率曝險**：不用管delta、gamma維護
- **靜態複製可行**：用一籃子選擇權就可以複製
- **跨資產有效**：股票、外匯、商品、利率都能做
- **可避險可投機**：長期投資人避險、對沖基金投機

但實戰必須注意跳空風險、流動性、交易對手、模型假設等隱性陷阱。

## 延伸閱讀

- Demeterfi, Derman, Kamal, Zou (1999) "More Than You Ever Wanted to Know About Volatility Swaps"
- Carr, Madan (2002) "Towards a Theory of Volatility Trading"
- [[VIX恐慌指數實戰判讀]]
- [[波動率微笑曲線與偏態Volatility-Smile-and-Skew]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution]]
- [[離散度交易Dispersion-Trading]]
- [[隱含波動率IV與歷史波動率HV實戰判讀]]