---
title: "DeMarker指標 DeMarker Oscillator"
tags: [技術分析, 動量指標, 震盪指標, Tom DeMark]
created: 2026-07-06
---

# DeMarker指標 DeMarker Oscillator

> Tom DeMark 開發的動量震盪指標，比較當期高低點與前一期的高低點，衡量買方壓力與賣方壓力的相對強弱，0~1區間運行，低於0.3超賣、高於0.7超買。

## 核心概念

**DeMarker 指標**（簡稱 DeM）由技術分析大師 Tom DeMark 所設計，用來辨識價格的耗盡點和潛在反轉時機。跟同一作者的 [[TD-Sequential序列指標Setup9Countdown13|TD Sequential]] 不同——DeMarker 是一個連續的震盪指標，而非離散的計數系統。

### 與其他震盪指標的差異

- **RSI**（[[RSI相對強弱指標]]）：用漲跌幅度計算，假設漲幅=買方力量、跌幅=賣方力量
- **KD**（[[KD指標隨機指標]]）：用收盤在近期區間的位置計算
- **DeMarker**：用**高低點比較**計算，衡量「買方能把價格推多高」vs「賣方能把價格壓多低」

DeMarker 的獨特之處在於它不看收盤價的位置，而是直接比較每期的高低點變化，因此能更純粹地反映多空推動力道。

## 計算公式

### 逐步計算（以N=14為例）

**Step 1：計算 DeMax（買方壓力）**

$$DeMax_i = \begin{cases} High_i - High_{i-1} & \text{if } High_i > High_{i-1} \\ 0 & \text{if } High_i \leq High_{i-1} \end{cases}$$

當期高點比前一期高點高 → 差值就是買方壓力；否則買方壓力為0。

**Step 2：計算 DeMin（賣方壓力）**

$$DeMin_i = \begin{cases} Low_{i-1} - Low_i & \text{if } Low_i < Low_{i-1} \\ 0 & \text{if } Low_i \geq Low_{i-1} \end{cases}$$

當期低點比前一期低點低 → 差值就是賣方壓力；否則賣方壓力為0。

**Step 3：計算 DeMarker**

$$DeM_i = \frac{\sum_{j=i-N+1}^{i} DeMax_j}{\sum_{j=i-N+1}^{i} DeMax_j + \sum_{j=i-N+1}^{i} DeMin_j}$$

分子是過去N期買方壓力總和，分母是買方壓力+賣方壓力總和。結果一定在0到1之間。

**直覺解讀**：DeMarker = 買方壓力 /（買方壓力 + 賣方壓力），就是買方在過去N期中貢獻了多大比例的推動力。

### 計算範例

假設過去3天的數據（簡化N=3）：

**Day 1**：High=105, Low=98（前日High=102, Low=100）
- DeMax = 105 - 102 = 3
- DeMin = 100 - 98 = 2

**Day 2**：High=108, Low=99（前日High=105, Low=98）
- DeMax = 108 - 105 = 3
- DeMin = 98 - 99 = 0（低點沒有更低，賣方壓力=0）

**Day 3**：High=107, Low=96（前日High=108, Low=99）
- DeMax = 0（高點沒有更高）
- DeMin = 99 - 96 = 3

$$DeM = \frac{3+3+0}{(3+3+0)+(2+0+3)} = \frac{6}{11} \approx 0.545$$

0.545 接近中值，代表多空力量相對均衡。

## 判讀法則

### 基本判讀

- **DeM > 0.7**：超買區，買方力量過強，價格可能即將回檔
- **DeM < 0.3**：超賣區，賣方力量過強，價格可能即將反彈
- **0.3 ~ 0.7**：中性區，多空力量相對均衡

### 進階用法

**1. 背離判讀（最強訊號）**
- **頂背離**：價格創新高但 DeMarker 沒有創新高 → 買方力量減弱，注意反轉
- **底背離**：價格創新低但 DeMarker 沒有創新低 → 賣方力量減弱，注意反彈

