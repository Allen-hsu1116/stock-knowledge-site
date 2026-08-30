---
title: 3/2隨機波動率模型 (Three-Halves Stochastic Volatility)
aliases: [3/2 Model, Three-Halves Model, 3/2 Stochastic Volatility, 三分之二模型]
category: "操作策略"
---

# 3/2隨機波動率模型 (Three-Halves Stochastic Volatility)


> 3/2 模型讓瞬時變異數的擴散項與 $V_t^{3/2}$ 成正比、高波動時擾動會超線性放大；它本身是非仿射隨機波動率模型，但倒數變異數 $1/V_t$ 服從 CIR 平方根過程，因此仍可用轉換方法處理香草、已實現變異數與波動率衍生品。

## 核心概念
3/2 模型讓瞬時變異數的擴散項與 $V_t^{3/2}$ 成正比、高波動時擾動會超線性放大；它本身是非仿射隨機波動率模型，但倒數變異數 $1/V_t$ 服從 CIR 平方根過程，因此仍可用轉換方法處理香草、已實現變異數與波動率衍生品。

## 名字不是三除以二的報酬率

「3/2」來自變異數擴散項的冪次：

$$V_t^{3/2}$$

它不是勝率、槓桿倍數，也不是什麼神秘黃金比例。模型想表達的是：當變異數變高，變異數本身的不確定性會更快增加。

經典 [[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston 模型]]使用 $\sqrt{V_t}=V_t^{1/2}$；3/2 模型則使用 $V_t^{3/2}$。差一個 $V_t$，尾部行為與高波動區的動態就完全不是同一齣戲。

## 倒數變異數是CIR過程

令：

$$U_t=\frac{1}{V_t}$$

用 Itô 引理可得：

$$dU_t=\left(\kappa+\varepsilon^2-\kappa\theta U_t\right)dt-\varepsilon\sqrt{U_t}\,dW_t^V$$

重新定義布朗運動符號後，可寫成 CIR 形式：

$$dU_t=\widetilde\kappa(\widetilde\theta-U_t)dt+\widetilde\varepsilon\sqrt{U_t}\,d\widetilde W_t$$

其中：

$$\widetilde\kappa=\kappa\theta$$

$$\widetilde\theta=\frac{\kappa+\varepsilon^2}{\kappa\theta}$$

$$|\widetilde\varepsilon|=\varepsilon$$

這個倒數關係是整個模型的計算命門：

- $V_t$ 本身非仿射
- $U_t=1/V_t$ 卻是平方根仿射過程
- 可借用 CIR 的轉移分布、非中心卡方結構與邊界理論
- 許多 Heston/CIR 的數值方法可經倒數轉換改造

但別偷懶說「3/2 就是 Heston 倒過來」。倒數變異數雖是 CIR，標的價格的擴散仍使用 $\sqrt{V_t}=1/\sqrt{U_t}$，所以聯合價格模型並不等於 Heston。

## 邊界與爆炸風險

若 $U_t$ 觸及零，$V_t=1/U_t$ 就會爆炸。因此要檢查倒數 CIR 的零邊界不可達條件。

由 CIR 的 Feller 條件：

$$2\widetilde\kappa\widetilde\theta\ge \widetilde\varepsilon^2$$

代入可得：

$$2(\kappa+\varepsilon^2)\ge\varepsilon^2$$

也就是：

$$\kappa\ge-\frac{\varepsilon^2}{2}$$

實務校準通常限制 $\kappa>0$，因此這個條件往往自然滿足。但數值實作仍要檢查離散誤差，因為理論不爆炸不代表你的 Euler 網格也有受過教育。

此外，風險中立下折現股價是否為真鞅，而非只是一個嚴格局部鞅，還會受相關係數與參數區域影響。定價引擎應做鞅性測試，不能只確認 $V_t>0$ 就下班。

## 為什麼高波動區特別不一樣

3/2 模型的瞬時變異數擾動標準差為：

$$\varepsilon V_t^{3/2}\sqrt{dt}$$

變異數每上升一倍，擾動幅度不只上升一倍，而是乘上 $2^{3/2}$。這使模型能描述：

- 高波動時 vol-of-vol 同步急升
- 危機期變異數分布右尾更厚
- 波動率指數與已實現變異數商品的凸性更明顯
- 同一個衝擊在低波動與高波動狀態下產生不同幅度

