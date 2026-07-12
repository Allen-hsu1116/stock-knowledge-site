# Copula 連接函數與尾部相依性 Copula and Tail Dependence

> **Sklar's Theorem (1959)** 的核心洞察——將多變量聯合分佈拆解為「各資產的邊際分佈」和「資產間的相依結構」兩個獨立部分。Copula 是描述相依結構的數學函數，讓我們能精確建模金融資產在危機時「一起跌」的現象——尾部相依性。

## 核心概念

### 為什麼需要 Copula？

傳統的相關係數（Pearson Correlation）只衡量**線性關係**，有三大致命缺陷：

1. **只捕捉線性關係**：如果 A 和 B 的關係是「平時不相關，危機時一起暴跌」，Pearson 相關係數接近 0，但尾部相依性極高
2. **假設邊際分佈是常態**：金融報酬分佈有肥尾，常態假設嚴重低估極端事件
3. **不區分上尾和下尾**：股市上漲時各股可以不相關，但下跌時往往高度相關（相關性崩潰）

**Copula 解決這三個問題**：分離邊際分佈與相依結構，精確建模尾部行為。

### Sklar's Theorem

對於任何多變量聯合分佈函數 $F(x_1, x_2, ..., x_n)$，存在一個 Copula 函數 $C$ 使得：

$$
F(x_1, x_2, ..., x_n) = C(F_1(x_1), F_2(x_2), ..., F_n(x_n))
$$

其中 $F_i(x_i)$ 是各變量的邊際分佈函數。

**翻譯成人話**：聯合分佈 = Copula（相依結構） × 各自的邊際分佈。你可以用任何邊際分佈（例如 Student-t）搭配任何 Copula（例如 Gaussian 或 t-Copula），靈活組合。

## 常見 Copula 函數

### 一、Gaussian Copula（高斯 Copula）

$$
C(u_1, u_2) = \Phi_\rho(\Phi^{-1}(u_1), \Phi^{-1}(u_2))
$$

- 基於多變量常態分佈
- **缺點**：尾部相依性為零——意味著極端事件不會同時發生，這在金融市場嚴重失真
- **優點**：計算簡單，參數只有相關矩陣
- **Li (2000) 的 Gaussian Copula 模型**：用於 CDO 定價，被指為 2008 金融危機的「公式殺手」

### 二、Student-t Copula（t Copula）

$$
C(u_1, u_2) = t_{\rho,\nu}(t_\nu^{-1}(u_1), t_\nu^{-1}(u_2))
$$

- 基於多變量 t 分佈
- **優點**：具有尾部相依性，極端事件可以同時發生
- 自由度 ν 越小，尾部越肥，尾部相依性越強
- **缺點**：上尾和下尾對稱（上尾相依 = 下尾相依），但金融市場通常下尾相依 > 上尾相依

### 三、Clayton Copula

$$
C(u_1, u_2) = (u_1^{-\theta} + u_2^{-\theta} - 1)^{-1/\theta}
$$

- **非對稱尾部相依**：下尾相依性高、上尾相依性為零
- 最適合描述「平時各自走，暴跌時一起跌」的金融行為
- 參數 θ > 0，越大代表下尾相依越強

### 四、Gumbel Copula

$$
C(u_1, u_2) = \exp\left(-\left[(-\ln u_1)^\theta + (-\ln u_2)^\theta\right]^{1/\theta}\right)
$$

- **非對稱尾部相依**：上尾相依性高、下尾相依性為零
- 適合描述「平時各自走，暴漲時一起漲」的行為（如泡沫資產）

### 五、Frank Copula

- 尾部相依性為零（類似 Gaussian），但允許負相依
- 適合無明顯尾部相依的資產組合

### 六、Joe-Clayton / BB1 Copula

- 允許上尾和下尾相依性獨立設定
- 最靈活但參數最多，過擬合風險高

## 尾部相依性 Tail Dependence

### 定義

**下尾相依係數（Lower Tail Dependence）**：

