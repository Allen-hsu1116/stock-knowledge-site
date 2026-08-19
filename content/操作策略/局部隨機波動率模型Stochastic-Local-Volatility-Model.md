---
title: 局部隨機波動率模型
aliases: [Stochastic Local Volatility Model, SLV Model, Local Stochastic Volatility, 局部隨機波動率]
---

# 局部隨機波動率模型 (Stochastic Local Volatility Model)

## 一句話解釋

局部隨機波動率模型把 Dupire 的局部波動率與 Heston 類隨機變異數相乘：用 leverage function 精確對齊今天的香草選擇權曲面，再用隨機波動率因子改善明天的微笑動態與奇異選擇權路徑；它想兩邊都拿，結果校準變成含條件期望的非線性逆問題，數值工程也跟著長牙齒。

## 為什麼要把兩種模型混在一起

[[操作策略/Dupire局部波動率模型Dupire-Local-Volatility-Model|Dupire 局部波動率模型]]的優點是理論上能精確匹配任何無靜態套利的香草選擇權曲面，但波動率完全由當下價格與時間決定，微笑動態與避險行為可能不符合市場。

[[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston 隨機波動率模型]]讓變異數本身隨機，能描述槓桿效應、波動率聚集與較合理的 smile dynamics，但少量參數未必能精確擬合每個期限與履約價，短天期尤其容易殘差明顯。

SLV 的企圖是：

- 以 local volatility 保留香草曲面的靜態一致性
- 以 stochastic volatility 引入額外波動率風險因子
- 讓障礙、亞式、前向起始等路徑依賴商品有更合理動態
- 透過少數隨機波動率參數控制 smile dynamics，再用 leverage function 補齊橫截面

所以它不是把兩個波動率直接相加，而是把局部調整函數與隨機因子相乘。

## 典型Heston-SLV結構

在風險中立測度下，一個常見規格是：

$$dS_t=(r-q)S_tdt+L(t,S_t)\sqrt{V_t}S_tdW_t^S$$

$$dV_t=\kappa(\theta-V_t)dt+\xi\sqrt{V_t}dW_t^V$$

$$dW_t^SdW_t^V=\rho dt$$

其中：

- $S_t$：標的價格
- $V_t$：隨機變異數因子
- $L(t,S)$：leverage function，局部槓桿函數
- $\kappa$：均值回歸速度
- $\theta$：長期變異數水準
- $\xi$：vol-of-vol
- $\rho$：價格與變異數衝擊相關係數

退化情況很直觀：

- $L(t,S)\equiv1$：回到純 Heston 型隨機波動率
- $V_t$ 退化成確定值並由 $L$ 吸收：接近純局部波動率
- 降低 $\xi$ 與 $\rho$ 的混合強度：動態逐漸靠近 local vol

隨機部分不一定非用 Heston，也可換成 SABR、inverse-gamma 或多因子模型。實務上 Heston-SLV 常見，是因為參數可解讀、數值工具成熟，而且大家已經被 Heston 折磨得很熟了。

## Gyöngy投影與核心校準公式

SLV 要與市場 local vol 具有相同的單一期限邊際分布，必須滿足 Markovian projection 關係：

$$\sigma_{loc}^2(t,S)=E\left[V_tL^2(t,S_t)\mid S_t=S\right]$$

因為在條件 $S_t=S$ 下，$L(t,S)$ 是確定值，所以：

$$\sigma_{loc}^2(t,S)=L^2(t,S)E\left[V_t\mid S_t=S\right]$$

因此 leverage function 應為：

$$L(t,S)=\frac{\sigma_{loc}(t,S)}{\sqrt{E[V_t\mid S_t=S]}}$$

這條式子看似一行結束，實際上是整個模型最靠北的地方。$L$ 需要條件期望 $E[V_t\mid S_t=S]$，但 $(S_t,V_t)$ 的聯合分布又由包含 $L$ 的 SDE 決定，所以它是一個隱式固定點問題，不是把兩個現成曲面相除就下班。

## 為什麼能匹配香草曲面

Dupire local vol 與 SLV 若在每個 $(t,S)$ 滿足上面的條件變異數投影，就具有相同的標的邊際分布：

$$S_t^{SLV}\overset{d}{=}S_t^{LV}$$

歐式香草選擇權 payoff 只依賴到期終值 $S_T$，因此兩者可有相同的歐式價格。可是路徑依賴商品不只看終值：

- 障礙選擇權在意途中是否碰到 barrier
- 亞式選擇權在意整段平均價格
- 前向起始選擇權在意未來某時點的 smile
- cliquet 在意多段局部報酬

SLV 與 local vol 的邊際分布可相同，聯合路徑分布仍不同。這就是 SLV 存在的主要價值，也是模型風險的主要來源。

