---
title: Heston隨機波動率模型
aliases: [Heston Model, Stochastic Volatility Model, 隨機波動率模型]
---

# Heston隨機波動率模型 (Heston Stochastic Volatility Model)

## 一句話解釋

Black-Scholes 假設波動率是常數，但現實中波動率會隨機變動。Steven Heston 1993 年提出讓波動率自己也是一個隨機過程，用 CIR (Cox-Ingersoll-Ross) 平方根過程驅動，能同時定價選擇權和重現波動率微笑。

## 背景與動機

[[操作策略/Black-Scholes定價模型|Black-Scholes 模型]]的核心假設之一是波動率 σ 為常數。這在實務上有明顯缺陷：

- **波動率微笑**：同一到期日、不同履約價的選擇權，算出來的隱含波動率不一樣，形成 U 型曲線
- **波動率聚集**：高波動後跟著高波動，低波動後跟著低波動（[[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting|GARCH 模型]]就是在描述這個現象）
- **肥尾效應**：實際報酬分配的尾部比常態分配厚，常數波動率無法解釋

Heston 的突破在於：把波動率也當成一個服從隨機微分方程的變數，而不是常數。

## 模型數學結構

### 股價過程

$$dS_t = \mu S_t \, dt + \sqrt{v_t} S_t \, dW_t^{(1)}$$

- S_t：股價
- v_t：瞬時變異數（instantaneous variance），即 σ²
- W^(1)：布朗運動

### 變異數過程（CIR 平方根過程）

$$dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}$$

五個參數的意義：

- **v_0**：初始變異數
- **θ (theta)**：變異數的長期均值——波動率最終回歸的水平
- **κ (kappa)**：均值回歸速度——κ 越大，回到 θ 的速度越快
- **ξ (xi)**：波動率的波動率（vol of vol）——控制變異數過程的擾動強度
- **ρ (rho)**：兩個布朗運動的相關係數，W^(1) 和 W^(2) 的關聯度

### Feller 條件

為確保變異數 v_t 恆正（不會變負數），需要滿足：

$$2\kappa\theta > \xi^2$$

實務上很多選擇權數據違反 Feller 條件，但模型仍能近似使用，只是 v_t 可能在邊界附近行為不完美。

### 相關係數 ρ 的關鍵角色

- **ρ < 0（負相關）**：股價跌時波動率漲，這就是**槓桿效應**（leverage effect）。絕大多數股票和指數的 ρ 都是負的，通常在 -0.5 到 -0.9 之間。負 ρ 產生偏斜（skew），即低履約價 Put 的 IV 高於高履約價 Call 的 IV
- **ρ = 0**：股價和波動率獨立，產生對稱的微笑曲線
- **ρ > 0**：少見，某些商品市場可能出現（價格漲帶動波動率漲）

## 封閉解

Heston 模型最大的優勢之一是**歐式選擇權有半封閉解**（semi-analytical solution），不需要蒙地卡羅模擬就能算價格：

$$C = S_0 e^{-qT} P_1 - K e^{-rT} P_2$$

其中 P_1 和 P_2 透過特徵函數的反傅立葉轉換求得。這讓校準（calibration）比純模擬模型快很多。

## 與其他波動率模型的比較

- **Black-Scholes**：常數波動率，無法解釋微笑。Heston 是它的推廣
- **[[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting|GARCH]]**：離散時間的波動率模型，波動率是過去的函數。Heston 是連續時間，更適合選擇權定價
- **Local Volatility (Dupire)**：波動率是股價和時間的確定性函數 σ(S,t)，可以完美擬合市場報價但外插能力差。Heston 是隨機的，擬合不完美但前瞻性更好
- **SABR**：另一種隨機波動率模型，主要用於利率衍生品。Heston 更常用於股票和外匯

## 校準實務

校準就是找到 (v_0, θ, κ, ξ, ρ) 五個參數，使模型價格最接近市場報價。常見做法：

1. **目標函數**：最小化模型價格與市場價格的平方差（或 IV 的平方差）
2. **優化方法**：Levenberg-Marquardt、Nelder-Mead、或全域優化如差分進化
3. **市場數據**：用同一到期日多個履約價的選擇權報價

**校準陷阱**：
- 參數不穩定——每天校準出來的參數跳動很大，影響希臘字母的穩定性
- 過度擬合——完美擬合當前微笑但對未來預測力差
- 解不唯一——不同參數組合可能產生相近的價格曲面

## 交易應用

### 1. 波動率曲面建模

用 Heston 模型校準出來的波動率曲面，可以用來：
- 定價場外奇異選擇權（barrier、Asian、cliquet 等）
- 找出市場報價中的套利機會（某些履約價的 IV 偏離模型曲面）
- 計算 [[操作策略/選擇權Greeks希臟字母|Greeks]] 時納入 vega 和 vanna 的波動率敏感度

### 2. 波動率套利

當市場 IV 和 Heston 模型隱含的「合理」波動率有偏差時：
- 如果市場 IV 系統性高於模型，可能意味著 [[風險管理/波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]] 偏高，適合賣出選擇權
- 負 ρ 意味著左尾風險被市場高估，Put 的 IV 偏高，可以考慮 Put 比例價差

### 3. VIX 相關交易

VIX 本質上是 S&P 500 選擇權的隱含波動率指數。Heston 模型可以：
- 估計 VIX 的理論水準
- 定價 VIX 選擇權和期貨（雖然 VIX 本身的動態更複雜）

## 模型限制

- **校準不穩定**：κ 和 ξ 的估計在不同時間窗口差異很大
- **無法完美擬合短期微笑**：Heston 產生的微笑曲線形狀不夠靈活，尤其對短期價外選擇權
- **跳躍風險未考慮**：純擴散過程無法捕捉市場崩盤時的跳躍，需要結合 Merton 跳躍擴散模型
- **計算複雜度**：雖然有半封閉解，但特徵函數的數值積分仍需小心處理分支問題

## 實作要點

在 Python 中可以用 `QuantLib` 或 `fftpacked` 來實作：

- **QuantLib**：內建 HestonModel 和 HestonEngine，校準用 HestonModelHelper
- **自建**：用特徵函數 + FFT（Fast Fourier Transform）計算選擇權價格，Lewis 2001 或 Carr-Madan 方法
- **校準稳定性**：建議固定 v_0 用當日 ATM IV 平方，只校準其他四個參數，可减少不穩定性

## 關鍵啟示

1. 波動率不是常數，它有自己的隨機動態——這是選擇權交易者必須內化的概念
2. 負相關係數 ρ 是股票市場的常態，理解它就能理解為什麼 Put 比 Call 貴
3. Heston 不是萬能的——校準穩定性是實務上最大的痛點，但作為理解波動率曲面的框架仍然是最重要的基礎模型
4. 與 [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|VVIX]] 的概念呼應：ξ 參數就是「波動率的波動率」的數學化表達

## 參考來源

- Heston, S. L. (1993). "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options." *Review of Financial Studies*, 6(2), 327-343.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Cox, J., Ingersoll, J., & Ross, S. (1985). "A Theory of the Term Structure of Interest Rates." *Econometrica*, 53(2), 385-407.

---

*最後更新：2026-08-17*