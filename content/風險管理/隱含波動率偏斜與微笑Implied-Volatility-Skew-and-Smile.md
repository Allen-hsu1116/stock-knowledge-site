---
title: "隱含波動率偏斜與微笑 Implied Volatility Skink and Smile"
category: "風險管理"
---

# 隱含波動率偏斜與微笑 Implied Volatility Skink and Smile

> 選擇權市場的隱含波動率隨履約價變化形成「微笑」或「偏斜」曲線，是市場對肥尾與崩盤風險的定價訊號。

## 核心概念

Black-Scholes 模型假設波動率是常數，但實際市場上同一到期日的選擇權，不同履約價算出來的隱含波動率不一樣。把隱含波動率對履約價畫圖，本來應該是一條水平線，結果出現了彎曲的形狀——這就是波動率微笑（Volatility Smile）或偏斜（Volatility Skew）。

### Smile vs Skew 的差異

- **波動率微笑（Volatility Smile）**：圖形兩端上翹，像笑臉。常見於外匯選擇權市場——深價外（OTM）的 Call 和 Put 隱含波動率都偏高，市場同時擔心大漲和大跌
- **波動率偏斜（Volatility Skew）**：圖形向下傾斜，左高右低，像「半個笑臉」或「皺眉」。常見於股票市場——價外 Put 的隱含波動率遠高於價外 Call，市場更怕大跌
- **Smirk**：偏斜的別名，指不對稱的微笑

### 1987 股災是分水嶺

美國股票選擇權在 1987 年黑色星期一股災之前幾乎沒有波動率偏斜，之後才出現明顯的左高右低偏斜。原因是投資人重新評估了「崩盤」的機率，開始願意用更高價格買價外 Put 做保護。這直接證明了 BS 模型假設的對數常態分配（log-normal）與現實不符——實際報酬分配有肥尾（kurtosis）和偏態（skew）。

### 偏斜的成因

- **投資型偏斜（Investment Skew）**：來自結構性因素，例如機構投資人常態性買 Put 做保護性避險（protective put），推高價外 Put 的 IV
- **需求型偏斜（Demand Skew）**：來自集中的買賣力量，例如投機客大量買特定履約價的選擇權，純粹是供需推動

## 市場實務公式

市場做市商用 Risk Reversal 和 Butterfly 來描述偏斜形狀：

**Call_x = ATM + 0.5 × RR_x + Fly_x**
**Put_x = ATM - 0.5 × RR_x + Fly_x**

- **ATM**：價平選擇權的隱含波動率
- **RR_x（Risk Reversal）**= Call_x - Put_x：衡量偏斜程度。RR > 0 代表 Call IV > Put IV（看多偏斜），RR < 0 代表 Put IV > Call IV（看空偏斜，股票市場常見）
- **Fly_x（Butterfly）**= 0.5 × (Call_x + Put_x) - ATM：衡量微笑彎曲程度（峰度）。Fly 越大，兩端翹越高

Risk Reversal 是 [[Risk-Reversal風險逆轉策略|風險逆轉策略]] 的定價基礎：做多 x% delta Call、做空 x% delta Put。Butterfly 則對應 [[蝶式價差Butterfly-Spread|蝶式價差]] 的定價。

## 期限結構與波動率曲面

### 期限結構（Term Structure）
同一履約價、不同到期日的 IV 也不同：
- **事件驅動**：財報公布前 IV 飆高，公布後崩跌。短期選擇權的 IV 波動（vol of vol）比長期大得多
- **商品期貨**：收成預報公布前 IV 飆高
- **公債期貨**：FOMC 會議前 IV 飆高

### 波動率曲面（Implied Volatility Surface）
把 IV 對履約價和到期日同時畫成 3D 曲面：
- z 軸 = 隱含波動率
- y 軸 = 履約價
- x 軸 = 到期天數

曲面的形狀同時包含偏斜和期限結構的資訊。

