---
title: "Almgren-Chriss 最優執行模型 Almgren-Chriss Optimal Execution Model"
tags: [操作策略, 機構交易, 演算法交易, 市場衝擊, 最優執行]
---

# Almgren-Chriss 最優執行模型

> 你要賣 10 萬張台積電，一次砸下去盤面直接崩給你看；分 30 天慢慢賣，市場可能先跌再說。Almgren-Chriss 模型把這個兩難變成數學：在「市場衝擊」和「時間風險」之間找到最優拆單軌跡。

## 核心概念

Almgren-Chriss 模型是機構交易執行領域的奠基性框架，由 Robert Almgren 和 Neil Chriss 在 1999 年提出、2000 年正式發表。它解決的是一個每個大戶和機構都會遇到的核心問題：**如何把大單拆成小單執行，同時在「衝擊成本」和「時間風險」之間取得平衡？**

### 兩難的本質

- **一次全砸（market order）**：市場衝擊巨大，成交均價遠劣於當前價格
- **慢慢分批**：衝擊小了，但持倉期間暴露在市場波動風險中，可能還沒賣完價格就先跌了

這就是執行成本中的**衝擊 vs 時間風險權衡**（impact-risk tradeoff）。

## 模型設定

### 基本框架

一個交易者持有 $X$ 股，必須在期限 $T$ 內全部出清。將 $T$ 分成 $N$ 個長度為 $\tau = T/N$ 的區間。

- $x_k$：第 $k$ 期結束時的剩餘持倉，$x_0 = X$，$x_N = 0$
- $n_k = x_{k-1} - x_k$：第 $k$ 期賣出的股數
- $v_k = n_k / \tau$：第 $k$ 期的賣出速率

### 價格動態

假設不受影響的價格服從算術布朗運動：

$$S_k = S_{k-1} + \sigma\sqrt{\tau}\xi_k - \tau g(v_k)$$

其中：
- $\sigma$：價格波動率
- $\xi_k$：獨立標準常態衝擊
- $g(v_k)$：**永久衝擊函數**（permanent impact），代表交易對均衡價格的持久影響

每筆交易的實際成交價還承受一個**臨時衝擊**（temporary impact）：

$$\tilde{S}_k = S_{k-1} - h(v_k)$$

臨時衝擊不持久——它反映的是當下的流動性成本，交易完成後就消失。

### 線性衝擊假設

原始模型假設兩種衝擊都是線性的：
- $g(v) = \gamma v$（永久衝擊係數）
- $h(v) = \eta v$（臨時衝擊係數）

$\gamma$ 和 $\eta$ 越大，代表市場對你的交易越敏感。

## 最優軌跡

### 目標函數

交易者最小化總執行成本的期望值加上風險懲罰：

$$E[C] + \lambda \text{Var}[C]$$

其中 $\lambda \geq 0$ 是**風險厭惡參數**。$\lambda$ 越大，交易者越怕時間風險，傾向快賣；$\lambda$ 越小，越不怕等，傾向慢賣。

### 封閉解

在線性衝擊假設下，最優清算軌跡有精確解：

$$x_k = X \frac{\sinh(\kappa(T - t_k))}{\sinh(\kappa T)}$$

其中 $\kappa$ 由衝擊係數和風險厭惡參數決定。

這是一條**雙曲正弦曲線**，在兩個極端之間插值：

**$\lambda = 0$（風險中立）**
- 軌跡變成線性，等於 TWAP（時間加權均價）策略
- 完全不管時間風險，只管衝擊最小化
- 等速拆單，每天賣一樣多

**$\lambda \to \infty$（極度風險厭惡）**
- 軌跡退化為 $t=0$ 一次全砸
- 寧可承受巨大衝擊也不願暴露在時間風險中
- 「先跑先贏」

**中間情況**
- 風險厭惡越高，軌跡越 front-loaded（前重後輕）
- 開頭賣多一點降低時間風險，後段慢慢收尾
- 這就是多數機構執行演算法的實際形狀

