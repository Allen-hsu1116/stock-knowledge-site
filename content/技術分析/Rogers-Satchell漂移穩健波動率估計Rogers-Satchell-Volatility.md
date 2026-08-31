---
title: "Rogers-Satchell漂移穩健波動率估計"
category: "技術分析"
date: 2026-08-31
source_date: 2026-08-31
status: raw_linked
---

# Rogers-Satchell漂移穩健波動率估計

> Rogers-Satchell利用開高低收的相對位置，在股價有明顯趨勢時仍能估日內波動；它解決漂移，不解決隔夜跳空，別看到「穩健」兩字就把腦袋關機。

## 核心概念

對第$i$日定義：

$$
r_{RS,i}=\ln\frac{H_i}{C_i}\ln\frac{H_i}{O_i}+\ln\frac{L_i}{C_i}\ln\frac{L_i}{O_i}
$$

$n$日變異數與年化波動率為：

$$
\widehat{\sigma}_{RS}^{2}=\frac{1}{n}\sum_{i=1}^{n}r_{RS,i}
$$

$$
\widehat{\sigma}_{RS,ann}=\sqrt{N\widehat{\sigma}_{RS}^{2}}
$$

它將日高與日低分別相對開盤、收盤交叉衡量，使期望值不依賴價格漂移。相較[[技術分析/Garman-Klass開高低收波動率估計Garman-Klass-Volatility]]，Rogers-Satchell犧牲一部分模型內效率，換取非零漂移下的適用性。

## 實作流程

1. 取得一致還原的OHLC，驗證K線價格順序與正值。
2. 計算$u_i=\ln(H_i/O_i)$、$d_i=\ln(L_i/O_i)$與$c_i=\ln(C_i/O_i)$。
3. 也可用等價式$r_{RS,i}=u_i(u_i-c_i)+d_i(d_i-c_i)$實作。
4. 在21日、42日或60日視窗內取$r_{RS,i}$平均。
5. 乘以252再開根號得到年化波動率。
6. 同時計算[[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]，監控隔夜風險占比是否上升。

## 實戰應用

### 趨勢市場的風險尺度

- 強勢股一路上漲時，Rogers-Satchell可降低零漂移假設對日內波動估計的干擾。
- 可用於波動率排序、動態停損寬度、風險平價與部位縮放，但不直接產生方向訊號。
- 若Rogers-Satchell下降、趨勢仍在，可代表日內路徑變順；仍須搭配成交量、流動性與隔夜風險確認。

### 合成資料驗算

以8日合法OHLC合成資料計算，日變異數約0.0006319439，日波動率約2.5138%；252日年化約39.9061%。

## 注意事項

- **不含隔夜跳空**：前收至今開沒有進公式，事件型股票仍會低估完整持有風險。
- **漂移穩健不等於跳空穩健**：解決一個假設，不是得到萬能估計器。
- **短窗不穩**：極少數大區間會支配平均值，需觀察中位數或多視窗敏感度。
- **資料品質**：錯誤高低價、零成交、還原不一致都會污染對數比率。
- **制度截斷**：漲跌停會壓住高低區間，低估潛在波動。
- **不得把低波動當安全**：流動性枯竭或停牌也可能讓日內區間看似很小，卻藏著下一次跳空。

## 相關主題

- [[技術分析/Parkinson高低價波動率估計Parkinson-Volatility]]
- [[技術分析/Garman-Klass開高低收波動率估計Garman-Klass-Volatility]]
- [[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]
- [[風險管理/波動率體制轉換模型Volatility-Regime-Switching-Model]]
- [[技術分析/ATR平均真實波幅-Average-True-Range]]

## 來源

- [Rogers-Satchell漂移穩健波動率來源學習紀錄](../../raw/2026-08-31/Rogers-Satchell漂移穩健波動率來源學習紀錄.md)
- [Rogers與Satchell（1991）：Estimating Variance From High, Low and Closing Prices](https://doi.org/10.1214/aoap/1177005835)
- [CRAN TTR volatility文件](https://search.r-project.org/CRAN/refmans/TTR/html/volatility.html)
