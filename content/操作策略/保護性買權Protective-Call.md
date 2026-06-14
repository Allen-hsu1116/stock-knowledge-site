---
category: "操作策略"
title: 保護性買權 Protective Call
date: 2026-06-04
---

# 保護性買權 Protective Call

> 持有空頭部位時買進買權做保險——空方版本的Protective Put，限制上行風險的對沖工具

## 核心概念

保護性買權（Protective Call）= **持有空頭部位（Short Stock 或 Short Put）+ 買進買權（Long Call）**

本質：你做空或看空，但怕行情反轉大漲，用買Call當保險鎖住上行風險。

- 你有空頭曝險，買Call讓你有權在特定價格買回股票平倉
- 權利金是你的保險費
- 與 [[保護性賣權與Collar避險策略Protective-Put-and-Collar|風險管理/保護性賣權與Collar避險策略Protective-Put-and-Collar]] 是鏡像關係：Protective Put 保護多方，Protective Call 保護空方

### 損益結構

以融券放空為例（Short Stock + Long Call）：

```
股價 ≤ 履約價：獲利 = (放空價 - 股價) - 權利金
股價 > 履約價：最大虧損 = (履約價 - 放空價) + 權利金
```

**關鍵數字**：
- 損益兩平 = 放空價 - 權利金
- 最大虧損 = (履約價 - 放空價) + 權利金（股價大漲時）
- 最大獲利 = 放空價 - 權利金（股價跌到0的理論極限）

## 實戰應用

### 一、為什麼需要 Protective Call？

**問題**：融券放空風險無限，理論上股價可以無限制上漲
- 沒有保護：軋空時血本無歸
- 有保護：最大虧損被鎖定

**實例**：融券放空某股 100 元
- 不做保護：股價漲到130虧30%，漲到150虧50%，沒有上限
- 買進 110 Call 權利金 5 元：最大虧損 = (110-100)+5 = 15 元（15%）

這15%就是你願意為「睡得著覺」付的保險費。

### 二、三種應用情境

#### 情境一：融券放空保險

最直接的用法。放空同時買Call做保險，組合效果近似Bear Put Spread。

**比較**：
| 策略 | 最大虧損 | 最大獲利 | 成本 |
|------|----------|----------|------|
| 純融券 | 無限 | 放空價（股價歸零） | 利息+保證金 |
| 融券 + Protective Call | 固定 | 放空價 - 履約價差 - 權利金 | 利息+保證金+權利金 |
| Bear Put Spread | 固定 | 固定 | 只有權利金 |

#### 情境二：賣出Put 的上方保護

賣出Put（看不跌）但怕大漲時被逼回補，買Call鎖住上方風險。

- 賣Put + 買Call = Synthetic Short Put with Cap
- 類似 Bull Put Spread 但用Call做上限保護
- 適合看不大漲但想收權利金的賣方

#### 情境三：期貨空單保險

持有台指期空單，買進台指Call做保險：
- 小台空單 + 買小台Call = 風險有限
- 保險成本 = Call 權利金
- 比設停損更精確——停損可能滑價，Call的保護是合約保證的

### 三、履約價選擇

| 履約價 | 權利金 | 保護力 | 獲利空間 | 適合情境 |
|--------|--------|--------|----------|----------|
| 價平（ATM） | 貴 | 強 | 小 | 極度怕漲 |
| 溫價外（OTM 3-5%） | 中 | 中 | 中 | 一般對沖 |
| 深價外（OTM 10%+） | 便宜 | 弱 | 大 | 只防黑天鵝 |

**實戰選擇**：OTM 3-5% 最平衡——保護力足夠且不會吃掉太多獲利。

### 四、到期日選擇

| 到期日 | 權利金 | 保護時段 | 彈性 |
|--------|--------|----------|------|
| 短期（1-2週） | 少 | 短 | 需頻繁續保 |
| 中期（1個月） | 中 | 中 | 主流選擇 |
| 長期（3個月+） | 多 | 長 | 長期避險 |

**實戰建議**：與空頭部位預期持有時間一致。如果你的空單打算持有一個月，就買一個月到期的Call做保險。

