---
title: Rough Heston粗糙Heston模型
aliases: [Rough Heston Model, 粗糙Heston模型, Rough Affine Volatility, Volterra Heston]
---

# Rough Heston粗糙Heston模型 (Rough Affine Volatility)

## 一句話解釋

Rough Heston 把經典 Heston 的平方根變異數改成帶冪次記憶核的 Volterra 過程，在保留非負變異數、槓桿效應與仿射轉換結構的同時，讓波動率路徑具有 $H<1/2$ 的粗糙度；代價是模型不再有限維 Markov，普通 Riccati 方程也升級成分數階 Riccati 方程。

## 為什麼要從Heston再往前走

[[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston 模型]]用 CIR 平方根過程描述瞬時變異數，優點是參數有經濟意義、變異數可維持非負，而且歐式選擇權可透過特徵函數快速定價。

問題是高頻波動率資料與超短天期隱含波動率常呈現更鋸齒的尺度：

- 對數波動率路徑的局部正則性常比標準布朗運動更低
- 短天期 ATM skew 可能隨到期縮短而快速變陡
- 單一均值回歸速度不一定能同時描述短端與長端記憶
- 為了硬追短期 skew，經典 Heston 的 vol-of-vol 與相關係數可能被校準器推到極端

Rough Heston 的做法不是加入一堆互相甩鍋的跳躍參數，而是改寫變異數衝擊如何跨時間傳遞。

## 模型結構

在風險中立測度下，可用以下簡化形式表示標的價格：

$$\frac{dS_t}{S_t}=(r-q)dt+\sqrt{V_t}\,dW_t^S$$

瞬時變異數不再用普通 SDE，而是用 Volterra 積分方程：

$$V_t=V_0+\int_0^t K(t-s)\kappa(\theta-V_s)ds+\int_0^t K(t-s)\nu\sqrt{V_s}\,dW_s^V$$

價格與變異數衝擊相關：

$$d\langle W^S,W^V\rangle_t=\rho\,dt$$

標準粗糙核可寫成：

$$K(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)},\qquad \alpha\in(1/2,1)$$

並令：

$$H=\alpha-\frac12\in(0,1/2)$$

因此 $H$ 控制局部粗糙度。當 $\alpha=1$、也就是 $H=1/2$ 時，$K(t)=1$，模型退化回經典 Heston。

不同論文會把 $\kappa$、$\nu$ 或核的正規化常數重新組合，抄參數前要先對定義。金融工程最常見的精密錯誤，就是公式長得差不多便當成完全一樣。

## 記憶核在做什麼

核 $K(t-s)$ 決定過去衝擊對現在變異數的權重。

當 $\alpha<1$ 時：

$$K(t-s)\propto(t-s)^{\alpha-1}$$

在 $s$ 接近 $t$ 時具有奇異性，表示最新衝擊對短期未來特別重要；較早衝擊則透過冪次衰減保留在狀態中。

這產生兩個效果：

- **局部粗糙**：變異數路徑比普通擴散更鋸齒
- **非Markov記憶**：預測未來不能只看當下 $V_t$，還要知道歷史如何進入卷積核

「粗糙」不是波動率數值很大，也不是一句「市場有長記憶」就講完。它首先描述的是短時間尺度下的路徑正則性；局部粗糙度與長期依賴不是同一件事。

## 參數分工

### $V_0$與$\theta$

- $V_0$ 影響近端 ATM 波動率水準
- $\theta$ 是長期變異數中樞
- 兩者仍保留 Heston 式的經濟解釋

### $\kappa$

$\kappa$ 控制均值回歸力量，但在 Volterra 模型中不能只把 $1/\kappa$ 當成唯一記憶期限，因為核本身已引入跨尺度記憶。

### $\nu$

$\nu$ 是 vol-of-vol，主要影響微笑曲率、變異數分布寬度與波動率商品風險。

### $\rho$

股票指數通常校準出負的 $\rho$：價格下跌時變異數上升，使左翼 Put IV 較高。

### $H$或$\alpha$

- $H$ 越小，路徑越粗糙
- 小 $H$ 能產生更陡的短天期 skew 尺度
- $H$ 與 $\nu$、$\rho$ 不是完全正交，校準時仍可能互相替代

## 與Rough Bergomi的根本差異

