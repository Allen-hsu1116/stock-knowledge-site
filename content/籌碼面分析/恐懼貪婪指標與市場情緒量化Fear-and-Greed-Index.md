---
category: "籌碼面分析"
title: "恐懼貪婪指標與市場情緒量化 Fear and Greed Index"
date: 2026-07-01
---

# 恐懼貪婪指標與市場情緒量化 Fear and Greed Index

> 市場在恐懼與貪婪之間擺盪——巴菲特說別人恐懼我貪婪、別人貪婪我恐懼，但「恐懼」和「貪婪」能不能量化？CNN Fear & Greed Index 用七個指標把市場情緒變成一個0-100的數字。

## 核心概念

**恐懼貪婪指標（Fear & Greed Index）** 是 CNN Business 開發的市場情緒綜合指標，將多個市場情緒指標合成為單一讀數，範圍 0-100：

- **0-24**：Extreme Fear（極度恐懼）
- **25-49**：Fear（恐懼）
- **50**：Neutral（中性）
- **51-74**：Greed（貪婪）
- **75-100**：Extreme Greed（極度貪婪）

核心邏輯是逆向思維：**極度恐懼時買進、極度貪婪時賣出**。

## CNN Fear & Greed Index 七大組成指標

### 1. 價格動量（Price Momentum）

- 標普500 vs 125日均線
- 價格在均線上方=貪婪，下方=恐懼
- 等同於 [[技術分析/乖離率BIAS|乖離率]] 的概念

### 2. 股價強度（Stock Price Strength）

- 紐約證交所創52週新高 vs 新低的股票數量比
- 新高多於新低=貪婪
- 搭配 [[技術分析/市場寬度與漲跌家數比進階判讀Market-Breadth-and-Advance-Decline-Ratio-Advanced|市場寬度]] 判讀

### 3. 股價廣度（Stock Price Breadth）

- 上漲股 vs 下跌股的成交量比（McClellan Volume Summation Index）
- 上漲量持續大於下跌量=貪婪
- 見 [[技術分析/McClellan-Oscillator麥克萊倫震盪指標|McClellan Oscillator]]

### 4. 賣權買權比（Put and Call Options）

- Put/Call Ratio 的5天和10天移動平均
- PCR高=散戶偏空=恐懼（逆向看多）
- PCR低=散戶偏多=貪婪（逆向看空）
- 詳見 [[籌碼面分析/Put-Call-Ratio選擇權籌碼|PCR選擇權籌碼]]

### 5. 垃圾債需求（Junk Bond Demand）

- 投資級 vs 高收益債的利差
- 利差縮小=市場追求風險=貪婪
- 利差擴大=市場規避風險=恐懼
- 與 [[基本面分析/信用評等與公司債違約風險判讀Credit-Rating-and-Default-Risk|信用風險]] 相關

### 6. 市場波動率（Market Volatility）

- VIX 恐慌指數的50日均線 vs 當前值
- VIX低於均線=貪婪，高於均線=恐懼
- 見 [[風險管理/VIX恐慌指數實戰判讀|VIX實戰判讀]]
- 搭配 [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|VVIX]] 看更深層

### 7. 避風港需求（Safe Haven Demand）

- 股票 vs 公債的報酬差（20日）
- 股票報酬優於債券=貪婪
- 債券報酬優於股票=恐懼
- 與 [[操作策略/跨市場分析Intermarket-Analysis|跨市場分析]] 的股債關係一致

## 台股版情緒量化指標

CNN Fear & Greed 是美股指標，台股投資人需要建立自己的情緒儀表板：

### 台股情緒指標組合

**1. VIX台指選擇權波動率指數**
- 均值約19.5
- <15：過熱（極度貪婪）
- 15-20：正常
- 20-30：擔憂
- 30-40：恐慌
- >40：極度恐慌（買進訊號）

**2. 融資餘額變化**
- 融資快速攀升=散戶貪婪
- 融資大幅減少=散戶恐懼
- 見 [[籌碼面分析/融資維持率大盤判讀與市場恐慌反轉訊號|融資維持率判讀]]

**3. 外資期貨未平倉**
- 外資期空歷史高=機構恐懼（但可能是避險非看空）
- 見 [[籌碼面分析/外資現貨期貨部位不一致判讀|外資部位判讀]]

**4. 騰落指數ADL**
- ADL與大盤背離=情緒與價格背離
- 見 [[技術分析/騰落指數ADL判讀|ADL判讀]]

