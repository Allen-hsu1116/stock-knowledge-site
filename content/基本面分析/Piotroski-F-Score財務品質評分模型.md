---
title: "Piotroski F-Score 財務品質評分模型"
---

# Piotroski F-Score 財務品質評分模型

> 用9個簡單的財報指標，把價值股裡的「贏家」和「輸家」分開——Stanford會計教授的量化選股經典。

## 核心概念

**Piotroski F-Score** 是史丹佛大學會計教授 Joseph Piotroski 於2002年在論文 *"Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers"* 中提出的財務品質評分系統。

核心問題：價值投資人專找低本益比、低股價淨值比的「便宜股」，但便宜股之所以便宜，往往是因為公司基本面爛。Piotroski 的想法是用9個二元指標（0或1分）快速篩選出財報正在改善的價值股，避開地雷。

**分數範圍**：0~9分，越高越好。

## 九大評分標準

### 獲利能力（Profitability）— 4分

1. **ROA為正** — 当年資產報酬率 > 0 得1分
2. **營業現金流為正** — 当年來自營運的現金流 > 0 得1分
3. **ROA較去年上升** — 当年ROA > 去年ROA 得1分
4. **應計項目品質** — 營業現金流/總資產 > ROA 得1分（賺的錢是真的進口袋而非紙上富貴）

### 槓桿、流動性與資金來源（Leverage, Liquidity & Source of Funds）— 3分

5. **槓桿下降** — 長期負債比率較去年下降 得1分
6. **流動比率上升** — 当年流動比率 > 去年 得1分
7. **未發行新股** — 当年未增資發行新股 得1分（稀釋 = 壞事）

### 營運效率（Operating Efficiency）— 2分

8. **毛利率上升** — 当年毛利率 > 去年 得1分
9. **資產週轉率上升** — 当年資產週轉率 > 去年 得1分

## 實戰應用

### 判讀標準
- **8~9分**：財務體質強健，價值股中的贏家
- **0~2分**：財務體質虛弱，就算便宜也別碰
- **3~7分**：灰色地帶，需進一步分析

**重要提醒**：不同產業的平均 F-Score 不同。金融業、製造業、科技業的基準差很多，跨產業比較沒有意義，應該同產業內橫向比較。

## 與其他模型的關係

- **[[基本面分析/Altman-Z-Score破產預測模型|Altman Z-Score]]**：預測破產風險（2年內），F-Score 評估財報改善趨勢
- **Beneish M-Score**：偵測盈餘操縱，F-Score 評估基本面好壞，兩者互補
- **[[基本面分析/Greenblatt魔力公式選股法Magic-Formula-Investing|Greenblatt魔力公式]]**：用ROC+盈餘殖利率排序選股，F-Score 可作為魔力公式選出的便宜股的品質確認

## 實證表現

Piotroski 原始論文回測1976-1996年美國股市：
- 高F-Score（8-9）的低P/B股票，年均超額報酬約7.5%
- 低F-Score（0-2）的低P/B股票，報酬顯著低於市場

2024年 Schwartz & Hanauer 研究比較F-Score、魔力公式、保守公式和收購者倍數四種公式投資法，發現四者都能產生顯著的原始與風險調整報酬，但沒有任何一種在所有績效指標上持續勝出。

## 注意事項
1. **只看一年vs前一年**：景氣循環股在衰退期F-Score必然低，不代表公司爛，是週期問題
2. **不適用金融業**：銀行保險的商業模式完全不同，應收帳款、毛利率等指標無意義
3. **已被市場部分定價**：20多年來被廣泛使用，套利空間縮小
4. **不考慮估值**：F-Score只看品質不看價格，需搭配低P/B或低P/E使用才有意義
5. **不考慮成長性**：高F-Score不代表公司有成長空間，只代表財報在改善

## 台股實戰應用

台股投資人可以用以下方式應用F-Score：

1. **先用估值篩選**：找出P/B < 1或P/E < 10的個股池
2. **再用F-Score過濾**：從池中挑出F-Score ≥ 7的標的
3. **產業內比較**：同產業中F-Score上升趨勢最明顯的公司
4. **搭配M-Score**：確認沒有盈餘操縱嫌疑

台股財報資料可從MOPS公開資訊觀測站取得，9項指標都能從資產負債表和現金流量表計算。

## 相關主題
- [[基本面分析/Altman-Z-Score破產預測模型]] — 破產預測
- [[基本面分析/Beneish-M-Score盈餘操縱偵測模型]] — 盈餘操縱偵測
- [[基本面分析/Greenblatt魔力公式選股法Magic-Formula-Investing]] — 量化選股
- [[基本面分析/NCAV淨流動資產價值選股法Net-Current-Asset-Value]] — 深度價值選股
- [[基本面分析/Ohlson-O-Score破產預測模型]] — 破產預測

## 來源
- Piotroski, Joseph D. (2002). "Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers"
- Wikipedia: Piotroski F-score
- Alpha Architect: Value Investing Research - Simple Methods to Improve the Piotroski F-Score
- Schwartz & Hanauer (2024). Formula Investing. SSRN Working Paper No. 5043197