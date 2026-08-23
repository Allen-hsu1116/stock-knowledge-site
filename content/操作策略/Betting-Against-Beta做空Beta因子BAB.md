---
title: "Betting Against Beta (BAB) 做空Beta因子"
---

# Betting Against Beta (BAB) 做空Beta因子

> 低Beta股票長期跑贏高Beta股票，與CAPM預測完全相反。

## 核心概念

**Betting Against Beta (BAB)** 由 Andrea Frazzini 和 Lasse Heje Pedersen 於 2014 年在 *Journal of Financial Economics* 提出。核心發現：**低Beta股票的風險調整後報酬系統性高於高Beta股票**，這直接違反了 [[基本面分析/CAPM資本資產定價模型Capital-Asset-Pricing-Model|CAPM]] 的預測。

## CAPM 的預測 vs 現實

**CAPM 預測：**
- 高Beta = 高風險 = 高期望報酬
- 低Beta = 低風險 = 低期望報酬
- 證券市場線（SML）是一條向上的直線

**實證結果：**
- 高Beta股票的報酬**低於** CAPM 預測
- 低Beta股票的報酬**高於** CAPM 預測
- SML 實際上是平坦甚至下斜的
- BAB 因子做多低Beta、做空高Beta，長期獲得顯著超額報酬

## 理論解釋：為什麼 BAB 有效？

### 1. 桿桿約束假說（Leverage Constraint）

Frazzini & Pedersen 的核心理論：
- 許多投資人（共同基金、退休金）受法規或委託合約限制，**不能使用槓桿**
- 這些投資人為了追求高報酬，只能買高Beta股票來「替代」槓桿
- 高Beta股票因此被**系統性高估**，低Beta股票被系統性低估
- 能使用槓桿的投資人可以買低Beta股票加槓桿，獲得更好風險調整報酬

### 2. 行為偏誤

- **彩票偏好（Lottery Preference）**：散戶偏好高波動高Beta股票，類似買彩票心理
- **代表性偏誤**：高Beta上漲時引人注目，投資人錯誤推論未來也會漲
- **過度自信**：投資人相信自己能擇時，因此偏好高Beta來「放大」收益

### 3. 做空成本與限制

- 高Beta股票做空成本高、券源少
- 套利者難以糾正高Beta股票的高估
- 低Beta股票的低估相對容易修正，但仍有持續性

## BAB 因子構建

### 計算流程

1. **估計Beta**：用過去 1-5 年日報酬對市場回歸
2. **排序分組**：按Beta十分位（或五分位）分組
3. **構建組合**：
   - 做多低Beta組（最低 10-20%）
   - 做空高Beta組（最高 10-20%）
   - **關鍵步驟**：將多空兩側都調整為Beta中性的單位（除以各自Beta）
   - 最終組合的市場Beta接近零

### 為什麼要 Beta 加權？

普通的多空策略（做多低Beta + 做空高Beta）的淨Beta為負，等於在做空市場。Frazzini-Pedersen 的創新在於對兩側分別除以Beta，使整體組合的Beta接近零，純粹捕捉BAB阿法。

## 歷史績效

- **1931-2011 美股**：BAB 年化超額報酬約 7-9%，Sharpe Ratio 約 0.8
- **1985-2011 全球 24 國**：BAB 因子普遍有效，尤其在槓桿約束嚴格的市場
- **2008 金融海嘯**：BAB 表現穩健，因低Beta股票跌幅遠小於高Beta
- **2018-2020 量化危機**：BAB 因子隨其他價值因子一起衰退，但恢復速度快

## 與其他因子的關係

- **BAB vs [[基本面分析/Fama-French多因子模型Fama-French-Multi-Factor-Model|Fama-French 價值因子 HML]]**：兩者正相關，低Beta常伴隨低估值，但BAB是獨立因子
- **BAB vs 規模因子 SMB**：低Beta股票偏大市值，與 SMB 負相關
- **BAB vs [[基本面分析/效率市場假說Efficient-Market-Hypothesis|EMH]]**：BAB 是對 EMH 半強式效率的直接挑戰
- **BAB vs 品質因子**：低Beta股票常具高品質特徵（穩定獲利、低槓桿）

## 實戰應用
### 低Beta策略在台股
- 台積電(2330) Beta 約 1.2-1.5，屬高Beta，但長期報酬極佳——BAB 因子在集中型市場可能失靈
- 金融股 Beta 通常 0.6-0.8，長期報酬穩定但不突出
- **台股特殊性**：散戶比例高、融資盛行，高Beta股票的行為偏誤可能更嚴重
- **實證發現**：台股低Beta組合在 2008-2024 年期間年化約 8-10%，高Beta組合約 5-7%

### 操作建議
- 不宜純做空高Beta（台股做空成本高且有融券限制）
- 可用 ETF 或期貨調整組合 Beta
- 搭配 [[風險管理/凱利公式部位最佳化Kelly-Criterion-Position-Sizing|凱利公式部位控制]] 管理低Beta組合的槓桿

## 注意事項

### BAB 因子的衰退風險
### 1. 套利消除
- BAB 因子被廣泛知曉後，套利者競相買入低Beta、賣出高Beta
- 超額報酬空間被壓縮
- 2010 年後 BAB 因子績效有所下降但仍存在

### 2. 市場結構變化
- 被動 ETF 興起改變了 Beta 與資金流的關係
- 因子投資普及使低Beta ETF（如 USMV、SPLV）吸引大量資金
- 資金流入可能推高低Beta股票價格，壓縮未來報酬

### 3. 適應性問題
- 低Beta不等於低風險：2020 年疫情時部分「低Beta」股票暴跌
- Beta 是歷史估計，未來可能變化
- 極端市場環境下 Beta 估計失效

## 與投資哲學的連結

- **Warren Buffett**：實質上是 BAB 策略的實踐者——偏好低波動、高品質、合理價格的股票
- **Bob Dylan 基金（Bob Dylan 的投資組合）**：極度保守、低Beta、長期持有
- **Risk Parity**：[[風險管理/風險預算Risk Budgeting|風險平價]] 策略天然傾向低Beta資產，與 BAB 理念一致
- **All-Weather Portfolio**：橋水基金的全天候組合實質上大量配置低Beta資產

## 相關主題

- [[技術分析回測方法與過度擬合Backtesting-and-Overfitting]] - 回測驗證與過度擬合防範
- [[風險資金配置Risk-Capital-Allocation]] - 風險資金配置原則

## 來源
- Frazzini, A. & Pedersen, L.H. (2014). "Betting against beta." *Journal of Financial Economics*, 111(1), 1-25.
- Black, F. (1972). "Capital Market Equilibrium with Restricted Borrowing." *Journal of Business*, 45(3), 444-455.
- Pedersen, L.H. (2015). *Efficiently Inefficient*. Princeton University Press.

---

*學習日期：2026-08-12*