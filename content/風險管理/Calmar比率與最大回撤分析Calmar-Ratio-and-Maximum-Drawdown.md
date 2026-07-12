---
title: "Calmar比率與最大回撤分析 Calmar Ratio and Maximum Drawdown"
tags: [風險管理, 績效評估, 回撤分析, Terry Young]
created: 2026-07-08
---

# Calmar比率與最大回撤分析 Calmar Ratio and Maximum Drawdown

> 年化報酬率除以最大回撤——你賺的錢值不值得你承受的痛？Calmar 比率用最直觀的方式回答這個問題：每承受 1% 的最大回撤，能換來多少 % 的年化報酬。

## 核心概念

**Calmar 比率** 由 Terry W. Young 於 1991 年在《Futures》期刊上首次發表。名稱來自他的公司 California Managed Accounts 和其通訊 CMA Reports 的縮寫：**CAL**ifornia **M**anaged **A**ccounts **R**eports。

Calmar 比率衡量的是**報酬與回撤的交換效率**：

$$\text{Calmar Ratio} = \frac{\text{年化報酬率}}{\text{最大回撤率}}$$

- 年化報酬率：過去 36 個月的平均年化報酬
- 最大回撤率：過去 36 個月的最大峰谷跌幅

### 為什麼用最大回撤而不是標準差？

[[風險管理/VaR風險值Value-at-Risk|Sharpe 比率]] 用標準差衡量風險，但標準差有個致命問題：**它把上漲和下跌一視同仁**。對投資人來說，漲 5% 和跌 5% 的痛苦程度完全不同。

最大回撤（Maximum Drawdown）衡量的是**從歷史最高點跌到最低點的最大跌幅**——這才是投資人真正感受到的痛。

### 一句話理解

- Calmar > 3：優秀的策略，賺的比痛的多很多
- Calmar 1-3：尚可，報酬和回撤大致匹配
- Calmar < 1：糟糕，承受的回撤比賺的報酬還大

## 最大回撤（Maximum Drawdown）

### 定義

$$\text{Drawdown}_t = \frac{\text{Peak}_t - \text{Value}_t}{\text{Peak}_t}$$

$$\text{Max Drawdown} = \max_t(\text{Drawdown}_t)$$

最大回撤就是從歷史淨值的最高峰，跌到之後的最低谷，中間的跌幅百分比。

### 計算範例

假設某策略淨值走勢：
- 第 1 月：100（Peak）
- 第 3 月：85 → 回撤 15%
- 第 6 月：110（新 Peak）
- 第 9 月：88 → 回撤 20%
- 第 12 月：120（新 Peak）

最大回撤 = 20%（從 110 跌到 88）

### 回撤的三個維度

只看最大回撤率還不夠，還要關注：
1. **回撤深度**（Depth）：跌了多少 %
2. **回撤持續時間**（Duration）：從峰到谷花了多久
3. **恢復時間**（Recovery）：從谷底回到前高花了多久

一個 -30% 但 2 個月就恢復的回撤，和一個 -30% 但花了 2 年才恢復的回撤，心理壓力完全不同。

## Calmar vs 其他風險調整指標

### Calmar vs Sharpe

- **Sharpe**（[[風險管理/VaR風險值Value-at-Risk|Sharpe 比率]]）：(報酬 - 無風險利率) / 標準差
- **Calmar**：年化報酬 / 最大回撤

| 比較 | Sharpe | Calmar |
|------|--------|--------|
| 風險衡量 | 標準差（波動） | 最大回撤（下行風險） |
| 上下行區分 | 不區分 | 只看下行 |
| 時間視角 | 逐期波動 | 路徑依賴 |
| 心理貼合度 | 低 | 高 |

### Calmar vs Sortino

- **Sortino**（[[風險管理/Omega比率Omega-Ratio|Sortino 比率]]）：(報酬 - 目標) / 下行標準差
- **Calmar**：年化報酬 / 最大回撤

Sortino 改善了 Sharpe 不區分上下行的問題，但下行標準差仍是一個統計量。Calmar 更直觀——直接用最大回撤。

### Calmar vs MAR Ratio

- **Calmar**：過去 36 個月數據
- **MAR Ratio**：從成立以來的所有數據

兩者常被混淆，差異在於時間窗口。MAR 使用更長的歷史數據，對存續期長的基金更有參考價值，但對新策略不適用。

### Calmar vs Sterling

- **Sterling Ratio**：平均年報酬 / (最大回撤 - 10%)
- **Calmar**：平均年報酬 / 最大回撤

