---
title: ROIIC增量投入資本報酬率Return-on-Incremental-Invested-Capital
aliases: [ROIIC, Return on Incremental Invested Capital, 增量投入資本報酬率, 邊際投入資本報酬率, 新增資本報酬率]
category: 基本面分析
date: 2026-08-26
---

# ROIIC增量投入資本報酬率Return-on-Incremental-Invested-Capital

> ROIC告訴你公司過去整鍋資本煮得怎樣，ROIIC則盯著最近加進去的那一瓢錢有沒有變出更多NOPAT；老廠曾經很賺，不代表新廠不是昂貴盆栽。

## 核心概念

投入資本報酬率ROIC是存量指標：

$$ROIC_t=\frac{NOPAT_t}{Invested\ Capital_{t-1}}$$

增量投入資本報酬率ROIIC則衡量新增稅後營業利益相對於前一期新增投入資本：

$$ROIIC_t=\frac{NOPAT_t-NOPAT_{t-1}}{Invested\ Capital_{t-1}-Invested\ Capital_{t-2}}$$

分母刻意落後一期，是因為先投入資本，之後才觀察它帶來多少NOPAT。不同研究可能採同期間或平均資本口徑，沒有哪一種寫法能把經濟現實焊死；重點是全公司、全期間使用一致定義，並揭露時間差。

ROIIC回答的是：

- 新建產能帶來多少新增獲利
- 研發、行銷與通路投資是否開始回收
- 併購後新增資本有沒有轉成營業利益
- 高ROIC是舊護城河遺產，還是新投資仍能複製
- 未來整體ROIC可能往上還是往下

## 為什麼ROIC不夠

公司可能有20%的歷史ROIC，但新增專案只賺8%；因為新資本不斷稀釋舊資本，整體ROIC遲早往下掉。反過來，轉機公司目前ROIC只有6%，若新增資本開始賺15%，整體ROIC會逐步被拉高。

因此要分清楚：

- **ROIC高、ROIIC高**：既有資產優秀，新投資也能複製，最接近複利型企業
- **ROIC高、ROIIC低**：舊本業很香，新投資品質下滑，護城河可能在收窄
- **ROIC低、ROIIC高**：整體仍普通，但邊際改善，可能是轉機或新產品開始放量
- **ROIC低、ROIIC低**：舊資本與新資本一起爛，管理層只是用擴張把問題做大

只看平均ROIC，就像拿全班三年平均成績評估這次考試，數字沒有錯，問題是你問錯時間。

## 多年度滾動ROIIC

單年資本支出、併購與NOPAT都可能跳動，Morgan Stanley建議可用3年或5年滾動值降低噪音。以3年為例：

$$ROIIC_{3Y}=\frac{NOPAT_t-NOPAT_{t-3}}{Invested\ Capital_{t-1}-Invested\ Capital_{t-4}}$$

這個比率是期間內新增NOPAT除以期間內新增資本，通常不應在沒有清楚經濟假設下硬轉成年化報酬。實務上可同時計算：

- 單年ROIIC：反應快，但很吵
- 3年ROIIC：兼顧轉折與穩定
- 5年ROIIC：適合重資產與建廠週期長的公司
- 全週期ROIIC：適合半導體、航運、原物料等景氣循環產業

## 算例

假設公司3年前NOPAT為100億元，目前為145億元；配合時間落後後，投入資本由700億元增至950億元：

$$ROIIC_{3Y}=\frac{145-100}{950-700}=18\%$$

這表示期間內每增加100元投入資本，對應增加18元NOPAT。接著不能直接按下買進鍵，還要問：

- 45億元新增NOPAT是否含景氣高峰、匯兌或一次性利益
- 250億元新增資本是否漏掉費用化研發、租賃與併購商譽
- 新產能是否已達正常稼動率
- 18%能否在下一輪投資重複
- 股價已隱含多高的未來ROIIC

## ROIIC與成長的連結

長期營業利益成長可概念性拆成：

$$g_{NOPAT}\approx Reinvestment\ Rate\times Return\ on\ New\ Investment$$

若用ROIIC近似新增投資報酬，則高成長必須同時有：

- 足夠再投資空間
- 新增資本能產生高ROIIC
- 護城河讓高報酬不會立刻被競爭吃掉
- 融資與稀釋成本沒有吞掉每股價值

