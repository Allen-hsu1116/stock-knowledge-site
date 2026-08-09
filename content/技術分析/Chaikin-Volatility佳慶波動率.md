---
title: "Chaikin Volatility 佳慶波動率"
category: "技術分析"
---

# Chaikin Volatility 佳慶波動率

> Marc Chaikin 設計的波動率指標，用高低價差的 EMA 變化率衡量波動程度——不是像 ATR 那樣看絕對波動大小，而是看波動「正在擴大還是收縮」。

## 什麼是 Chaikin Volatility

Chaikin Volatility（CHV）是由 Marc Chaikin 開發的技術指標，用來衡量市場波動程度的變化。與 [[技術分析/ATR平均真實波幅-Average-True-Range|ATR（平均真實波動幅度）]]不同，ATR 衡量波動的「絕對大小」，CHV 衡量波動的「變化率」——波動正在加速還是減速。

**核心邏輯**：波動率本身有聚類效應（Volatility Clustering）——高波動後通常接高波動、低波動後接低波動。但波動率的「轉折點」往往領先價格轉折，CHV 用來捕捉這個轉折訊號。

## 計算公式

### Step 1：計算每日高低價差

```
HL = High - Low
```

### Step 2：計算 HL 的指數移動平均

```
EMA_HL = EMA(HL, n)
```

- 預設參數 n = 10

### Step 3：計算 CHV

```
CHV = (EMA_HL(今日) - EMA_HL(m日前)) / EMA_HL(m日前) × 100
```

- 預設 m = 10

所以 CHV 本質上是「高低價差 EMA 的 m 期變化率」，衡量波動寬度的動量。

## 參數設定

- **預設值**：n=10, m=10（Chaikin 原始設定）
- **短線**：n=5, m=5（更靈敏但雜訊多）
- **長線**：n=20, m=20（更平滑但落後）

## 判讀方法

### 1. 波動率擴張與收縮

- **CHV 上升**：高低價差正在擴大，波動增加，市場可能即將出現趨勢
- **CHV 下降**：高低價差正在縮小，波動減少，市場進入收縮或盤整
- **CHV 接近零**：波動率穩定，高低價差沒有明顯變化

### 2. 波動率高潮與低潮

- **CHV 暴衝後回落**：波動率高潮已過，可能伴隨趨勢反轉或進入整理
- **CHV 長期極低檔**：波動率壓縮到極限，類似 [[技術分析/布林通道Bollinger-Bands三軌八型態|布林通道]] 的 Squeeze 狀態，大行情可能即將爆發

### 3. 與價格的背離

- **價格創新高但 CHV 未創新高**：波動力道減弱，趨勢可能即將結束（類似量價背離）
- **價格創新低但 CHV 未創新低**：下殺力道減弱，底部可能接近

### 4. 趨勢確認

- **上升趨勢中 CHV 溫和上升**：健康趨勢，波動隨趨勢擴大
- **上升趨勢中 CHV 急劇上升**：可能過熱，注意回檔風險
- **下降趨勢中 CHV 上升**：恐慌性拋售，可能是底部訊號
- **盤整中 CHV 持續下降**：壓縮過程，等待突破方向

## 與其他波動率指標比較

**CHV vs ATR**
- ATR 看波動的絕對值（多少點）
- CHV 看波動的變化率（擴大還是收縮）
- 兩者互補：ATR 定大小，CHV 定方向

**CHV vs [[技術分析/布林通道Bollinger-Bands三軌八型態|布林通道]]**
- 布林通道用標準差畫通道寬度，視覺化波動
- CHV 用數字量化波動變化率
- 布林 Squeeze（通道壓縮）≈ CHV 長期低檔

**CHV vs [[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting|GARCH]]**
- GARCH 是統計模型預測未來波動率
- CHV 是技術指標觀察過去波動率變化
- GARCH 更嚴謹但更複雜，CHV 更直覺但更粗糙

**CHV vs [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|VVIX]]**
- VVIX 衡量 VIX 自身的波動率（恐慌的恐慌）
- CHV 衡量標的高低價差的變化率
- VVIX 是市場層級情緒指標，CHV 是個股或指數層級技術指標

## 實戰策略

### 策略 1：壓縮突破

1. CHV 下降至近期低位（波動率壓縮）
2. 搭配 [[技術分析/TTM-Squeeze壓縮指標實戰判讀|TTM Squeeze]] 或布林通道確認壓縮
3. 等待價格帶量突破方向
4. CHV 確認——突破時 CHV 應該同步上升

### 策略 2：波動高潮反轉

1. CHV 暴衝至歷史高位（恐慌拋售或瘋狂追漲）
2. 價格出現 [[技術分析/單日反轉Reversal-Day|單日反轉]] 或長下影線
3. CHV 開始回落確認波動高潮已過
4. 進場做均值回歸或反轉交易

### 策略 3：趨勢健康度檢查

1. 上升趨勢中定期檢查 CHV
2. CHV 溫和上升 = 趨勢健康，繼續持有
3. CHV 急劇暴衝 = 可能過熱，考慮 [[操作策略/分批停利策略Partial-Exit-Strategy|分批停利]]
4. CHV 背離價格 = 警訊，加強 [[風險管理/移動停利停損Trailing-Stop|移動停利]]

## 與 Chaikin 指標家族的關係

Marc Chaikin 設計了一系列指標，知識庫中已有的：

- [[技術分析/Chaikin-Money-Flow佳慶資金流量指標|Chaikin Money Flow (CMF)]] — 用收盤位置×成交量衡量資金流向
- [[技術分析/Chaikin-Oscillator佳慶震盪指標|Chaikin Oscillator]] — A/D 線的 MACD 版

CHV 與 CMF/CO 的差異：
- CMF 和 CO 衡量「資金流向」（用成交量）
- CHV 衡量「波動率變化」（用高低價差）
- 三者可以組合使用：CMF 看資金方向 + CHV 看波動狀態

## 優缺點

**優點**：
- 捕捉波動率轉折——領先價格轉折的早期訊號
- 與 ATR 互補——一個看大小一個看方向
- 背離訊號有參考價值
- 適合搭配壓縮突破策略

**缺點**：
- 只用高低價差不看收盤位置——忽略盤中方向資訊
- 不考慮跳空缺口——隔夜跳空不反映在當日高低價差中
- 參數敏感——不同 n 和 m 設定結果差異大
- 單獨使用效果有限——必須搭配趨勢指標和量能確認
- 極端行情下失真——連續漲停/跌停時高低價差失真

## 相關文章

- [[技術分析/ATR平均真實波幅-Average-True-Range|ATR 平均真實波幅]] — 波動率絕對值指標，CHV 的互補
- [[技術分析/布林通道Bollinger-Bands三軌八型態|布林通道 Bollinger Bands]] — 用標準差衡量波動的視覺化工具
- [[技術分析/Chaikin-Money-Flow佳慶資金流量指標|Chaikin Money Flow]] — 同作者的資金流向指標
- [[技術分析/Chaikin-Oscillator佳慶震盪指標|Chaikin Oscillator]] — 同作者的震盪指標
- [[技術分析/TTM-Squeeze壓縮指標實戰判讀|TTM Squeeze]] — 波動壓縮偵測指標，可與 CHV 搭配
- [[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting|GARCH 模型]] — 波動率的統計建模方法
- [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|VVIX]] — 波動率的波動率

---

*標籤：#技術分析 #波動率指標 #Marc-Chaikin #壓縮突破 #背離訊號*

## 核心概念

（待補充）

## 實戰應用

（待補充）

## 注意事項

（待補充）

## 相關主題

（待補充）