$$
\lambda_L = \lim_{u \to 0^+} P(U_2 \leq u \mid U_1 \leq u)
$$

**上尾相依係數（Upper Tail Dependence）**：

$$
\lambda_U = \lim_{u \to 1^-} P(U_2 > u \mid U_1 > u)
$$

**翻譯**：當 A 資產暴跌時（跌到底部 5%），B 資產也暴跌的機率有多大？

- λ = 0：尾部獨立（極端事件不同時發生）
- λ = 1：尾部完全相依（一個暴跌另一個必暴跌）
- 金融市場的特徵：下尾 λ_L > 0，上尾 λ_U ≈ 0（或 λ_L > λ_U）

### 各 Copula 的尾部相依性

- **Gaussian**：λ_L = λ_U = 0（無尾部相依，除非完全相關）
- **Student-t**：λ_L = λ_U > 0（對稱尾部相依）
- **Clayton**：λ_L > 0, λ_U = 0（下尾相依，上尾獨立）
- **Gumbel**：λ_L = 0, λ_U > 0（上尾相依，下尾獨立）
- **Joe**：λ_L = 0, λ_U > 0（類似 Gumbel）

## 金融市場的 Copula 實證

### 正常時期 vs 危機時期

- **正常時期**：資產間相關性低，Gaussian Copula 可能足夠
- **危機時期**：相關性急升（趨近 1），只有 t-Copula 或 Clayton Copula 才能描述
- **這就是 [[風險管理/相關性崩潰Correlation-Breakdown|相關性崩潰]] 的數學本質**：Copula 的參數在危機時發生結構性變化

### 2008 金融危機的教訓

- Li (2000) 的 Gaussian Copula 模型被廣泛用於 CDO 定價
- 模型假設房貸違約的相依結構可以用 Gaussian Copula 描述
- 實際上房貸違約具有極強的下尾相依性（房價崩跌時所有房貸一起違約）
- Gaussian Copula 的零尾部相依假設嚴重低估了系統性違約風險
- Warren Buffett 稱衍生品為「大規模毀滅性金融武器」，Copula 模型的誤用是原因之一

### 混合 Copula（Mixture Copula）

實務上可以用混合 Copula 描述不同市場狀態：

$$
C_{mix} = \pi \cdot C_{Gaussian} + (1-\pi) \cdot C_{Clayton}
$$

- π 代表「正常狀態」的權重
- (1-π) 代表「危機狀態」的權重
- 類似 [[風險管理/波動率體制轉換模型Volatility-Regime-Switching-Model|波動率體制轉換模型]] 的概念，但應用於相依結構

## 實戰應用

### 一、投資組合風險評估

傳統 VaR 用 Pearson 相關係數，低估危機時的組合風險。改用 Copula 模型：

1. 估計各資產的邊際分佈（例如用 EVT/GARCH 擬合肥尾）
2. 估計 Copula 參數（例如 t-Copula 的相關矩陣 + 自由度）
3. 用 Copula 模擬聯合分佈，計算 Copula-VaR
4. Copula-VaR 通常 > 傳統 VaR，因為它捕捉了尾部相依

### 二、信用風險定價

- CDO/CLO 等結構型信用產品的定價依賴違約相依性建模
- t-Copula 或 Clayton Copula 更適合描述違約的尾部相依
- Basel III 的信用風險模型已逐步引入 Copula 方法

### 三、配對交易選擇

- 傳統配對交易用相關係數篩選，可能選到「平時相關但危機時脫鉤」的假配對
- 用 Clayton Copula 的下尾相依係數篩選，能找到「平時各自走、極端時一起動」的真配對
- 與 [[操作策略/共整合檢定Cointegration-Test|共整合檢定]] 互補：共整合看長期均衡，Copula 看尾部行為

### 四、分散投資驗證

- 計算投資組合中各資產對的 Clayton 下尾相依係數
- 下尾相依高的資產組合，在危機時分散效果崩潰
- 選擇下尾相依低的資產組合，才能在危機中真正分散

## 估計方法

