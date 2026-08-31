---
title: "Parkinson高低價波動率估計"
category: "技術分析"
date: 2026-08-31
source_date: 2026-08-31
status: raw_linked
---

# Parkinson高低價波動率估計

> Parkinson估計器只用每日最高價與最低價，把收盤價漏掉的日內震盪撿回來；資料需求低、模型內效率高，但對隔夜跳空、趨勢漂移與漲跌停一概裝死。

## 核心概念

收盤到收盤波動率每天只看一個價格。股價即使盤中從100衝到105、再跌回100，收盤報酬仍是零；Parkinson則利用高低價區間保留這段路徑資訊。

對$n$個交易日，日變異數估計為：

$$
\widehat{\sigma}_{P}^{2}=\frac{1}{4n\ln 2}\sum_{i=1}^{n}\left(\ln\frac{H_i}{L_i}\right)^2
$$

若以每年$N$個交易日年化：

$$
\widehat{\sigma}_{P,ann}=\sqrt{N\widehat{\sigma}_{P}^{2}}
$$

原始推導以無漂移布朗運動為核心。文獻整理顯示，在模型假設成立時，其理論效率最高約為傳統收盤估計器的5.2倍；這代表估計誤差較小，不代表明天方向或波動預測勝率變成5.2倍。

## 實作流程

1. 取得同一還原基礎的日最高價$H_i$與最低價$L_i$。
2. 排除價格非正、$H_i<L_i$、停牌與明顯錯價。
3. 計算$r_i=\ln(H_i/L_i)$。
4. 在21日、42日或60日視窗內計算$r_i^2$平均，再除以$4\ln2$。
5. 需要年化時乘以252再開根號；不同市場應使用對應交易日數。
6. 與含隔夜風險的[[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]並列，不要只呈現最好看的那個。

## 實戰應用

### 波動率排序與部位縮放

- 在同產業內以21日Parkinson波動率排序，可辨識盤中震盪突然擴大的股票。
- 目標風險部位可粗略寫成「目標年化波動率 ÷ 估計年化波動率」；波動升高便降低部位。
- Parkinson上升但收盤波動率不變，表示盤中來回變激烈，限價、停損與滑價假設應加嚴。

### 合成資料驗算

以8日合法OHLC合成資料計算，日變異數約0.0005341887，日波動率約2.3113%；以252日年化約36.6900%。

## 注意事項

- **漏掉隔夜跳空**：前收至今開不在公式中，財報與政策事件後會低估完整持有風險。
- **零漂移假設**：長週期或強趨勢樣本會偏離原始推導條件。
- **漲跌停截斷**：台股價格被漲跌幅限制卡住時，高低區間不是自由形成的極值，估計會被壓低。
- **低流動性失真**：最高與最低可能只是極少量成交，未必代表可執行價格。
- **還原必須一致**：只調整收盤、不調整高低價，會讓區間比率在除權息或拆股日炸爛。
- **估計不等於預測**：模型內效率較高，不保證下一期波動率預測優於其他方法。

## 相關主題

- [[技術分析/Garman-Klass開高低收波動率估計Garman-Klass-Volatility]]
- [[技術分析/Rogers-Satchell漂移穩健波動率估計Rogers-Satchell-Volatility]]
- [[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]
- [[技術分析/隱含波動率IV與歷史波動率HV實戰判讀]]
- [[技術分析/ATR平均真實波幅-Average-True-Range]]

## 來源

- [Parkinson與Garman-Klass區間波動率來源學習紀錄](../../raw/2026-08-31/Parkinson與Garman-Klass區間波動率來源學習紀錄.md)
- [Parkinson（1980）：The Extreme Value Method for Estimating the Variance of the Rate of Return](https://doi.org/10.1086/296071)
- [CRAN TTR volatility文件](https://search.r-project.org/CRAN/refmans/TTR/html/volatility.html)
