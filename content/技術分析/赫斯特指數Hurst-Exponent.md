---
title: 赫斯特指數 Hurst Exponent
date: 2026-06-29
category: "技術分析"
---

# 赫斯特指數 Hurst Exponent

> 一個介於 0 和 1 之間的數字，告訴你這個市場是趨勢盤、盤整盤還是隨機漫步

## 核心概念

Hurst Exponent（赫斯特指數，記為 H）用來衡量時間序列的**長期記憶性**（long-term memory），最早由英國水文學家 Harold Edwin Hurst 在研究尼羅河水位變化時提出，後來由 Benoît Mandelbrot 引入金融市場分析。

H 值的三種狀態：

- **H > 0.5（0.5 ~ 1.0）：持續性（Persistent）** — 正自相關，漲了還會繼續漲、跌了還會繼續跌。趨勢市的核心特徵，適合趨勢追蹤策略
- **H = 0.5：隨機漫步（Random Walk）** — 無記憶，當前價格變化與過去無關，效率市場假說的預設狀態
- **H < 0.5（0 ~ 0.5）：反持續性（Anti-persistent / Mean-reverting）** — 負自相關，漲了容易回跌、跌了容易反彈。盤整/均值回歸市的核心特徵

H 與分形維度 D 的關係：**D = 2 - H**
- H 接近 1 → D 接近 1，價格路徑平滑如直線（強趨勢）
- H 接近 0 → D 接近 2，價格路徑充滿整個平面（高度震盪）

## 估算方法

### R/S 分析（Rescaled Range Analysis）

最經典的估算方法，步驟如下：

1. 把長度為 N 的時間序列切成多個長度為 n 的子序列（n = N, N/2, N/4, ...）
2. 對每個子序列計算重標極差 R(n)/S(n)：
   - 計算均值 m
   - 建立均值調整序列 Yt = Xt - m
   - 計算累積偏差序列 Zt = ΣYi
   - R = max(Z) - min(Z)（最大累積偏差減最小累積偏差）
   - S = 標準差
   - R/S = R(n) / S(n)
3. 對所有長度 n 的子序列取 R/S 平均值
4. 在 log-log 圖上繪製 log[R/S] vs log(n)，斜率即為 H

### DFA（Detrended Fluctuation Analysis）

去趨勢波動分析，適合非平穩時間序列，比 R/S 更穩健。

### 信心區間

Weron 用 bootstrapping 推導出近似的信心區間公式。以 95% 信心水準為例：

- **R/S（Anis-Lloyd 修正）**：0.5 - exp(-7.33·log(log M) + 4.21) 到 exp(-7.20·log(log M) + 4.04) + 0.5
- **DFA**：0.5 - exp(-2.93·log M + 4.45) 到 exp(-3.10·log M + 4.77) + 0.5

其中 M = log₂(N)，N 為序列長度。子序列長度 n > 50 才建議使用，太短會有高變異。

## 實戰應用

### 判斷市場體制

這是 Hurst Exponent 最有價值的用途——在策略選擇之前先判斷市場處於什麼狀態：

- **H > 0.6**：強趨勢市 → 趨勢追蹤策略（移動停利、突破策略、均線交叉）
- **0.4 < H < 0.6**：不確定區 → 縮小部位或觀望
- **H < 0.4**：均值回歸市 → 區間交易策略、網格交易、RSI 超買超賣

實作上用滾動窗口（如 100~200 日）計算 H 值，觀察其變化趨勢。

### 搭配其他指標

- **H + ADX**：H > 0.5 且 ADX > 25 → 高機率趨勢啟動
- **H + 布林通道**：H < 0.4 且布林通道窄 → 盤整確認，適合區間交易
- **H + VIX**：H 下降到 0.4 以下可能代表從趨勢轉盤整

### 選股應用

不同股票有不同的 H 值特性：
- 大型權值股 H 值通常接近 0.5（接近效率市場）
- 小型投機股 H 值可能 > 0.6（趨勢性強，但也容易反轉）
- 可用 H 值篩選適合自己策略的股票池

### 與 [[技術分析/FRAMA分形自適應移動平均線|FRAMA]] 的關係

FRAMA 指標內部計算的分形維度 D 就是基於 Hurst 的理論。D = 2 - H，FRAMA 根據 D 值動態調整均線速度。

## 注意事項

1. **樣本不足不準**：少於 100 個數據點時 H 估計變異很大，建議至少 200 點以上
2. **R/S 分析的偏誤**：小樣本下 R/S 會高估 H（偏向 >0.5），需使用 Anis-Lloyd 修正
3. **H 值會變動**：市場體制會轉換，H 不是固定值，要用滾動窗口持續計算
4. **非平穩性問題**：股價本身非平穩，通常用報酬率（log return）而非原始價格計算 H
5. **效率市場假說**：如果 H 顯著偏離 0.5，理論上代表市場不效率、可以預測，但實務上交易成本和滑價會吃掉大部分優勢
6. **多分形**：廣義 Hurst 指數 H(q) 如果對不同 q 值變化很大，代表市場具有多分形特徵，單一 H 值不夠描述

## 相關主題

- [[技術分析/FRAMA分形自適應移動平均線]] — 基於分形維度的自適應均線
- [[操作策略/市場體制識別Market-Regime-Detection]] — 用 H 值判斷市場體制
- [[技術分析/ADX趨勢強度過濾盤整]] — 趨勢強度判斷的互補指標
- [[技術分析/斬波指標Choppiness-Index]] — 盤整判斷的互補指標
- [[技術分析/ATR平均真實波幅-Average-True-Range]] — 波動度量的基礎工具

## 來源

- [Hurst Exponent - Wikipedia](../raw/2026-06-29/赫斯特指數Hurst-Exponent.md)
- Hurst, H.E. (1951). "Long-term storage capacity of reservoirs". Transactions of the American Society of Civil Engineers.
- Mandelbrot, B.B. (1968). "Noah, Joseph, and operational hydrology". Water Resources Research.
- Weron, R. (2002). "Estimating long-range dependence: finite sample properties and confidence intervals". Physica A.