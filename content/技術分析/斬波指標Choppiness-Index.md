---
title: 斬波指標 Choppiness Index (CHOP)
date: 2026-05-18
categories: [技術分析]
tags: [CHOP, 斬波指標, 趨勢判斷, 盤整判斷, 假突破過濾, ATR, Fibonacci]
---

# 斬波指標 Choppiness Index (CHOP)

> 用分形幾何量化市場效率的狀態指標，高分=盤整、低分=趨勢，是過濾假突破的利器。

## 核心概念

斬波指標（Choppiness Index, CHOP）由澳洲商品交易員 E.W. Dreiss 開發，基於**混沌理論與分形幾何（Fractal Geometry）**，用來量化市場的「混亂程度」或「效率」。

**關鍵特徵：CHOP 不是方向性指標**。它不告訴你漲跌，而是告訴你市場現在處於「趨勢」還是「盤整」狀態——這是一個**狀態指標**。

### 數學邏輯

CHOP 的核心思想：比較價格「實際走過的路」和「最終產生的位移」。

- **高效率（趨勢）**：價格走勢像一條直線，兩點距離最短 → CHOP 數值低
- **低效率（盤整）**：價格走勢像一團亂麻，走了很長的路但沒移動多少距離 → CHOP 數值高

### 計算公式

```
CHOP = 100 × LOG10( SUM(ATR(1), n) / (MaxHi(n) - MinLo(n)) ) / LOG10(n)
```

- **分子**：過去 N 天的真實波幅（TR）總和 = 價格「走過的路」
- **分母**：過去 N 天的最高價 - 最低價 = 價格「產生的位移」
- **取對數**：計算分形維度
- 預設週期：14 天

## 實戰應用

### 1. 假突破過濾器（最核心用途）

當你的主策略（如 MACD、突破策略）發出訊號時，**先檢查 CHOP**：

| 情境 | CHOP 數值 | 判定 | 操作 |
|------|-----------|------|------|
| 價格突破 + CHOP > 61.8 | 高盤整 | 假突破機率極高 | 忽略訊號、不追價 |
| 價格突破 + CHOP < 38.2 | 高效率趨勢 | 趨勢有效 | 確認進場 |
| 價格突破 + CHOP 38.2~61.8 | 過渡區 | 訊號不明確 | 縮小部位或等待 |

**實戰心法**：CHOP > 50 時忽略突破訊號，CHOP < 50 時確認突破有效。

### 2. 抓起漲點（The Squeeze）

CHOP 最迷人的地方在於**極值反轉**：

- 當 CHOP 飆升到 **70 以上**（極度壓縮），代表波動率低到極點
- 這是「暴風雨前的寧靜」，市場即將變盤（大漲或大跌）
- **選股應用**：設定條件「CHOP > 70」→ 篩選出即將爆發的潛力股清單
- 但 CHOP 不告訴方向，需搭配方向性指標（如均線、趨勢線）判斷多空

### 3. 順勢持有判斷

TradingSim 的實戰建議：**如果 CHOP 未連續出現 3 次以上超過 61.8，且股價在明確趨勢中，繼續持有**。

- 回檔只是趨勢中的噪音，不需要過度反應
- 只有當 CHOP 持續回到 61.8 以上，才需警覺趨勢可能結束

### 4. 盤整中操作

- CHOP > 61.8 時可進行**區間操作**（高出低進）
- 但 TradingSim 認為盤整交易不是 CHOP 的強項，因為它不像超買超賣指標能精確抓轉折
- 建議搭配 [[KD指標隨機指標]] 或 [[威廉指標Williams-%R]] 輔助

### 5. XQ 語法範例

```xq
Input: Length(14, "計算週期");
Variable: TR(0), SumTR(0), MaxHi(0), MinLo(0), RangeLen(0), CHOP(0);

TR = TrueRange;
SumTR = Summation(TR, Length);
MaxHi = Highest(High, Length);
MinLo = Lowest(Low, Length);
RangeLen = MaxHi - MinLo;

if RangeLen > 0 and SumTR > 0 then begin
  Value1 = SumTR / RangeLen;
  CHOP = 100 * Log(Value1) / Log(Length);
end else begin
  CHOP = 50;
end;

Plot1(CHOP, "Choppiness Index");
Plot2(61.8, "盤整界線");
Plot3(38.2, "趨勢界線");
```

## 注意事項

1. **CHOP 不預測方向**：它只告訴你「市場現在什麼狀態」，不會告訴你漲或跌。高 CHOP 後的突破可能是向上也可能是向下，必須搭配方向性指標。

2. **鈍化問題**：CHOP > 61.8 不代表市場會「馬上」變盤。盤整可能持續很長時間，極端值（> 70）才是更有意義的壓縮訊號。

3. **不適合所有股票**：有些股票的 CHOP 不會乖乖遵守 61.8/38.2 的界線，頻繁出現假訊號。TradingSim 建議：**如果某檔股票不適配 CHOP，別硬調參數，直接剔除**。

4. **需要搭配其他指標**：CHOP 是過濾器，不是進場訊號。最佳搭配：
   - 搭配 [[ADX趨勢強度過濾盤整]]：雙重確認趨勢/盤整狀態
   - 搭配 [[ATR平均真實波幅-Average-True-Range]]：ATR 是 CHOP 的計算基礎，兩者天然相關
   - 搭配 [[布林通道Bollinger-Bands三軌八型態]]：CHOP 過濾 + 布林帶突破 = 高品質進場
   - 搭配成交量：突破時必須有量能配合

5. **參數不要亂改**：預設 14 期是經過驗證的，61.8/38.2 的 Fibonacci 界線也是標準值。過度客製化只會導致過度擬合。

6. **盤整交易風險高**：TradingSim 明確指出「交易盤整（trading the chop）長期以來效果不好」，CHOP 的強項在於**確認趨勢和過濾假突破**，而非在盤整中找交易機會。

## 相關主題

- [[ADX趨勢強度過濾盤整]] - 另一個判斷趨勢/盤整的指標，可與 CHOP 雙重確認
- [[ATR平均真實波幅-Average-True-Range]] - CHOP 計算的核心基礎
- [[假突破三道過濾]] - CHOP 是假突破過濾的利器
- [[布林通道Bollinger-Bands三軌八型態]] - 布林帶突破搭配 CHOP 過濾
- [[多指標共振交易系統Multi-Indicator-Confluence]] - 多指標共振框架
- [[技術指標鈍化與對策]] - 指標鈍化的通用對策
- [[支撐壓力互換與真假突破判斷]] - 真假突破判斷原則
- [[斐波那契回撤Fibonacci-Retracement]] - CHOP 的 61.8/38.2 界線來自 Fibonacci

## 來源

- [斬波指標 Choppiness Index (CHOP) - XQ](../raw/2026-05-18/斬波指標Choppiness-Index-XQ.md)
- [Choppiness Index Indicator: Trading Guide - TradingSim](../raw/2026-05-18/Choppiness-Index-TradingSim.md)
- [Choppiness Index (CHOP) - TradingView](../raw/2026-05-18/Choppiness-Index-TradingView.md)