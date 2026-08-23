---
title: "Fama-French多因子模型 Fama-French Multi-Factor Model"
category: "基本面分析"
---

# Fama-French多因子模型 Fama-French Multi-Factor Model

> CAPM只用市場Beta解釋報酬，Fama-French用三個、五個甚至六個因子——從單一維度到多維度的報酬歸因框架，是現代因子投資的學術基石

## 核心概念

Fama-French多因子模型是Eugene Fama和Kenneth French於1992年提出的資產定價模型，用來解釋股票報酬的來源。傳統CAPM（資本資產定價模型）只用一個因子——市場風險溢酬（Market Beta）——來解釋股票的超額報酬，但實證發現CAPM只能解釋約70%的分散投資組合報酬變異。Fama-French加入了規模因子和價值因子，將解釋力提升到90%以上。

### 三因子模型（1992）

三因子模型的公式：

```
E(R) = Rf + β × (Rm - Rf) + bs × SMB + bv × HML + α
```

- **Rf**：無風險利率
- **Rm - Rf**：市場溢酬（Market Premium），與CAPM相同
- **SMB（Small Minus Big）**：小型股減大型股的報酬差，衡量規模因子
- **HML（High Minus Low）**：高帳面市值比減低帳面市值比的報酬差，衡量價值因子
- **α**：模型無法解釋的超額報酬（Jensen's Alpha），α顯著不為零代表還有未被捕捉的風險因子
- **β、bs、bv**：分別是市場、規模、價值三個因子的敏感度係數

### 因子構建方法

Fama和French用NYSE、Amex、NASDAQ所有股票構建因子投資組合：

- **規模分組**：以NYSE市值中位數為界，分為Small和Big兩組
- **帳面市值比分組**：按NYSE股票的BTM比率排序，底部30%為Low（成長股），中間40%為Medium，頂部30%為High（價值股）
- **6個投資組合**：2×3交叉分組形成S/L、S/M、S/H、B/L、B/M、B/H六個組合
- **SMB**：三個Small組合平均報酬減三個Big組合平均報酬
- **HML**：兩個High組合平均報酬減兩個Low組合平均報酬

歷史因子數據可從Kenneth French的個人網頁免費下載，涵蓋全球多個市場。

## 五因子模型（2015）

2015年Fama和French進一步擴展為五因子模型，加入獲利能力和投資兩個因子：

```
E(R) = Rf + β × (Rm - Rf) + bs × SMB + bv × HML + bw × RMW + bc × CMA + α
```

- **RMW（Robust Minus Weak）**：高獲利公司減低獲利公司的報酬差，衡量獲利能力因子。獲利能力用營業利潤除以股東權益衡量
- **CMA（Conservative Minus Aggressive）**：保守投資公司減積極投資公司的報酬差，衡量投資因子。投資強度用資產成長率衡量

### 五因子的關鍵發現

在美國市場1963-2013年的樣本期間，加入RMW和CMA後：

- **HML因子變得冗餘**：HML的報酬序列幾乎完全被其他四個因子解釋，尤其是CMA與HML相關係數高達0.7
- **解釋力提升**：五因子模型比三因子模型能解釋更多投資組合的報酬變異
- **仍未完全通過GRS檢定**：Gibbons-Ross-Shanken檢定仍被拒絕，代表五因子仍無法完全解釋所有預期報酬。問題主要出在「小型且積極投資但低獲利」的投資組合上——這類組合有顯著的負五因子Alpha

### Carhart四因子模型（1997）

Mark Carhart在三因子基礎上加入動能因子（MOM），形成四因子模型：

```
E(R) = Rf + β × (Rm - Rf) + bs × SMB + bv × HML + bm × MOM + α
```

- **MOM（Momentum）**：買入過去12個月表現最好的股票、賣出表現最差的股票的報酬差

Fama和French原始模型未包含動能因子，因為少數投資組合對動能有顯著載荷。但AQR Capital創辦人Cliff Asness（Fama的博士生）強力主張動能應被納入。實務上，Carhart四因子是績效歸因最常用的基準之一。

## 實戰應用

### 1. 績效歸因與Alpha評估

這是Fama-French模型最常見的用途。將基金或策略的報酬對因子做回歸：

- **α顯著為正**：基金經理有真正的選股能力，而非只是承擔了某種系統性因子風險
- **α不顯著**：報酬來自因子曝險而非選股能力，買因子ETF可能更划算
- **因子載荷分析**：β高代表跟隨大盤、bs高代表偏重小型股、bv高代表偏重價值股

> 相關頁面：[[風險管理/詹森Alpha與特雷諾比率Jensen-Alpha-and-Treynor-Ratio]] — Fama-French三因子Alpha比單因子CAPM Alpha更可靠

### 2. 因子投資與Smart Beta

Fama-French模型從學術走向實務，催生了整個因子投資產業：

- **單因子ETF**：純價值ETF、純小型股ETF、純動能ETF
- **多因子ETF**：結合價值+品質+動能等多因子，降低單因子衰退風險
- **Smart Beta策略**：用因子加權取代市值加權，系統化捕捉因子溢酬

> 相關頁面：[[操作策略/Smart-Beta因子投資策略]]、[[操作策略/因子投資與量化危機]]

### 3. 風險歸因

將投資組合的風險拆解到各因子，了解自己到底在承擔什麼風險：