[[操作策略/Rough-Bergomi粗糙波動率模型Rough-Volatility|Rough Bergomi]]和 Rough Heston 都使用 rough kernel，但不是同一個模型換皮。

### Rough Heston

- 對瞬時變異數使用平方根型 Volterra 動態
- 保留 Heston 式均值回歸參數
- 屬於 rough affine volatility 家族
- 特徵函數可由分數階 Riccati 方程取得
- 適合傅立葉定價與仿射模型延伸

### Rough Bergomi

- 對數變異數是 Gaussian Volterra 指數模型
- 直接以初始遠期變異數曲線 $\xi_0(t)$ 錨定市場期限結構
- 變異數因指數形式自然為正
- 一般不具 Rough Heston 那種仿射特徵函數
- 定價通常更依賴蒙地卡羅

簡單說，rBergomi 是 forward variance 與 lognormal 結構優先；Rough Heston 是平方根變異數與 affine tractability 優先。兩個都粗糙，但 CPU 被折磨的方式不同。

## 仿射Volterra結構

經典 Heston 的核心計算優勢是對數價格特徵函數具有 exponential-affine 形式，係數由普通 Riccati ODE 決定。

Rough Heston 雖然非 Markov，仍保留無限維仿射結構。El Euch 與 Rosenbaum 證明，對數價格特徵函數仍可寫成類似 Heston 的指數形式，但係數函數改由分數階 Riccati 方程決定。

概念形式為：

$$D^\alpha h(u,t)=F(u,h(u,t))$$

其中 $D^\alpha$ 是分數階導數，而 $F$ 仍是 Heston 型的二次函數：

$$F(u,h)=c_0(u)+c_1(u)h+c_2h^2$$

當 $\alpha=1$ 時，分數階導數退化成普通一階導數，便回到經典 Heston Riccati 方程。

這個結果很重要：模型雖然失去低維 PDE，卻沒有被迫把所有歐式商品都丟進蒙地卡羅黑洞。

## 分數階Riccati方程的數值解

分數階 Riccati 方程通常沒有顯式解，可改寫成 Volterra 積分方程：

$$h(t)=\frac{1}{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}F(u,h(s))ds$$

常見解法包括：

- fractional Adams predictor-corrector
- 卷積求積法
- 高階分數階數值積分
- sum-of-exponentials 核近似
- 多因子 Markovian lift

直接在每個時間點回頭計算全部歷史卷積，成本通常接近 $O(N^2)$。用快速卷積或把冪次核近似成多個指數核，可把無限維記憶轉成有限個均值回歸因子，大幅加速重複定價。

## 定價方法

### 歐式香草選擇權

1. 數值解分數階 Riccati 方程
2. 建立對數價格特徵函數
3. 用 Fourier inversion、Carr-Madan FFT 或 COS method 定價
4. 反推出模型隱含波動率

這條路通常比全路徑蒙地卡羅有效率，尤其適合大量履約價的同期限切片。

### 路徑依賴商品

障礙、亞式、前向起始與其他路徑依賴商品仍常使用：

- Volterra Euler 類離散化
- 直接卷積模擬
- Markovian multi-factor approximation
- 混合精確與近似核方法
- 蒙地卡羅加控制變量、準蒙地卡羅或多層蒙地卡羅

平方根項要特別處理非負性。把普通 Euler 原封不動套上去，再把負變異數用絕對值修掉，雖然程式會跑，但那不叫模型，只叫把錯誤藏起來。

## 校準流程

1. 清理履約價、到期日、遠期價、利率、股利與 bid-ask
2. 建立無靜態套利的市場 IV 曲面
3. 用 ATM 期限結構初始化 $V_0$ 與 $\theta$
4. 用長短期限衝擊消退情況初始化 $\kappa$
5. 用 smile 曲率初始化 $\nu$
6. 用左右翼不對稱初始化 $\rho$
7. 用短天期 ATM skew 的期限尺度初始化 $H$
8. 跨多期限共同最小化模型 IV 誤差
9. 對參數加入合理邊界與逐日平滑懲罰
10. 用樣本外 smile dynamics、Greeks 與避險損益驗證

單日 RMSE 很小不代表模型很好。只代表優化器成功討好今天的報價，明天參數全部翻臉照樣算你倒楣。

## 交易與風控應用

