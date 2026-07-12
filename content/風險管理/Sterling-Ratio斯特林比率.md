# Sterling Ratio 斯特林比率

> 用年化報酬除以平均年度回撤衡量風險調整報酬——Calmar 的「平均版」，不看單一最壞回撤而是看每年回撤的平均值。

## 什麼是 Sterling Ratio

Sterling Ratio 是風險調整報酬指標，由 Deane Sterling Jones 於 1981 年提出。與 [[風險管理/Calmar比率與最大回撤分析Calmar-Ratio-and-Maximum-Drawdown|Calmar比率]] 類似都是用回撤做分母，但關鍵差異在於：

- **Calmar**：用「最大回撤」（Max Drawdown）——整段期間最慘的那一次
- **Sterling**：用「平均年度最大回撤」（Average Annual Drawdown）——每年各自取最大回撤再平均

Sterling 的邏輯是：單一極端回撤可能只是運氣不好的一次黑天鵝，用平均回撤更能反映策略「常態化」的風險水準。

## 計算公式

### 原始版本（Deane Sterling Jones 1981）

```
SR = Compound ROR / (|Avg. Annual DD| + 10%)
```

- **Compound ROR**：複合年化報酬率
- **Avg. Annual DD**：每年最大回撤的絕對值平均
- **10%**：1981 年時國庫券殖利率約 10%，加入分母做為無風險利率基準

當時的設計理念：國庫券不會有回撤（回撤為 0），分母 = 0 + 10% = 10%，分子 = 10%，SR = 1.0。所以 SR > 1.0 代表比無風險投資更好的風險報酬權衡。

### 現代調整版（類似 Sharpe 結構）

```
SR = (Annual Portfolio Return - Annual Risk-Free Rate) / Average Largest Drawdown
```

這個版本把無風險利率從分母移到分子做減項，結構更像 [[風險管理/風險調整報酬指標夏普比率與索提諾比率|Sharpe Ratio]]。

### 實務計算步驟

1. 將歷史資料按年切分
2. 計算每年的最大回撤（當年內最高點到最低點的跌幅）
3. 將所有年度回撤取絕對值後平均
4. 年化報酬率 ÷ (平均回撤 + 10%)

**範例**：
- 年化報酬 20%
- 第一年回撤 8%，第二年回撤 12%，第三年回撤 5%
- 平均回撤 = (8% + 12% + 5%) / 3 = 8.33%
- SR = 20% / (8.33% + 10%) = 20% / 18.33% = 1.09

## Sterling vs Calmar vs Sharpe vs Sortino

| 指標 | 分子 | 分母 | 核心差異 |
|------|------|------|----------|
| Sharpe | 超額報酬 | 標準差（總波動） | 懲罰上漲和下跌波動 |
| [[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced\|Sortino]] | 超額報酬 | 下行標準差 | 只懲罰下跌波動 |
| Calmar | 年化報酬 | 最大回撤 | 單一最壞情況 |
| Sterling | 年化報酬 | 平均年度回撤 | 回撤的平均水準 |
| [[風險管理/Omega比率Omega-Ratio\|Omega]] | 收益潛力 | 損失風險 | 用整個分配而非單一統計量 |

**Sterling 的定位**：在 Calmar 和 Sharpe 之間。比 Sharpe 更貼近投資者真實感受（回撤比標準差直觀），比 Calmar 更穩定（平均回撤不會被單一極端值扭曲）。

## 判讀標準

- **SR > 1.0**：優於無風險投資（原始定義的基準）
- **SR > 2.0**：優秀的策略，報酬是平均回撤的兩倍以上
- **SR > 3.0**：頂級策略
- **SR < 0.5**：風險報酬權衡差，回撤太大相對於報酬

## 優缺點

**優點**：
- 平均回撤比最大回撤更穩定——不受單一極端事件扭曲
- 更貼近投資者「常態體感」——每年都會經歷回撤，平均更有意義
- 適合評估長期運作的策略，樣本越多越準確

**缺點**：
- 定義不統一——原始版和現代版結果不同，跨來源比較要小心
- 10% 固定無風險利率過時——1981 年時 T-Bill 10%，現在利率環境完全不同
- 平均回掩蓋極端風險——如果某年回撤 50% 但其他年回撤都 3%，平均值會稀釋那 50% 的恐怖
- 樣本期間敏感——只有 2-3 年的數據算平均回撤不夠穩健
- 不如 Calmar 直覺——最大回撤是「最多虧多少」，平均回撤意義較模糊

## 實戰應用

**1. 策略評估**
- 搭配 Calmar 一起看：兩個都高代表策略穩健，Sterling 高但 Calmar 低代表平均表現好但有過單一極端回撤
- 用於比較同類型策略的「日常風險」水準

**2. 基金篩選**
- 對沖基金和 CTA 策略常用 Sterling 做評比
- 篩選條件可設 SR > 1.5 且 Calmar > 1.0 做雙重過濾

**3. 台股 ETF 篩選**
- 算台股 ETF 的 Sterling 比率需要至少 3 年以上月度淨值數據
- 適合用來比較 0050、006208 等大盤 ETF 和產業型 ETF 的風險調整報酬

## 與回撤分析體系的關聯

Sterling 是回撤分析體系的一環：

- [[風險管理/回撤分析進階Drawdown-Analysis-Advanced|回撤分析進階]] — 回撤有深度和持續時間兩個維度
- [[風險管理/Calmar比率與最大回撤分析Calmar-Ratio-and-Maximum-Drawdown|Calmar比率]] — 用單一最大回撤
- [[風險管理/CDaR條件回撤風險Conditional-Drawdown-at-Risk|CDaR]] — 用回撤的尾部期望值
- [[風險管理/Ulcer-Index潰瘍指數與Martin-Ratio|Ulcer Index & Martin Ratio]] — 用回撤深度×持續時間

Sterling 用「平均回撤」，在這個體系中介於 Calmar（最保守）和 CDaR（最激進）之間。

## 參考來源

- Wikipedia: Sterling ratio
- Carl Bacon, *Practical Portfolio Performance Measurement and Attribution* 2nd edition, Wiley 2008, ISBN 978-0-470-05928-9

---

*標籤：#風險管理 #績效評估 #回撤分析 #風險調整報酬*