同時，漂移中的 $-\kappa V_t^2$ 會在高水位強力均值回歸。這種非線性回復與非線性擾動的競爭，是 3/2 模型和線性漂移平方根模型的核心差別。

## 與Heston模型比較

### Heston

$$dV_t=\kappa(\theta-V_t)dt+\xi\sqrt{V_t}\,dW_t$$

- 變異數是 CIR 過程
- 聯合價格與變異數具有仿射結構
- 特徵函數與歐式定價成熟
- 高變異數時擾動只按 $\sqrt V$ 增加

### 3/2模型

$$dV_t=\kappa V_t(\theta-V_t)dt+\varepsilon V_t^{3/2}dW_t$$

- 變異數本身非仿射
- 倒數變異數是 CIR
- 高波動時 vol-of-vol 超線性增加
- 對積分變異數與波動率商品具有特殊解析可處理性
- 模擬與鞅性檢查更容易挖坑

沒有誰宇宙第一。Heston 常在香草定價速度與穩定性勝出；3/2 的優勢主要在高波動非線性與方差相關商品的結構。

## 與4/2模型的關係

4/2 模型把 Heston 型與 3/2 型價格波動率暴露合併，常見形式讓標的瞬時波動率包含：

$$a\sqrt{V_t}+\frac{b}{\sqrt{V_t}}$$

平方後同時產生與 $V_t$、$1/V_t$ 相關的成分，因此名稱取自 $1/2$ 與 $3/2$ 兩類結構的結合。

它比單一 3/2 更彈性，但參數更多、校準識別更麻煩。模型升級不是免費加料，通常只是讓優化器多幾個地方藏屍體。

## 定價方法

### 轉換方法

3/2 模型下，對數價格與積分變異數：

$$I_T=\int_0^T V_s ds$$

可透過倒數 CIR 結構推導聯合 Laplace/Fourier transform。這使下列商品可用轉換方法處理：

- 歐式香草選擇權
- 方差交換
- 已實現變異數選擇權
- 波動率交換的近似或轉換定價
- timer options
- VIX 類商品的模型化定價

實作上常用數值積分、Fourier inversion、特殊函數與封閉形式的部分轉換。

### PDE方法

對一般商品可建立以 $(S,V)$ 為狀態的二維 PDE。高 $V$ 區係數快速增大，網格上界、邊界條件與變數轉換很重要。

可改用 $U=1/V$ 建網格，將平方根過程放在較熟悉的數值框架中，但價格擴散係數會變成 $1/\sqrt U$，零附近仍然難搞。

### 蒙地卡羅

常見方法包括：

- 模擬倒數 CIR，再取 $V=1/U$
- 基於非中心卡方轉移的近似或精確抽樣
- explicit weak solution simulation
- full truncation 或 positivity-preserving scheme
- 重要性抽樣與控制變量

直接對 $V_t$ 使用普通 Euler 可能產生負值或極端爆點。把負值截成零雖方便，卻會扭曲積分變異數與尾部選擇權，正好把最在意的地方修壞。

## 校準流程

1. 清理香草與波動率商品報價
2. 用 ATM IV 期限結構初始化 $V_0$ 與 $\theta$
3. 用衝擊消退速度初始化 $\kappa$
4. 用 smile 曲率與波動率商品初始化 $\varepsilon$
5. 用股票下跌與波動率上升關係初始化 $\rho$
6. 同時使用多期限、多履約價，避免只擬合單一切片
7. 若有可靠資料，加入方差交換或 VIX 期限結構約束
8. 對倒數 CIR 邊界、折現股價鞅性與參數可識別性做檢查
9. 比較模型價格、IV 誤差、Greeks 與樣本外避險損益
10. 用多起點優化，檢查是否存在多組近似最優參數

## 模型限制

- **變異數本身非仿射**：計算不像 Heston 那麼直接
- **高波動數值敏感**：$V^{3/2}$ 會放大離散誤差與極端路徑
- **純擴散沒有價格跳躍**：財報或隔夜跳空仍可能低估短期尾翼
- **固定參數限制狀態變化**：危機期與平穩期可能需要不同參數
- **參數識別問題**：$\varepsilon$、$\rho$、$V_0$ 都可能影響短端 smile
- **鞅性不是自動保證**：局部鞅若不是真鞅，標準風險中立定價會出問題
- **VIX映射依賴定義**：模型瞬時變異數、未來平均變異數與市場 VIX 並非直接畫等號
- **歷史參數不等於風險中立參數**：選擇權校準含波動率風險溢價

