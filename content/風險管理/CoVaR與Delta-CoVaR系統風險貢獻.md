---
title: "CoVaR與Delta CoVaR系統風險貢獻"
category: "風險管理"
date: 2026-08-28
tags:
  - 系統性風險
  - CoVaR
  - 分位數迴歸
---

# CoVaR與Delta CoVaR系統風險貢獻

> VaR問「自己最慘會怎樣」，CoVaR問「它出事時整個系統會怎樣」。只盯單一公司的波動，跟只看自己家有沒有著火、不管隔壁是不是瓦斯行差不多。

## 核心概念

CoVaR（Conditional Value-at-Risk）衡量金融系統報酬在「某機構處於特定狀態」條件下的尾部分位數。若用報酬率表示，概念式為：

$$
CoVaR_q^{sys\mid i}=VaR_q\left(R_{sys}\mid R_i=VaR_q(R_i)\right)
$$

其中：

- $R_{sys}$：金融系統或市場投資組合報酬。
- $R_i$：機構或股票$i$的報酬。
- $q$：尾部分位數，例如5%。
- 條件式表示機構$i$正處於自己的尾部壓力狀態。

單看CoVaR水準會混入整體市場原本就很危險的程度，因此Adrian與Brunnermeier提出Delta CoVaR：

$$
\Delta CoVaR_q^{sys\mid i}=CoVaR_q^{sys\mid i,distress}-CoVaR_q^{sys\mid i,median}
$$

它比較同一機構處於壓力狀態與中位狀態時，系統尾部風險改變多少。

## 符號先講清楚

- 用「報酬率」表示時，越負代表越慘，Delta CoVaR可能呈負值。
- 用「正的損失率」表示時，越大代表越慘，Delta CoVaR通常寫成正值。
- 排名、圖表與警戒線必須統一符號慣例。公式抄得漂亮但正負號亂掉，模型就只是昂貴的靠北製造機。

## 如何估計

原始研究以分位數迴歸估計條件尾部：

$$
Q_q(R_{sys,t}\mid X_t)=\alpha_q+\beta_qR_{i,t}+\gamma_q'Z_{t-1}
$$

實作流程：

1. **定義系統**：可用金融類股價值加權組合、金融指數或廣泛市場指數。
2. **固定尾部門檻**：常用5%或1%，門檻越極端越貼近危機，但資料會少得可憐。
3. **估計分位數迴歸**：把機構報酬與滯後狀態變數帶入系統報酬的尾部分位數模型。
4. **代入壓力與中位狀態**：分別得到distress CoVaR與median CoVaR。
5. **計算Delta並重抽樣**：用block bootstrap或其他保留時間相依的方法估計信賴區間。
6. **滾動監控**：固定窗口或擴張窗口追蹤排名，避免一次估完就供在神桌上。

## 假設例子

假設以正的損失率表示：

- 某金融股處於中位狀態時，系統5%尾部損失為3%。
- 該股落入自身壓力分位數時，系統5%尾部損失為7%。
- Delta CoVaR為4個百分點，代表條件狀態改變後，系統尾部損失加深4個百分點。

這是條件關聯，不是「這家公司必然害市場多跌4%」的因果判決。

## 與其他風險指標的差異

- **[[風險管理/VaR風險值Value-at-Risk|VaR]]**：衡量單一標的或組合自身尾部分位數。
- **[[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall|CVaR／Expected Shortfall]]**：衡量超過自身VaR後的平均尾部損失。
- **CoVaR**：衡量機構處於某狀態時，系統尾部分位數落在哪裡。
- **Delta CoVaR**：衡量機構從正常轉為壓力狀態時，系統尾部風險的變化。

## 實戰檢查清單

- [ ] 系統投資組合定義固定且可重現
- [ ] 報酬率與損失率符號一致
- [ ] 尾部分位數與估計窗口事前固定
- [ ] 使用調整後價格並處理停牌與缺值
- [ ] 有信賴區間或重抽樣穩健性檢查
- [ ] 與槓桿、規模、流動性和共同曝險交叉驗證
- [ ] 不把條件關聯寫成因果結論

## 實戰應用

### 金融股風險排名

- 以台灣金融類股或自行建構的上市金融機構價值加權組合作為$R_{sys}$。
- 對銀行、金控、保險與證券股分別估計Delta CoVaR，觀察誰在壓力狀態下與金融系統尾部共振最強。
- 週資料可降低個股不同步交易與日頻雜訊，但樣本數會下降；日資料則需處理停牌、漲跌停與流動性差異。

### 投資組合風控

- 同時持有多檔金融股時，不只看各自波動率，也看Delta CoVaR是否集中在少數部位。
- 高Delta CoVaR部位可搭配較低權重、較嚴格風險預算或市場壓力時自動降曝險。
- 搭配[[風險管理/Copula連接函數與尾部相依性Copula-and-Tail-Dependence|Copula尾部相依性]]與[[風險管理/金融傳染風險Financial-Contagion|金融傳染風險]]，分辨一般相關與危機尾部共振。

## 注意事項

- **把相關當因果**：共同持有相同資產、同受利率衝擊，也會產生高CoVaR。
- **系統定義亂換**：用大盤、金融指數或等權金融股組合，結果不是同一件事。
- **忽略規模與流動性**：大型股容易影響價值加權系統，小型股則可能因價格僵滯低估風險。
- **只看點估計**：尾部樣本少，沒有信賴區間的精確排名常常只是小數點演戲。
- **直接當買賣訊號**：Delta CoVaR是風險配置工具，不是明天漲跌預言機。

## 相關主題

- [[風險管理/VaR風險值Value-at-Risk|VaR風險值]]
- [[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall|CVaR與Expected Shortfall]]
- [[風險管理/金融傳染風險Financial-Contagion|金融傳染風險]]
- [[風險管理/Copula連接函數與尾部相依性Copula-and-Tail-Dependence|Copula與尾部相依性]]

## 來源

- [Adrian & Brunnermeier, CoVaR, NBER Working Paper 17454](https://www.nber.org/papers/w17454)
- [Adrian & Brunnermeier, CoVaR, American Economic Review](https://www.aeaweb.org/articles?id=10.1257/aer.20120555)
- 本地研究素材：`raw/2026-08-28/Adrian-Brunnermeier-CoVaR研究摘錄.md`