## 實戰應用

### 實戰意義
### 給散戶的啟示

你可能不需要寫微分方程來拆單，但 Almgren-Chriss 的核心邏輯值得每個人理解：

1. **大單不要一次砸**：你會把價格打跑，成交均價遠差於你看到的盤面價
2. **但也不要拖太久**：持倉期間的市場風險可能比衝擊成本更貴
3. **風險越高越要快**：高波動環境下，慢拆的時間風險放大，應該縮短執行時間
4. **front-loaded 是常態**：多數機構的前端執行比重比後端高，這不是直覺而是數學最優

### 與 [[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle Lambda]] 的關聯

Kyle（1985）的 $\lambda$ 衡量的是「價格衝擊係數」——每單位交易量推動價格多少。Almgren-Chriss 中的 $\gamma$ 和 $\eta$ 本質上就是 Kyle Lambda 的離散化版本。兩者描述的是同一件事：**你的交易量越大，市場被你推得越遠。**

### 與 VWAP/TWAP 的關係

- **TWAP**：等速拆單，是 Almgren-Chriss 在 $\lambda = 0$ 時的特例
- **VWAP**：跟隨市場成交量分佈拆單，Kato（2015）證明在風險中立下加入體積過程後最優執行收斂至 VWAP
- **Almgren-Chriss**：更一般的框架，TWAP 和 VWAP 都是特殊情況

### 機構如何使用

實務上，大型券商的執行演算法（implementation shortfall 策略、arrival price 策略）幾乎都以 Almgren-Chriss 為基礎：
1. 估計 $\sigma$、$\gamma$、$\eta$（用歷史成交量和價格衝擊數據）
2. 根據客戶的風險偏好設定 $\lambda$
3. 算出最優軌跡
4. 即時監控偏離度，必要時動態調整

## 模型延伸

- **非線性衝擊**：Almgren（2003）將臨時衝擊改為冪律形式，因實證發現價格讓步隨交易量次線性成長
- **連續時間**：用 Hamilton-Jacobi-Bellman 方法推導連續時間版本，允許動態重新優化
- **適應性策略**：Almgren & Lorenz（2007）指出變異數目標具有動態不一致性，需要適應性重優化
- **Lévy 過程**：Løkka & Xu（2020）將價格動態推廣到 Lévy 過程，納入跳躍風險

## 注意事項

- 本指標/概念僅供參考，實際操作需結合當時市場環境與其他指標綜合判斷
- 歷史數據不代表未來表現，回測結果可能存在過度擬合風險
- 散戶在使用時應注意自身風險承受能力，避免過度槓桿

## 來源

- Almgren, R. & Chriss, N. (2001). "Optimal execution of portfolio transactions." *Journal of Risk*, 3(2), 5-39.
- Cartea, Á., Jaimungal, S. & Penalva, J. (2015). *Algorithmic and High-Frequency Trading*. Cambridge University Press.
- Bertsimas, D. & Lo, A. (1998). "Optimal control of execution costs." *Journal of Financial Markets*, 1(1), 1-50.
- Wikipedia: [Almgren–Chriss model](https://en.wikipedia.org/wiki/Almgren%E2%80%93Chriss_model)

## 相關主題
- [[操作策略/執行演算法VWAP-TWAP-Execution-Algorithm]] — Almgren-Chriss 在 $\lambda=0$ 時收斂至 TWAP
- [[操作策略/實施短缺與最佳執行Implementation-Shortfall-and-Best-Execution]] — 執行成本框架
- [[操作策略/VWAP執行演算法與機構交易策略VWAP-Execution-Algorithms]] — VWAP 執行演算法
- [[操作策略/交易成本分析Transaction-Cost-Analysis]] — 交易成本完整分析
- [[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model]] — Kyle Lambda 價格衝擊模型
- [[風險管理/滑價與交易執行風險]] — 滑價風險基礎