## 實戰檢查清單

- 採用的 3/2 參數化是否和文獻一致
- $V_t$ 是變異數還是波動率，別把平方根抄錯
- 倒數過程 $U=1/V$ 的 CIR 參數推導是否正確
- Feller/非爆炸條件是否滿足
- 折現股價是否通過蒙地卡羅鞅性測試
- 時間步長縮小時價格是否收斂
- 是否直接模擬倒數 CIR，而不是任由 $V$ 的 Euler 路徑發瘋
- 積分變異數的數值誤差是否小於商品 bid-ask
- 深尾報價是否有真實成交，而非一張幽靈掛單支配校準
- 樣本外 Greeks 與避險損益是否優於較簡單模型

## 關鍵啟示

1. 3/2 的名稱來自變異數擴散項 $V^{3/2}$
2. 高波動時 vol-of-vol 超線性增加，但二次漂移也提供更強均值回歸
3. $V$ 非仿射，倒數 $1/V$ 卻是 CIR，這是定價與模擬的關鍵
4. 模型對方差、VIX 與高波動尾部商品特別有研究價值
5. 理論上的非爆炸與實作上的數值穩定是兩回事，別讓 Euler 幫你發明新金融危機

## 實戰應用
### 波動率衍生品相對價值

3/2 模型對高波動狀態的非線性特別敏感，可用來比較：

- 香草 IV 曲面隱含的尾部風險
- 方差交換期限結構
- VIX 期貨或選擇權的凸性
- 已實現變異數選擇權的右尾價格

市場價高於模型價不是自動賣出訊號，也可能代表模型低估跳躍、波動率風險溢價或流動性保費。

### 高波動壓力測試

3/2 路徑適合測試：

- $V_t$ 在高位時 vol-of-vol 進一步放大
- 負相關使現貨下跌與變異數上升同時發生
- Vega、Vomma 與 Vanna 在非線性波動狀態下惡化
- Delta 對沖頻率不足造成的尾部損失

### 模型比較

將 Black-Scholes、Heston、3/2 與跳躍模型對同一商品定價，可觀察常數波動、平方根變異數、超線性變異數與價格跳躍各自貢獻多少模型風險。

## 注意事項

### 風險中立模型結構
常見規格為：

$$\frac{dS_t}{S_t}=(r-q)dt+\sqrt{V_t}\,dW_t^S$$

$$dV_t=\kappa V_t(\theta-V_t)dt+\varepsilon V_t^{3/2}dW_t^V$$

$$d\langle W^S,W^V\rangle_t=\rho\,dt$$

其中：

- $S_t$：標的價格
- $V_t$：瞬時變異數
- $\kappa$：均值回復強度尺度
- $\theta$：變異數中樞
- $\varepsilon$：變異數的 vol-of-vol 係數
- $\rho$：價格與變異數衝擊相關性

漂移可展開為：

$$\kappa\theta V_t-\kappa V_t^2$$

因此高變異數時，$-\kappa V_t^2$ 提供很強的向下拉回力量；同時擴散項 $\varepsilon V_t^{3/2}$ 也快速變大。模型在高波動區同時踩油門和拉手煞車，這正是它能產生厚尾、又不必任由變異數永久飛走的原因。

## 相關主題
- [[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model]]
- [[操作策略/方差交換與波動率衍生品Variance-Swap-and-Volatility-Derivatives]]
- [[基本面分析/VIX恐慌指數Volatility-Index]]
- [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility]]
- [[風險管理/隱含波動率偏斜與微笑Implied-Volatility-Skew-and-Smile]]
- [[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]

## 來源
- Carr, P., & Sun, J. (2007). "A new approach for option pricing under stochastic volatility." *Review of Derivatives Research*, 10, 87-150. https://doi.org/10.1007/s11147-007-9014-6
- Kouarfate, I. R., Kouritzin, M. A., & MacKay, A. (2021). "Explicit solution simulation method for the 3/2 model." https://arxiv.org/abs/2009.09058
- Zheng, W., & Zeng, P. (2016). "Pricing timer options and variance derivatives with closed-form partial transform under the 3/2 model." https://arxiv.org/abs/1504.08136

---

*最後更新：2026-08-20*
