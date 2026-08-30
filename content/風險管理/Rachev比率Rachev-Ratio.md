---
title: "Rachev比率 Rachev Ratio"
category: "風險管理"
tags: [風險調整報酬, 績效評估, CVaR, 尾部風險, 量化指標, Rachev, 非常態分佈]
created: 2026-08-11
---

# Rachev比率 Rachev Ratio

> 夏普比率用標準差當分母，把上漲的波動也當成壞事；索提諾比率只看下行標準差，但還是假設分佈形狀可被標準差描述。Rachev 比率直接用 CVaR 當分母、預期尾部報酬當分子——不看中間，只看兩端尾巴有多不對稱。

## 核心概念

**Rachev 比率**（又稱 R-Ratio）由 Svetlozar Rachev 等人在 2004 年提出，是一種**報酬對風險**（reward-to-risk）的風險調整績效指標。與夏普和索提諾等**報酬對變異性**（reward-to-variability）指標不同，Rachev 比率專門設計用於**非常態分佈**環境下衡量極端正報酬潛力相對於極端負報酬風險的比值。

### 為什麼需要 Rachev 比率

傳統風險調整報酬指標的問題：

- **[[風險管理/風險調整報酬指標夏普比率與索提諾比率|夏普比率]]**：用標準差當風險，但標準差不區分漲跌，且假設報酬常態分佈
- **[[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced|索提諾比率]]**：只用下行標準差，但仍假設下行風險可用標準差描述，忽略肥尾
- **兩者都關注「中心趨勢」**：用均值和離散度摘要整個分佈，但真實報酬分佈有偏態和肥尾

Rachev 比率直接使用分佈的**兩端尾部**：
- **分子**：右尾（最好 q% 的情況）的平均報酬——Expected Tail Return（ETR）
- **分母**：左尾（最差 q% 的情況）的平均損失——Expected Tail Loss（ETL，也就是 CVaR）

## 計算公式

### 原始定義

