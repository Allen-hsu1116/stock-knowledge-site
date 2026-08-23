---
title: Merton跳躍擴散模型
aliases: [Merton Jump-Diffusion Model, Jump-Diffusion, 跳躍擴散模型, Merton 1976]
---

# Merton跳躍擴散模型 (Merton Jump-Diffusion Model)


> Robert Merton 在 1976 年把 Black-Scholes 的連續股價過程加上「跳躍」成分——平時用幾何布朗運動描述連續波動，突發事件用卜瓦松過程驅動的跳躍來建模。這讓模型能解釋市場崩盤、跳空缺口等 Black-Scholes 完全無法處理的現象。
## 核心概念
Robert Merton 在 1976 年把 Black-Scholes 的連續股價過程加上「跳躍」成分——平時用幾何布朗運動描述連續波動，突發事件用卜瓦松過程驅動的跳躍來建模。這讓模型能解釋市場崩盤、跳空缺口等 Black-Scholes 完全無法處理的現象。

## 背景與動機

[[操作策略/Black-Scholes定價模型|Black-Scholes 模型]]假設股價服從連續的幾何布朗運動——路徑是連續的，不會有突然的跳空。但現實市場中：

- **1987 黑色星期一**：道瓊單日跌 22.6%，這不是連續過程能產生的
- **跳空缺口**：台股隔夜美股大跌，開盤直接跳空 3-5%
- **肥尾效應**：實際報酬分配的尾部機率遠高於常態分配預測
- **波動率微笑的短期深度**：短期價外 Put 的 IV 遠高於 Black-Scholes 預測

Merton（就是那個 Merton，跟 [[基本面分析/Merton結構化信用風險模型與KMV違約距離Merton-Model-and-KMV|Merton 信用風險模型]]同一人）提出：在連續擴散之上加一個跳躍過程。

## 模型結構

### 股價動態

$$\frac{dS_t}{S_t} = (\mu - \lambda \cdot E[J]) \, dt + \sigma \, dW_t + J \, dN_t$$

三個組成部分：

1. **漂移項** (μ − λ·E[J]) dt：調整後的期望報酬率。扣掉 λ·E[J] 是因為跳躍本身有期望值，要避免重複計算
2. **連續擴散** σ dW_t：熟悉的幾何布朗運動部分，W 是標準布朗運動
3. **跳躍部分** J dN_t：N_t 是卜瓦松過程，J 是跳躍幅度

### 卜瓦松過程 N_t