高再投資率配低ROIIC是價值毀損；低再投資率配高ROIIC則可能只是市場空間太小。真正稀有的是「能長期投入大量資本，新增報酬仍高」。大家都會寫成長故事，能讓新錢繼續生高品質獲利的沒幾家。

## ROIIC為何會突然很高

高ROIIC不必然代表新專案神勇，常見來源包括：

- 軟體與平台型企業新增收入幾乎不需有形資本
- 既有產能利用率上升，固定成本被更多銷量攤薄
- 先前研發與行銷費用化，投入資本被低估
- 景氣谷底回升，NOPAT跳升但資本變化不大
- 延後CapEx或釋放營運資金，使分母暫時偏小
- 資產減損、處分或大額回購改變投入資本口徑

因此高ROIIC最好搭配增量營業利益率、產能利用率、營運資金、費用化無形投資與部門別資料一起看。

## ROIIC不是IRR，也不宜機械對比WACC

Morgan Stanley提醒，ROIIC雖有助於觀察變化，但不是完整的經濟報酬率：

- 它忽略沉沒成本，假設既有投入資本報酬保持穩定
- 它沒有完整處理每期現金流與時間價值
- 競爭優勢期間越長，ROIIC與真正經濟報酬的偏差可能越大
- ROIIC高於資本成本時可能高估經濟報酬，低於資本成本時可能低估

所以ROIIC可以當方向儀，不是拿來假裝精密的IRR。判斷價值仍應把未來自由現金流、投資時點、WACC與競爭優勢期間放回DCF。

## 實戰啟示

1. 平均ROIC看家底，ROIIC看新增資本的現在進行式
2. ROIIC持續高於歷史ROIC，整體資本效率通常有上升潛力
3. ROIC仍高但ROIIC連續下滑，是成長股最值得警戒的早期訊號之一
4. 單年ROIIC很會發瘋，3至5年滾動值比較不容易被會計時點耍
5. ROIIC是診斷工具，不是IRR替身；最終仍要回到現金流、時間與估值

## 實戰應用

1. 由營業利益扣現金稅率估NOPAT，排除業外與一次性項目
2. 用營運資金、固定資產、租賃與其他營業資產減無息營業負債估投入資本
3. 統一商譽、現金、資產減損與庫藏股口徑
4. 計算單年、3年與5年ROIIC
5. 將併購、建廠、處分與景氣循環標註在時間軸
6. 與營收增量、增量營業利益率及產能利用率交叉驗證
7. 分部可得時分開計算，避免高報酬事業替低效部門擦脂抹粉
8. 用反向DCF檢查目前價格要求未來ROIIC維持多久
9. 只把可重複的邊際報酬放進估值，不拿景氣反彈當永久護城河

## 注意事項

- **分母接近零會爆表**：少量新增資本配正常獲利波動，就能算出荒謬高值
- **負分母難解釋**：公司縮減資本時，傳統ROIIC符號可能失去直觀意義
- **投資與回收有落後**：半導體新廠、藥物研發、品牌投資不會隔天吐出NOPAT
- **併購會製造斷點**：交割一次增加大量商譽與投入資本，短期ROIIC通常下滑
- **景氣循環會假改善**：售價上漲與稼動率回升可讓ROIIC暴增，未必可持續
- **無形投資被費用化**：研發與部分行銷若全列費用，NOPAT與投入資本會同時失真
- **平均數掩蓋部門差異**：一半資本創造價值，另一半燒錢，合併值可能看起來普通
- **會計回報不是市場報酬**：ROIIC高不代表買入後報酬高，價格與預期才決定投資結果

## 相關主題

- [[基本面分析/ROIC投入資本報酬率]]
- [[基本面分析/再投資率與基本面成長率Reinvestment-Rate-and-Fundamental-Growth]]
- [[基本面分析/WACC加權平均資本成本]]
- [[基本面分析/現金流量折現法DCF估值]]
- [[基本面分析/反向DCF估值法Reverse-Engineered-DCF]]
- [[基本面分析/營業槓桿與財務槓桿聯合槓桿判讀Operating-Financial-Combined-Leverage]]

## 來源

- Mauboussin, M. J., & Callahan, D. (2022). [Return on Invested Capital: How to Calculate ROIC and Handle Common Issues](https://www.morganstanley.com/im/publication/insights/articles/article_returnoninvestedcapital.pdf), Counterpoint Global Insights, pp. 22–23.
- Damodaran, A. [Estimating Growth](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/growth.pdf), NYU Stern valuation lecture notes.

---

*最後更新：2026-08-26*
