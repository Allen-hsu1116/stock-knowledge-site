---
title: "GARCH 模型與波動率預測 GARCH Model and Volatility Forecasting"
category: "風險管理"
---

# GARCH 模型與波動率預測 GARCH Model and Volatility Forecasting

> 波動率不是常數而是會聚集、會延續、會回歸——GARCH 把「波動率的波動率」變成可預測的數學模型，是量化風控的基石，也是 VaR 與選擇權定價的引擎

## 核心概念

GARCH（Generalized Autoregressive Conditional Heteroskedasticity，廣義自回歸條件異方差模型）由 Tim Bollerslev 於 1986 年提出，是 Robert Engle 的 ARCH 模型（1982）的推廣。它解決了傳統統計模型中「恆定方差」假設在金融數據中完全不適用的問題。

**一句話理解**：今天的波動率取決於過去的波動率（自回歸）和過去的「驚喜」（ARCH 效應），但長期會回歸到一個均值水平。

### 為什麼需要 GARCH？

金融時間序列有三大「異常特徵」是傳統線性模型（ARMA、ARIMA）無法處理的：

- **波動率聚集（Volatility Clustering）**：高波動後面跟著高波動，低波動後面跟著低波動。市場不會從平靜瞬間跳到恐慌，也不會從恐慌瞬間回到平靜
- **肥尾分佈（Fat Tails）**：常態分佈預測「4個標準差以外的事件」每157年發生一次，現實中市場每隔幾年就來一次
- **槓桿效應（Leverage Effect）**：下跌時波動率上升得比上漲時多——恐慌比貪婪更暴力

### ARCH vs GARCH 的差異

- **ARCH(q)**：當期波動率只取決於過去 q 期的「驚喜」（殘差平方），需要很多期才能捕捉波動率聚集
- **GARCH(p,q)**：當期波動率同時取決於過去的「驚喜」和過去的「波動率本身」，用更少的參數達到更好的擬合

## 數學模型

### GARCH(1,1) 公式

最常用且通常已足夠的版本：

```
σ²(t) = ω + α·ε²(t-1) + β·σ²(t-1)
```

- **σ²(t)**：第 t 期的條件方差（當期預測的波動率平方）
- **ω**：長期均值項（Long-run average variance 的權重）
- **α**：ARCH 係數——最近一期「驚喜」的影響權重
- **β**：GARCH 係數——上一期波動率的持續性權重
- **ε²(t-1)**：上一期的殘差平方（「驚喜」的平方）
- **σ²(t-1)**：上一期的條件方差

### 參數限制條件

- **ω > 0**：長期方差必須為正
- **α ≥ 0**：ARCH 係數不能為負
- **β ≥ 0**：GARCH 係數不能為負
- **α + β < 1**：平穩性條件——波動率最終會回歸均值，不會無限發散

### 長期無條件方差

當 α + β < 1 時，長期均衡波動率為：

```
σ²(long-run) = ω / (1 - α - β)
```

這是 GARCH 模型最重要的預測值——不管當前波動率多高或多低，最終都會回歸到這個水平。

### 半衰期（Half-Life of Volatility Shocks）

一個波動率衝擊消退一半需要多長時間：

```
Half-Life = ln(0.5) / ln(α + β) = -0.693 / ln(α + β)
```

典型參數 α+β ≈ 0.97-0.99，半衰期約 20-70 天。這意味著市場恐慌的「餘震」可以持續 1-3 個月。

## 實戰應用

### 一、VaR 風險值的動態計算

傳統 VaR 用恆定波動率，GARCH 用動態波動率：

- **傳統 VaR**：VaR = Portfolio × 1.65 × σ(歷史)，σ 是過去 N 天的固定標準差
- **GARCH VaR**：VaR = Portfolio × 1.65 × σ(t)，σ(t) 是 GARCH 預測的當期波動率

**實戰意義**：市場剛經歷大跌後，GARCH 預測的 σ(t) 會遠高於歷史平均，VaR 自然提高，提醒你減倉——傳統 VaR 還在用「太平時期」的波動率，毫無警覺。

### 二、選擇權定價的隱含波動率校正

- Black-Scholes 假設波動率恆定，但實際上波動率本身是隨機的
- GARCH 可用來預測未來波動率期限結構（Volatility Term Structure）
- GARCH 預測的 N 天後波動率 = √(σ²(t) + σ²(t+1) + ... + σ²(t+N)) / √N
- 短期波動率預測 > 長期波動率預測時 → 期限結構倒掛（Contango → Backwardation），市場處於恐慌期

### 三、波動率體制判斷

GARCH 的 α+β 接近 1 代表波動率持續性極強（恐慌或亢奮期），遠離 1 代表波動率快速回歸均值（平靜期）。

- **α+β > 0.99**：極端持續性，波動率衝擊半衰期 > 70 天——深處危機或泡沫期
- **α+β 0.95-0.99**：正常持續性，半衰期 15-70 天——常態市場
- **α+β < 0.95**：低持續性，半衰期 < 15 天——波動率快速消化，市場效率高

### 四、GARCH 變體模型

| 模型 | 特色 | 適用場景 |
|------|------|----------|
| **EGARCH** | 指數形式，不需非負限制，內建非對稱效應 | 股市（下跌波動 > 上漲波動） |
| **GJR-GARCH** | 加入虛擬變數捕捉槓桿效應 | 需要明確區分漲跌的波動率 |
| **TGARCH** | 門檻 GARCH，不同方向不同係數 | 股價指數、個股 |
| **IGARCH** | 積分 GARCH，α+β=1，非平穩 | 極端市場（少用） |
| **DCC-GARCH** | 多變量動態條件相關 | 投資組合的相關性時變 |
| **FIGARCH** | 分數積分 GARCH，捕捉長記憶 | 高頻數據、外匯 |

