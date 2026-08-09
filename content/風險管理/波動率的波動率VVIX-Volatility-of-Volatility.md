---
title: 波動率的波動率VVIX Volatility of Volatility
date: 2026-06-28
category: "風險管理"
---

# 波動率的波動率 VVIX Volatility of Volatility

> VIX 衡量市場預期的波動率，VVIX 衡量 VIX 自己的波動率——波動率本身也會波動，而它的波動藏著更深的市場情緒密碼。

## 核心概念

**VVIX**（CBOE Volatility of Volatility Index）是 CBOE 計算的「VIX 的 VIX」——它衡量的是 VIX 期貨 30 天遠期價格的預期波動率。簡單說：

- **VIX** = S&P 500 選擇權隱含的 30 天預期波動率
- **VVIX** = VIX 選擇權隱含的 30 天預期波動率

VIX 是「恐懼指數」，VVIX 就是「恐懼的恐懼指數」——衡量市場對「波動率即將劇烈變動」的預期程度。

### VIX 的本質回顧

[[風險管理/VIX恐慌指數實戰判讀|VIX 恐慌指數實戰判讀]]的重點：

- VIX = S&P 500 index options 隱含的 30 天年化標準差
- 公式：VIX = √(風險中性預期變異數)，由 out-of-the-money call 和 put 的加權平均計算
- VIX 不能直接買賣，只能透過 VIX 期貨、選擇權、ETF/ETN 間接交易
- VIX 期貨 ETF 與 VIX 指數本身的相關性很差，尤其 VIX 在變動時

### VVIX 的計算邏輯

VVIX 用與 VIX 相同的方法論，但底層資產從 S&P 500 選擇權換成 VIX 選擇權：

```
VVIX = √(VIX 選擇權隱含的 30 天預期變異數)
```

這意味著 VVIX 衡量的是「市場認為 VIX 在未來 30 天會有多波動」。

### VVIX vs VIX 的關係

| 情境 | VIX | VVIX | 意義 |
|------|-----|------|------|
| 市場平靜 | 低（< 15） | 低（< 80） | 沒人擔心，也沒人擔心會開始擔心 |
| 市場開始緊張 | 上升中 | 急升 | 波動率本身在劇烈變動 |
| 恐慌高峰 | 極高（> 40） | 極高（> 150） | 大家在恐慌，而且恐慌程度在暴衝 |
| 恐慌消退 | 下降中 | 下降但可能高於平時 | 波動率回落，但回落過程本身也波動 |

關鍵特徵：
- **VVIX 通常高於 VIX**：因為 VIX 本身比 S&P 500 更波動，它的選擇權也更貴
- **VVIX 對 VIX 的變化敏感**：VIX 急升時 VVIX 往往飆更高，因為市場不確定波動率會衝到哪裡
- **VVIX 是 VIX 選擇權定價的核心**：交易 VIX 選擇權就是在交易 VVIX

## 實戰應用

### 1. 判斷「波動率體制轉換」

VIX 從低檔急升時，VVIX 往往領先反應。當你看到 VVIX �始拉升但 VIX 還沒大動，可能預示波動率體制即將從「低波動平靜期」轉向「高波動動盪期」。

這對 [[風險管理/波動率目標策略Volatility-Targeting|波動率目標策略]]很重要——如果你的策略依賴波動率體制判斷，VVIX 是一個比 VIX 更前瞻的訊號。

### 2. VIX 選擇權交易的定價參考

如果你交易 VIX 選擇權（[[操作策略/選擇權組合策略|選擇權組合策略]]），VVIX 就是你的「隱含波動率」：
- VVIX 高 → VIX 選擇權貴 → 賣方有利
- VVIX 低 → VIX 選擇權便宜 → 買方有利

這跟普通股票選擇權看 [[技術分析/隱含波動率IV判讀|IV 判讀]]的邏輯一樣，只是標的從股票變成 VIX 本身。

### 3. 尾部風險預警

VVIX 飆高是 [[風險管理/黑天鵝事件與尾部風險基礎Black-Swan-and-Tail-Risk-Fundamentals|尾部風險]]的前兆訊號之一。當 VVIX 突然從 80 跳到 130+，代表市場開始為「波動率暴衝」定價——這通常是某種尾部事件的前奏。

搭配觀察：
- [[風險管理/波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]]（VRP）是否收窄
- [[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew|波動率偏態]]是否變陡
- VIX 期貨期限結構是否轉為 backwardation

### 4. 波動率套利進階

[[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利]]的進階玩法涉及 VVIX：
- 做 VVIX 期貨與 VIX 期貨的價差交易
- 用 VVIX 判斷 VIX 選擇權的 Vega 是否被高估或低估
- VVIX 與 VIX 的比值可作為「波動率的波動率風險溢價」指標

### 5. 多資產波動率監控面板

把 VVIX 納入你的 [[風險管理/風險儀表板與每日風控檢查Risk-Dashboard|風險儀表板]]，形成三層波動率監控：
- 第一層：個股 IV（看單一標的波動預期）
- 第二層：VIX（看大盤波動預期）
- 第三層：VVIX（看波動率本身的波動預期）

三層同時拉升 = 市場進入極端不確定狀態。

## 注意事項

- **VVIX 比 VIX 更難取得**：不是所有看盤軟體都有 VVIX 即時數據，CBOE 官網有
- **VIX 期貨 ETF ≠ VIX**：VIX ETF（如 UVXY、VXX）與 VIX 指數相關性差，VVIX 的可交易性更差，幾乎只能透過 VIX 選擇權間接操作
- **VVIX 有均值回歸特性**：跟 VIX 一樣，VVIX 長期會回歸均值，但「回歸時間」不確定，不要因為 VVIX 高就做空它
- **台股沒有直接對應指標**：台指 VIX 有，但沒有「台指 VIX 的 VIX」。可用 VIX 期貨本身的已實現波動率作為代理
- **VVIX 高時 VIX 選擇權定價風險大**：賣 VIX 選擇權在 VVIX 高時權利金豐厚，但 Gamma 風險也最大——[[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|Greeks 進階判讀]]是必修

## 相關主題

- [[風險管理/VIX恐慌指數實戰判讀|VIX 恐慌指數實戰判讀]]
- [[風險管理/波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]]
- [[風險管理/波動率目標策略Volatility-Targeting|波動率目標策略]]
- [[風險管理/波動率拖累與槓桿ETF損耗Volatility-Drag-and-Leveraged-ETF-Decay|波動率拖累與槓桿 ETF 損耗]]
- [[技術分析/隱含波動率IV與歷史波動率HV實戰判讀|隱含波動率 IV 與歷史波動率 HV 實戰判讀]]
- [[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew|波動率微笑曲線與偏態]]
- [[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利與 Delta-Neutral 策略]]
- [[操作策略/波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution|波動率期限結構與曲面演化]]
- [[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|選擇權 Greeks 進階組合判讀]]
- [[風險管理/黑天鵝事件與尾部風險基礎Black-Swan-and-Tail-Risk-Fundamentals|黑天鵝事件與尾部風險基礎]]
- [[風險管理/風險儀表板與每日風控檢查Risk-Dashboard|風險儀表板]]

## 來源

- [VIX - Wikipedia](https://en.wikipedia.org/wiki/VIX)
- CBOE VIX & VVIX 白皮書
- Brenner, M. & Galai, D. (1989). "New Financial Instruments for Hedging Changes in Volatility"