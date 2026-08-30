---
title: SVI隱含波動率曲面參數化 (Stochastic Volatility Inspired)
aliases: [SVI, Stochastic Volatility Inspired, SVI Volatility Surface, 隨機波動率啟發式參數化]
category: "操作策略"
---

# SVI隱含波動率曲面參數化 (Stochastic Volatility Inspired)


> SVI 用五個參數描述單一到期日的總隱含變異數微笑，能快速、平滑地擬合履約價方向並提供合理翼端；把各期限切片連起來後可形成完整波動率曲面，但如果不約束蝶式與日曆套利，擬合再漂亮也可能是一張可以直接撿錢的破網。

## 核心概念
SVI 用五個參數描述單一到期日的總隱含變異數微笑，能快速、平滑地擬合履約價方向並提供合理翼端；把各期限切片連起來後可形成完整波動率曲面，但如果不約束蝶式與日曆套利，擬合再漂亮也可能是一張可以直接撿錢的破網。

## SVI到底是什麼

SVI 全名是 Stochastic Volatility Inspired，由 Jim Gatheral 在 Merrill Lynch 於 1999 年設計，2004 年公開發表。名字有 stochastic volatility，不代表它本身一定是一個完整的隨機微分方程模型；實務上它主要是**隱含波動率曲面的參數化工具**。

它的目標是把[[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew|微笑與偏斜]]從一堆離散報價，整理成平滑、可微分、可插值、可外插的函數，供定價、Greeks、風險中立密度與局部波動率使用。

## 為何參數化總變異數

SVI 不直接擬合 IV，而是擬合總隱含變異數：

$$w(k,T)=\sigma_{BS}^2(k,T)T$$

其中對數遠期價內程度為：

$$k=\ln\left(\frac{K}{F_T}\right)$$

- $K$：履約價
- $F_T$：同到期日遠期價格
- $T$：到期時間
- $\sigma_{BS}$：Black-Scholes 隱含波動率

總變異數比 IV 更適合跨期限建模，因為在無日曆套利條件下，固定 $k$ 的 $w(k,T)$ 應隨 $T$ 不下降。直接比較不同期限 IV 高低，常常會把時間尺度搞成一鍋粥。

## Raw SVI公式

對固定到期日，raw SVI 寫成：

$$w(k)=a+b\left[\rho(k-m)+\sqrt{(k-m)^2+\sigma^2}\right]$$

參數限制通常包括：

$$b\ge0,\quad |\rho|<1,\quad \sigma>0$$

為確保總變異數非負，還需要：

$$a+b\sigma\sqrt{1-\rho^2}\ge0$$

## 五個參數的作用

### a：整體高度

增加 $a$ 會讓總變異數曲線整體上移，近似控制波動率水準。

### b：翼端斜率與微笑緊度

$b$ 越大，左右兩翼越陡，微笑更緊。它控制尾部總變異數隨 $|k|$ 增加的速度。

### rho：左右不對稱

$\rho$ 控制旋轉與偏斜：

- 增加 $\rho$ 會降低左翼斜率、提高右翼斜率
- 股票指數常見 $\rho<0$，對應左翼較陡、價外 Put IV 較高

### m：水平位置

$m$ 將微笑中心沿 $k$ 軸平移。它不是 ATM 履約價本身，但會影響最低點與偏斜中心的位置。

### sigma：ATM曲率

$\sigma$ 控制中心區域的平滑與曲率。增加 $\sigma$ 通常降低 ATM 附近曲率，讓微笑中心更寬、更平。

## 翼端行為為何重要

當 $|k|$ 很大時，SVI 的總變異數對 $k$ 呈線性，符合 Roger Lee moment formula 所給的翼端漸近結構。這讓 SVI 比任意高次多項式更適合外插：多項式在樣本外很容易突然飛天或鑽地，SVI 至少知道尾巴該往哪個方向長。

