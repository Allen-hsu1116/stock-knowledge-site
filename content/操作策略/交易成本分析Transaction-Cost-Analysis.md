---
title: "交易成本分析 Transaction Cost Analysis (TCA)"
category: "操作策略"
---

# 交易成本分析 Transaction Cost Analysis (TCA)

> 機構投資人用來衡量交易執行品質的系統化方法——你的交易到底在什麼價格成交的？跟理想價格差多少？差在哪裡？

## 核心概念

交易成本分析（Transaction Cost Analysis, TCA）是金融機構用來評估交易執行品質的框架。Financial Times 的定義是：「研究交易價格以判斷交易是否在有利價格成交——買進時價格越低越好、賣出時價格越高越好。」

### 為什麼需要 TCA？

- **隱形成本比顯性成本大**：手續費和稅金看得到，但市場衝擊、滑價、延遲成本看不到，而後者通常是前者的數倍
- **法規要求**：歐洲 MiFID II 等法規要求金融機構必須實現「最佳執行」（Best Execution），TCA 是合規工具
- **績效歸因**：基金經理人要知道績效不佳是因為選錯股還是執行太差
- **供應商管理**：機構要評估券商的執行品質，TCA 提供量化依據

## 交易成本的四大分類

### 1. 顯性成本（Explicit Cost）
- 手續費、交易稅、過戶費、清算費
- 看得見、可預估、容易比較
- 台股：手續費 0.1425%（折扣後可低至 0.01-0.0285%）、賣出交易稅 0.3%