## Fokker-Planck方法

令 $p(t,S,V)$ 為 $(S_t,V_t)$ 的聯合密度。它滿足二維 Fokker-Planck 前向方程，包含：

- 價格方向漂移
- 變異數方向均值回歸
- 價格方向二階擴散
- 變異數方向二階擴散
- 由 $\rho$ 產生的混合二階導數

條件期望可由聯合密度計算：

$$E[V_t\mid S_t=S]=\frac{\int_0^{\infty}Vp(t,S,V)dV}{\int_0^{\infty}p(t,S,V)dV}$$

典型迭代如下：

1. 給定前一時間層的 $L(t,S)$
2. 解聯合密度的 Fokker-Planck PDE
3. 由密度計算條件期望
4. 用投影公式更新 $L(t,S)$
5. 向下一時間層推進
6. 最後重建 local vol 與香草價格，檢查是否回復市場曲面

二維 PDE 常用 ADI，例如 Douglas、Douglas-Rachford、Craig-Sneyd 或 Hundsdorfer-Verwer。邊界條件、零通量處理、初始 Dirac mass 平滑與交叉項離散化都會影響穩定性，不是套個 PDE library 就會自動長出正確答案。

## 粒子法與條件期望估計

另一條路是蒙地卡羅粒子法：

1. 模擬大量 $(S_t,V_t)$ 粒子
2. 在每個時間點，用核回歸、分箱或局部回歸估計 $E[V_t\mid S_t=S]$
3. 更新 leverage function
4. 用新 $L$ 繼續模擬下一時間步

優點：

- 容易擴充隨機利率、多因子波動率與其他狀態變數
- 避免高維 PDE 的維度災難
- 可與奇異選擇權定價共用模擬框架

缺點：

- 條件期望估計有統計噪音
- 深價內外區域粒子稀疏，分母接近零
- $L$ 的更新噪音會回饋到下一步路徑
- 核帶寬、分箱與時間步都是隱含模型選擇

在低機率尾部，粒子很少卻偏偏是障礙與深價外商品最關心的地方。市場就是這麼貼心，資料最少的地方通常風險最大。

## 為什麼校準是逆問題

SLV 校準通常先取得：

- 一張由市場香草報價推導的 $\sigma_{loc}(t,S)$
- 一組預先選定或校準的 stochastic volatility 參數

再反推出 $L(t,S)$。困難包括：

- 市場報價稀疏且有 bid-ask 雜訊
- local vol 本身需要對價格曲面求導，已經會放大雜訊
- 條件期望在低密度區域不穩
- $L$ 與聯合密度互相依賴
- 不同 leverage surface 可能在資料點附近產生近似價格

Saporito、Yang 與 Zubelli 將其視為逆問題，使用 Tikhonov regularization，同時限制資料誤差與 leverage function 的不平滑程度。研究中的數值結果顯示，正則化方法比直接 benchmark 更新在深價內外區域更穩、噪音更小，且不需要先把稀疏市場資料粗暴插值到整個 PDE 網格。

## 正則化的經濟意義

一般形式可想成最小化：

$$\text{市場擬合誤差}+\alpha_1\times\text{時間粗糙懲罰}+\alpha_2\times\text{價格方向粗糙懲罰}$$

正則化不是為了把曲面磨得像塑膠，而是在資料不足處承認「我不知道」，避免模型為了追一個髒報價製造巨大 leverage spike。

懲罰太小：

- 過度擬合
- 尾部爆炸
- Greeks 劇烈跳動

懲罰太大：

- 曲面過度平滑
- 失去真實 skew 與期限結構
- 香草回復誤差增加

所以正則化係數必須用殘差、穩定度、樣本外結果與風控用途共同決定，沒有一個全市場通用神奇數字。

## Mixing fraction

有些實作會引入混合比例 $\lambda_m\in[0,1]$，例如調整：

$$\xi_{mix}=\lambda_m\xi,\qquad \rho_{mix}=\lambda_m\rho$$

- $\lambda_m=0$：接近純 local vol
- $\lambda_m=1$：使用完整 stochastic volatility 動態
- 中間值：在香草擬合不變的前提下，調整奇異選擇權價格與 smile dynamics

mixing fraction 可用流動性較高的障礙或其他奇異商品校準。它不是多一顆免費旋鈕；若只為配一筆價格而調，其他路徑商品可能同時被扭歪。

## 標準校準流程

