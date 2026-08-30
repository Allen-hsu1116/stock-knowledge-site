---
title: "Pain Index 與 Pain Ratio"
category: "風險管理"
---

# Pain Index 與 Pain Ratio

> 用回撤的「深度 × 持續時間」平均來衡量投資痛苦程度，比最大回撤更能反映持有過程的心理負擔。

## 核心概念

Pain Index 由 Zephyr Associates（現 StyleAdvisor）開發，核心邏輯是把投資組合在整段分析期間的**每一個時間點的回撤值取算術平均**，而不像最大回撤（MDD）只看最慘的那一瞬間。

具體計算方式：對每個時間點 t，先算回撤 D(t) = (Peak(t) - Value(t)) / Peak(t)，再對整段期間所有時間點的 D(t) 取算術平均。

- **Pain Index** = 平均回撤（mean drawdown）
- **Pain Ratio** = (年化報酬 - 無風險利率) / Pain Index

Pain Ratio 的結構跟 Sharpe Ratio 一模一樣，只是把分母從標準差換成 Pain Index。數值越高越好，代表「每單位痛苦換來的報酬」越高。

## 與其他回撤指標的比較

- **[[MDD最大回撤計算與恢復難度|MDD 最大回撤]]**：只看最壞那一瞬間的回撤深度，完全忽略「回撤持續了多久」。兩支基金 MDD 相同，但一支跌 30% 一個月就回來、另一支跌 30% 持續兩年，心理負擔天差地別
- **[[Calmar-Ratio年化報酬MDD|Calmar Ratio]]**：年化報酬 / MDD，基於「最壞情況」的假設，但「最壞情況」可能只出現一瞬間
- **[[Ulcer-Index潰瘍指數與Martin-Ratio|Ulcer Index]]**：回撤平方的平均再開根號，對深度回撤的懲罰更重（因為平方放大），且 Martin Ratio = 年化報酬 / Ulcer Index
- **Pain Index**：回撤的算術平均，包含持續時間訊息，但不像 Ulcer 那樣加重深度
- **[[CDaR條件回撤風險Conditional-Drawdown-at-Risk|CDaR]]**：條件回撤風險，看最壞 n% 的回撤分位數

簡單說：MDD 看最壞瞬間、Pain Index 看平均痛苦、Ulcer Index 看加權痛苦、CDaR 看尾部痛苦。

## 實戰應用

**基金篩選**：比較同類基金時，Pain Ratio 比 Sharpe Ratio 更能反映「持有過程的心理負擔」。兩支基金 Sharpe 相同，但 Pain Index 差很多代表其中一支回撤頻繁且持續久，持有體驗差很多。

**策略特性比較**：
- 均值回歸策略：回撤淺但頻繁 → Pain Index 中等，MDD 低
- 動量策略：回撤深但恢復快 → Pain Index 中等偏高，MDD 高
- 趨勢追蹤策略：回撤深且持續久 → Pain Index 高，MDD 高

**資產配置**：在優化中加入 Pain Index 約束，會偏好「回撤持續時間短」的資產組合，而非只追求報酬率最高。

## 注意事項

- **取樣頻率影響數值**：日頻 Pain Index > 週頻 > 月頻，比較時必須用相同頻率
- **不區分「正在回撤」和「已恢復」**：只看絕對回撤值，一個深度回撤後已經創新高跟還在回撤中是一樣的
- **與 Ulcer Index 高度相關**：兩者都在衡量「回撤的平均程度」，擇一使用即可，不需要同時報告
- **無風險利率選擇**：Pain Ratio 的無風險利率會影響數值，長期分析用 10 年期公債殖利率、短期用 3 個月 T-Bill

## 相關主題

- [[Ulcer-Index潰瘍指數與Martin-Ratio]] — 回撤平方平均版，對深度回撤懲罰更重
- [[Calmar-Ratio年化報酬MDD]] — 用 MDD 當分母的風險調整報酬
- [[MDD最大回撤計算與恢復難度]] — Pain Index 的基礎組成元素
- [[回撤持續時間Drawdown-Duration]] — Pain Index 隱含的時間維度
- [[回撤分析進階Drawdown-Analysis-Advanced]] — 回撤分析完整體系
- [[風險調整報酬指標夏普比率與索提諾比率]] — Pain Ratio 的同類指標
- [[Sterling-Ratio斯特林比率]] — 另一個用回撤做分母的績效指標

## 來源

- [一致性風險測度 Coherent Risk Measures](../../raw/2026-08-07/Pain-Index與Pain-Ratio.md)
- Zephyr Associates / StyleAdvisor 原始定義
- 行業知識整理