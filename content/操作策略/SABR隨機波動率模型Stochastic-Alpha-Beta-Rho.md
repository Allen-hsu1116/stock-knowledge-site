---
title: SABR隨機波動率模型 (Stochastic Alpha Beta Rho)
aliases: [SABR Model, Stochastic Alpha Beta Rho, SABR模型, 隨機Alpha Beta Rho]
category: "操作策略"
---

# SABR隨機波動率模型 (Stochastic Alpha Beta Rho)


> SABR 是一個讓遠期價格與自身波動率同時隨機變動、而且彼此相關的模型；它用 $\alpha$、$\beta$、$\rho$、$\nu$ 四個核心參數，快速擬合隱含波動率微笑並描述微笑隨標的移動的動態，尤其常見於利率與外匯選擇權。

## 核心概念
SABR 是一個讓遠期價格與自身波動率同時隨機變動、而且彼此相關的模型；它用 $\alpha$、$\beta$、$\rho$、$\nu$ 四個核心參數，快速擬合隱含波動率微笑並描述微笑隨標的移動的動態，尤其常見於利率與外匯選擇權。

## 為什麼需要SABR

[[操作策略/Black-Scholes定價模型|Black-Scholes]]只有常數波動率，無法解釋市場的[[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew|微笑與偏斜]]。局部波動率模型雖可精確擬合今天的曲面，但 Hagan 等人指出，它預測的微笑移動方向可能和市場相反，導致 Delta 與 Vega 避險不穩。

SABR 的設計目標很務實：

- 保留少量、可解讀的參數
- 讓波動率本身是隨機的
- 讓遠期價格與波動率相關，以產生偏斜
- 提供近似封閉形式的隱含波動率公式，交易桌可快速校準與報價

## 模型方程

在適當的遠期測度下：

$$dF_t=\alpha_tF_t^{\beta}dW_t^{(1)}$$

$$d\alpha_t=\nu\alpha_tdW_t^{(2)}$$

$$dW_t^{(1)}dW_t^{(2)}=\rho dt$$

- $F_t$：標的遠期價格或遠期利率
- $\alpha_t$：隨機波動率水準
- $\beta$：價格彈性參數
- $\nu$：波動率的波動率，常念作 vol-of-vol
- $\rho$：遠期價格與波動率衝擊的相關係數

SABR 這個名字就是 Stochastic Alpha、Beta、Rho 的縮寫；但真正校準時別漏掉 $\nu$，不然名字記得比模型完整也是很有才。

## 四個參數的經濟意義

### Alpha：整體波動率水準

$\alpha$ 主要控制平值附近的波動率高度。其他條件不變時，$\alpha$ 增加會讓整條微笑大致上移。

因為模型中的即時擴散係數是 $\alpha F^\beta$，所以 $\alpha$ 的數值不能脫離 $F$ 與 $\beta$ 解讀。

### Beta：微笑骨架與價格彈性

$\beta$ 通常限制在 $0\le\beta\le1$：

- $\beta=0$：接近常態或 Bachelier 型動態，波動以絕對價格單位表達
- $\beta=1$：接近對數常態或 Black 型動態，波動以百分比表達
- $0<\beta<1$：介於兩者之間，形成 CEV 式彈性

$\beta$ 主要決定 backbone，也就是 ATM 波動率隨遠期價格改變的長期斜率。實務上常先固定 $\beta$，避免它與 $\rho$ 互相搶著解釋 skew，搞到參數每天跳針。

### Rho：偏斜方向

$\rho$ 控制價格與波動率衝擊的聯動：

- $\rho<0$：價格下跌時波動率傾向上升，形成股票市場常見的左高右低偏斜
- $\rho=0$：微笑較對稱
- $\rho>0$：價格上漲時波動率傾向上升，某些商品或利率環境可能出現

$\rho$ 的絕對值越大，微笑左右不對稱通常越明顯。

### Nu：曲率與尾翼

$\nu$ 越大，$\alpha_t$ 自己波動得越兇，微笑曲率與兩翼通常越明顯。它對遠離 ATM 的選擇權尤其重要，也直接影響 Vanna 與 Volga 類風險。

## Hagan近似公式的意義

SABR 最成功的地方，不是模型方程看起來很潮，而是 Hagan 等人用奇異擾動法推導出 Black 隱含波動率的近似代數公式：

$$\sigma_{BS}(F,K,T)\approx \frac{\alpha}{(FK)^{(1-\beta)/2}}\frac{z}{x(z)}\times\text{高階修正項}$$

其中：

$$z=\frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln\frac{F}{K}$$

$$x(z)=\ln\left(\frac{\sqrt{1-2\rho z+z^2}+z-\rho}{1-\rho}\right)$$

完整公式還包含 $\beta$、$\rho$、$\nu$ 與到期時間的高階修正。它是漸近近似，不是宇宙真理；極端履約價、長天期或 vol-of-vol 很高時，誤差與套利問題都可能冒出來。

## 標準校準流程

