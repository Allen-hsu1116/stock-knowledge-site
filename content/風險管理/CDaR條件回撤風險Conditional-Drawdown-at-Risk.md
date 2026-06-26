---
title: "CDaR條件回撤風險 Conditional Drawdown at Risk"
date: 2026-06-26
---

# CDaR條件回撤風險 Conditional Drawdown at Risk

> VaR/CVaR衡量的是單期損失分佈，CDaR衡量的是整段持有期間的回撤分佈——把回撤當風險測度的進階框架

## 核心概念

CDaR（Conditional Drawdown at Risk）是Alexei Chekhlov等人於2005年提出的風險測度，將Expected Shortfall的概念從單期損失延伸到路徑依賴的回撤（Drawdown）序列。傳統VaR/CVaR只看某一時點的損失分配，完全忽略了「帳戶從高點跌到谷底」這段過程中的心理壓力與資金風險。

### Drawdown的三個維度

回撤不只是「跌多少」，還包含「跌多久」和「跌幾次」：

- **幅度（Depth）**：從歷史最高點到之後最低點的跌幅百分比
- **持續時間（Duration）**：從高峰到恢復至前高的天數
- **頻率（Frequency）**：一段時間內發生回撤的次數

CDaR聚焦在幅度維度，但用條件期望值的方式捕捉回撤分佈的尾部特徵。

### CDaR的數學定義

設 portfolio 的資金曲線為一系列報酬率累積值，定義回撤序列：

```
DD(t) = max(0, max_{s≤t} [CumRet(s)] - CumRet(t))
```

即每個時點的回撤 = 歷史最高累積報酬 − 當前累積報酬（取正數部分）。

**DDα（Drawdown at Risk）**：回撤序列的α分位數（例如α=95%，即95%的時間回撤不超過此值）

**CDaRα**：在回撤超過DDα的條件下，回撤的條件期望值

```
CDaRα = E[DD(t) | DD(t) ≥ DDα]
```

### CDaR vs CVaR的關鍵差異

- **CVaR**：衡量單期損失的尾部期望值，不考慮路徑
- **CDaR**：衡量回撤的尾部期望值，考慮整個持有期間的路徑
- CVaR可能低估風險：連續多期小虧損的累積回撤可能遠大於單期VaR
- CDaR更貼近交易者真實感受：回撤才是帳戶的「胃痛指數」

### CDaR滿足一致性公理

CDaR與CVaR一樣滿足Artzner等人（1999）的一致性風險測度四大性質：

1. **單調性**：回撤較小的策略風險較小
2. **次可加性**：分散投資降低回撤風險
3. **正齊次性**：部位放大回撤等比例放大
4. **平移不變性**：加入無風險資產等量改變回撤

## 實戰應用

### 1. 策略評估與比較

回測兩個策略時，不只看Sharpe Ratio或MDD，還看CDaR：
- 策略A：MDD=15%、CDaR(95%)=12%
- 策略B：MDD=15%、CDaR(95%)=14%

策略B的MDD雖然跟A一樣，但「回撤超過DDα後的平均回撤」更大，代表尾部回撤更深、恢復更難。

### 2. 投資組合優化

用CDaR替代CVaR或方差做投資組合優化：
- 目標：最小化CDaRα（在給定報酬率約束下）
- 優勢：直接控制「最壞情況下的平均回撤深度」
- Rockafellar-Uryasev的線性規劃方法同樣適用於CDaR優化

### 3. 回撤路徑風險管理

CDaR揭示了VaR/CVaR看不見的路徑風險：
- 一個策略可能每日VaR都很小，但連續虧損30天後累積回撤極大
- CDaR把整條回撤路徑納入考量，逼你正視「溫水煮青蛙」式的風險

### 4. 搭配回撤持續時間分析

CDaR衡量回撤深度，搭配[[風險管理/回撤持續時間Drawdown-Duration|回撤持續時間]]一起看才完整：
- 高CDaR + 長持續時間 = 最危險的組合（深跌且久不恢復）
- 低CDaR + 短持續時間 = 健康的回撤模式（淺跌快速恢復）

### 5. 台股實務計算範例

假設某台股策略過去250個交易日的每日回撤值排序後：
- 95% DD（Drawdown at Risk）= 8%（95%的交易日回撤不超過8%）
- 95% CDaR = 最差5%交易日的平均回撤 = 14%

含義：如果今天回撤超過8%，平均會經歷14%的回撤深度——這比單看MDD更能反映「尾部回撤的嚴重程度」。

## 注意事項

### 1. 計算複雜度高
CDaR需要計算整條資金曲線的回撤序列，再對回撤序列做分位數與條件期望值運算。相比CVaR只需單期報酬率分佈，CDaR的計算量和數據需求更大。

### 2. 回撤序列非獨立同分佈
回撤序列有強烈的序列相關性（今天回撤大，明天大概率也大），不能像CVaR那樣直接套用i.i.d.假設的統計檢定。建議用Block Bootstrap或蒙地卡羅模擬處理序列相依性。

### 3. 樣本期間敏感
回撤深度高度依賴樣本期間是否包含極端事件。250個交易日若恰好包含一次崩盤，CDaR會大幅上升；若沒有則可能嚴重低估。建議用[[風險管理/蒙地卡羅模擬交易驗證Monte-Carlo-Simulation|蒙地卡羅模擬]]產生多條路徑計算CDaR分佈。

### 4. CDaR與MDD的關係
MDD是回撤序列的最大值（一個點），CDaR是尾部回撤的條件期望值（一個區間的平均）。MDD告訴你「最壞一次跌多少」，CDaR告訴你「最壞的那段時間平均跌多少」。兩者互補但CDaR統計上更穩定（期望值比極值穩定）。

### 5. 實務上優先看什麼
- 散戶：先看MDD（最直覺）→ 再看[[風險管理/Ulcer-Index潰瘍指數與Martin-Ratio|Ulcer Index]]（深度×持續時間）→ 最後看CDaR（進階）
- 機構：CDaR可用於策略篩選與組合優化，但需搭配[[風險管理/回撤分析進階Drawdown-Analysis-Advanced|回撤分析進階]]的多維度框架

## 相關主題

- [[風險管理/回撤分析進階Drawdown-Analysis-Advanced]]
- [[風險管理/回撤持續時間Drawdown-Duration]]
- [[風險管理/MDD最大回撤進階實戰各資產歷史回撤與管理方法]]
- [[風險管理/追蹤回撤Trailing-Drawdown固定回撤差異]]
- [[風險管理/CVaR條件風險價值Conditional-Value-at-Risk]]
- [[風險管理/蒙地卡羅模擬交易驗證Monte-Carlo-Simulation]]
- [[風險管理/Ulcer-Index潰瘍指數與Martin-Ratio]]
- [[風險管理/Calmar-Ratio年化報酬MDD]]
- [[風險管理/回撤恢復數學與帳戶生存Drawdown-Recovery-Math]]

## 來源

- [Expected Shortfall Wikipedia](../raw/2026-06-26/Expected-Shortfall-Wikipedia.md)
- Chekhlov, A., Uryasev, S., & Zabarankin, M. (2005). Drawdown Measure in Portfolio Optimization
- Rockafellar, R.T. & Uryasev, S. (2000). Optimization of Conditional Value-at-Risk