但「線性翼端」不代表任意參數都無套利。左右翼斜率仍要符合矩條件與密度非負限制。

## 兩種靜態套利

Gatheral 與 Jacquier 將波動率曲面的靜態無套利拆成兩部分：

### 1. 日曆價差套利

固定對數遠期價內程度 $k$ 時，總變異數必須隨到期時間不下降：

$$\frac{\partial w(k,T)}{\partial T}\ge0$$

如果較長天期的總變異數反而更低，就可能構造跨期限套利。每個期限各自擬合得再好，也可能在期限之間互砍。

### 2. 蝶式套利

同一到期日的買權價格必須隨履約價遞減且保持凸性；等價地，買權價格對履約價的二階導數所隱含的風險中立密度不能為負。

對平滑總變異數切片 $w(k)$，Gatheral-Jacquier 定義：

$$g(k)=\left(1-\frac{kw'(k)}{2w(k)}\right)^2-\frac{w'(k)^2}{4}\left(\frac{1}{w(k)}+\frac{1}{4}\right)+\frac{w''(k)}{2}$$

在適當翼端條件下，需有：

$$g(k)\ge0$$

這就是為什麼只最小化報價誤差不夠。優化器會很開心地交出一組殘差超小、密度卻為負的參數，然後人類再拿著漂亮 RMSE 去開會互相感動。

## SVI的等價形式

除了 raw SVI，實務上還有：

- **Natural SVI**：用更接近幾何形狀的參數表達
- **Jump-Wings SVI**：以 ATM 總變異數、左右翼斜率、最小方差等交易桌較直覺的量表示
- **SSVI**：Surface SVI，直接把期限結構納入參數化，更容易控制整張曲面的無套利性

不同形式本質上可互相轉換。Raw SVI 公式最簡潔，但直接對五個 raw 參數加無套利約束並不輕鬆；Jump-Wings 適合報價解讀，SSVI 適合全曲面建構。

## 校準流程

### 第一步：清理市場資料

- 用 bid/ask 中間價或經流動性加權的價格
- 剔除零 bid、明顯錯價、價差過寬與無合理 Vega 的報價
- 用一致的利率、股利與遠期價格
- 將履約價轉成 $k=\ln(K/F_T)$
- 將 IV 轉成 $w=\sigma_{imp}^2T$

### 第二步：逐期限取得初始切片

以加權最小平方法擬合 raw SVI：

$$\min_{a,b,\rho,m,\sigma}\sum_i\omega_i\left[w_{SVI}(k_i)-w_{mkt}(k_i)\right]^2$$

權重 $\omega_i$ 可依 Vega、bid-ask 寬度、成交量或 ATM 距離設定。用價格誤差還是 IV 誤差，會對深價內外選擇權產生完全不同的重視程度。

### 第三步：施加單切片無套利條件

- 總變異數保持非負
- 檢查 $g(k)\ge0$
- 檢查極端履約價的翼端限制
- 在合理 $k$ 網格之外也要測試，不要只在有報價的位置自我感覺良好

### 第四步：處理期限結構

- 固定 $k$ 檢查 $w(k,T)$ 是否隨 $T$ 單調不降
- 對相鄰到期切片做聯合校準或約束
- 插值應在總變異數與適當的價內程度座標進行
- 外插要保留合理的短端與長端行為

### 第五步：重新定價與驗證

- 將 SVI IV 代入 Black-Scholes 重新定價
- 確認模型價格大致落在市場 bid/ask 內
- 檢查數值 Delta、Vega、Vanna、Volga 是否平滑
- 用壓力情境測試 ATM、skew、curvature 與翼端變化

## 與Heston等模型的關係

[[操作策略/Heston隨機波動率模型Heston-Stochastic-Volatility-Model|Heston]]是一個有價格與變異數聯合動態的隨機模型；SVI 主要是一個曲面形狀參數化。兩者不是同層級的替代品。

Gatheral 與 Jacquier 的研究指出，Heston 隱含波動率微笑在大到期極限下恰好收斂到 SVI 形式，這也是 Stochastic Volatility Inspired 名稱背後的數學理由之一。

- 需要標的路徑與波動率動態：用 Heston、SABR 或其他動態模型
- 需要快速、穩定地整理市場曲面：SVI 很實用
- 需要兩者：可先用 SVI 建市場基準，再用動態模型校準或做模型風險比較

## 實戰檢查清單

- 遠期價與折現因子是否正確
- 使用的是 log-forward moneyness 與 total variance
- 報價是否經過流動性與 bid-ask 清理
- 每個切片是否總變異數非負
- 是否在夠寬的 $k$ 網格檢查 $g(k)\ge0$
- 期限之間是否滿足總變異數單調性
- 左右翼端斜率是否合理
- 模型價格是否大多落在 bid/ask 內
- Greeks 與風險中立密度是否平滑
- 插值與外插規則是否有版本控管

## 關鍵啟示

1. SVI 的核心不是畫出漂亮微笑，而是用少量參數建立可微分、可外插、可檢查套利的總變異數切片
2. 單一切片無蝶式套利，加上跨期限無日曆套利，才是一張合格曲面
3. SVI 是市場曲面表示法，不應被誤當成完整的波動率動態模型
4. 對交易者而言，曲面殘差只有超過交易成本與模型不確定性，才可能變成可執行的相對價值訊號

## 實戰應用
### 1. 波動率曲面報價

SVI 將離散履約價轉成連續曲線，可快速取得未掛牌履約價的合理 IV，也能讓交易系統用一致方式插值。

### 2. 相對價值交易

比較市場 IV 與無套利 SVI 曲面的偏離，可找出特定履約價或期限的相對貴賤。偏離必須超過 bid-ask、滑價與模型誤差才叫機會，否則只是螢幕上的幻覺。

### 3. 風險中立密度

由平滑買權價格曲線的二階導數可估計市場隱含分配，進一步觀察尾部風險與事件機率。曲面不平滑時，二階導數會把小雜訊放大，所以無套利平滑是前置條件。

### 4. 局部波動率輸入

局部波動率需要對履約價與期限求導。SVI 提供解析且平滑的履約價切片，可作為反推 local vol 的曲面底座；但期限方向也必須平滑，否則求時間導數照樣爆炸。

### 5. Greeks與壓力測試

可直接對 $a,b,\rho,m,\sigma$ 或 Jump-Wings 參數做 bump，建立高度、偏斜、曲率與翼端的風險情境，並搭配[[操作策略/波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution|波動率期限結構與曲面演化]]管理整本部位。

## 注意事項
- 直接對 IV 而非總變異數亂插值
- 用現貨價而非同期限遠期價計算價內程度
- 每個期限獨立校準，完全不檢查日曆套利
- 只限制 $b>0$、$|\rho|<1$ 就以為無套利
- 只在市場履約價範圍檢查密度，忽略外插翼端
- 把 SVI 參數當成穩定經濟因子，卻沒檢查參數識別與日間跳動
- 用單一離群深價外報價扭曲整條尾翼

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Gatheral, J., & Jacquier, A. (2014). "Arbitrage-free SVI volatility surfaces." *Quantitative Finance*, 14(1), 59-71. https://arxiv.org/abs/1204.0646
- Gatheral, J. (2004). "A Parsimonious Arbitrage-Free Implied Volatility Parameterization with Application to the Valuation of Volatility Derivatives." Global Derivatives presentation.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Gatheral, J., & Jacquier, A. (2011). "Convergence of Heston to SVI." *Quantitative Finance*, 11(8), 1129-1132.
- Lee, R. W. (2004). "The Moment Formula for Implied Volatility at Extreme Strikes." *Mathematical Finance*, 14(3), 469-480.

---

*最後更新：2026-08-18*