**5. 當沖比率**
- 當沖比異常高=市場過熱
- 見 [[籌碼面分析/當沖成交比重與市場過熱判讀Day-Trading-Ratio-and-Market-Overheating|當沖比重]]

**6. Put/Call Ratio**
- PCR極端值是散戶情緒的反向指標
- 見 [[籌碼面分析/Put-Call-Ratio選擇權籌碼|PCR選擇權籌碼]]

## 實戰應用

### 策略一：極端值逆向操作

- **極度恐懼（<25）**：分批進場，買進市值型ETF或高品質個股
- **極度貪婪（>75）**：提高現金比重，減碼高估值標的
- **注意**：極端值可維持很長時間，不要試圖精準抄底逃頂

### 策略二：情緒趨勢確認

- 恐懼指標從極度恐懼開始回升=底部確認訊號
- 貪婪指標從極度貪婪開始回落=頭部預警
- 重點是**轉折方向**而非絕對值

### 策略三：多指標共振確認

- 單一情緒指標容易誤判，至少3個以上同時發出極端訊號才可靠
- 例如：VIX>30 + 融資大減 + PCR極端高 = 恐慌底部
- 搭配 [[技術分析/底部訊號綜合判讀Bottom-Signal-Confluence|底部訊號綜合判讀]]

### 策略四：情緒指標當濾網不當進出場訊號

- 情緒指標單獨解釋力有限（約3-6%），類似季節性
- 最佳用法是當「濾網」：基本面/技術面發出訊號後，用情緒指標確認或過濾
- 股癌筆記中提到：「用CNN恐懼貪婪指標做交易的人每天最高殺低，交易頻率太高根本抱不住波段」

## 注意事項

### 情緒指標的陷阱

- **極端可以更極端**：極度貪婪可以維持數月甚至數年
- **指標鈍化**：長期牛市中指標長期偏高，失去預警功能
- **市場結構變化**：ETF被動買盤、量化交易改變了情緒指標的有效性
- **日內波動大**：CNN指標日內波動可能很大，看趨勢不看單日數值
- **台股不適用美國指標**：CNN指標反映美股情緒，台股有自己的情緒週期

### 2026年台股情緒快照

- 融資突破6000億（歷史新高）→ 極度貪婪訊號
- 外資期空8.3萬口 → 機構端恐懼
- VIX未極端飆高 → 市場未進入恐慌
- 當沖比偏高 → 過熱特徵
- 結論：散戶極度貪婪、機構避險水位高，情緒分化本身就是風險訊號

## 相關主題

- [[風險管理/VIX恐慌指數實戰判讀]] — VIX情緒溫度計
- [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility]] — VIX的波動率
- [[籌碼面分析/Put-Call-Ratio選擇權籌碼]] — PCR散戶情緒反向指標
- [[籌碼面分析/融資維持率大盤判讀與市場恐慌反轉訊號]] — 融資維持率反轉
- [[籌碼面分析/當沖成交比重與市場過熱判讀Day-Trading-Ratio-and-Market-Overheating]] — 當沖過熱判讀
- [[技術分析/騰落指數ADL判讀]] — 騰落指數背離
- [[技術分析/市場寬度與漲跌家數比進階判讀Market-Breadth-and-Advance-Decline-Ratio-Advanced]] — 市場寬度
- [[技術分析/底部訊號綜合判讀Bottom-Signal-Confluence]] — 底部訊號綜合判讀
- [[風險管理/市場情緒週期與反脆弱交易系統Market-Sentiment-Cycle-and-Antifragile-System]] — 情緒週期
- [[操作策略/跨市場分析Intermarket-Analysis]] — 跨市場情緒傳導
- [[風險管理/交易情緒控制與紀律心法Emotional-Control-and-Discipline-Mindset]] — 個人情緒管理
- [[基本面分析/信用循環與明斯基時刻Credit-Cycle-and-Minsky-Moment]] — 信用循環與情緒
- [[風險管理/後悔厭惡與決策理論Regret-Aversion]] — 情緒偏誤

## 來源

- CNN Business: [Fear & Greed Index](https://edition.cnn.com/markets/fear-and-greed)
- Wikipedia: [Fear and Greed Index](https://en.wikipedia.org/wiki/Fear_and_Greed_Index)（尚無獨立條目）
- 股癌 EP673 筆記中對CNN恐懼貪婪指標的評論