Sterling 在分母減 10% 是因為認為 10% 以內的回撤不算「真正風險」。Calmar 不做此假設，更保守。

### Calmar vs CDaR

- [[風險管理/CDaR條件回撤風險Conditional-Drawdown-at-Risk|CDaR]]：條件回撤風險，衡量最壞 5% 的平均回撤
- **Calmar**：只用單一最大回撤

CDaR 比 Calmar 更穩健——單一最大回撤可能是極端異常值，CDaR 取條件期望值更穩定。

## 實戰應用

### 應用一：策略評估

比較兩個策略：
- 策略 A：年化 25%，最大回撤 20% → Calmar = 1.25
- 策略 B：年化 18%，最大回撤 8% → Calmar = 2.25

策略 B 雖然報酬較低，但 Calmar 更高——**每承受 1% 回撤換來的報酬更多**，風險效率更好。

### 應用二：基金/ETF 篩選

在篩選基金或 ETF 時：
- Calmar > 3 視為優秀
- Calmar 1-3 視為可接受
- Calmar < 0.5 應警惕

台股指數型 ETF（如 0050）的 Calmar 比率約 0.5-1.5（視計算期間），主動型優質基金可能達 2-3。

### 應用三：部位控制

根據 Calmar 比率動態調整部位：
- Calmar 上升 → 策略風險效率改善 → 加碼
- Calmar 下降 → 策略風險效率惡化 → 減碼
- Calmar 跌破 1 → 考慮暫停或更換策略

### 應用四：回撤恢復評估

不只看 Calmar 數字本身，還要看回撤恢復能力：
- 快速恢復（< 3 個月） → Calmar 數字的含金量高
- 慢速恢復（> 12 個月） → 即使 Calmar 數字好看，心理承受難度高

## 限制與陷阱

### 1. 樣本期間敏感性

Calmar 用 36 個月數據，不同起點計算可能差異很大。一個恰好沒有大回撤的 36 個月窗口會得到異常高的 Calmar。

### 2. 單一極端值影響

最大回撤是單一數據點——一次極端事件就能壓垮 Calmar。建議搭配 CDaR 或平均回撤一起看。

### 3. 不適合新策略

新策略或新基金沒有 36 個月歷史，Calmar 無法計算或不可靠。

### 4. 報酬計算方式影響

原始 Calmar 用算術平均年報酬，後來有版本改用 CAGR（複合年成長率）。兩者結果可能差異顯著，比較時要確認計算方式。

### 5. 忽略回撤路徑

同樣是 -30% 最大回撤：
- 路徑 A：直線下跌一個月到位 → 痛但短
- 路徑 B：陰跌兩年慢慢到位 → 溫水煮青蛙

Calmar 完全不區分這兩種路徑。

## 台股實戰框架

### 個股 Calmar 計算

1. 取過去 36 個月月收盤價
2. 計算每月報酬率的算術平均 × 12 = 年化報酬
3. 計算累積淨值曲線的最大回撤
4. Calmar = 年化報酬 / 最大回撤

### 選股應用

- 篩選 Calmar > 1.5 的個股作為候選池
- 搭配 [[基本面分析/Piotroski-F-Score進階實戰|F-Score]] 過濾基本面
- 搭配 [[技術分析/相對成交量RVOL-Relative-Volume|RVOL]] 確認流動性
- 定期重新計算（至少每季），監控 Calmar 變化

### 投資組合層面

- 計算整體投資組合的 Calmar
- 目標組合 Calmar > 2
- 如果組合 Calmar < 1，檢視是否需要降低槓桿或調整持倉結構

## 相關頁面

- [[風險管理/VaR風險值Value-at-Risk]] — Sharpe 比率的風險衡量基礎
- [[風險管理/Omega比率Omega-Ratio]] — Sortino 和 Omega 比率
- [[風險管理/CDaR條件回撤風險Conditional-Drawdown-at-Risk]] — Calmar 的進階版，用條件回撤而非單一最大回撤
- [[風險管理/風險管理總論]] — 風險管理框架
- [[風險管理/風險資金配置Risk-Capital-Allocation]] — 部位控制方法
- [[操作策略/凱利公式Kelly-Criterion最佳下注比例]] — 最適下注比例
- [[基本面分析/Piotroski-F-Score進階實戰]] — 搭配基本面篩選

## 參考來源

- [Calmar ratio - Wikipedia](https://en.wikipedia.org/wiki/Calmar_ratio)
- Terry W. Young, "Calmar Ratio", Futures Magazine, 1991
- California Managed Accounts (CMA) Reports

## 注意事項

（待補充）

## 相關主題

（待補充）
