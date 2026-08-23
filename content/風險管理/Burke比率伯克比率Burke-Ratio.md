---
title: "Burke 比率（伯克比率）Burke Ratio"
---

# Burke 比率（伯克比率）Burke Ratio

> 用回撤的平方根取代標準差，衡量每單位「痛苦深度」換來多少超額報酬。

## 核心概念
Burke Ratio 由 Kevin Burke 於 1990 年代提出，屬於[[風險管理/風險調整報酬指標夏普比率與索提諾比率|風險調整報酬指標]]家族的一員。與[[風險管理/Calmar-Ratio年化報酬MDD|Calmar Ratio]]類似，它用回撤（Drawdown）而非標準差作為風險衡量基準，但有一個關鍵差異：

- **Calmar** 用「最大回撤」（MDD）——只看最慘的那一次
- **Burke** 用「所有回撤的平方和開根號」——把每次回撤都算進去

## 公式

```
Burke Ratio = (R_p - R_f) / √(Σ DD_i²)
```

其中：
- **R_p** = 投資組合年化報酬率
- **R_f** = 無風險利率
- **DD_i** = 第 i 次回撤的深度（負值取絕對值）
- **Σ DD_i²** = 期間內所有回撤深度的平方和

分母的設計是關鍵：平方後加總再開根號，讓**深度回撤的權重遠大於淺度回撤**。一次 20% 的回撤貢獻 0.04，而四次 5% 的回撤只貢獻 0.01——前者是後者的 4 倍權重。

## 與其他指標的關係

**Burke vs Sharpe：**
- Sharpe 用標準差當分母，上漲波動和下跌波動一視同仁
- Burke 只看回撤，認為「上漲的波動不是風險，回撤才是」

**Burke vs Calmar：**
- Calmar 只看單一最大回撤，如果某策略在 10 年內只有一次大回撤，Calmar 可能過度樂觀
- Burke 把所有回撤都納入，對「頻繁小回撤」的策略更敏感

**Burke vs Sortino：**
- [[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced|Sortino]] 用下行標準差（ downside deviation），考慮所有低於目標的偏差
- Burke 用回撤序列，更直觀反映「資金曲線的坑洞有多深」

**Burke vs [[風險管理/Ulcer-Index潰瘍指數與Martin-Ratio|Ulcer Index / Martin Ratio]]：**
- Ulcer Index = √(Σ DD_i² / N)，多了除以 N（回撤持續時間加權）
- Martin Ratio = (R_p - R_f) / Ulcer Index
- Burke 不除以 N，所以不考慮回撤持續時間，只看深度

## 實戰應用

### 何時用 Burke？

- **多筆回撤的策略評估**：如果一個策略有多次中等回撤而非一次大回撤，Burke 比 Calmar 更能反映真實風險
- **CTA / 期貨策略比較**：這類策略回撤頻繁但恢復快，Calmar 容易失真
- **基金經理人篩選**：比單看 MDD 更全面，避免「倖存者偏差」式的 MDD 運氣

### 計算範例

假設一個策略年化報酬 15%，無風險利率 2%，期間內有四次回撤：-5%、-8%、-12%、-3%

```
Σ DD_i² = 0.05² + 0.08² +  0.12² + 0.03²
        = 0.0025 + 0.0064 + 0.0144 + 0.0009
        = 0.0242

√(Σ DD_i²) = √0.0242 ≈ 0.1556

Burke Ratio = (0.15 - 0.02) / 0.1556 ≈ 0.836
```

### 判讀標準

- **Burke > 0.5**：尚可，回撤控制一般
- **Burke > 1.0**：良好，超額報酬足以補償回撤深度
- **Burke > 2.0**：優秀，每單位回撤平方根換來 2 倍以上超額報酬
- **Burke < 0**：策略報酬不如無風險利率，直接淘汰

## 注意事項
**優點：**
- 所有回撤都納入計算，比 Calmar 更穩健
- 平方加權讓大回撤的影響更突出，符合投資人心理感受
- 不受上漲波動影響，只懲罰「往下掉」

**缺點：**
- 回撤定義不統一（有人用日線、有人用月線），跨研究比較困難
- 不考慮回撤持續時間（一個 -10% 持續 3 天和持續 3 個月在 Burke 中權重相同）
- 樣本量小時計算不穩定，需要至少 3 年以上月度數據
- 學術文獻較少，不如 Sharpe / Sortino 普及

## 與其他回撤指標的系統定位

Burke Ratio 屬於回撤調整報酬指標家族的一員：

- **深度導向**：Calmar（只看 MDD）、Burke（看所有回撤平方和）
- **持續時間導向**：Ulcer Index、Martin Ratio
- **條件回撤**：[[風險管理/CDaR條件回撤風險Conditional-Drawdown-at-Risk|CDaR]]（只看特定分位數以上的回撤）

選擇哪個指標取決於你最在意什麼：只怕一次大崩盤用 Calmar，怕頻繁回撤用 Burke，怕長期套牢用 Ulcer/Martin。

## 相關主題

- [[風險管理/風險管理總論]]

## 來源
- Burke, K. (1994). "A Sharper Sharpe Ratio." *Computerized Investing* (AAII)
- Eling, M. & Schuhmacher, F. (2007). "Does the Choice of Performance Measure Influence the Evaluation of Hedge Funds?" *Journal of Banking & Finance*
-相關概念可參考 [[風險管理/回撤分析進階Drawdown-Analysis-Advanced|回撤分析進階]] 與 [[風險管理/回測績效評估完整體系Backtest-Performance-Evaluation|回測績效評估完整體系]]