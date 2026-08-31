---
title: "Yang-Zhang隔夜跳空波動率估計"
category: "技術分析"
date: 2026-08-31
source_date: 2026-08-31
status: raw_linked
---

# Yang-Zhang隔夜跳空波動率估計

> Yang-Zhang把前收至今開的隔夜跳空、開盤至收盤報酬與Rogers-Satchell日內區間合併，兼顧漂移與休市風險；對台股持倉者比只看日內區間更接近真的會痛的地方。

## 核心概念

對$n$個交易日定義：

$$
o_i=\ln\frac{O_i}{C_{i-1}},\qquad c_i=\ln\frac{C_i}{O_i}
$$

其中$o_i$是隔夜報酬，$c_i$是開盤至收盤報酬。再計算：

$$
\widehat{\sigma}_{o}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(o_i-\bar{o})^2
$$

$$
\widehat{\sigma}_{c}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(c_i-\bar{c})^2
$$

以及[[技術分析/Rogers-Satchell漂移穩健波動率估計Rogers-Satchell-Volatility]]的日內變異數$\widehat{\sigma}_{RS}^{2}$。Yang-Zhang總變異數為：

$$
\widehat{\sigma}_{YZ}^{2}=\widehat{\sigma}_{o}^{2}+k\widehat{\sigma}_{c}^{2}+(1-k)\widehat{\sigma}_{RS}^{2}
$$

常用權重為：

$$
k=\frac{0.34}{1.34+\frac{n+1}{n-1}}
$$

最後以$\sqrt{N\widehat{\sigma}_{YZ}^{2}}$年化。它是多期估計器，不能只拿一根K線硬算。

## 實作流程

1. 每個視窗需多取一筆前日收盤，才能計算第一個隔夜報酬。
2. 整組OHLC與前收必須使用一致的還原方式。
3. 分別計算隔夜報酬樣本變異數、日盤報酬樣本變異數及Rogers-Satchell日內變異數。
4. 依視窗長度計算$k$，在變異數層級加權後才開平方根。
5. 以21日、42日及60日多視窗檢查穩健性；短窗只看單一數字，很容易被一次跳空綁架。
6. 額外記錄$\widehat{\sigma}_{o}^{2}/\widehat{\sigma}_{YZ}^{2}$，當作隔夜風險占比的診斷指標。

## 實戰應用

### 台股隔夜風險儀表板

- 台股收盤後仍會受到美股、ADR、匯率、法說、財報與政策消息影響，隔日開盤跳空是實際持有成本，不是統計髒點。
- Yang-Zhang明顯高於Rogers-Satchell，表示風險主要累積在休市期間；隔夜部位上限、事件前槓桿與停損滑價假設都應收緊。
- 兩者同步升高，代表日內與隔夜波動都在惡化，部位縮放不能只砍一點意思意思。

### 合成資料驗算

以8日合法OHLC及前一日收盤計算：

- $k\approx0.1294886$
- 隔夜日變異數約0.0001042226。
- 日盤報酬變異數約0.0003042990。
- Rogers-Satchell日變異數約0.0006319439。
- Yang-Zhang日變異數約0.0006937402，日波動率約2.6339%，252日年化約41.8118%。

## 注意事項

- **先加變異數再開根號**：把三個波動率直接相加是量綱看似對、統計上亂來。
- **公司行動假跳空**：除權息與拆併股若未一致還原，隔夜變異數會被灌爆。
- **停牌復牌**：累積多日資訊一次反映，不應與普通隔夜同等看待，需另設事件標記。
- **漲跌停截斷**：實際潛在價格可能超出限制，高低價與收盤價都被制度壓住。
- **視窗依賴**：$k$與樣本變異數依$n$變動，跨股票比較必須使用同一視窗與年化規則。
- **不是未來預言**：它是歷史實現波動率估計；要做預測仍須搭配[[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting]]或其他時間序列模型。
- **不是選擇權IV**：歷史OHLC估計與市場前瞻定價不同，需配合[[技術分析/隱含波動率IV與歷史波動率HV實戰判讀]]解讀。

## 相關主題

- [[技術分析/Parkinson高低價波動率估計Parkinson-Volatility]]
- [[技術分析/Garman-Klass開高低收波動率估計Garman-Klass-Volatility]]
- [[技術分析/Rogers-Satchell漂移穩健波動率估計Rogers-Satchell-Volatility]]
- [[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting]]
- [[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]

## 來源

- [Yang-Zhang隔夜跳空波動率來源學習紀錄](../../raw/2026-08-31/Yang-Zhang隔夜跳空波動率來源學習紀錄.md)
- [Yang與Zhang（2000）：Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices](https://doi.org/10.1086/209650)
- [RePEc論文摘要](https://ideas.repec.org/a/ucp/jnlbus/v73y2000i3p477-91.html)
- [CRAN TTR volatility文件](https://search.r-project.org/CRAN/refmans/TTR/html/volatility.html)