### 五、EGARCH 模型（最常用變體）

EGARCH（Exponential GARCH）由 Nelson（1991）提出：

```
ln(σ²(t)) = ω + α·[|ε(t-1)|/σ(t-1) - √(2/π)] + γ·ε(t-1)/σ(t-1) + β·ln(σ²(t-1))
```

**關鍵優勢**：
- 取對數後 σ² 自動為正，不需施加 ω>0、α≥0 的限制
- γ 項捕捉非對稱效應：γ < 0 代表壞消息（負衝擊）帶來更大波動——這就是槓桿效應
- 比標準 GARCH 更符合股票市場的實際行為

## 台股實戰框架

### 數據準備

- 使用台股加權指數日報酬率（對數報酬 = ln(P_t / P_{t-1})）
- 最少 500 個交易日（約 2 年）數據量才能穩定估計
- 報酬率需先去除均值（去趨勢）：r(t) - μ = ε(t)

### 參數估計

- 使用最大概似法（MLE）估計 ω, α, β
- 常態分佈假設在肥尾數據下估計仍無偏但不精確
- 建議用 t 分佈或 GED（廣義誤差分佈）作為創新分佈，更能捕捉肥尾

### 預測流程

1. **估計 GARCH(1,1) 參數**：用過去 500+ 天的報酬率數據
2. **計算當期條件方差**：σ²(t) = ω + α·ε²(t-1) + β·σ²(t-1)
3. **N 步預測**：反覆迭代，每一步用前一步的預測值代入
4. **年化波動率**：σ(年化) = σ(日) × √252

### GARCH vs VIX 的關係

- **VIX** 是市場對未來 30 天波動率的「隱含預期」（基於選擇權價格）
- **GARCH 預測** 是基於歷史報酬率的「統計預測」
- 兩者差值（VIX - GARCH預測）可視為「恐慌溢價」：
  - VIX >> GARCH → 市場定價的恐慌超過統計模型預測，選擇權賣方有利
  - VIX << GARCH → 市場低估未來波動，選擇權買方有利
- 參見 [[波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]]

## 注意事項

### 🚨 參數不穩定
- GARCH 參數會隨著估計窗口變化而變化
- 金融危机期間估計的參數與平靜期差異極大
- 建議用滾動窗口（如 250 天）定期重新估計

### 🚨 預測誤差隨時間擴大
- GARCH 短期預測（1-5天）較為可靠
- 超過 10 天的預測基本收斂到長期方差 ω/(1-α-β)
- 長期預測價值有限，不要把 30 天後的預測當真理

### 🚨 尾部風險仍然低估
- GARCH 捕捉了波動率聚集，但常態分佈假設仍低估極端事件
- 搭配 [[極端值理論EVT量化肥尾風險|EVT 極端值理論]] 或 t 分佈改進
- GARCH-EVT 組合是學術界公認的尾部風險最佳實踐

### 🚨 結構性變化
- 2008 金融危機、2020 COVID 等結構性斷裂會讓 GARCH 參數永久改變
- 單一 GARCH 模型無法捕捉 regime switching，需搭配 [[波動率體制轉換模型Volatility-Regime-Switching-Model|馬可夫轉換模型]]

### 🚨 過度擬合風險
- GARCH(1,1) 通常已足夠，更高階模型容易過度擬合
- AIC/BIC 資訊準則比較不同階數，不要盲目追求複雜模型

### 🚨 不是交易訊號
- GARCH 預測波動率方向，不預測價格方向
- 波動率上升不代表會跌——可能大漲也可能大跌
- 用於風險管理和部位調整，不是進出場訊號

## 相關主題

- [[VIX恐慌指數實戰判讀]] - VIX 與 GARCH 的隱含 vs 統計波動率對比
- [[VaR風險值Value-at-Risk]] - GARCH 動態 VaR 的基礎
- [[CVaR條件風險值Conditional-Value-at-Risk]] - GARCH-CVaR 進階風險度量
- [[波動率風險溢價Volatility-Risk-Premium]] - IV vs GARCH 預測的差值套利
- [[波動率體制轉換模型Volatility-Regime-Switching-Model]] - GARCH + Markov 轉換
- [[極端值理論EVT量化肥尾風險]] - GARCH-EVT 尾部風險組合
- [[波動率的波動率VVIX-Volatility-of-Volatility]] - VVIX 與 GARCH 的關聯
- [[蒙地卡羅模擬交易驗證Monte-Carlo-Simulation]] - GARCH 蒙地卡羅模擬路徑
- [[波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution]] - GARCH 預測的期限結構

## 來源

- Engle, R. F. (1982). "Autoregressive Conditional Heteroskedasticity with Estimates of the Variance of United Kingdom Inflation." *Econometrica*
- Bollerslev, T. (1986). "Generalized Autoregressive Conditional Heteroskedasticity." *Journal of Econometrics*
- Nelson, D. B. (1991). "Conditional Heteroskedasticity in Asset Returns: A New Approach." *Econometrica*
- Glosten, L. R., Jagannathan, R., & Runkle, D. E. (1993). "On the Relation between the Expected Value and the Volatility of the Nominal Excess Return on Stocks." *Journal of Finance*