1. 用遠期價 $F$、折現因子、履約價與市場價格反推每個履約價的 IV
2. 選擇報價慣例：Black lognormal vol 或 Bachelier normal vol
3. 先固定 $\beta$，可依歷史 backbone、產品慣例或風險政策決定
4. 用 ATM IV 取得 $\alpha$ 的初始值
5. 用微笑斜率估 $\rho$，用曲率與兩翼估 $\nu$
6. 以加權最小平方法最小化模型 IV 與市場 IV 的差異
7. 權重可用 Vega、bid-ask 寬度或流動性調整，避免深價外髒報價主導結果
8. 檢查校準後的選擇權價格、Greeks、參數穩定度與靜態套利

常見做法是每個到期日各校準一組參數，再對期限方向做平滑。逐日逐切片硬擬合而不管參數連續性，明天的風控報表就會像喝醉一樣左右亂晃。

## 微笑動態與避險

SABR 的核心價值是讓微笑隨 $F$ 的移動更符合市場經驗。由於 $F$ 與 $\alpha$ 相關，標的價格變動會同步改變隱含波動率，不再假裝每個履約價的 IV 各自活在平行宇宙。

交易桌可由 SABR 曲面計算：

- Delta：包含微笑隨標的移動造成的額外風險
- Vega：對整體波動率水準 $\alpha$ 的敏感度
- Vanna：標的與波動率交叉敏感度
- Volga/Vomma：對波動率變動的凸性

這些風險可搭配[[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|進階 Greeks]]統一管理跨履約價部位。

## 負利率與位移SABR

標準 lognormal SABR 在價格接近零或可能為負時會出問題。利率市場常用 shifted SABR：

$$F_t^{shift}=F_t+s$$

先把遠期與履約價加上一個正位移 $s$，再套模型。位移不是免費午餐；不同 $s$ 會改變 skew、Greeks 與尾部行為，因此它是模型參數，不是隨手補丁。

另一種做法是使用 normal SABR，以 Bachelier 隱含波動率報價，較能直接容納負利率。

## 與其他模型比較

- **Black-Scholes/Black 76**：只有單一常數波動率，最快但沒有微笑
- **局部波動率**：可精確擬合當下曲面，但微笑動態可能不符合市場
- **SABR**：參數少、近似公式快、微笑動態可解讀，特別適合利率與 FX
- **Heston**：也有隨機波動率與相關性，股票與外匯常見，具有特徵函數半封閉解
- **純曲面參數化**：可以更靈活地擬合報價，但不一定提供標的與波動率的聯合動態

## 實戰檢查清單

- 報價是 normal vol 還是 lognormal vol
- 遠期價、折現與股利或持有成本是否一致
- $\beta$ 是固定還是自由校準，理由是否可重複
- 每個到期日的參數是否平滑、穩定
- 深價外報價是否有足夠流動性
- 校準權重是否納入 Vega 與 bid-ask
- 曲面是否通過蝶式與日曆套利檢查
- 極端價格與波動率情境下 Greeks 是否爆炸
- 是否需要 shifted 或 normal SABR

## 關鍵啟示

1. SABR 不只擬合微笑，也試圖擬合微笑怎麼動，這是它比純靜態曲面更有價值的地方
2. $\beta$ 決定骨架、$\rho$ 決定偏斜、$\nu$ 決定曲率、$\alpha$ 決定整體水準
3. 固定 $\beta$ 後校準其他三個參數，通常比四個一起自由亂跑更穩
4. 近似封閉公式讓 SABR 適合交易桌，但速度快不等於沒有模型風險

## 實戰應用

### 主要應用
### 利率選擇權

SABR 最經典的應用是 caplet、floorlet 與 swaption。它能以少量參數擬合利率微笑，且近似公式計算快，適合大量報價與風險重算。

### 外匯選擇權

可用 SABR 描述 ATM、risk reversal 與 butterfly 形成的微笑結構。不過 FX 市場的 delta-based strike 慣例與報價轉換必須處理正確。

### 股票與商品選擇權

也能使用，但股票市場常有更強的短期跳躍與左尾風險，純 SABR 未必足夠。應和[[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston]]、跳躍模型或市場直接曲面比較。

## 注意事項
### 1. 近似公式不是精確解

Hagan 公式在 ATM 附近通常很好，但極端履約價、長期限、高 $\nu$ 或接近邊界的 $\rho$ 可能誤差放大。

### 2. 可能產生靜態套利

未受約束的 SABR 切片可能造成負風險中立密度或翼端不合理。校準得很貼不代表無套利，這種模型笑得越漂亮，口袋裡可能越多刀。

### 3. 參數不可完全識別

$\beta$ 與 $\rho$ 都會影響 skew，$\alpha$ 與 $\beta$ 也互相關聯。全部自由校準時，可能有多組參數產生近似曲面。

### 4. Alpha沒有均值回歸

基本 SABR 的 $\alpha$ 是對數常態擴散，沒有長期均值回歸。長天期模擬可能出現不合理波動率路徑。

### 5. 沒有價格跳躍

純 SABR 是連續擴散，無法直接捕捉突發跳空；超短天期深價外選擇權尤其容易低估事件尾部。

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Hagan, P. S., Kumar, D., Lesniewski, A. S., & Woodward, D. E. (2002). "Managing Smile Risk." *Wilmott Magazine*, September, 84-108. https://www.next-finance.net/IMG/pdf/pdf_SABR.pdf
- Obłój, J. (2008). "Fine-Tune Your Smile: Correction to Hagan et al." *Wilmott Magazine*.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.

---

*最後更新：2026-08-18*