### 五、Protective Call vs 停損單

| 比較 | Protective Call | 停損單 |
|------|----------------|--------|
| 保證 | 合約保證，不會滑價 | 可能滑價，跳空時無效 |
| 成本 | 權利金（確定成本） | 無直接成本 |
| 獲利影響 | 不論漲跌都要付權利金 | 只有觸發時才影響 |
| 跳空保護 | ✅ 有效 | ❌ 跳空缺口無保護 |
| 適合 | 怕跳空、怕軋空 | 正常波動時成本更低 |

**最差情境**：隔夜大利多跳空開高
- 停損單：開盤直接跳空超過停損價，以最差價格成交
- Protective Call：不論跳空多大，最多虧到履約價為止

這就是 Protective Call 的價值——在你最需要保護的時候不會失效。

### 六、Collar 策略中的 Protective Call

Collar = Short Stock + Protective Put（保護下跌？不，保護上漲）+ Covered Call... 

更準確地說，空方 Collor = 融券放空 + 買Call保護上行 + 賣Put降低保險成本。這就是 [[保護性賣權與Collar避險策略Protective-Put-and-Collar|風險管理/保護性賣權與Collar避險策略Protective-Put-and-Collar]] 在空方情境的應用。

## 注意事項

### 1. 保險費是沉沒成本

- 股價下跌（方向看對），權利金仍然歸零
- 保險的本質就是：沒出事保費白付，出事保費超值
- 不要因為「上次買保險都沒用到」就不買——黑天鵝不會事先通知

### 2. 權利金可能很高

- 高波動時期Call權利金暴增，保護成本可能佔預期獲利很大比例
- IV > 30% 時 Protective Call 的成本效率下降
- 解法：用深價外Call降低成本，接受較高扣除額

### 3. 部位管理複雜度

- 融券 + Call 到期日可能不同步
- Call 到期後需決定續保或裸露
- 建議設定系統化的續保SOP

### 4. 時間衰減是敵人

- Call 的時間價值每天都在流失
- 如果空單長期持有，每個月都要付保險費
- 長期累積的保險成本可能吃掉大部分空單利潤

### 5. 不要用 Protective Call 取代紮實的停損紀律

- Protective Call 是補充工具，不是停損的替代品
- 有了保險就不設停損 = 買了汽車保險就不繫安全帶
- 最佳實踐：停損 + Protective Call 雙重保護

### 6. 與 Synthetic Short 的關係

- Short Stock + Long Call = Synthetic Short Put
- 本質上你在做一個「賣出Put」的合成部位
- 如果這不是你原本的意圖，需要重新檢視策略邏輯

## 相關主題

- [[保護性賣權與Collar避險策略Protective-Put-and-Collar|風險管理/保護性賣權與Collar避險策略Protective-Put-and-Collar]] - 多方版本的保險策略，Protective Call的鏡像
- [[融券放空策略與軋空判讀實戰Short-Selling-Strategy-and-Short-Squeeze|操作策略/融券放空策略與軋空判讀實戰Short-Selling-Strategy-and-Short-Squeeze]] - 放空策略最需要Protective Call
- [[選擇權四大基本策略|操作策略/選擇權四大基本策略]] - Long Call是四大基本策略之一
- [[選擇權Greeks希臘字母|操作策略/選擇權Greeks希臘字母]] - 理解Gamma和Theta對保險成本的影響
- [[垂直價差Vertical-Spread牛市價差與熊市價差|操作策略/垂直價差Vertical-Spread牛市價差與熊市價差]] - Bear Put Spread是Protective Call的替代結構
- [[黑天鵝事件與尾部風險基礎Black-Swan-and-Tail-Risk-Fundamentals|風險管理/黑天鵝事件與尾部風險基礎Black-Swan-and-Tail-Risk-Fundamentals]] - 黑天鵝事件是買保險的最佳理由
- [[跳空缺口風險Gap-Risk|風險管理/跳空缺口風險Gap-Risk]] - Protective Call防跳空是最大價值

## 來源

- 綜合整理自知識庫現有選擇權與風險管理策略資料