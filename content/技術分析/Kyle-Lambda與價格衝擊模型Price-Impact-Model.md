# Kyle's Lambda 與價格衝擊模型 Price Impact Model

> 機構大單如何推動價格？Kyle's Lambda 量化「交易量→價格移動」的敏感度，是市場微結構的核心定價工具。

## 核心概念

Kyle's Lambda（λ）是市場微結構理論中衡量**價格衝擊（Price Impact）**的參數——每單位交易量能推動價格多少。Lambda 越大，代表市場流動性越差，相同交易量會造成更大的價格移動。

**基本公式：**
```
ΔP = λ × V
```
其中 ΔP=價格變動、V=交易量（或訂單流）、λ=價格衝擊係數

## Kyle (1985) 模型基礎

Albert Kyle 在 1985 年的論文 "Continuous Auctions and Insider Trading" 中提出了這個框架：

### 三類參與者
- **內線交易者（Insider）**：知道資產真實價值，策略性選擇交易量
- **噪音交易者（Noise Trader）**：不具資訊優勢，隨機交易
- **做市商（Market Maker）**：觀察總交易量，設定價格

### 核心洞見
- 做市商無法分辨哪些交易來自內線、哪些來自噪音
- 只能根據**總交易量**推斷資訊含量，動態調整價格
- 價格衝擊 = 做市商對資訊不對稱的防禦機制
- Lambda 就是做市商「學習」的結果：交易量越大，越可能含有資訊，價格移動越多

### Kyle 模型的三個結論
1. **線性價格衝擊**：價格變動與交易量成正比（λ 是常數）
2. **內線交易者最適策略**：將交易均勻分散在整個交易期間（不集中交易）
3. **市場深度恆定**：在均衡狀態下，Lambda 不隨時間變化

## 價格衝擊的兩種類型

### 永久性衝擊（Permanent Impact）
- 交易揭示了新的資訊，價格永久移動到新均衡
- 買入推動價格上漲、賣出推動價格下跌
- Kyle 模型主要描述這種類型
- 永久衝擊 = 市場對「你為什麼買/賣」的推斷

### 暫時性衝擊（Temporary Impact）
- 大單消耗流動性，價格暫時偏離均衡但會回復
- 買入推動價格上漲後，價格部分回落
- Almgren-Chriss 模型同時考慮永久和暫時衝擊
- 暫時衝擊 = 流動性消耗成本

### Almgren-Chriss 模型（2000）
```
Total Cost = Permanent Impact × V + Temporary Impact × (V/T)²
```
其中 V=總交易量、T=執行時間

- 永久衝擊與交易量成正比（線性）
- 暫時衝擊與交易強度（V/T）的平方成正比（非線性）
- 最適執行策略：在執行時間內均勻分配交易（類似 TWAP）
- 詳見 [[操作策略/執行演算法VWAP-TWAP-Execution-Algorithm|VWAP/TWAP 執行演算法]]

## 如何估計 Lambda

### 方法一：回歸法
```
ΔP_t = λ × V_t + ε_t
```
- 用歷史數據回歸價格變動對交易量的關係
- Lambda = 回歸係數
- 需要足夠的數據量和適當的時間窗口

### 方法二：VPIN（Volume-Synchronized Probability of INformed Trading）
- Easley & O'Hara 開發的指標
- 用訂單流不平衡（OFI）替代交易量
- 更精確地捕捉資訊交易的比例

### 方法三：Amihud 非流動性指標
```
ILLIQ = |Return_t| / Volume_t
```
- Lambda 的倒數概念：ILLIQ 越大 = Lambda 越大 = 流動性越差
- 詳見 [[風險管理/Amihud非流動性指標Amihud-Illiquidity-Measure|Amihud 非流動性指標]]

## Lambda 的實戰應用

