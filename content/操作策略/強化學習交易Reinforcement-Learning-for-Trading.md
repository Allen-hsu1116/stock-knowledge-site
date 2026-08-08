---
title: "強化學習交易 Reinforcement Learning for Trading"
tags: [操作策略, 機器學習, 量化交易, 強化學習, AI交易]
---

# 強化學習交易 Reinforcement Learning for Trading

> 傳統 ML 告訴你「明天大概會漲」，強化學習告訴你「在這種狀態下買進，持有 3 天再賣，長期累積報酬最大」。差別在於前者預測價格，後者直接學會一套決策策略——而且能在過程中接受短期虧損換取長期收益。

## 核心概念

強化學習（Reinforcement Learning, RL）是機器學習三大範式之一（另外兩個是監督式學習和非監督式學習）。它的核心邏輯是：**一個代理人（agent）透過與環境互動、從試錯中學習，找到能最大化長期累積獎勣的最佳策略。**

### 與傳統 ML 的關鍵差異

- **監督式學習**：每個時間點都有標籤，模型預測「下一根 K 線漲跌」或「明天報酬率」
- **強化學習**：不需要每步都有標籤，只在交易結束時收到獎勵（報酬），模型自己學會「什麼狀態下做什麼動作長期最優」

**最大優勢**：RL 能學會「延遲滿足」策略——短期虧損但長期獲利的決策。傳統 ML 做不到這件事，因為它在每個時間點都在追求預測準確。

## RL 的五大組件（交易語境）

### 1. 狀態（State）

狀態是決策所需的資訊集合。交易中的 state 可以包含：
- 技術指標（RSI、MACD、均線偏離等）
- 歷史價量數據
- 籌碼面資訊（法人買賣超、融資餘額）
- 基本面數據（營收動能、本益比）
- 情緒面數據（新聞情緒、社群討論度）

**關鍵要求**：state 數據應該弱預測性（weakly predictive）且弱平穩性（weakly stationary），ML 模型在平穩數據上表現較好。

### 2. 動作（Action）

代理人可以執行的操作：
- 單一標的：買進、賣出、持有
- 投資組合：各資產的資金配置權重
- 倉位管理：加碼、減碼、平倉

### 3. 獎勵（Reward）

策略的終極目標函數：
- 每筆交易利潤
- Sharpe Ratio
- 每筆報酬率
- **實測最有效**：用 PnL 正負號（二元獎勵）——模型學得更快，專注於穩定獲利而非追逐大賺

### 4. 策略（Policy）

策略是 state 到 action 的映射函數 $\pi(s, a) = \Pr(A_t = a \mid S_t = s)$，分兩階段：

- **探索（Exploration）**：初期什麼都不懂，隨機嘗試不同動作，從結果中學習
- **利用（Exploitation）**：用學到的經驗選擇長期報酬最大的動作

**探索-利用權衡**是 RL 最核心的難題。常用的 ε-greedy 策略：

$$\varepsilon_t = \frac{1}{t^k} + \varepsilon_{\min}$$

隨時間衰減探索率，但保留最低探索機率防止策略僵化。

### 5. 環境（Environment）

環境處理代理人的動作，計算獎勵並轉移到下一狀態。交易中環境就是市場本身（或回測引擎）。

## Q-Learning：RL 的核心演算法

### Q-Table

Q-Table 的行是狀態、列是動作、值是 Q-value（該狀態下做該動作的預期未來報酬）。代理人選 Q-value 最大的動作。

### Bellman 方程式

Q-value 的更新規則：

$$Q(s, a) = R(s, a) + \gamma \max[Q(s', a')]$$

其中：
- $R(s, a)$：當前狀態動作的即時獎勵
- $\gamma$：折扣因子（0~1），越接近 1 越重視未來報酬
- $\max[Q(s', a')]$：下一狀態的最佳 Q-value

**直覺**：今天做某動作的價值 = 即時獎勵 + 未來最佳可能性的折扣值。這就是「延遲滿足」的數學基礎。

### Deep Q-Network（DQN）

當狀態空間太大（如連續價格數據），Q-Table 不可行。DQN 用神經網路替代 Q-Table：
- 輸入 state，輸出每個 action 的 Q-value
- 從回放緩衝區（replay buffer）隨機抽樣訓練，打破樣本間相關性
- 是 RL 在交易中最常見的實作方式

## 進階技術

- **Double DQN（DDQN）**：用兩個網路——主網路選動作、目標網路估值，減少 Q-value 高估偏差
- **優先經驗回放（PER）**：重要的轉換被抽樣得更頻繁
- **Dueling Networks**：分離 state value 和 action advantage 的估計
- **分佈式 RL**：建模整個報酬分佈而非只估期望值
- **Rainbow DQN**：組合多種改進的 SOTA 模型
- **Soft Actor-Critic（SAC）**：加入熵正則化促進穩健探索

## 交易中的挑戰

### Type 2 混沌

訓練時模型在隔離環境中操作，不影響市場。上線後你的交易本身會影響市場——觀察者影響被觀察的系統。這在訓練階段幾乎不可能量化。

### 金融數據的雜訊

RL 模型可能把隨機雜訊解讀為可操作信號。去雜訊方法存在，但要在去除雜訊和保留重要資訊之間平衡。

### 非平穩性

市場規則持續變化——今天有效的策略明天可能失效。RL 模型需要持續學習和適應，但過度適應近期數據又會過擬合。

### 獎勵函數設計

用純 PnL 當獎勵，模型可能學會承擔過度風險。加入風險調整（如 Sharpe、最大回撤懲罰）可以緩解，但獎勵函數的設計本身就是一門藝術。

## 實戰建議

1. **從簡單開始**：先建立 Q-Table 版本的 RL，確認基本邏輯正確再上 DQN
2. **獎勵用二元 PnL**：正報酬 +1、負報酬 -1，模型學得比連續報酬更快
3. **state 不要太複雜**：5-10 個有效特徵勝過 50 個雜訊特徵
4. **回測記得加交易成本**：RL 很容易學會高頻交易策略，但手續費一加就虧
5. **和 [[風險管理/通縮夏普比率Deflated-Sharpe-Ratio|DSR]] 一起用**：RL 調參空間巨大，選擇偏差嚴重，試驗次數極多
6. **不要全自動上線**：RL 模型應該是決策輔助工具而非全自動交易機器人

## 與傳統策略的互補

RL 不是取代傳統技術分析或基本面分析，而是提供一個**自動化學習決策框架**。最佳用法是：
- 用技術/基本面分析定義 state 空間
- 用 RL 學習在這些 state 下的最優動作序列
- 用傳統風控框架限制 RL 的風險承擔

## 來源

- Wikipedia: [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
- QuantInsti: [Reinforcement Learning in Trading](https://blog.quantinsti.com/reinforcement-learning-trading/)
- Sutton, R. & Barto, A. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
- Dr. Tom Starke, *Deep Reinforcement Learning in Trading*

## 相關筆記

- [[技術分析/XGBoost技術指標整合策略]] — 監督式 ML 在交易中的應用
- [[風險管理/通縮夏普比率Deflated-Sharpe-Ratio]] — RL 回測必須搭配的偏差修正
- [[風險管理/過度擬合Overfitting量化判斷]] — RL 模型過擬合風險極高
- [[風險管理/回測過擬合Backtest-Overfitting]] — 回測過擬合通用框架
- [[操作策略/交易策略回測與過擬合Backtesting-and-Overfitting]] — 回測框架
- [[操作策略/交易系統體制適應策略Adaptive-Trading-System]] — 自適應交易系統