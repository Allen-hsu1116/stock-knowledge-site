# 蒙地卡羅模擬交易驗證 Monte Carlo Simulation for Trading

> 把回測的單一結果變成一萬條平行宇宙的資金曲線，用機率分布取代點估計，戳破「歷史回測等於未來」的幻想

## 核心概念

蒙地卡羅模擬（Monte Carlo Simulation）是一種統計技術，透過注入隨機性到資料集中，生成機率分布以進行更好的風險分析與量化決策。

### 為什麼需要蒙地卡羅？

歷史回測有三大盲點：

1. **順序風險（Sequence Risk）**：同樣的100筆交易，虧損集中在前期 vs 集中在後期，結局完全不同。前期連續虧損可能直接斷頭，根本撐不到後面賺錢
2. **過度擬合隱蔽**：回測最佳化容易把雜訊當訊號，蒙地卡羅可以區分穩健型態 vs 歷史巧合
3. **尾部風險低估**：單一路徑回測忽略「差一點就發生」的極端情境

### 四種蒙地卡羅方法

| 方法 | 做什麼 | 用途 |
|------|--------|------|
| **Reshuffle（重排）** | 打亂歷史交易順序，1000條曲線終點相同但路徑不同 | 回撤與風險估算 |
| **Resample（重抽）** | 取後放回抽樣，同一筆交易可出現多次，終點不同 | 更寬廣的分布，部位最佳化 |
| **Randomized（隨機出場）** | 保留原始進場，隨機化出場 | 檢測進場是否真有edge，抓過擬出場 |
| **Permutation（置換）** | 打亂價格變動的統計特性，重建合成數據 | 策略穩健性壓力測試 |

## 實戰應用

### 1. 預估真實MDD（95%信賴區間）

回測MDD 15%，蒙地卡羅可能告訴你95%信心下MDD會高達28%。用蒙地卡羅的MDD來準備保證金，不是用回測的。

**操作步驟**：
1. 提取回測交易清單
2. 跑 5,000-10,000 次模擬
3. 看 MDD 分布的第 95 百分位數
4. 用這個數字來決定部位大小和資金準備

### 2. 破產機率分析（Risk of Ruin）

設定破產臨界點（如虧損50%），蒙地卡羅會告訴你在一萬個平行宇宙中觸及底線的次數。

- **專業機構標準**：破產機率 > 1% 就打回票
- **解法不是改策略，是降部位**：從5%降到2%，破產機率可能斷崖式下降

### 3. Equity Curve Bands（策略健康監控）

在回測資金曲線尾端隨機加100筆交易，重複1000次，取第5和第95百分位。如果實盤落在區間外，策略可能壞了。

### 4. 連勝連敗序列分析

回測最多6連虧，蒙地卡羅可能告訴你9連虧完全可能。心理準備要建立在蒙地卡羅的分布上，不是回測的。

### 5. 參數敏感度測試

對策略參數加入小幅隨機擾動。如果MA從20天改成21天績效就崩潰，你的策略是脆弱的。

## 注意事項

### 模擬次數
- 最低1000次，理想5000-10000次
- 少於1000次估計不穩定
- 可以跑兩次比較結果驗證穩定性

### 交易依賴性
- 配對交易的兩腿不可分開打亂
- 相關聯的交易要分組處理

### 不要把模擬當最佳化
- 蒙地卡羅揭露不確定性，不會改善策略
- 用模擬結果選參數 = 換個方式過擬合

### 市場制度效應
- 跨制度打亂（牛市+熊市混在一起）可能產生不現實情境
- 考慮分層抽樣（stratified shuffling）保留制度結構

### 小樣本陷阱
- 交易次數 < 100，蒙地卡羅結果多為雜訊
- 需要幾百筆以上才有真正洞察

### 過度解讀小差異
- 兩個策略的蒙地卡羅分布重疊 → 無法判斷誰優誰劣
- 差異可能是雜訊

## Python 實作框架

```python
import numpy as np

def monte_carlo_reshuffle(trades, n_sim=5000):
    results = []
    for _ in range(n_sim):
        shuffled = np.random.permutation(trades)
        equity = np.cumsum(shuffled)
        mdd = np.max(np.maximum.accumulate(equity) - equity)
        results.append(mdd)
    return np.array(results)

# 使用方式
trades = np.array([...])  # 你的交易損益列表
mdd_dist = monte_carlo_reshuffle(trades, 10000)
print(f"95% MDD: {np.percentile(mdd_dist, 95):.1f}")
print(f"破產機率: {np.mean(mdd_dist > 破產閾值):.2%}")
```

## 相關主題

- [[風險管理/回測過擬合Backtest-Overfitting|回測過擬合 Backtest Overfitting]]
- [[風險管理/過度擬合Overfitting量化判斷|過度擬合Overfitting量化判斷]]
- [[風險管理/回測驗證Backtesting陷阱|回測驗證Backtesting陷阱]]
- [[風險管理/策略壓力測試Stress-Testing|策略壓力測試Stress Testing]]
- [[風險管理/風險報酬比Risk-Reward-Ratio|風險報酬比Risk Reward Ratio]]
- [[風險管理/交易期望值Trading-Expectancy|交易期望值Trading Expectancy]]
- [[風險管理/資金曲線管理Equity-Curve-Management|資金曲線管理Equity Curve Management]]

## 來源

- [蒙地卡羅模擬在程式交易中的應用](../raw/2026-05-01/蒙地卡羅模擬程式交易壓力測試.md)
- [Monte Carlo Simulation Complete Guide](../raw/2026-05-01/MonteCarloSimulationCompleteGuide.md)
- [Monte Carlo Practical Guide Strategy Validation](../raw/2026-05-01/MonteCarloPracticalGuideStrategyValidation.md)
- [蒙特卡罗模拟法 - 知乎](../raw/2026-05-01/蒙特卡罗模拟法专业交易员.md)