### 對散戶的意義
- **Lambda 大的股票**：大單進出會顯著推動價格，散戶容易看到「大戶腳印」
- **Lambda 小的股票**：大單能悄無聲息地進出，散戶看不出資金流向
- 台股小型股 Lambda 通常遠大於大型股，這就是為什麼小型股容易被「作線」

### 機構交易者的考量
- 估計自己的 Lambda → 計算執行成本 → 決定最適執行策略
- 大單拆小單（VWAP/TWAP/IS 演算法）就是為了降低 Lambda 的衝擊
- 一般建議：單筆交易不超過日成交量 5-10%，超過就必須拆單

### 與流動性的關係
- Lambda = 1/市場深度 = 流動性的反向指標
- 高 Lambda = 淺碟市場 = 容易被大單操縱
- 低 Lambda = 深度市場 = 大單也能平穩執行
- 詳見 [[風險管理/市場微結構與流動性定價Market-Microstructure-and-Liquidity-Pricing|市場微結構與流動性定價]]

## 與既有知識的連結

### 與 OFI 的關係
- [[技術分析/訂單流失衡OFI-Order-Flow-Imbalance|訂單流失衡 OFI]] 量化買賣力量失衡
- Lambda × OFI = 預期價格衝擊
- 兩者結合可以預測極短期價格方向

### 與流動性風險的關係
- [[風險管理/流動性風險Liquidity-Risk|流動性風險]] 的核心來源就是 Lambda
- Lambda 在壓力時期會暴增（流動性蒸發），原本可控的大單突然變成致命衝擊
- 2008金融危機、2020 COVID 崩盤都是 Lambda 暴增的典型案例

### 與 VWAP 的關係
- [[操作策略/VWAP執行演算法與機構交易策略VWAP-Execution-Algorithms|VWAP 執行演算法]] 的存在就是為了最小化 Lambda 衝擊
- 機構把大單拆成小單跟著成交量分佈走，讓每筆小單的衝擊微乎其微

## 非線性價格衝擊模型

Kyle 的線性模型是基礎，實證顯示真實市場更接近**凹函數**（concave）：

```
ΔP = λ × V^α ,  α < 1（通常 0.5~0.7）
```

- **平方根法則（Square Root Law）**：α ≈ 0.5，價格衝擊與交易量的平方根成正比
- 意味著大單的邊際衝擊遞減（比線性模型預測的更溫和）
- 但小單的衝擊比線性模型更大
- 台股小型股的 α 可能接近 1（接近線性），大型股的 α 更接近 0.5

## 實戰總結：散戶如何利用 Lambda 概念

1. **觀察大單足跡**：Lambda 大的小型股，大單進出會在盤中留下明顯價格痕跡，用 [[技術分析/相對成交量RVOL-Relative-Volume|RVOL]] 和 [[技術分析/訂單流失衡OFI-Order-Flow-Imbalance|OFI]] 搭配判讀
2. **避開高 Lambda 時段**：開盤前15分鐘和收盤前5分鐘 Lambda 最高，小單也能推動大價格移動，滑價風險最大
3. **部位控制**：散戶雖然不會造成市場衝擊，但要理解大戶在 Lambda 高的環境中必須拆單，這解釋了為什麼盤中會出現規律性的小單買賣
4. **除權息旺季**：Lambda 會因流動性下降而上升，大戶的執行成本增加，這也是為什麼除權息季節大單動作會更謹慎

## 參考資料

- Kyle, A.S. (1985). "Continuous Auctions and Insider Trading." Econometrica.
- Almgren, R. & Chriss, N. (2000). "Optimal Execution of Portfolio Transactions." Journal of Risk.
- Bouchaud, J.P. et al. (2004). "Fluctuations and Response in Financial Markets: The Minor Game." (Square Root Law)
- Wikipedia: Market Impact
- Easley, D. & O'Hara, M. — VPIN 相關論文系列

## 實戰應用
（待補充）


## 注意事項
（待補充）


## 相關主題
（待補充）
