---
title: Fisher Transform 費雪轉換指標
date: 2026-06-22
category: "技術分析"
---

# Fisher Transform 費雪轉換指標

> 將價格的非常態分佈轉為近似常態分佈，讓極端轉折點更清晰、訊號更果斷的動能震盪指標

## 核心概念

Fisher Transform 由 J.F. Ehlers 開發，核心思想是**金融價格的分佈並非常態分佈**——價格在趨勢中會形成尾部肥厚（fat tails）和偏態（skewness），使得傳統震盪指標在極端區域反應遲鈍。Fisher Transform 利用反雙曲正切函數（arctanh）將價格數列轉換為近似常態分佈，讓轉折點的訊號更加尖銳且及時。

### 計算步驟

1. **將價格正規化到 -1 ~ +1 區間**：
   - 取近期 N 期（通常 10 期）的最高價與最低價
   - Value = (Price - LowestLow) / (HighestHigh - LowestLow) - 0.5
   - 限制在 -0.999 ~ +0.999 之間（避免 arctanh 無法定義）

2. **Fisher Transform 計算**：
   - Fisher = 0.5 × ln[(1 + Value) / (1 - Value)]
   - 數學上等價於 arctanh(Value) × 2
   - 轉換後的值通常在 -3 ~ +3 之間，極端可達 ±5 以上

3. **信號線**：
   - Signal = 前一期的 Fisher 值（即 Fisher[1]）
   - Fisher 與 Signal 的交叉即為交易訊號

### 為什麼有效

| 特性 | 原始價格 | Fisher Transform 後 |
|------|---------|---------------------|
| 分佈型態 | 偏態、肥尾 | 近似常態分佈 |
| 極端值頻率 | 較少但波動大 | 更頻繁且更對稱 |
| 轉折速度 | 漸進、遲鈍 | 尖銳、果斷 |
| 超買超賣界定 | 難以固定閾值 | ±2 以上即極端 |

關鍵在於 arctanh 函數的特性：輸入值接近 ±1 時輸出急遽放大，這讓價格在極端區域的微小變化被放大，使轉折訊號比 RSI、KD 等傳統指標更早出現。

## 實戰應用

### 1. 基本交叉策略

- **Fisher 上穿 Signal**（即 Fisher 向上突破前一期值）→ 買進訊號
- **Fisher 下穿 Signal** → 賣出訊號
- Fisher 在零軸上方表示多頭動能，下方表示空頭動能

### 2. 極端值反轉策略

- Fisher > +2 → 超買區，準備反轉向下
- Fisher < -2 → 超賣區，準備反轉向上
- ±2 並非硬性閾值，需搭配歷史分位數校準
- **Fisher 從極端區回到零軸附近再交叉**比極端區直接反向更可靠

### 3. 零軸趨勢確認

- Fisher 穿越零軸上方 → 短期趨勢轉多
- Fisher 穿越零軸下方 → 短期趨勢轉空
- 零軸附近交叉適合趨勢確認，極端區交叉適合抓反轉

### 4. 多時間框架搭配

- 日線 Fisher 判斷中短期方向
- 60分鐘 Fisher 找進場時機
- 週線 Fisher 確認大趨勢
- 三個時間框架同向時勝率最高

### 5. 背離交易

- 價格創新高但 Fisher 未創新高 → 頂背離，賣出訊號
- 價格創新低但 Fisher 未創新低 → 底背離，買進訊號
- Fisher 的背離比 RSI 背離更早出現，因為轉換後的值對動能變化更敏感

## 注意事項

### 陷阱與限制

1. **盤整市假訊號多**：Fisher 在盤整時反覆穿越零軸，產生大量假訊號，必須搭配 [[ADX趨勢強度過濾盤整]] 或 [[斬波指標Choppiness-Index]] 過濾
2. **參數敏感度高**：10 期是常用設定，但短週期（5）雜訊多、長週期（20）訊號滯後，需依標的波動特性調整
3. **不適合長線持有**：Fisher Transform 是短線動能指標，訊號頻繁，長線投資者應搭配基本面分析
4. **極端值不等於反轉**：Fisher > +2 不代表一定反轉，強趨勢中 Fisher 可長時間維持在極端區（類似 [[技術指標鈍化與對策|指標鈍化]]），硬反向會被趨勢碾壓
5. **回測過擬合風險**：參數和閾值容易在回測中被過度最佳化，需做 [[技術分析回測方法與過度擬合Backtesting-and-Overfitting|樣本外驗證]]

### 最佳搭配組合

- **Fisher + ADX**：ADX > 25 確認趨勢存在，只用 Fisher 的交叉訊號，盤整時忽略
- **Fisher + 布林通道**：Fisher 極端值 + 價格觸及布林上/下軌 → 反轉機率更高
- **Fisher + 成交量**：Fisher 交叉需帶量確認，量縮交叉假訊號機率高（參考 [[成交量確認原則Volume-Confirmation]]）
- **Fisher + 多時間框架**：大週期 Fisher 方向與小週期交叉一致才進場

## 相關主題

- [[技術分析/RSI相對強弱指標]] — 同為動能震盪指標，但 Fisher 轉折更尖銳
- [[技術分析/Stochastic-RSI隨機RSI]] — 對 RSI 再加工的指標，概念類似 Fisher 對價格再加工
- [[技術分析/MACD指標實戰判讀]] — 另一種動能判讀工具，MACD 較平滑、Fisher 較靈敏
- [[技術分析/ADX趨勢強度過濾盤整]] — Fisher 的最佳過濾器，盤整時關閉 Fisher 訊號
- [[技術分析/多時間框架分析]] — Fisher 多時間框架搭配提升勝率
- [[技術分析/技術指標鈍化與對策]] — 極端區鈍化問題與應對
- [[技術分析/背離Divergence進階實戰]] — Fisher 背離訊號的進階應用
- [[技術分析/多指標共振交易系統Multi-Indicator-Confluence]] — Fisher 作為共振系統的動能組件

## 來源

- Ehlers, J.F. (2002). "Trading with the Fisher Transform." Technical Analysis of Stocks & Commodities
- Wikipedia: Fisher transformation — 統計學基礎理論
- TradingView Community: Fisher Transform 指標文檔與社群討論