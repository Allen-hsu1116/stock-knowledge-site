---
title: 價內程度 Moneyness 實戰判讀
date: 2026-06-27
category: "操作策略"
---

# 價內程度 Moneyness 實戰判讀

> 選擇權的價內程度不只是「價內、價外、價平」三分法——量化 Moneyness 讓你用標準差和機率衡量選擇權的真實價值，是理解波動率曲面和 Delta 避險的基礎座標系

## 核心概念

Moneyness（價內程度）是選擇權標的價格與履約價的相對位置關係。它是選擇權分析最基礎的分類系統，也是量化波動率曲面時的關鍵座標軸。

### 三分法分類

- **價內（In the Money, ITM）**：立即行使有正內含價值
  - Call：標的價格 > 履約價
  - Put：標的價格 < 履約價
- **價外（Out of the Money, OTM）**：立即行使無價值
  - Call：標的價格 < 履約價
  - Put：標的價格 > 履約價
- **價平（At the Money, ATM）**：標的價格 = 履約價
  - 只有時間價值，無內含價值

### Spot vs. Forward

實務上用現貨價（Spot），理論上用遠期價（Forward）更精確：
- **ATM Spot**：履約價 = 現貨價
- **ATM Forward（ATMF）**：履約價 = 遠期價
- 低利率、短期限下兩者差異很小，但長期或高利率環境差異顯著

### 內含價值與時間價值

- **內含價值（Intrinsic Value）**：假設立即行使的價值
- **時間價值（Time Value）**：總價值減去內含價值
- 時間價值來自未來價格變動的不確定性 + 折現因子的展開
- 歐式選擇權時間價值可能為負（無法提前行使），美式選擇權若時間價值為負就會被提前行使

### 量化 Moneyness 的層次

從簡單到複雜，Moneyness 有多種量化方式：

1. **絕對 Moneyness**：直接用 S 或 K，不改變座標
2. **簡單 Moneyness**：S/K（或 K/S），ATM = 1，ITM > 1，OTM < 1
3. **對數簡單 Moneyness**：ln(F/K)，ATM = 0，ITM 為正，OTM 為負
4. **標準化 Moneyness**：m = ln(F/K) / (σ√τ)，以標準差為單位
5. **機率 Moneyness**：N(d₂)，風險中性下到期時價內的機率

## 實戰應用

### Delta 作為 Moneyness 代理

交易員最常以 Delta 的絕對值作為 Moneyness 的近似：
- **50 Delta Call** ≈ ATM Call（實際略低於 50% moneyness）
- **25 Delta Call** ≈ 25% 機率到期時價內
- **10 Delta Put** ≈ 10% 機率到期時價內

但 Delta ≠ 真實機率：
- N(d₊) = Delta（以資產為計價單位的風險中性機率）
- N(d₋) = 真實機率 Moneyness（以現金為計價單位）
- N(m) = 標準化 Moneyness 的百分位
- 排序：N(d₋) < N(m) < N(d₊) = Delta

差異來自幾何布朗運動中均值與中位數的偏移（修正因子 σ²τ/2）。波動率高或期限長時差異更大。

### 25 Delta 選擇權的實戰意義

- **25 Delta Call**：市場認為約 25% 機率會漲到該履約價以上
- **25 Delta Put**：市場認為約 25% 機率會跌到該履約價以下
- **Risk Reversal**：25 Delta Call IV − 25 Delta Put IV，衡量偏斜方向
- **Butterfly**：0.5 × (25 Delta Call IV + 25 Delta Put IV) − ATM IV，衡量微笑曲線的「微笑程度」

### ITM vs OTM 的交易邏輯

- **買 ITM 選擇權** = 借出內含價值等額的資金，資金效率低
- **ITM Call = 遠期合約 + OTM Put**（合成關係）
- 因此 **ATM 和 OTM 是主要交易標的**，ITM 流動性通常較差
- 深度 ITM 選擇權的 Delta 接近 ±1，行為近似標的本身

### 波動率曲面的座標系

Moneyness 是波動率曲面的核心座標：
- **絕對波動率曲面**：以履約價 K 和到期時間 τ 為座標
- **相對波動率曲面**：以 Moneyness（如 Delta）和到期時間 τ 為座標
- 相對曲面讓不同標的、不同價位水準的波動率結構可以直接比較

### 台股選擇權實戰

- 台指選擇權履約價間距固定（如 100 點或 200 點），「近價平」的選擇權流動性最好
- 交易者習慣用「價外幾檔」而非 Delta 來描述 Moneyness
- 買方偏好 OTM（低成本高槓桿），賣方偏好 OTM（高勝率收權利金）
- 深度 OTM 選擇權在台股流動性極差，買賣價差可能佔權利金 20%+

## 注意事項

- **Delta ≠ 真實機率**：Delta 是風險中性機率的一種，高估了真實 ITM 機率（因為修正因子），實戰中差異通常很小但波動率高時不可忽略
- **Spot vs Forward 差異**：高利率或長期限環境下，ATM Spot 和 ATMF 的選擇權價格和 IV 有明顯差異
- **ITM 流動性陷阱**：深度 ITM 選擇權買賣價差極寬，看似便宜實際交易成本高昂
- **Moneyness 非方向預測**：Moneyness 告訴你選擇權的價內程度，不預測標的價格走向
- **標準化 Moneyness 假設 BS 模型**：σ√τ 的標準化依賴 Black-Scholes 假設，真實分布有胖尾時標準化 Moneyness 可能失真

## 相關主題

- [[操作策略/選擇權Greeks希臘字母]]
- [[操作策略/Black-Scholes定價模型]]
- [[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew]]
- [[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]
- [[操作策略/垂直價差Vertical-Spread牛市價差與熊市價差]]
- [[操作策略/選擇權組合策略]]

## 來源

- [Moneyness - Wikipedia](../../raw/2026-06-27/Moneyness-Wikipedia.md)