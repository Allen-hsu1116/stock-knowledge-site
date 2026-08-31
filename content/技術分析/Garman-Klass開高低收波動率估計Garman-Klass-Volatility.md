---
title: "Garman-Klass開高低收波動率估計"
category: "技術分析"
date: 2026-08-31
source_date: 2026-08-31
status: raw_linked
---

# Garman-Klass開高低收波動率估計

> Garman-Klass把高低區間與開收到盤報酬合併，通常比只看高低價的Parkinson更有效率；代價是仍依賴零漂移、無開盤跳空等乾淨到有點不食人間煙火的假設。

## 核心概念

Garman-Klass同時利用開盤、最高、最低與收盤，日變異數項為：

$$
g_i=\frac{1}{2}\left(\ln\frac{H_i}{L_i}\right)^2-(2\ln2-1)\left(\ln\frac{C_i}{O_i}\right)^2
$$

$n$日變異數及年化波動率為：

$$
\widehat{\sigma}_{GK}^{2}=\frac{1}{n}\sum_{i=1}^{n}g_i
$$

$$
\widehat{\sigma}_{GK,ann}=\sqrt{N\widehat{\sigma}_{GK}^{2}}
$$

第一項吸收日內完整高低區間，第二項扣除開盤到收盤方向性移動的重複資訊。在模型假設成立時，文獻與TTR文件列出的理論相對效率最高約為收盤估計器的7.4倍。

## 實作流程

1. 檢查每根K線滿足$L_i\le\min(O_i,C_i)\le\max(O_i,C_i)\le H_i$。
2. 對整組OHLC使用一致的公司行動還原因子。
3. 分別計算$\ln(H_i/L_i)$與$\ln(C_i/O_i)$。
4. 逐日計算$g_i$，在固定視窗內取平均。
5. 若視窗平均變異數為負，先查資料錯誤、四捨五入與樣本過短，禁止直接取絕對值粉飾。
6. 與[[技術分析/Parkinson高低價波動率估計Parkinson-Volatility]]、[[技術分析/Rogers-Satchell漂移穩健波動率估計Rogers-Satchell-Volatility]]及[[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]並排比較。

## 實戰應用

### 區分日內與隔夜風險

- Garman-Klass平穩、Yang-Zhang突然升高：風險主要來自隔夜跳空。
- Garman-Klass與Yang-Zhang同步升高：日內與隔夜風險都在擴張。
- Garman-Klass高於收盤波動率很多：盤中震盪被收盤價掩蓋，日內停損與滑價壓力較大。

### 合成資料驗算

以8日合法OHLC合成資料計算，日變異數約0.0006375030，日波動率約2.5249%；252日年化約40.0813%。

## 注意事項

- **零漂移**：強趨勢或過長視窗會降低原始估計器適切性。
- **無開盤跳空**：基本式假設開盤接近前收，不能把休市消息造成的跳空當空氣。
- **價格限制**：漲跌停、處置分盤與停牌會改變高低價形成機制。
- **極值可執行性**：日高日低可能只有一小筆成交，不代表你的部位能在那裡成交。
- **效率不是預測力**：同一期變異數估得更精準，不代表下一期預測一定更準。
- **不是方向指標**：高波動只代表風險尺度變大，不代表應做多或放空。

## 相關主題

- [[技術分析/Parkinson高低價波動率估計Parkinson-Volatility]]
- [[技術分析/Rogers-Satchell漂移穩健波動率估計Rogers-Satchell-Volatility]]
- [[技術分析/Yang-Zhang隔夜跳空波動率估計Yang-Zhang-Volatility]]
- [[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting]]
- [[操作策略/波動率目標策略Volatility-Targeting]]

## 來源

- [Parkinson與Garman-Klass區間波動率來源學習紀錄](../../raw/2026-08-31/Parkinson與Garman-Klass區間波動率來源學習紀錄.md)
- [Garman與Klass（1980）：On the Estimation of Security Price Volatilities from Historical Data](https://doi.org/10.1086/296072)
- [CRAN TTR volatility文件](https://search.r-project.org/CRAN/refmans/TTR/html/volatility.html)
