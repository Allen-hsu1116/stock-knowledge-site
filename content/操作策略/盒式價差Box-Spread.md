---
title: "盒式價差 Box Spread"
tags: [操作策略, 選擇權, 套利, 無風險策略, Put-Call Parity]
created: 2026-07-06
---

# 盒式價差 Box Spread

> 四腿選擇權組合創造確定無風險報酬——用牛市買權價差+熊市賣權價差鎖定固定收益，本質是Put-Call Parity的套利執行，機構用來替代國庫券借貸，散戶玩美式選擇權曾因此虠損57,000美元。

## 核心概念

**Box Spread（盒式價差）**是由四個選擇權部位組成的組合策略，其到期報酬在任何股價下都是固定的——等於兩個履約價的差額。這使得 Box Spread 成為一個**無風險（delta neutral）的利率部位**。

### 組成結構

一個 Long Box Spread 由四個腿組成（假設 K₁ < K₂）：

1. **買入 Call @ K₁**（Long bull call spread 的多頭腿）
2. **賣出 Call @ K₂**（Long bull call spread 的空頭腿）
3. **買入 Put @ K₂**（Long bear put spread 的多頭腿）
4. **賣出 Put @ K₁**（Long bear put spread 的空頭腿）

到期時不論股價在哪裡，報酬恆為 K₂ - K₁。

### 為什麼叫 Box

四個選擇權的報價在選擇權報價表上形成一個矩形（box）——Call 欄和 Put 欄各兩個履約價格，正好四個角。

## 無風險報酬的數學原理

### Put-Call Parity 基礎

Put-Call Parity 公式：

$$c - p = S - K \cdot e^{-rT}$$

在兩個不同履約價 K₁ 和 K₂ 下：

$$c_1 - p_1 = S - K_1 \cdot e^{-rT}$$
$$c_2 - p_2 = S - K_2 \cdot e^{-rT}$$

兩式相減（消掉 S）：

$$(c_1 - c_2) - (p_2 - p_1) = (K_2 - K_1) \cdot e^{-rT}$$

左邊就是 Long Box Spread 的淨成本，右邊是固定報酬的現值。

### 套利邏輯

- 如果 **淨成本 < (K₂ - K₁) × e^(-rT)** → 買入 Box Spread（Long Box），鎖定無風險利潤
- 如果 **淨成本 > (K₂ - K₁) × e^(-rT)** → 賣出 Box Spread（Short Box），鎖定無風險利潤
- 在高效市場中，套利空間通常小於交易成本

### 三種視角看 Box Spread

**水平視角**：
- Long bull call spread（K₁/K₂）+ Long bear put spread（K₁/K₂）

**垂直視角**：
- Long synthetic stock @ K₁ + Short synthetic stock @ K₂

**對角視角**：
- Long strangle @ K₁/K₂ + Short strangle @ K₁/K₂

## 計算範例

### 基本範例

假設某股票現價 $100，3個月到期，利率8%年化，波動率30%：

- K₁ = $90：Call = $13.10, Put = $1.65
- K₂ = $110：Call = $3.05, Put = $10.90

**Long Box Spread 淨成本**：
- 買 Call@90：-$13.10
- 賣 Call@110：+$3.05
- 買 Put@110：-$10.90
- 賣 Put@90：+$1.65
- 淨成本 = 13.10 - 3.05 + 10.90 - 1.65 = **$19.30**

**到期報酬** = K₂ - K₁ = $110 - $90 = **$20.00**（不論股價在哪）

**理論公允價格** = $20 × e^(-0.08×0.25) = $20 × 0.9802 = **$19.60**

**名義利潤** = $19.60 - $19.30 = $0.30（在無交易成本下）

### 到期報酬驗證

| 股價區間 | Call@90 | Call@110 | Put@110 | Put@90 | 總計 |
|---------|---------|----------|---------|--------|------|
| S < 90 | 0 | 0 | 110-S | -(90-S) | 20 |
| 90 < S < 110 | S-90 | 0 | 110-S | 0 | 20 |
| S > 110 | S-90 | -(S-110) | 0 | 0 | 20 |

**任何股價下報酬都是 $20**——這就是「literally cannot go tits up」的原因（但有前提，見下文）。

## 機構用法

### 1. 借貸工具

**Short Box Spread = 借錢**：
- 賣出 Box Spread 收取權利金（如收到 $19.30）
- 到期支付固定金額（如 $20.00）
- 差額就是利息成本（$0.70，3個月利率約1.46%年化）