### 一、Inference Functions for Margins (IFM)

1. 第一步：用最大概似法估計各資產的邊際分佈參數
2. 第二步：固定邊際參數，估計 Copula 參數
- 優點：計算簡單，兩步分開
- 缺點：估計效率不如聯合估計

### 二、全最大概似法（Full MLE）

同時估計所有邊際和 Copula 參數，精度最高但計算量大。

### 三、基於經驗分佈的非參數估計

用經驗 CDF 代替理論邊際，直接估計 Copula。適合邊際分佈難以確定的情況。

## 優缺點

### 優點
- 分離邊際分佈與相依結構，靈活組合
- 精確建模尾部相依性，補 Pearson 相關係數的不足
- 可描述非對稱相依（上尾 vs 下尾）
- 廣泛應用於信用風險、組合風險、配對交易

### 缺點
- 計算複雜度高，實務上需要專業軟體
- 樣本量要求大，小樣本估計不穩定
- 模型風險：選錯 Copula 族可能比不用 Copula 更危險
- 參數不穩定：危機前估計的 Copula 參數在危機中可能失效
- 維度詛咒：資產數量增加時，高維 Copula 估計極困難
- Gaussian Copula 的誤用是 2008 危機的重要原因

## 與其他風險管理的關係

- **與 [[風險管理/相關性崩潰Correlation-Breakdown|相關性崩潰]] 的關係**：相關性崩潰是 Copula 參數在危機時變化的現象，Copula 是其數學描述
- **與 [[風險管理/相關性風險Correlation-Risk|相關性風險]] 的關係**：Correlation Risk 是 Copula 參數不確定性的風險
- **與 [[風險管理/VaR風險值Value-at-Risk|VaR]] 的關係**：Copula-VaR 是 VaR 的進階版，考慮尾部相依
- **與 [[風險管理/CVaR條件風險價值Conditional-Value-at-Risk|CVaR]] 的關係**：Copula-CVaR 比 Copula-VaR 更穩健，因為 CVaR 是一致性風險測度
- **與 [[風險管理/極端值理論EVT量化肥尾風險|EVT 極值理論]] 的關係**：EVT 擬合單變量尾部，Copula 連接多變量尾部，兩者組合 = 完整的尾部風險建模
- **與 [[風險管理/分散投資七法與相關係數Diversification-Seven-Methods|分散投資]] 的關係**：Copula 下尾相依係數量化分散在危機時的失效程度

## 注意事項

（待補充）

## 相關主題

（待補充）

## 來源

- Sklar, A. (1959). "Fonctions de répartition à n dimensions et leurs marges"
- Li, D. X. (2000). "On Default Correlation: A Copula Function Approach" — Gaussian Copula 模型論文（爭議性）
- Nelsen, R. B. (2006). *An Introduction to Copulas*
- Embrechts, P., McNeil, A., Straumann, D. (2002). "Correlation and Dependence in Risk Management"
- Salmon, F. (2009). "Recipe for Disaster: The Formula That Killed Wall Street" — Wired 雜誌對 Gaussian Copula 危機的深度報導

---

**相關筆記**：
- [[風險管理/相關性崩潰Correlation-Breakdown|相關性崩潰 Correlation Breakdown]]
- [[風險管理/相關性風險Correlation-Risk|相關性風險 Correlation Risk]]
- [[風險管理/VaR風險值Value-at-Risk|VaR 風險值]]
- [[風險管理/CVaR條件風險價值Conditional-Value-at-Risk|CVaR 條件風險價值]]
- [[風險管理/極端值理論EVT量化肥尾風險|EVT 極值理論]]
- [[風險管理/分散投資七法與相關係數Diversification-Seven-Methods|分散投資七法與相關係數]]
- [[風險管理/投資組合相關性分析實戰Portfolio-Correlation-Analysis-in-Practice|投資組合相關性分析實戰]]
- [[操作策略/共整合檢定Cointegration-Test|共整合檢定]]
- [[操作策略/配對交易進階實戰|配對交易進階實戰]]