**2. 趨勢確認**
- DeMarker 持續在0.5以上 → 多方主導
- DeMarker 持續在0.5以下 → 空方主導
- 0.5是多方與空方的分界線

**3. 與其他指標組合**
- DeMarker + [[MACD指標實戰判讀|MACD]]：DeMarker 超買/超賣 + MACD 背離確認 → 高勝率反轉訊號
- DeMarker + [[布林通道Bollinger-Bands三軌八型態|布林通道]]：DeMarker 超買 + 價格觸及布林上軌 → 強烈賣出訊號
- DeMarker + [[ADX趨勢強度過濾盤整|ADX]]：ADX>25（強趨勢）時忽略 DeMarker 超買/超賣，只看背離

### DeMarker vs RSI 比較

- **DeMarker** 比較高低點 → 反映價格推動力的方向
- **RSI** 比較漲跌幅 → 反映價格變動的幅度
- DeMarker 通常比 RSI 更平滑，訊號更少但更可靠
- RSI 在強趨勢中容易鈍化（[[RSI鈍化應對策略RSI-Passivation-Response|RSI鈍化]]），DeMarker 也有同樣問題

## 實戰策略

### 策略一：超買超賣均值回歸

1. DeMarker 跌破0.3 → 觀察是否有底背離
2. 確認背離後進場做多
3. 停損設在背離低點下方
4. DeMarker 回到0.5以上或出現頂背離時出場

### 策略二：趨勢中的回檔買點

1. 大趨勢向上（[[均線多頭排列與空頭排列|均線多頭排列]]）
2. 價格回檔，DeMarker 跌至0.3-0.4
3. DeMarker 開始回升 + 價格出現止跌K線（如[[鎚子線與射擊之星實戰判讀Hammer-and-Shooting-Star|鎚子線]]）
4. 進場做多，順著大趨勢操作

### 策略三：背離反轉交易

1. 等待 DeMarker 與價格出現背離
2. 使用較小時間框架確認進場點（[[多時間框架分析|多時間框架分析]]）
3. 進場後用[[ATR平均真實波幅-Average-True-Range|ATR]]設停損
4. 目標設在前一個結構高低點

## 台股實戰注意事項

- DeMarker 在台股的適用性與 RSI 類似，適合震盪市或趨勢中的回檔判讀
- 台股個股波動較大時，可考慮將參數從14調整為9（更靈敏）或21（更平滑）
- 搭配[[量價關係九種型態高低檔判讀|量價關係]]確認：DeMarker 超賣 + 縮量整理 → 更可靠的底部訊號
- 權值股如台積電、鴻海等大市值股票的 DeMarker 訊號比小型股更可靠

## DeMarker 的限制

1. **盤整失效**：跟所有震盪指標一樣，盤整市中 DeMarker 會在0.3-0.7間來回波動產生大量假訊號
2. **鈍化問題**：強趨勢中 DeMarker 可能長時間停留在超買或超賣區，類似 [[技術指標鈍化與對策|RSI鈍化]]
3. **落後性**：作為動量指標，DeMarker 本質上是落後指標，背離確認需要等待
4. **參數敏感**：不同N值對結果影響顯著，需根據標的特性調整

## Tom DeMark 指標家族

DeMarker 只是 Tom DeMark 指標體系的一員：

- **[[TD-Sequential序列指標Setup9Countdown13|TD Sequential]]**：計數9和13捕捉趨勢耗盡
- **TD Combo**：類似 TD Sequential 但計數規則不同
- **DeMarker**：連續震盪指標，本頁所述
- **TD Lines**：趨勢線系統
- **TD Points**：支撐壓力點系統

## 參考來源

- Tom DeMark, *The New Science of Technical Analysis* (1994)
- Tom DeMark, *DeMark on Day-Trading Options* (1999)
- MQL5 技術指標文檔：iDeMarker，參數為 symbol, period, ma_period（預設14）
- DeMarker 的0.3/0.7閾值與 MQL5 示例代碼中的 indicator_level1=0.3, indicator_level2=0.7 一致

## 實戰應用

（待補充）

## 注意事項

（待補充）

## 相關主題

（待補充）