### 短天期skew相對價值

Rough Heston 提供一套由 roughness、vol-of-vol 與槓桿相關性共同產生短端 skew 的基準。若市場左翼遠高於模型，可能反映：

- 已知事件跳躍
- 災難保險需求
- 造市商庫存壓力
- 報價流動性不足
- 模型缺少跳躍或期限化參數

不能看到模型價較低就直接賣 Put。模型沒有寫進去的炸彈，不會因為 Excel 顯示便宜就消失。

### 模型風險區間

可將 Rough Heston、經典 Heston、局部波動率與 rBergomi 對同一商品定價，差異可視為 smile dynamics 與路徑假設造成的模型風險區間。

### Greeks與曲面情境

除了 Delta、Gamma、Vega，至少要測試：

- ATM IV 平行上移
- 短端 skew steepening
- $H$ 改變造成的期限尺度重估
- vol-of-vol shock
- 現貨下跌與波動率上升的聯合情境
- 核近似階數改變造成的數值風險

## 模型限制

- **非Markov**：不能直接使用低維 PDE，歷史卷積增加計算量
- **分數階數值誤差**：步長、卷積權重與初始奇異性都會影響價格
- **參數識別困難**：$H$、$\nu$、$\rho$ 可能共同改變短期 skew
- **非負性實作不簡單**：平方根 Volterra 過程需要經過驗證的離散方法
- **純模型沒有價格跳躍**：財報、政策與隔夜缺口仍可能低估尾部
- **roughness估計有爭議**：市場微結構雜訊與時間聚合可能影響 $H$ 的估計
- **核外插是模型假設**：超長期限資料不足時，記憶結構不是市場直接告訴你的
- **校準快不等於避險好**：特徵函數能快速算香草價格，不代表路徑商品與動態 Greeks 自動正確

## 實戰檢查清單

- 核 $K(t)$ 的正規化與參考文獻是否一致
- 使用的是 $H$ 還是 $\alpha=H+1/2$
- $\nu$ 是否因核正規化不同而不可直接比較
- 分數階 Riccati 解是否通過 $\alpha\to1$ 的 Heston 極限測試
- 特徵函數是否滿足 $\phi(0)=1$
- 折現標的是否維持鞅性
- 時間網格是否解析了 $t=0$ 附近的核奇異性
- Markovian lift 的因子數是否足以覆蓋交易期限
- 模型 IV 誤差是否小於 bid-ask，而不是只追求小數點後幻覺
- 參數是否跨日穩定，且樣本外避險誤差有改善
- 已知事件是否需要額外跳躍或確定時點衝擊

## 關鍵啟示

1. Rough Heston 是 Heston 的 Volterra 粗糙化，不只是把波動率參數調大
2. $H=\alpha-1/2$ 控制局部粗糙度，$\alpha=1$ 時回到經典 Heston
3. 模型雖非 Markov，仍保留仿射結構，普通 Riccati 方程改為分數階 Riccati 方程
4. 相較 rBergomi，Rough Heston 更重視平方根變異數與特徵函數可計算性
5. 真正風險不只在參數，而在卷積核、數值離散、曲面外插與缺少跳躍

## 相關連結

- [[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model]]
- [[操作策略/Rough-Bergomi粗糙波動率模型Rough-Volatility]]
- [[操作策略/Hawkes自激點過程與交易應用Hawkes-Process-Trading]]
- [[操作策略/SVI隱含波動率曲面參數化Stochastic-Volatility-Inspired]]
- [[操作策略/方差交換與波動率衍生品Variance-Swap-and-Volatility-Derivatives]]
- [[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]

## 參考來源

- El Euch, O., & Rosenbaum, M. (2019). "The characteristic function of rough Heston models." *Mathematical Finance*, 29(1), 3-38. https://arxiv.org/abs/1609.02108
- Abi Jaber, E., Larsson, M., & Pulido, S. (2019). "Affine Volterra processes." *The Annals of Applied Probability*, 29(5), 3155-3200. https://doi.org/10.1214/19-AAP1477
- Gatheral, J., Jaisson, T., & Rosenbaum, M. (2018). "Volatility is rough." *Quantitative Finance*, 18(6), 933-949. https://doi.org/10.1080/14697688.2017.1393551

---

*最後更新：2026-08-20*