1. 蒐集同步的香草選擇權 bid-ask、遠期、利率與股利資料
2. 建立平滑、無蝶式與日曆套利的 IV 曲面
3. 由無套利曲面計算 Dupire local vol
4. 校準或固定 Heston/SV 參數，先決定希望的 smile dynamics
5. 選擇 PDE、粒子法或混合校準引擎
6. 逐時間層解聯合密度或模擬粒子
7. 計算 $E[V_t\mid S_t=S]$ 並更新 $L(t,S)$
8. 在低密度區域施加正則化、合理外插與正值限制
9. 重新定價全部香草，確認誤差落在 bid-ask 或容忍範圍內
10. 用障礙、前向 smile 與 Greeks 檢查動態，而不是香草 RMSE 過關就放煙火

## 交易與風控應用

### 障礙選擇權

local vol 與 stochastic vol 即使匹配同一批香草，觸碰障礙的機率仍可差很多。SLV 常用於 FX barrier、autocallable 與其他路徑商品，因為它能同時尊重市場曲面與波動率隨機性。

### 前向微笑

SLV 的 stochastic factor 影響未來 smile 的分布，可用來定價 forward-start、cliquet 與依賴未來 ATM 波動率的商品。這些商品正好會揭穿只擬合今天曲面的模型。

### Greeks一致性

Delta、Vega、Vanna 與 barrier sensitivity 會受到 leverage surface 與 stochastic factor 共同影響。應搭配[[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|進階 Greeks]]，並檢查：

- bump 市場曲面後是否重新校準 $L$
- bump SV 參數時是否保持香草曲面一致
- 網格、帶寬與正則化變動造成的 model Greeks
- 低密度尾部的 Greeks 是否被外插規則主導

若只 bump 一個參數卻不重新校準，算到的可能是模型內部敏感度，不是交易桌維持市場曲面後真正會承受的風險。

## 模型限制

- **校準昂貴**：每次更新都可能需要二維 PDE 或大量粒子
- **隱式固定點**：leverage function 與聯合分布互相依賴
- **尾部不穩定**：條件密度很小時，條件期望分母容易失控
- **兩階段誤差累積**：先估 local vol，再估 leverage，前一步的髒資料會傳下去
- **SV參數不唯一**：多組隨機波動率參數都可透過不同 $L$ 匹配同一香草曲面
- **路徑商品仍有模型風險**：香草一致不代表 barrier 或 autocall 價格唯一
- **高維災難**：加入隨機利率、多資產或多因子後 PDE 維度快速膨脹
- **實作依賴細節**：邊界條件、網格、核帶寬與正則化都會改變結果

## 與其他模型的定位

- **Dupire local vol**：香草靜態擬合強、計算較簡單，動態較僵硬
- **Heston**：動態可解讀、計算快，但香草擬合不一定精確
- **SLV**：香草擬合與動態兼顧，適合奇異商品，校準最複雜
- **SVI曲面**：是無套利曲面參數化，可作為 SLV 的市場輸入，但本身不提供完整路徑動態
- **跳躍模型**：直接描述不連續尾部；SLV 基本版本仍是連續路徑

## 實戰檢查清單

- 輸入 IV 曲面是否無蝶式與日曆套利
- Dupire local vol 是否經過穩健平滑與外插
- stochastic volatility 參數是歷史估計、香草校準還是奇異商品校準
- leverage function 是否保持正值、平滑且邊界合理
- 條件密度過低時採用什麼穩定化規則
- PDE 是否保存總機率並處理零通量邊界
- 粒子法是否有足夠有效樣本與合理核帶寬
- 香草重新定價誤差是否在 bid-ask 內
- 障礙與前向 smile 是否做跨模型比較
- Greeks 是否在重新校準與不重新校準兩種情境下都被理解
- 正則化係數與網格變動是否納入模型風險

## 關鍵啟示

1. SLV 用 leverage function 對齊香草邊際分布，用 stochastic factor 改變路徑與 smile dynamics
2. 核心公式含 $E[V_t\mid S_t=S]$，而這個條件期望又依賴 $L$，所以校準本質上是非線性固定點與逆問題
3. 香草擬合完全相同的模型，仍可對障礙與前向商品報出不同價格
4. SLV 最危險的地方不是公式，而是低密度尾部、資料雜訊與數值穩定化悄悄主導結果

## 參考來源

- Saporito, Y. F., Yang, X., & Zubelli, J. P. (2019). "The calibration of stochastic local-volatility models: An inverse problem perspective." *Computers & Mathematics with Applications*, 77(12), 3120-3137. https://doi.org/10.1016/j.camwa.2019.01.029
- Saporito, Y. F., Yang, X., & Zubelli, J. P. (2017). arXiv:1711.03023. https://arxiv.org/abs/1711.03023
- Gyöngy, I. (1986). "Mimicking the one-dimensional marginal distributions of processes having an Itô differential." *Probability Theory and Related Fields*, 71, 501-516.
- Guyon, J., & Henry-Labordère, P. (2012). "Being Particular About Calibration." *Risk*, 25(1), 88-93.

---

*最後更新：2026-08-19*
