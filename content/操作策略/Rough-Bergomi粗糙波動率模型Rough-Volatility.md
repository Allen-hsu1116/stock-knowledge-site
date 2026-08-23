---
title: Rough Bergomi粗糙波動率模型
aliases: [Rough Bergomi Model, rBergomi, Rough Volatility, 粗糙波動率模型]
---

# Rough Bergomi粗糙波動率模型 (Rough Volatility)


> Rough Bergomi 模型用 Hurst 指數 $H<1/2$ 的分數型 Volterra 核驅動對數變異數，讓波動率路徑比傳統布朗擴散更鋸齒、更不平滑；它以初始遠期變異數曲線、roughness、vol-of-vol 與價格波動率相關性，重現短天期陡峭 skew 和整張波動率曲面，但沒有便宜的封閉解，計算通常靠蒙地卡羅。
## 核心概念
Rough Bergomi 模型用 Hurst 指數 $H<1/2$ 的分數型 Volterra 核驅動對數變異數，讓波動率路徑比傳統布朗擴散更鋸齒、更不平滑；它以初始遠期變異數曲線、roughness、vol-of-vol 與價格波動率相關性，重現短天期陡峭 skew 和整張波動率曲面，但沒有便宜的封閉解，計算通常靠蒙地卡羅。

## 「粗糙」到底是什麼

一般人聽到 rough volatility，容易以為只是波動率很大。不是。這裡的「粗糙」是數學上的路徑正則性：波動率在很短時間尺度上變化得非常鋸齒，局部路徑比標準布朗運動更不平滑。

分數布朗運動的 Hurst 指數 $H$ 控制路徑粗糙度：

- $H=1/2$：局部粗糙度接近標準布朗運動
- $H<1/2$：反持續、變化更鋸齒，稱為 rough
- $H>1/2$：路徑較平滑，具有較強持續性

高頻實現變異數研究發現，對數波動率在合理時間尺度上可近似為 $H$ 約 0.1 的分數型過程。這個觀察促成 Rough Fractional Stochastic Volatility 與 rBergomi 模型。注意：小 $H$ 描述局部粗糙度，不等於一句「市場沒有長記憶」；局部正則性與長期依賴是不同問題，混在一起就像拿體溫計量身高。

## 為什麼傳統模型不夠

[[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston 模型]]的變異數由標準布朗運動驅動，具有 Markov 性與半封閉解，計算方便。但在實務上：

- 超短天期的平值 skew 常比 Heston 能產生的更陡
- 為了追短期翼端，Heston 參數可能被逼到不穩定或違反 Feller 條件
- 不同到期日常需要不同參數，單一均值回歸結構不一定夠彈性
- 波動率的高頻路徑看起來比標準擴散更粗糙

rBergomi 的核心不是再加十個參數，而是換掉波動率驅動核的局部尺度結構。Bayer、Friz 與 Gatheral 的研究指出，rBergomi 能以較少參數更好擬合 SPX 波動率曲面，並把模型預測與實際方差交換期限曲線連接起來。

## 模型結構

在零利率或使用折現後標的的簡化表示下：

$$\frac{dS_t}{S_t}=\sqrt{v_t}\,dZ_t$$

瞬時變異數寫成：

$$v_t=\xi_0(t)\exp\left(\eta W_t^H-\frac{1}{2}\eta^2t^{2H}\right)$$

其中分數型 Volterra 過程可寫為：

$$W_t^H=\sqrt{2H}\int_0^t(t-s)^{H-\frac{1}{2}}dW_s$$

價格與波動率衝擊相關：

$$d\langle Z,W\rangle_t=\rho dt$$

也可寫成：

$$Z_t=\rho W_t+\sqrt{1-\rho^2}W_t^{\perp}$$

$W^{\perp}$ 與 $W$ 獨立。

不同文獻可能把正規化常數吸收到 $\eta$ 中，所以公式外觀會略有不同。比較參數前要先確認定義，否則拿兩套不同單位的 $\eta$ 比大小，只是在精密地比錯。

## 四個核心輸入

### 初始遠期變異數曲線 $\xi_0(t)$

$\xi_0(t)$ 是今天對未來瞬時變異數的風險中立預期曲線，可由[[操作策略/方差交換與波動率衍生品Variance-Swap-and-Volatility-Derivatives|方差交換]]或平滑選擇權曲面推導。

在模型中：

$$E[v_t]=\xi_0(t)$$

指數中的 $-\frac12\eta^2t^{2H}$ 是高斯指數鞅修正，使變異數的期望維持在初始遠期曲線上。它把當下觀察到的波動率期限結構直接嵌進模型，而不是只用一個長期均值硬扛全部期限。

### Hurst指數 $H$

$H$ 控制粗糙度與短期尺度：

- $H$ 越小，波動率路徑越鋸齒
- 小 $H$ 可產生非常陡峭的短期 ATM skew
- $H$ 接近 $1/2$ 時，模型逐漸靠近較傳統的 lognormal volatility 結構