機構用 SPX（S&P 500 指數選擇權）Box Spread 借貸，利率通常接近國庫券利率，且有 OCC（Options Clearing Corporation）擔保。SPX Box Spread 市場日均名義成交量超過 $9 億。

**稅務優勢**：在美國，Box Spread 借貸的利息被歸類為交易損失，可依 IRS Sec 1256 抵扣資本利得。

### 2. 現金管理工具

**Long Box Spread = 借出/投資**：
- 買入 Box Spread 支付權利金（如支付 $19.30）
- 到期收取固定金額（如 $20.00）
- 差額是利息收入

**BOXX ETF**（2022年上市）：用 SPX 指數選擇權構建 Box Spread，複製短期國庫券報酬，提供潛在稅務效率優勢。

### 3. 無風險利率基準

Box Spread 的隱含利率可作為市場無風險利率的替代指標。與國庫券利率的差距（convenience yield）約 35 基點，金融不穩定時差距擴大。

## 散戶陷阱：Robinhood 事件

2019年1月，Reddit /r/WallStreetBets 一名用戶用 $5,000 本金在 Robinhood 上做了 Box Spread，宣稱「literally cannot go tits up」，結果虧損超過 $57,000。

### 為什麼會虧

1. **美式選擇權**：他使用的是美式選擇權（可提前行使），不是歐式
2. **提前行使風險**：Box Spread 的某一腿被提前行使，整個組合失去對沖
3. **裸部位曝險**：被行使後的裸部位面臨無限風險（暴露達 $212,500）
4. **Robinhood 保證金不足**：平台未正確計算組合保證金，允許過度槓桿

### 教訓

- **只用歐式選擇權做 Box Spread**——到期前不可行使
- **不是真正無風險**——有提前行使風險、流動性風險、保證金風險
- **手續費吞噬利潤**——四腿交易的手續費可能吃掉微薄套利空間（故又稱「alligator spread」）
- Robinhood 事件後禁止平台用戶開 Box Spread

## 台股適用性分析

### 台指選擇權

台灣期貨交易所的台指選擇權為**歐式選擇權**（到期前不可行使），理論上適合 Box Spread：

- **優勢**：無提前行使風險、結算保證機制完善
- **劣勢**：
  - 流動性不足——遠月履約價的報價價差大，四腿同時成交困難
  - 手續費成本——四腿各需手續費，加上滑價，套利空間幾乎為零
  - 交易稅——買賣權利金各課稅，進一步壓縮利潤
  - 保證金——賣出腿需要保證金，資金效率低

### 實務結論

- 散戶在台股做 Box Spread 套利**幾乎不可能獲利**——手續費+滑價+保證金成本遠大於套利空間
- 機構或大戶可能透過演算法交易在接近結算時捕捉微小套利
- **教育價值大於實戰價值**——理解 Box Spread 等於理解 Put-Call Parity，這是選擇權定價的基石

## 與其他選擇權策略的關係

- [[選擇權四大基本策略]]：Box Spread 由四個基本策略組合而成
- [[跨式Straddle與勒式Strangle|Straddle/Strangle]]：Box Spread 可視為 Long Strangle + Short Strangle
- [[比率價差Ratio-Spread|比率價差]]：不對稱腿數的策略，與 Box 的對稱結構不同
- [[鐵蝴蝶Iron-Butterfly|鐵蝴蝶]]：同履約價的 Box Spread 變體
- [[選擇權Greeks希臘字母|Greeks]]：Box Spread 的 Delta/Gamma/Vega/Theta 接近零，只有利率敏感

## 風險提示

1. **流動性風險**：四腿同時成交可能面臨部分腿未成交的裸部位風險
2. **保證金風險**：賣出腿需繳保證金，可能佔用大量資金
3. **交易成本**：手續費+滑價可能完全吃掉套利空間
4. **除息風險**：若標的在到期前除息，Box Spread 報酬會受影響（股價下降影響 Call/Put 內含價值）
5. **美式 vs 歐式**：美式選擇權有提前行使風險，只在歐式選擇權上做 Box Spread

## 參考來源

- Wikipedia: Box spread（含完整數學推導、Robinhood 事件、BOXX ETF）
- CME Group: "Index Options Box Spreads as Financing Tool" (2024)
- Cboe: "Long-Dated Box Spreads: A Better Way to Buy a Home" (2025)
- SyntheticFi: 機構級 Box Spread 借貸服務
- Put-Call Parity 基礎理論

## 實戰應用

（待補充）

## 注意事項

（待補充）

## 相關主題

（待補充）
