---
title: "投資人情緒異象 Investor Sentiment Anomaly"
category: "基本面分析"
---

# 投資人情緒異象 Investor Sentiment Anomaly

> 散戶的情緒不是噪音，而是一種可量化、可預測、可獲利的市場異象。Baker & Wurgler 證明情緒高漲時小型股、高波動股、虧損股被系統性高估，情緒低落時被系統性低估——市場的定價錯誤有週期性規律。

## 核心概念

**投資人情緒（Investor Sentiment）** 是市場參與者對未來價格走勢的集體心理態度。Baker & Wurgler（2006）在《Investor Sentiment and the Cross-Section of Stock Returns》中正式提出情緒異象：投資人情緒不是隨機噪音，而是系統性地影響股票橫截面報酬的定價因子。

**核心發現**：情緒高漲後，最容易被情緒驅動的股票（小型股、高波動股、虧損股、成長股）未來報酬系統性偏低；情緒低迷後，這些股票未來報酬系統性偏高。這直接違反[[基本面分析/效率市場假說Efficient-Market-Hypothesis|效率市場假說]]的半強式效率預測。

## 理論基礎

### Baker-Wurgler 情緒代理變數

Baker & Wurgler（2006）構建了六個情緒代理變數的複合指標：

- **封閉式基金折價率（Closed-End Fund Discount）**：Zweig（1973）和Lee et al.（1991）發現封閉式基金折價與散戶情緒高度相關，折價擴大=情緒悲觀
- **IPO數量與首日報酬率**：IPO 熱潮與首日暴漲反映投機情緒高漲，Ljungqvist et al.（2006）確認 IPO 活動是情緒的可靠代理
- **紐約證券交易所成交量（NYSE Turnover）**：高換手率代表投機活動旺盛
- **股利溢價（Dividend Premium）**：配息股與不配息股的帳面市值比差異，不配息股受追捧=情緒高漲
- **權益發行比例（Equity Share in New Issues）**：IPO 佔全部新股發行的比例，高比例=市場情緒樂觀企業趁機上市
- **市場流動性**：流動性越高情緒越樂觀，與[[基本面分析/流動性溢價Liquidity-Premium|流動性溢價]]直接關聯

### 情緒影響的不對稱性

情緒對不同類型股票的影響不對稱，這是本異象的核心：

- **情緒高漲時被高估的股票**：小型股（難以套利）、高波動股（不確定性高）、虧損股（無法用傳統估值）、成長股（未來現金流遙遠）、不配息股（缺乏估值錨點）
- **情緒低迷時被低估的股票**：同上——情緒反轉後這些股票反彈最強
- **情緒影響較小的股票**：大型股、穩定獲利股、配息股——這些股票有清晰的估值錨點，套利者容易介入修正價格

## 情緒測量的五大方法

根據 Wikipedia 市場情緒條目與學術文獻，投資人注意力/情緒的測量有五大方法：

**1. 市場基於指標（Market-Based Measures）**
- VIX 恐慌指數（Whaley 2001, Baker & Wurgler 2007）
- 交易量（Gervais et al. 2001, Hou et al. 2009）
- 極端單日報酬率（Barber & Odean 2008）
- 封閉式基金折價率
- 共同基金資金流向（Brown et al. 2003）
- 零股交易數據（Kumar & Lee 2006）
- 廣告支出與投資人注意力（Grullon et al. 2004）

**2. 調查基於指標（Survey-Based Sentiment Indexes）**
- 密西根大學消費者情緒指數
- Conference Board 消費者信心指數
- UBS/Gallup 投資人樂觀指數
- 缺點：頻率低（週/月級）、受訪者敷衍回答

**3. 文本情緒分析（Textual Sentiment Analysis）**
- Tetlock（2007）用華爾街日報專欄負面詞彙數量預測市場報酬
- Twitter/StockTwits 情緒追蹤（Zhang et al. 2011, Bollen et al. 2011）
- 新聞情緒分析對股價有顯著預測力（Dougal et al. 2012）

**4. 網路搜尋行為（Internet Search Behavior）**
- Google Trends 搜尋量（Da et al. 2014）
- 搜尋量領先交易量1天以上（Bordino et al. 2012）
- 財經 Wikipedia 頁面瀏覽量（Moat et al. 2013）
- 搜尋量與 VIX 和實現波動率正相關（Dimpfl & Jank 2015）

**5. 非經濟因素（Non-Economic Factors）**
- 體育賽事結果影響情緒：輸球後股市異常下跌（Edmans et al. 2007）
- 天氣與日照：陽光分鐘數影響交易者行為（Hirshleifer & Shumway 2003）
- 空難新聞導致小盘股異常下跌（Kaplanski & Levy 2010）

## 與其他異象的關聯