實證常看到 $H$ 約 0.1，但它不是全市場、全時期固定常數。資料頻率、微結構雜訊、估計方法與樣本區間都會影響結果。

### Vol-of-vol參數 $\eta$

$\eta$ 控制對數變異數的擾動幅度：

- 越高代表變異數分布越寬
- 微笑曲率與翼端通常更明顯
- 波動率商品與[[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|vol-of-vol]]風險更大

$H$ 與 $\eta$ 會共同影響曲面，校準時可能替代。不能看到 $\eta$ 大就直接宣布市場比較瘋，還得看採用的核與期限尺度。

### 相關係數 $\rho$

$\rho$ 控制價格與波動率衝擊聯動：

- 股票指數通常 $\rho<0$
- 價格下跌時變異數傾向上升，形成槓桿效應
- 越負通常讓左翼 IV 與負 skew 越明顯

$H$ 主要控制短期 skew 的期限尺度，$\rho$ 控制方向與幅度，$\eta$ 則參與整體曲率。三者不是完全正交，校準照樣會互相踩腳。

## 為什麼短期skew特別重要

市場常觀察到 ATM skew 的絕對值在到期時間縮短時快速增加。傳統 Markov 隨機波動率模型對短期 skew 的尺度限制較強，而 rough volatility 的奇異核：

$$K(t-s)\propto(t-s)^{H-\frac12}$$

在 $H<1/2$ 時，靠近當下的權重具有奇異性，使最新波動率衝擊對短期未來特別重要。結果是模型能以自然尺度產生陡峭短期 skew，而不必只靠極端 vol-of-vol 或跳躍參數硬拗。

這不代表所有短期尾部都由 roughness 解釋。已知事件、隔夜跳空與流動性斷裂仍可能需要顯式跳躍模型。粗糙和跳躍可以共存，金融市場沒有義務只選一種方式搞你。

## Forward variance視角

rBergomi 屬於 forward variance model。建模重心不是只追蹤當下 $v_t$，而是追蹤整條未來變異數條件期望曲線：

$$\xi_t(u)=E_t[v_u],\quad u\ge t$$

好處包括：

- 今日曲線可直接對接市場方差期限結構
- 變異數衍生品的經濟意義較清楚
- 不需要用單一 $\theta$ 把長短期限全塞進一個均值回歸水準
- 可以分析波動率曲線受新資訊衝擊後如何整體重排

但狀態變數變成一條曲線，模型因此通常是無限維且非 Markov。理論很漂亮，CPU 看完則想離職。

## 非Markov與非半鞅問題

當 $H\ne1/2$ 時，分數型驅動通常不是有限維 Markov 過程；波動率因子本身也不是一般 Itô 半鞅。重要區分是：

- 標的價格仍可在適當條件下用 Itô 積分表示
- 波動率驅動具有記憶核與非 Markov 結構
- 不能直接把 Heston 的 PDE 與封閉解原封不動搬過來
- 歷史路徑或整條 forward variance curve 會影響未來分布

這是 rBergomi 靈活度的來源，也是計算成本的來源。

## 定價方法

rBergomi 通常沒有 Heston 那種便宜的歐式選擇權半封閉解，主流方法是蒙地卡羅：

1. 在時間網格上模擬分數型高斯過程 $W^H$
2. 由 $W^H$ 與 $\xi_0(t)$ 建立 $v_t$
3. 用相關布朗運動模擬標的價格
4. 計算路徑終值或路徑依賴 payoff
5. 平均、折現並反推出模型 IV

直接用普通 Euler/Riemann 和處理奇異核會有明顯偏差。Bennedsen、Lunde 與 Pakkanen 的 hybrid scheme：

- 在靠近奇異點的前幾格保留冪次核的精確積分結構
- 較遠處再用階梯或 Riemann 近似
- 在相近計算複雜度下，大幅降低粗糙區域的均方誤差
- 其實驗顯示，rBergomi 模擬出的 IV smile 可與精確高斯模擬幾乎無法區分

其他加速方法包括：

- Cholesky 精確高斯模擬，準確但網格大時昂貴
- FFT convolution
- Markovian lift，以多個指數核近似冪次核
- 多因子近似與量化壓縮
- quasi-Monte Carlo、控制變量與多層蒙地卡羅
- 神經網路代理模型，用於大量重複校準

## 校準流程

1. 清理選擇權報價並建立無靜態套利 IV 曲面
2. 從市場方差期限結構取得或參數化 $\xi_0(t)$
3. 以短天期 ATM skew 的期限尺度初始化 $H$
4. 以 smile 曲率與波動率商品初始化 $\eta$
5. 以左右不對稱與槓桿效應初始化 $\rho$
6. 用多期限、多履約價共同最小化模型 IV 誤差
7. 使用固定亂數、common random numbers 與控制變量降低目標函數雜訊
8. 檢查不同網格、路徑數與模擬方法下參數是否穩定
9. 比較樣本外 smile 動態與 Greeks，而非只看當日擬合