- 你以為在選股，其實在承擔規模因子（重壓小型股）
- 你以為在做Alpha，其實在承擔價值因子（買低本益比股）
- 因子曝險透明化後，才能判斷報酬來自能力還是因子Beta

> 相關頁面：[[風險管理/風險歸因Risk-Attribution]]、[[風險管理/因子風險管理Factor-Risk-Management]]

### 4. 台股因子投資實務

- **規模因子**：台股小型股溢酬存在但流動性差，交易成本侵蝕報酬
- **價值因子**：高股息+低本益比在台股有長期效果，但需排除假高殖利率股
- **動能因子**：台股動能效應顯著但反轉速度快，適合中短期波段
- **獲利因子**：高ROE公司在台股長期跑贏大盤，與品質因子重疊
- **在地化因子**：Griffin（2002）研究顯示本地因子比全球因子更能解釋各國股票報酬，台股應用在地化因子數據更有效

## 因子的爭議與局限

### 1. 因子是否為風險溢酬還是行為偏差

學術界對SMB和HML的本質有激烈辯論：

- **風險故事**：小型股和價值股承擔更高系統性風險（如經濟衰退時更脆弱），高報酬是風險補償
- **行為故事**：投資人對成長股過度樂觀、對價值股過度悲觀，因子溢酬來自行為偏差而非風險
- **兩者皆有**：不同市場不同時期，因子溢酬的來源可能不同

### 2. 因子會衰退甚至消失

- **價值因子2007-2020年嚴重衰退**：成長股大幅跑贏價值股，2018-2020年被稱為「量化危機」——半世紀以來首次其他因子補不了價值因子的虧損
- **因子擁擠**：太多資金追逐同一因子會壓縮溢酬，知名因子可能被套利掉
- **交易成本**：高周轉率因子策略（如動能）的理論溢酬在扣除交易成本後大幅縮水

> 相關頁面：[[操作策略/因子投資與量化危機]] — 2018-2020年量化危機深度分析

### 3. 五因子模型的未解問題

- **HML冗餘**：五因子模型中HML幾乎被CMA取代，但其他市場（如英國）HML仍有獨立解釋力
- **獲利能力定義爭議**：Foye（2018）質疑Fama-French的獲利能力衡量方式在英國不適用
- **動能缺席**：五因子未納入動能，但動能在實務上是最強的因子之一
- **GRS檢定未過**：即使五因子也無法完全解釋所有投資組合的預期報酬

### 4. 因子模型簡化現實

三因子或五因子模型無法捕捉所有風險來源：
- 殘差項α就是模型沒解釋到的風險
- 新因子不斷被發現（低波動因子、配息因子等），「因子動物園」問題日益嚴重
- 過度擬合風險：用歷史數據發現的因子可能只是數據挖掘的結果

> 相關頁面：[[風險管理/投資組合理論與分散投資的局限Portfolio-Theory-and-Diversification-Limits]] — Fama-French比CAPM更準確但仍無法解釋所有異象

## 散戶實戰要點

1. **不要只看單一指標選股**：本益比低可能只是價值因子曝險，不代表真的好
2. **了解自己的因子曝險**：重壓小型股+低本益比 = 承擔SMB+HML因子風險
3. **因子分散比個股分散更重要**：單一因子可能長期失效（如價值因子2007-2020），多因子組合更穩健
4. **因子輪動是進階技巧**：不同經濟週期不同因子表現不同，但擇時輪動極難
5. **用因子模型做績效歸因**：你的選股報酬到底是Alpha還是因子Beta？回歸一下就知道

## 相關頁面

- [[風險管理/詹森Alpha與特雷諾比率Jensen-Alpha-and-Treynor-Ratio]] — 用Fama-French三因子Alpha取代單因子Alpha評估選股能力
- [[風險管理/因子風險管理Factor-Risk-Management]] — 因子曝險拆解、因子擁擠監控與多因子分散框架
- [[風險管理/風險歸因Risk-Attribution]] — 用因子模型做風險歸因的完整方法論
- [[操作策略/Smart-Beta因子投資策略]] — Fama-French模型在ETF和因子投資中的實務應用
- [[操作策略/因子投資與量化危機]] — 2018-2020年量化危機，價值因子半世紀來最嚴重衰退
- [[基本面分析/基本面因子選股總論Quantitative-Fundamental-Factors]] — 價值+成長+品質+動能+低波動五大因子系統化選股
- [[基本面分析/每股淨值進階判讀BVPS與Graham-Number]] — HML因子的核心輸入是帳面市值比
- [[基本面分析/盈餘公告後價格漂移PEAD]] — 在Fama-French五因子+動能框架下PEAD效應更大
- [[風險管理/投資組合理論與分散投資的局限Portfolio-Theory-and-Diversification-Limits]] — 多因子模型比CAPM更準確但仍有局限

## 來源
- [Fama–French three-factor model - Wikipedia](https://en.wikipedia.org/wiki/Fama%E2%80%93French_three-factor_model)
- Fama, E. F.; French, K. R. (1993). "Common risk factors in the returns on stocks and bonds". Journal of Financial Economics. 33: 3–56.
- Fama, E. F.; French, K. R. (2015). "A Five-Factor Asset Pricing Model". Journal of Financial Economics. 116: 1–22.
- Carhart, M. M. (1997). "On Persistence in Mutual Fund Performance". The Journal of Finance. 52 (1): 57–82.
- Kenneth French Data Library: [https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

## 注意事項
（待補充）


## 相關主題
（待補充）