$$\rho(x' r) = \frac{CVaR_{(1-\alpha)}(r_f - x' r)}{CVaR_{(1-\beta)}(x' r - r_f)}$$

或等價表示為：

$$\rho(x' r) = \frac{ETL_\alpha(r_f - x' r)}{ETL_\beta(x' r - r_f)}$$

其中：
- $x' r$ = 投資組合報酬
- $r_f$ = 無風險利率
- $\alpha, \beta \in (0, 1)$ = 分位數水準（對稱版本中 $\alpha = \beta$）
- $ETL_\alpha$ = 期望尾部損失，即 [[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall|CVaR/Expected Shortfall]]

### ETL 的定義

$$ETL_\alpha = \frac{1}{\alpha} \int_0^\alpha VaR_q(X) \, dq$$

也就是「超過 VaR 之後的平均損失」：

$$ETL_\alpha(X) = E[L \mid L > VaR_\alpha]$$

### ETR 的定義

ETR 是 ETL 的鏡像——「超過 Profit-at-Risk 之後的平均獲利」：

$$ETR_\beta(X) = E[G \mid G > PaR_\beta]$$

### 廣義 Rachev 比率

廣義版本引入了冪次數 γ 和 δ，用來調整投資者對風險的厭惡程度：

$$\rho(x' r) = \frac{ETL_{(\gamma, \alpha)}(r_f - x' r)}{ETL_{(\delta, \beta)}(x' r - r_f)}$$

其中 $ETL_{(\gamma, \alpha)}(X) = E[\max(L, 0)^\gamma \mid L > VaR_\alpha]$ 是冪次 CVaR。γ 越大，對極端損失的懲罰越重。

## 直覺解讀

- **Rachev > 1**：右尾報酬潛力大於左尾損失風險，策略有正的尾部不對稱性
- **Rachev = 1**：兩端尾部對稱，極端獲利和極端虧損的幅度相當
- **Rachev < 1**：左尾損失風險大於右尾報酬潛力，策略有負的尾部不對稱性

**關鍵區別**：夏普比率問「平均報酬 vs 平均波動」，Rachev 比率問「最好的時候能賺多少 vs 最差的時候會賠多少」。

## 實務計算

### 樣本版本（Ex-Post 分析）

給定 N 個歷史報酬觀測值 $r_1, r_2, \ldots, r_N$：

1. **計算左尾 ETL（分母）**：
   - 找出最差的 $\alpha \times N$ 個報酬
   - 計算這些報酬的平均值（取絕對值）
   
2. **計算右尾 ETR（分子）**：
   - 找出最好的 $\beta \times N$ 個報酬
   - 計算這些報酬的平均值

3. **Rachev = ETR / ETL**

**範例**：1000 個日報酬，α = β = 5%
- 最差 50 天的平均虧損 = 3.2%
- 最好 50 天的平均獲利 = 4.8%
- Rachev = 4.8 / 3.2 = 1.5

### 參數選擇

- **α = β = 5%**：最常見的對稱設定，衡量 5% 最差 vs 5% 最好
- **α = 5%, β = 10%**：更看重下行風險，分母用更寬的尾部
- **α = 1%, β = 1%**：只看極端尾部，適合黑天鵝策略
- **γ = δ = 2**：廣義版本，對極端值加平方權重

## Rachev 比率的性質

### 優點

1. **不需要常態分佈假設**：直接從歷史數據或模擬計算 CVaR
2. **捕捉偏態和肥尾**：分子分母分別反映右尾和左尾的厚度
3. **可自定義風險偏好**：α、β、γ、δ 四個參數讓投資者精確調整
4. **ex-ante 和 ex-post 都可用**：事前可用模型預測分佈計算，事後直接用歷史數據
5. **適合非對稱策略**：選擇權賣方、CTA、尾部避險等策略的分佈嚴重偏態，Rachev 比夏普更公平

### 局限

1. **樣本需求大**：尾部 5% 需要足夠多的觀測值才可靠，建議至少 200+ 數據點
2. **優化困難**：Rachev 是兩個 CVaR 的比值，CVaR 是凸函數，比值可能有多個局部極值
3. **對極端值敏感**：單一極端事件（如 2008 金融海嘯）可能主導 ETL 值
4. **參數選擇主觀**：α、β 的選擇沒有標準答案，不同設定可能給出不同排名
5. **忽視中間分佈**：只看兩端尾巴，可能忽略整體報酬分佈的形狀

## 與 [[風險管理/一致性風險測度Coherent-Risk-Measures|一致性風險測度]] 的關係

Rachev 比率的分母 ETL（CVaR）是一種一致性風險測度（Coherent Risk Measure），滿足四個公理：

1. **單調性**：如果 X ≤ Y 則 ρ(X) ≥ ρ(Y)
2. **次可加性**：ρ(X + Y) ≤ ρ(X) + ρ(Y)
3. **正齊次性**：ρ(λX) = λρ(X) for λ > 0
4. **平移不變性**：ρ(X + c) = ρ(X) - c

VaR 不滿足次可加性，所以不是一致性風險測度。Rachev 用 CVaR 而非 VaR 作為分母，在數學上更嚴謹。

## 適用場景

### 1. 選擇權賣方策略
賣方策略的報酬分佈嚴重左偏——大量小賺、偶爾大賠。夏普比率會高估這類策略的品質（因為小賺多讓均值高、標準差低），Rachev 比率會正確顯示左尾風險遠大於右尾潛力。

### 2. 尾部避險策略
買 Put 做尾部避險的策略報酬分佈右偏——大量小賠、偶爾大賺。夏普比率會低估這類策略（因為經常小賠讓均值低），Rachev 比率會正確顯示右尾潛力。

### 3. CTA / 期貨基金
趨勢追蹤策略的報酬分佈通常正偏態——截斷虧損讓利潤奔跑。Rachev 比率能正確衡量這種「不對稱」的價值。

### 4. 非流動性資產
非流動性資產的報酬分佈有嚴重肥尾，夏普比率的常態假設完全失效。Rachev 比率直接從歷史尾部計算，更可靠。

## 實戰應用

### 在台股的應用考量
- **漲跌幅限制**：台股 10% 漲跌幅限制截斷了極端尾部，使得 ETL 和 ETR 的計算受到人為限制。與無漲跌幅限制的市場相比，Rachev 比率在台股的區分度可能較低
- **除權息季節**：除權息造成的跳空缺口會產生人造的「極端報酬」，在計算 ETR/ETL 時需要調整
- **樣本量**：台股個股歷史數據可能不足以可靠估計 1% 尾部，建議用 5% 分位數

## 注意事項

### 與其他風險調整報酬指標的比較
**指標分類**：
- **報酬對變異性**（Reward-to-Variability）：夏普、索提諾、[[風險管理/Omega比率Omega-Ratio|Omega]] — 用某種離散度當分母
- **報酬對風險**（Reward-to-Risk）：Rachev、[[風險管理/Calmar比率與最大回撤分析Calmar-Ratio-and-Maximum-Drawdown|Calmar]] — 用某種損失量當分母

**Rachev 的獨特之處**：
- 分子和分母都是尾部指標——不關心中間 90% 的表現，只看極端
- 不需要假設分佈形狀——CVaR 直接從歷史數據或模擬計算
- 可以用不同的 α 和 β——例如你想更看重下行風險，就設 α < β
- 廣義版本的 γ 和 δ 可以調整尾部權重——比 CVaR 更靈活

**與 Omega 比率的差異**：
- Omega 用整個分佈的收益面積 ÷ 損失面積
- Rachev 只看尾部 q% 的條件期望值
- Omega 更全面但對極端值不夠敏感，Rachev 更聚焦尾部但可能遺漏中間資訊

## 相關主題
- [[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall]] — Rachev 比率的分母就是 CVaR
- [[風險管理/一致性風險測度Coherent-Risk-Measures]] — CVaR 的數學性質
- [[風險管理/風險調整報酬指標夏普比率與索提諾比率|夏普比率]] — Rachev 的「前輩」，用標準差當分母
- [[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced|索提諾比率]] — 用下行標準差當分母
- [[風險管理/Omega比率Omega-Ratio|Omega 比率]] — 用整個分佈的收益/損失面積比
- [[風險管理/Calmar比率與最大回撤分析Calmar-Ratio-and-Maximum-Drawdown|Calmar 比率]] — 另一種 reward-to-risk 指標，用 MDD 當分母
- [[風險管理/光譜風險測度Spectral-Risk-Measure]] — CVaR 的廣義框架
- [[風險管理/蒙地卡羅模擬交易驗證Monte-Carlo-Simulation]] — 用模擬產生尾部數據計算 Rachev

## 來源
- Biglova, A., Ortobelli, S., Rachev, S.T. & Stoyanov, S. (2004). "Different Approaches to Risk Estimation in Portfolio Theory". The Journal of Portfolio Management, 31(1), 103-112.
- Rachev, S.T., Stoyanov, S.V. & Fabozzi, F.J. (2008). "Advanced Stochastic Models, Risk Assessment, and Portfolio Optimization". Wiley.
- Cheridito, P. & Kromer, E. (2013). "Reward-Risk Ratios". Journal of Investment Strategies, 3(1), 3-18.
- Farinelli, S. et al. (2008). "Beyond Sharpe ratio: Optimal asset allocation using different performance ratios". Journal of Banking and Finance, 32(10), 2057-2063.