由於每次目標函數評估都可能包含蒙地卡羅，暴力全域搜尋非常貴。代理模型可以加速，但代理誤差必須和蒙地卡羅誤差、報價誤差分開監控，否則模型裡又套模型，最後只剩信仰。

## Greeks與避險

rBergomi 的 Delta、Vega 與更高階 Greeks 可透過：

- bump-and-revalue
- pathwise derivative
- likelihood ratio
- 自動微分
- 代理模型微分

風控重點不只是一個 Vega。整條 $\xi_0(t)$ 曲線都有期限桶風險，$H$、$\eta$、$\rho$ 改變也會扭曲整張 smile。應搭配[[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|進階 Greeks]]與曲面情境測試，至少觀察：

- ATM level shift
- skew steepening 或 flattening
- vol-of-vol shock
- 短端與長端方差曲線 twist
- 價格下跌與波動率上升的聯合情境

## 實戰應用
### 短天期skew相對價值

模型能提供短天期 Put skew 的動態基準。若市場 skew 比模型更陡，可能是事件跳躍、供需擁擠或避險需求，不應自動解讀為無風險錯價。

### 方差期限結構

因 $\xi_0(t)$ 直接進模型，可分析近月與遠月方差價格、曲線斜率與 roll-down。它適合連結[[風險管理/波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]]、方差交換與選擇權 smile，而不是只把每個到期日分開看成孤島。

### 模型風險比較

對障礙、前向起始或波動率衍生品，可同時用 Heston、局部波動率與 rBergomi 定價。價格差不是誰一定錯，而是不同微笑動態與路徑假設的模型風險區間。

## 注意事項
- **計算昂貴**：通常依賴大量蒙地卡羅與細時間網格
- **非Markov**：不能直接使用低維 PDE，歷史記憶增加實作複雜度
- **參數識別**：$H$、$\eta$ 與 $\rho$ 對曲面效果並非完全分離
- **roughness估計有爭議**：微結構雜訊、估計偏差與時間聚合都可能影響小 $H$ 結論
- **沒有顯式跳躍**：純 rBergomi 路徑連續，事件尾部未必足夠
- **初始曲線依賴資料**：$\xi_0(t)$ 的品質取決於方差曲線與 IV 曲面清理
- **外插仍是模型假設**：深尾與超長期限沒有免費真相
- **數值誤差會污染校準**：網格偏差與蒙地卡羅噪音可能被優化器誤認成市場訊號

## 與其他模型的定位

- **Heston**：有限維 Markov、計算快、半封閉解；短期 skew 彈性較弱
- **SABR**：參數少且有快速近似公式，利率與 FX 交易桌常用
- **Dupire local vol**：精確擬合今天的香草曲面，但微笑動態可能失真
- **rBergomi**：以 rough kernel 改善短期 skew 與 forward variance 動態，計算最重
- **跳躍擴散**：以不連續事件產生肥尾；和 roughness 解釋的是不同機制

## 實戰檢查清單

- $H$ 的定義與核正規化是否和參考實作一致
- $\eta$ 是否因不同正規化而使用不同單位
- $\xi_0(t)$ 是否由無套利曲面與可靠方差期限資料取得
- 時間網格是否足以解析核在零附近的奇異性
- 是否使用 hybrid scheme 或經驗證的替代方法
- 蒙地卡羅標準誤是否小於 bid-ask 與校準容忍度
- 不同亂數種子與路徑數下參數是否穩定
- 是否檢查 discounted spot 的鞅性與離散化偏差
- Greeks 是否包含整條 forward variance curve 的桶狀風險
- 已知事件是否需要額外跳躍，而不是全塞給小 $H$

## 關鍵啟示

1. Rough volatility 的「rough」是局部路徑不平滑，不是單純波動率很高
2. 小 $H$ 改變短期尺度，能自然產生陡峭的短天期 skew
3. 初始遠期變異數曲線把當下波動率期限結構直接嵌入模型，是 rBergomi 的核心輸入
4. 擬合能力不是免費午餐；非 Markov 記憶核把複雜度從參數表搬進了計算引擎

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Bayer, C., Friz, P., & Gatheral, J. (2016). "Pricing under rough volatility." *Quantitative Finance*, 16(6), 887-904. https://doi.org/10.1080/14697688.2015.1099717
- Bayer, C., Friz, P., & Gatheral, J. (2015). SSRN 2554754. https://doi.org/10.2139/ssrn.2554754
- Bennedsen, M., Lunde, A., & Pakkanen, M. S. (2017). "Hybrid scheme for Brownian semistationary processes." *Finance and Stochastics*, 21, 931-965. https://arxiv.org/abs/1507.03004
- Gatheral, J., Jaisson, T., & Rosenbaum, M. (2018). "Volatility is rough." *Quantitative Finance*, 18(6), 933-949.

---

*最後更新：2026-08-19*