### 2. 隱性成本（Implicit Cost / Market Impact）
- 買進時推高價格、賣出時壓低價格
- 大單比小單影響更大——[[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle's Lambda]] 量化這個關係
- 市場衝擊 = 實際成交均價 − 決策時的市場價格（Arrival Price）

### 3. 延遲成本（Delay Cost）
- 從投資決策到實際下單之間，價格已經移動
- 例如 PM 決定買台積電 800 元，等交易員拿到單子時台積電已經 805 元，5 元就是延遲成本

### 4. 機會成本（Opportunity Cost）
- 沒成交的後果——想買沒買到，股價漲了
- 實施短缺（Implementation Shortfall）框架中的機會成本 = 未成交部位 × （期末價格 − 決策時價格）

## TCA 的兩個階段

### 盤前分析（Pre-Trade Analysis）

**目的**：在交易前預估成本、決定最佳執行策略

**Almgren-Chriss 模型核心**：
- 交易速度與成本之間存在「效率前緣」（Efficient Frontier）
- 交易越快 → 市場衝擊越大 → 成本越高
- 交易越慢 → 風險越大（價格可能跑掉）→ 風險成本越高
- 在前緣上選擇風險-成本的最優組合

**決策變數：**
- 參與率（Participation Rate）：不超過該時段成交量的 X%
- 執行時間：分幾天完成、每天交易多少
- 演算法選擇：[[操作策略/執行演算法VWAP-TWAP-Execution-Algorithm|VWAP/TWAP/POV/IS]]

### 盤後分析（Post-Trade Analysis）

**四步驟框架：**

**Step 1 — 記錄（Record）**
- 記錄每筆訂單生命週期的完整事件：下單時間、修改、成交、拒絕
- 使用 FIX（Financial Information eXchange）協議確保數據一致性
- OMS/EMS 的數據粒度不夠，需補充券商通訊記錄

**Step 2 — 衡量（Measure）**
- 對比多種基準計算成本：
  - **VWAP**（成交量加權均價）：最常見，適合流動性好的標的
  - **TWAP**（時間加權均價）：適合均勻分散執行
  - **Arrival Price**（到達價）：決策時的市場價格
  - **Implementation Shortfall**（[[操作策略/實施短缺與最佳執行Implementation-Shortfall-and-Best-Execution|實施短缺]]）：所有顯性+隱性+機會成本總和
  - **PWP**（參與加權均價）：考慮自身交易對市場的影響

**Step 3 — 歸因（Attribute）**
- 把總成本拆解到各個來因：
  - 訂單大小 vs 市場深度
  - 波動率
  - 買賣價差
  - 市場趨勢（上漲時買進成本高、下跌時賣出成本低）
  - 交易員技術
- 區分「市場因素」（產業、地區、市值、動量）和「人為技能」

**Step 4 — 評估與監控（Evaluate & Monitor）**
- 生成定期報告：週報、月報
- 視覺化趨勢：成本走勢圖、券商比較圖
- 設定改善目標，追蹤後續交易的改進效果

## 實施短缺（Implementation Shortfall）詳解

**公式：**

IS = 顯性成本 + 隱性成本 + 延遲成本 + 機會成本

= 手續費稅金 + (成交均僑 − Arrival Price) × 成交股數 + (Arrival Price − 決策價) × 未成交股數

**解讀：**
- IS > 0 且主要來自隱性成本 → 交易太快，市場衝擊大
- IS > 0 且主要來自機會成本 → 交易太慢，沒成交的部位漲走了
- IS ≈ 0 → 執行品質良好

**台股情境：**
- PM 決定買台積電 100 張，決策時 800 元（Arrival Price）
- 當天買進均價 802 元，成交 80 張
- 手續費 802×80×0.001425 ≈ 9,143 元
- 剩餘 20 張沒買到，收盤台積電 810 元
- 顯性成本 = 9,143 元
- 隱性成本 = (802 − 800) × 80,000 = 160,000 元
- 機會成本 = (810 − 800) × 20,000 = 200,000 元
- IS = 9,143 + 160,000 + 200,000 = 369,143 元
- 隱性+機會占 97.5%，顯性只占 2.5%

## 散戶的 TCA 應用

散戶不用做機構級 TCA，但核心概念可以應用：

**簡化版 TCA Checklist：**
- **盤前**：大單拆小單，不要一次下 500 張，分批進場
- **盤中**：記錄你的決策價格 vs 實際成交價格
- **盤後**：定期算一下自己的「滑價成本」= 實際成交均價 − 決策時價格
- **比對**：如果滑價持續 > 0.5%，考慮改用限價單或拆單

**台股散戶常見的隱形成本陷阱：**
- 用市價單買流動性差的股票 → 買在漲停價
- 除權息前一天大單進出 → 衝擊成本 + 稅務成本
- 盤中追漲殺跌 → 心理成本轉化為實際成本

## TCA 與最佳執行的關係

TCA 是實現 [[操作策略/實施短缺與最佳執行Implementation-Shortfall-and-Best-Execution|Best Execution]] 的測量工具：
- Best Execution 是「目標」——確保交易在最有利條件成交
- TCA 是「方法」——量化衡量是否達成 Best Execution
- MiFID II 要求機構每季發布 Best Execution 報告，TCA 是其數據基礎

## 相關連結

- [[操作策略/實施短缺與最佳執行Implementation-Shortfall-and-Best-Execution]] — TCA 的核心基準
- [[操作策略/執行演算法VWAP-TWAP-Execution-Algorithm]] — 執行策略選擇
- [[操作策略/VWAP執行演算法與機構交易策略VWAP-Execution-Algorithms]] — VWAP 執行細節
- [[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model]] — 市場衝擊的理論基礎
- [[風險管理/交易總成本TCT與滑價風險]] — 散戶版交易成本
- [[風險管理/滑價與交易執行風險]] — 滑價風險
- [[風險管理/交易執行力缺口Execution-Gap]] — 執行落差
- [[風險管理/市場微結構與流動性定價Market-Microstructure-and-Liquidity-Pricing]] — 微結構基礎


## 實戰應用
（待補充）


## 注意事項
（待補充）


## 相關主題
（待補充）

## 來源

- Wikipedia: Transaction cost analysis
- Almgren, R. and Chriss, N. (2000). "Optimal execution of portfolio transactions." J. Risk 3(2), 5-39
- Perold, A. "The Implementation Shortfall: Paper vs. Reality." Journal of Portfolio Management 14(3), 1988
- Financial Times Lexicon: TCA definition
- 實戰經驗整理