- 與[[基本面分析/MAX效應彩票需求異象Lottery-Demand-Effect|MAX效應]]直接相關：彩票偏好是情緒驅動的子類型，散戶情緒高漲時偏好 MAX 最高的股票
- 與[[基本面分析/資產成長異象Asset-Growth-Anomaly|資產成長異象]]關聯：情緒高漲時企業外部融資容易，過度投資與過度發行正是情緒影響的傳導機制
- 與[[風險管理/前景理論Prospect-Theory|前景理論]]互為補充：前景理論解釋個體層面的情緒反應，情緒異象解釋市場層面的集體後果
- 與[[風險管理/羊群效應Herding-Effect|羊群效應]]：情緒傳染通過羊群行為放大，散戶同步買賣（Kumar & Lee 2006 證實）
- 與[[風險管理/行為財務學總論Behavioral-Finance-Overview|行為財務學總論]]：情緒異象是行為財務學挑戰 EMH 的核心實證之一
- 與[[基本面分析/Fama-French多因子模型Fama-French-Multi-Factor-Model|Fama-French 多因子模型]]：情緒異象無法被五因子模型完全解釋，暗示情緒是獨立的定價因子

## 學術爭議

- **聯合假設問題**：測試情緒影響需要風險模型，如果風險模型本身有誤則情緒效應可能是模型設定錯誤的產物
- **情緒指標的內生性**：市場基於指標是市場均衡的結果，可能受情緒以外的力量驅動（Da et al. 2014 指出的核心缺陷）
- **套利限制**：情緒驅動的錯誤定價可能持續數月甚至數年，套利者無法無限期承受——這與[[操作策略/適應市場假說Adaptive-Market-Hypothesis|適應市場假說]]的「異象循環」一致

## 歷史案例

- **2000年網路泡沫**：IPO 首日報酬率平均65%、不配息虧損股暴漲=情緒極端高漲的教科書案例
- **2021年Meme股狂潮**：GameStop、AMC 等虧損小型股暴漲=散戶情緒驅動的極端案例
- **2026年台股AI泡沫辯論**：融資從5000億暴增到6700億、處置股頻繁、零股交易熱絡=情緒高漲訊號，國巨從1200跌到456也驗證了情緒反轉的殺傷力

## 實戰應用

### 情緒反向選股策略

1. **情緒極端高漲時**：避開小型股、虧損股、高波動股、不配息成長股；轉向大型穩定配息股
2. **情緒極端低迷時**：加碼被錯殺的小型股、高波動股——這是情緒修復後反彈最強的標的
3. **IPO 熱潮是反向訊號**：IPO 數量暴增、首日報酬率飆高時，市場整體未來報酬偏低

### 台股情緒觀察指標

- **融資餘額變化**：融資暴增=散戶情緒高漲（反向指標），與[[籌碼面分析/大盤融資餘額判讀|大盤融資餘額判讀]]直接關聯
- **散戶多空比**：小台指散戶多空比極端值是情緒反向訊號，與[[籌碼面分析/散戶多空比判讀|散戶多空比判讀]]系統整合
- **處置股數量**：處置股暴增代表市場過熱散戶追價失控，與[[籌碼面分析/處置股交易限制與籌碼影響|處置股交易限制]]關聯
- **零股交易量**：零股熱潮=小額散戶進場=情緒高漲訊號，與[[籌碼面分析/零股交易與散戶籌碼溫度|零股交易與散戶籌碼溫度]]直接連結
- **台股 VIX**：與美國 VIX 類似的恐慌指標

### 量化情緒指標構建

```
情緒複合指標 = 加權平均(
  VIX反向分數 × 0.20,
  融資餘額Z分數 × 0.20,
  IPO數量年增率 × 0.15,
  散戶多空比極端值 × 0.15,
  零股交易量Z分數 × 0.10,
  處置股數量 × 0.10,
  Google Trends「股票」搜尋量 × 0.10
)
```

當複合指標 > 1.5 標準差 = 情緒極端高漲（減倉訊號）
當複合指標 < -1.5 標準差 = 情緒極端低迷（加倉訊號）

## 注意事項

本文方法不保證未來績效；實際使用須檢查資料品質、樣本外穩定性、交易成本、流動性與適用市場。

## 相關主題

- [[基本面分析/基本面分析總論]]

## 來源
- Baker, M. & Wurgler, J. (2006). "Investor Sentiment and the Cross-Section of Stock Returns." *Journal of Finance*, 61(4), 1645-1680.
- Baker, M. & Wurgler, J. (2007). "Investor Sentiment in the Stock Market." *Journal of Economic Perspectives*, 21(2), 129-152.
- Da, Z., Engelberg, J. & Gao, P. (2014). "The Sum of All FEARS: Investor Sentiment and Asset Prices." *Review of Financial Studies*.
- Kumar, A. & Lee, C. (2006). "Retail Investor Sentiment and Return Comovements." *Journal of Finance*, 61(5), 2451-2486.
- Tetlock, P. (2007). "Giving Content to Investor Sentiment." *Journal of Finance*, 62(3), 1139-1168.

---

*學習日期：2026-08-14*
*來源：Wikipedia Market Sentiment、Baker & Wurgler (2006) 學術論文、YouTube "Order Flow Toxicity Explained" 相關搜尋*
