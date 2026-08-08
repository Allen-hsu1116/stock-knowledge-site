---
title: "通縮夏普比率 Deflated Sharpe Ratio"
tags: [風險管理, 績效評估, 多重檢定, 回測偏差]
---

# 通縮夏普比率 Deflated Sharpe Ratio

> 你回測 100 個策略，挑出 Sharpe 最高的那個——恭喜，你選到的可能只是統計上的幸運兒。Deflated Sharpe Ratio 把這份「多重檢定幻覺」量化，告訴你扣除選擇偏差後真正的風險調整報酬還剩多少。

## 核心概念

Deflated Sharpe Ratio（DSR）由 Bailey & López de Prado（2014）提出，是對傳統 Sharpe Ratio 的**多重檢定偏差修正**。問題的核心很簡單：當你測試 N 個策略並選擇 Sharpe 最好的那個時，你正在進行一場統計上的選美比賽——最大的值不一定是真正最好的，可能只是雜訊中跑得最快的那個。

**傳統 Sharpe Ratio 最大的問題不在於公式本身，而在於你怎麼得到它。** 回測越多策略、用越多年資料、調越多參數，你的「最佳」策略就越可能是過度擬合的產物。DSR 的目的就是把這層偏差扣掉。

## 計算邏輯

### 三個關鍵變量

DSR 的計算需要三個輸入：

1. **觀測 Sharpe Ratio（$\hat{SR}$）**：你回測得到的 Sharpe 值
2. **試驗次數（$N$）**：你總共測試了多少個策略（包含被淘汰的）
3. **樣本數（$T$）**：每個策略的回測資料筆數

### 最小 Sharpe 期望值 $\text{SR}_0$

在 $N$ 個獨立策略中，即使所有策略的真實 Sharpe 為零，光是靠隨機變異，最大觀測 Sharpe 的期望值就是：

$$\text{SR}_0 = \sqrt{V[\hat{SR}]} \cdot \left[ (1-\gamma) \Phi^{-1}(1 - 1/N) + \gamma \Phi^{-1}(1 - 1/(N e)) \right]$$

其中：
- $\gamma$ 是 Euler-Mascheroni 常數（≈0.5772）
- $\Phi^{-1}$ 是標準常態分佈的反函數
- $V[\hat{SR}]$ 是 Sharpe 估計值的變異數，近似為 $\frac{1}{T}(1 - \text{skew} \cdot \text{SR} + \frac{\kappa-1}{4} \text{SR}^2)$，其中 skew 為偏態、$\kappa$ 為峰態

### Deflated Sharpe Ratio

$$\text{DSR} = \frac{\hat{SR} - \text{SR}_0}{\sqrt{V[\hat{SR}]}}$$

**解讀**：DSR 告訴你觀測 Sharpe 扣除「在 N 次試驗中純靠運氣可能達到的最大 Sharpe」後，還剩多少超額表現。如果 DSR 接近零或為負，代表你的策略可能只是統計上的幸運兒。

## 為什麼重要：選擇偏差的數學

想像你丟 1000 次硬幣，有人連續擲出 10 次正面。你會認為他擲硬幣的技巧比較好嗎？當然不會——在夠多次試驗中，極端結果本來就會發生。

回測策略的邏輯完全一樣。Harvey & Liu（2014）的研究指出，學術論文平均測試 300+ 個因子，最後只發表顯著的那個。這等同於在 300 次試驗中選最大值，然後宣稱「這個因子有效」。

**DSR 把這個「選擇偏差」量化成一個可計算的折扣。** 試驗次數越多，$\text{SR}_0$ 越高，你的觀測 Sharpe 被扣得越多。

## 實戰應用

### 判斷策略是否真正有效

- **DSR > 2**：在 95% 信心水準下拒絕「策略 Sharpe 為零」的虛無假設
- **DSR ≈ 0**：你的策略可能只是雜訊，選擇偏差就足以解釋觀測結果
- **DSR < 0**：連選擇偏差都解釋不了你的策略比隨機好，趕快回去重做

### 記錄試驗次數

這是 DSR 最容易被忽略的實務難點：**你必須誠實計算你到底測了多少策略。** 包括：
- 不同參數組合（每調一個參數就算一次）
- 不同指標組合
- 不同時間區間
- 被你「看一眼就丟掉」的策略

多數人只記得最後上線的那個，忘記前面測了一百個失敗的——這正是 DSR 要修正的偏差來源。

### 與 PBO（Probability of Backtest Overfitting）的關係

Bailey & López de Prado 同時提出 PBO，用交叉驗證來估計回測過擬合的機率。DSR 和 PBO 互補：
- **DSR** 修正選擇偏差對 Sharpe 的影響
- **PBO** 估計整個回測框架的過擬合機率
- 兩者一起用才是完整的回測可信度評估

## 與其他績效指標的比較

- **Sharpe Ratio**：不考慮試驗次數，容易被選擇偏差污染
- **[[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced|Sortino Ratio]]**：只看下行風險，但同樣有選擇偏差問題
- **[[風險管理/信息比率與追蹤誤差Information-Ratio-and-Tracking-Error|Information Ratio]]**：用相對基準，但多重檢定問題一樣存在
- **Deflated Sharpe Ratio**：唯一直接量化選擇偏差的指標

## 關鍵限制

1. **獨立性假設**：DSR 假設各策略獨立，但實務上策略間常有相關性（同一因子不同參數），真實的選擇偏差可能比 DSR 估計的更大
2. **常態分佈假設**：$\text{SR}_0$ 的推導假設 Sharpe 估計值服從常態分佈，但報酬分佈有肥尾時此假設不成立
3. **試驗次數難以精確計算**：主觀認知與實際嘗試之間有巨大落差，人傾向低估自己測了多少策略

## 對散戶的啟示

你不需要寫論文，但 DSR 的核心邏輯每個交易者都該知道：

1. **回測越多策略不代表你越強**——你可能只是在增大找到「幸運策略」的機率
2. **在 100 個策略中選 Sharpe 2.0 的那個**，和**在 2 個策略中選 Sharpe 2.0 的那個**，可信度完全不同
3. **樣本數要夠**：用 3 個月日資料測出 Sharpe 3.0，和用 10 年月資料測出 Sharpe 1.5，後者可能更可信
4. **誠實記錄你的試驗次數**：這是 DSR 最有價值的概念——不是算出一個精確數字，而是讓你意識到自己到底「調」了多少

## 來源

- Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality." *Journal of Portfolio Management*, 40(5), 94-107.
- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. Chapter 8: "Backtesting Strategies"
- Harvey, C. & Liu, Y. (2014). "Backtesting" *Journal of Portfolio Management*

## 相關筆記

- [[風險管理/回測過擬合Backtest-Overfitting]] — DSR 修正的偏差來源
- [[風險管理/過度擬合Overfitting量化判斷]] — 過擬合的量化判斷方法
- [[風險管理/風險調整報酬指標夏普比率與索提諾比率]] — Sharpe 基礎
- [[風險管理/生存者偏差Survivorship-Bias]] — 另一種回測偏差
- [[操作策略/交易策略回測與過擬合Backtesting-and-Overfitting]] — 回測框架完整討論