$$P(N_t = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$$

- **λ (lambda)**：跳躍強度（jump intensity），即單位時間內的期望跳躍次數
- λ = 0 時退化為純 Black-Scholes
- λ 越大，跳躍越頻繁

### 跳躍幅度 J

Merton 假設跳躍幅度 J 服從**對數常態分配**：

$$\ln J \sim N(\mu_J, \sigma_J^2)$$

- **μ_J**：跳躍幅度的對數均值（平均跳躍方向）
- **σ_J**：跳躍幅度的對數標準差（跳躍大小的離散程度）
- E[J] = exp(μ_J + σ_J²/2)

**重要選擇**：Merton 用對數常態是為了保持封閉解。其他分佈（如雙指數分佈的 Kou 模型）更貼近現實但計算更複雜。

## 封閉解

Merton 模型幸運地有**級數封閉解**——不需要蒙地卡羅：

$$C = \sum_{n=0}^{\infty} \frac{e^{-\lambda T}(\lambda T)^n}{n!} C_{BS}(S, K, T, r_n, \sigma_n)$$

其中：
- C_BS 是 Black-Scholes 公式
- 每一項對應 n 次跳躍的情況
- r_n = r − λ·E[J] + n·μ_J/T
- σ_n² = σ² + n·σ_J²/T

實務上取前 10-20 項就收斂。

## 與其他模型的比較

### vs. Black-Scholes

Black-Scholes 是 Merton 跳躍擴散的特例（λ=0）。Merton 模型在以下方面更優：

- 能產生**肥尾**——報酬分配的尾部比常態分配厚
- 能定價**短期價外選擇權**——跳躍風險讓低履約價 Put 的 IV 自然偏高
- 能解釋**跳空缺口**——連續模型做不到

但 Black-Scholes 參數更少（只有 σ），Merton 需要估計 λ、μ_J、σ_J 三個額外參數。

### vs. [[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston 隨機波動率模型]]

- **Heston**：波動率隨機變化但路徑連續——能解釋波動率聚集和微笑曲線形狀，但不能解釋極端跳空
- **Merton**：波動率常數但有跳躍——能解釋跳空和肥尾，但不能解釋波動率的時變性
- **Bates 模型**：Heston + Merton = 隨機波動率 + 跳躍，兩者結合。這是實務上最先進的選擇權定價模型之一

### vs. Variance Gamma / CGMY

更近代的 Lévy 過程模型（Variance Gamma、CGMY、Normal Inverse Gaussian）用更靈活的純跳躍過程取代擴散+跳躍的分離，能更精細地擬合報酬分配的特徵，但失去封閉解的便利性。

## 實戰應用
### 1. 選擇權定價與波動率微笑

Merton 跳躍模型產生的波動率微笑特徵：
- **短期微笑更深**：短期價外 Put 和 Call 的 IV 都比 ATM 高，因為跳躍風險在短期更集中
- **長期微笑較淺**：長期來看跳躍的影響被連續波動率稀釋
- **不對稱性**：如果 μ_J < 0（平均跳躍方向為負），會產生偏斜，低履約價 IV 更高

### 2. 尾部風險定價

跳躍風險溢價（jump risk premium）是選擇權賣方要求的額外補償：
- 市場的 IV 通常高於純擴散模型預測，差額部分就是跳躍風險溢價
- 與 [[風險管理/波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]]互補——後者補償連續波動率的不確定性，跳躍風險溢價補償突發事件

### 3. 賣方策略的風險管理

賣出價外 Put 的交易者：
- Black-Scholes 算出的 theta 報酬看起來很香
- 但 Merton 模型告訴你：跳躍風險讓「不會跌到那裡」的假設破產
- 1987 以前很多人賣價外 Put 賺穩定權利金，一次跳躍就歸零
- **教訓**：賣方必須考慮跳躍風險，不能只用連續波動率模型

### 4. 台股跳空風險

台股特有的跳躍風險來源：
- **隔夜美股跳空**：台股開盤直接反映昨夜美股變化
- **漲跌停板**：跌停時想賣也賣不掉，流動性跳躍
- **突發事件**：地緣政治、自然災害、政策變動

用 Merton 模型的 λ 參數可以量化台股的跳躍頻率。學術研究估計台股加權指數的 λ 約 2-5（每年 2-5 次顯著跳空），高於美股市場。

## 參數估計

### 從歷史數據估計

- **λ**：用每日報酬超過某門檻（如 3 個標準差）的頻率估計
- **μ_J 和 σ_J**：用超出門檻的報酬的樣本均值和標準差
- **σ（連續波動率）**：用剔除跳躍後的日報酬變異數

### 從選擇權市場校準

- 用市場選擇權報價反推 (λ, μ_J, σ_J, σ)
- 通常 μ_J 為負（市場傾向跳跌）
- σ_J 通常遠大於 σ（跳躍幅度遠大於日常波動）

## 注意事項
- **對數常態跳躍假設過簡**：實際跳躍幅度分佈可能更複雜（冪律尾巴等）
- **跳躍強度固定**：λ 是常數，但實際跳躍頻率有時變性（危機時 λ 飆升）
- **無法捕捉跳躍聚集**：一次大跳躍後常有更多跳躍（自激過程，可參考 [[操作策略/Hawkes自激點過程與交易應用Hawkes-Process-Trading|Hawkes 自激點過程]]）
- **封閉解收斂速度**：高 λ 時級數收斂慢，需更多項數

## 關鍵啟示

1. **市場不連續**——這是 Merton 跳躍模型最重要的哲學。Black-Scholes 的連續假設是簡化，不是真理
2. **尾部風險來自跳躍**—— VaR 和 ES 等風險指標如果只用連續模型，會系統性低估極端損失
3. **跳躍風險溢價是選擇權賣方的隱性報酬來源**——但也是炸彈，一次跳躍可以吃掉數月的權利金
4. **Heston + Merton = Bates** 是理解現代選擇權定價的必經之路——隨機波動率 + 跳躍，兩者缺一不可

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Merton, R. C. (1976). "Option Pricing When Underlying Stock Returns Are Discontinuous." *Journal of Financial Economics*, 3(1-2), 125-144.
- Kou, S. G. (2002). "A Jump-Diffusion Model for Option Pricing." *Management Science*, 48(8), 1086-1101.
- Bates, D. S. (1996). "Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutsche Mark Options." *Review of Financial Studies*, 9(1), 69-107.
- Cont, R., & Tankov, P. (2004). *Financial Modelling with Jump Processes*. Chapman & Hall/CRC.

---

*最後更新：2026-08-17*