### 演化：Sticky
- **Sticky Strike**：價格變動時，同一絕對履約價的 IV 不變
- **Sticky Delta（Sticky Moneyness）**：價格變動時，同一 moneyness（價內外程度）的 IV 不變

例：股價從 100 漲到 120。Sticky Strike 認為 120 履約價的 IV 等於它之前的 IV（本來是價外現在變價平）。Sticky Delta 認為 120 履約價的 IV 等於之前 100 履約價的 IV（因為兩者都是當時的價平）。

實務上，短期選擇權偏向 Sticky Delta，長期偏向 Sticky Strike。

## 實戰應用

**判讀市場情緒**：
- 偏斜加劇（Put IV 相對 Call IV 上升）→ 市場恐慌加劇，資金在搶 Put 做保護
- 偏斜收斂 → 恐慌消退或市場轉樂觀
- 微笑曲線變平 → 市場對尾部風險定價下降
- 微笑曲線變深 → 市場預期極端波動

**台股應用**：台指選擇權的偏斜是市場情緒指標。觀察 10% delta Put 與 10% delta Call 的 IV 差（即 10% RR），可以量化「市场偏空」程度。當 RR 擴大到極端值時，往往是底部訊號（恐慌到頂）。

**選擇權定價與套利**：
- 偏斜形狀異常時可能存在套利機會
- 隱含分配可以從曲面反推，用來定價奇異選擇權
- [[選擇權Greeks風險判讀|Greeks]] 在非平面的 IV 曲面上需要調整

**壓力測試**：假設 IV 曲面變平或變陡，評估部位損益變化，是選擇權部位風控的核心。

## 注意事項

- **BS 模型缺陷的表面證據**：微笑/偏斜本身就是 BS 假設錯誤的證據。用 BS 算 IV 只是把市場價格「重新標示」成波動率，不代表真實的波動率結構
- **流動性問題**：深價外選擇權的 IV 可能因流動性不足而失真，分析偏斜時要注意成交量和 bid-ask spread
- **模型選擇**：要正確定價偏斜，需要隨機波動率模型（Heston、SABR）或局部波動率模型（Dupire），BS 做不到
- **微笑不等於套利**：IV 曲面彎曲不一定有套利機會，它反映的是市場對未來分配的真實預期

## 相關主題

- [[選擇權Greeks風險判讀]] — 選擇權風險判讀基礎
- [[保護性賣權與Collar避險策略Protective-Put-and-Collar]] — 波動率偏斜直接影響 Put 保護成本
- [[Risk-Reversal風險逆轉策略]] — Risk Reversal 是偏斜的定價基礎
- [[蝶式價差Butterfly-Spread]] — Butterfly 衡量微笑彎曲度
- [[VIX恐慌指數實戰判讀]] — VIX 是 S&P 500 選擇權 IV 的整合指標
- [[波動率風險溢價Volatility-Risk-Premium]] — IV 和實現波動率的差就是波動率風險溢價
- [[波動率的波動率VVIX-Volatility-of-Volatility]] — VIX 選擇權本身的 IV
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]] — 利用 IV 偏斜的套利策略
- [[方差交換與波動率衍生品Variance-Swap-and-Volatility-Derivatives]] — 波動率衍生品的偏斜定價
- [[黑天鵝事件與尾部風險基礎Black-Swan-and-Tail-Risk-Fundamentals]] — 偏斜是市場對黑天鵝的定價
- [[極端值理論EVT量化肥尾風險]] — 肥尾的量化基礎
- [[波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution]] — 期限結構專論

## 來源

- [隱含波動率偏斜與微笑](../../raw/2026-08-07/隱含波動率偏斜與微笑Implied-Volatility-Skink-and-Smile.md)
- Wikipedia: Volatility smile
- Natenberg, S. (2015). Option Volatility and Pricing, 2nd ed. McGraw-Hill