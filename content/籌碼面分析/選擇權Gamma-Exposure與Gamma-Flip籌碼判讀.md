---
title: "選擇權Gamma Exposure與Gamma Flip籌碼判讀"
category: "籌碼面分析"
date: 2026-08-29
source_date: 2026-08-29
status: raw_linked
---

# 選擇權Gamma Exposure與Gamma Flip籌碼判讀

> Gamma Exposure把分散在各履約價與到期日的Gamma換成造市商可能需要調整的Delta避險量；正Gamma傾向壓抑波動，負Gamma傾向放大波動，但公開未平倉量通常無法直接看出真正的造市商正負號。

## 核心概念

### Gamma與GEX在量什麼

Gamma衡量標的價格改變時，選擇權Delta會改變多少。造市商若維持Delta中性，就必須隨價格變動調整現貨或期貨避險。

單一契約常用的「標的移動1%之GEX」近似為：

$$
\mathrm{GEX}_{1\%}=\Gamma\times OI\times M\times S^2\times 0.01
$$

- $\Gamma$：每一單位標的價格變動造成的Delta變化。
- $OI$：未平倉口數。
- $M$：契約乘數。
- $S$：標的現價。
- 計算結果代表標的移動1%後，理論Delta避險名目金額要調整多少；不是報酬預測。

例如標的100元、Gamma為0.02、OI為10,000口、契約乘數100時，標的移動1%約使總Delta改變20,000股，按100元換算約200萬元避險名目額。數字很大不等於方向已知，先搞清楚誰長誰短，不然只是拿計算機替幻想加字幕。

### 正Gamma與負Gamma

以下方向都站在「造市商淨庫存」角度：

- **造市商淨長Gamma**：價格上漲時Delta增加，為維持中性需賣出標的；價格下跌時需買入標的。避險流量逆著行情，傾向壓低實現波動、促進均值回歸。
- **造市商淨短Gamma**：價格上漲時需追買，價格下跌時需追賣。避險流量順著行情，可能放大動能、跳躍與尾盤趨勢。
- **Gamma規模接近零**：選擇權避險流量相對中性，現貨方向更可能由資訊、主動資金與其他部位主導。

Anderegg、Ulmann與Sornette的模型及外匯市場實證支持這個回饋機制：造市商負Gamma與較高現貨波動相連，正Gamma則傾向降低波動。Baltussen等人的跨資產研究也把短Gamma避險需求與最後30分鐘的盤中動能連結起來。

### Gamma Flip與Gamma Wall

- **Gamma Flip／Zero Gamma**：把各履約價、各到期日GEX加總，並在不同標的價格下重新估值；總GEX穿越零的位置就是Gamma Flip。
- **正Gamma區**：理論上較容易出現波動受抑制與價格回拉。
- **負Gamma區**：理論上較容易出現順勢避險與波動擴張。
- **Gamma Wall**：某履約價附近Gamma高度集中，可能成為避險流量反覆出現的區域；它不是不會破的支撐壓力，更不是宇宙磁鐵。

## 實戰應用

### GEX估計五步驟

1. **固定範圍**：分開計算近月、週選、0DTE與全期限，避免遠月低Gamma把近月風險稀釋掉。
2. **逐契約估Gamma**：輸入現價、履約價、剩餘期限、隱含波動率、利率與股息，取得每個Call與Put的Gamma。
3. **乘上OI與契約乘數**：轉成每個履約價的Gross GEX，再依造市商庫存方向加正負號。
4. **建立價格情境網格**：讓標的價格上下移動並重新估Gamma，找Gamma Flip與高Gamma集中區。
5. **用流動性標準化**：把GEX除以標的期貨或現貨日成交額；名目額不和市場深度相比，純粹就是數字健身。

### 每日判讀SOP

- **盤前**：記錄總GEX正負、Gamma Flip、前三大正負Gamma履約價與最近到期日。
- **盤中**：觀察現價是否跨越Gamma Flip、價平附近成交是否暴增、期貨是否出現順勢追價或逆勢吸收。
- **事件日**：利率決策、財報、結算與指數調整日要降低對靜態GEX的信任，因新資訊與大量平倉可瞬間改變部位。
- **盤後**：用新OI、IV與剩餘期限重算，不沿用昨天圖表。Gamma會隨時間與現價變動，昨天的牆今天可能只剩壁癌。

### 訊號組合

- **正GEX＋現價在Gamma Flip上方＋實現波動下降**：偏向區間、均值回歸與履約價附近釘住，但仍需確認沒有重大資訊衝擊。
- **負GEX＋現價跌破Gamma Flip＋成交與波動同步擴張**：順勢避險可能放大跌勢，應縮小逆勢抄底部位。
- **負GEX＋價格上漲＋期貨尾盤加速**：可能存在追買避險，但要和主動買盤、槓桿ETF再平衡及指數事件區分。
- **高Gross GEX但買賣流平衡**：淨造市商曝險可能很小，不該只看成交量或OI喊世界末日。

## 關鍵限制

### 公開OI看不到真正方向

未平倉量只告訴你契約還在，不告訴你：

- 客戶是買方還是賣方。
- 造市商是長Gamma還是短Gamma。
- 部位是開倉、平倉、價差腿或跨商品對沖。
- 造市商是否用其他到期日、期貨、ETF或場外部位抵銷。

很多免費GEX圖會假設「Call OI由客戶買、Put OI由客戶買」或直接替Call與Put指定正負號。這能產生估計值，但不是觀測到的真實庫存。Cboe憑交易所資料可辨識參與者、買賣與開平倉；一般公開資料做不到，兩者不能裝作同一回事。

### 其他陷阱

- **Volume不等於Exposure**：成交量很大但買賣平衡，淨Gamma可以接近零。
- **GEX不是方向指標**：它較適合判斷「波動可能被壓抑或放大」，不直接回答明天漲跌。
- **Gamma Flip會移動**：IV、時間、現價與新部位都會讓零點改變。
- **模型依賴**：Black-Scholes Gamma在跳空、流動性枯竭與離散避險下只是近似。
- **跨市場不可硬套**：SPX、臺指選、個股選擇權與權證的參與者、乘數、結算與流動性都不同。

## 相關主題

- [[籌碼面分析/自營商權證避險Delta操作機制]]
- [[籌碼面分析/選擇權籌碼綜合判讀框架Option-Chip-Integrated-Framework]]
- [[籌碼面分析/選擇權支撐壓力表]]
- [[操作策略/二階與三階Greeks進階Vanna-Vomma-Charm]]
- [[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]

## 來源

- [Gamma Exposure與造市商避險研究摘錄](../../raw/2026-08-29/Gamma-Exposure與造市商避險研究摘錄.md)
- [Cboe：Evaluating the Market Impact of SPX 0DTE Options](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)
- [Anderegg、Ulmann、Sornette：The impact of option hedging on the spot market volatility](https://doi.org/10.1016/j.jimonfin.2022.102627)
- [Baltussen等人：Hedging demand and market intraday momentum](https://doi.org/10.1016/j.jfineco.2021.04.029)
