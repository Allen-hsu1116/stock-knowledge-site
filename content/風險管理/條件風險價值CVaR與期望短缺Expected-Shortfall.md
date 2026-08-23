---
title: "條件風險價值 CVaR 與期望短缺 Expected Shortfall"
category: "風險管理"
---

# 條件風險價值 CVaR 與期望短缺 Expected Shortfall

> VaR 告訴你「最壞情況下的損失底線」，CVaR 告訴你「如果真的踩到那條底線，平均會賠多少」。一個看門檻，一個看門檻之後的地獄。

## 核心概念

**Expected Shortfall (ES)**，又稱 **Conditional Value at Risk (CVaR)**、Average Value at Risk (AVaR)、Tail Value at Risk (TVaR)，是一種衡量投資組合尾部風險的**一致性風險測度 (Coherent Risk Measure)**。

- **VaR(α)** = 在 α 信心水準下，最壞情況的損失上限（例如 95% VaR 表示有 5% 機率損失超過此值）
- **CVaR/ES(α)** = 在最壞的 α% 情境下，損失的**期望值**（平均損失）

用一句話講：VaR 告訴你「門檻在哪」，CVaR 告訴你「跨過門檻之後平均會跌多深」。

## 數學定義

給定一個投資組合的損益分配 X，信心水準 α ∈ (0, 1]：

$$ES_\alpha(X) = \frac{1}{\alpha} \int_0^\alpha VaR_\gamma(X) \, d\gamma$$

白話文：把 0 到 α 所有 VaR 值取平均。當分配連續時，等價於：

$$ES_\alpha(X) = -E[X \mid X \leq -VaR_\alpha(X)]$$

即「在損失超過 VaR 的條件下，損失的期望值」。

## 與 VaR 的比較

**VaR 的致命缺陷：**
- 只看分位數，不看尾部形狀 — 兩個分配可以有相同的 95% VaR，但一個尾部厚一個薄
- **不是一致性風險測度** — 不滿足次可加性 (subadditivity)，組合的 VaR 可能大於各成分 VaR 之和
- 2008 金融海嘯後被廣泛批評，巴塞爾協議 III 已轉向 ES

**CVaR 的優勢：**
- **考量尾部嚴重度** — 不只看門檻，還看門檻後的平均損失
- **一致性風險測度** — 滿足次可加性，分散投資永遠不會增加風險
- **更保守** — ES ≥ VaR（同一信心水準下），作為資本準備更安全
- 可轉化為**線性規劃**求解（Rockafellar & Uryasev 2000），實務上可優化

## 計算範例

假設一個投資組合的損益分配：

- **10% 機率** 虧損 100
- **30% 機率** 虧損 20
- **40% 機率** 損益兩平
- **20% 機率** 獲利 50

計算 ES₅% 和 ES₂₀%：

**ES₅%**：最壞 5% 全落在第一行（虧損 100），所以 ES₅% = 100

**ES₂₀%**：最壞 20% = 10% 來自第一行 + 10% 來自第二行
$$ES_{20\%} = \frac{10/100 \times (-100) + 10/100 \times (-20)}{20/100} = \frac{-10 + (-2)}{0.2} = -60$$

對比 VaR₅% = 100，VaR₂₀% = 100（因為前 10% 的 VaR 就是 100，20% 的 VaR 是 20）

## 常見分配的封閉公式

**常態分配**（損益 X ~ N(μ, σ²)）：
$$ES_\alpha(X) = -\mu + \sigma \cdot \frac{\varphi(\Phi^{-1}(\alpha))}{\alpha}$$

其中 φ 是標準常態 PDF，Φ⁻¹ 是標準常態分位函數。

**Student's t 分配**（自由度 ν，厚尾）：
$$ES_\alpha(X) = -\mu + \sigma \cdot \frac{\nu + (T^{-1}(\alpha))^2}{\nu - 1} \cdot \frac{\tau(T^{-1}(\alpha))}{\alpha}$$

t 分配的 ES 比常態分配更大，因為厚尾 — 這正是 CVaR 比 VaR 更有價值的地方：在厚尾分配下，VaR 可能嚴重低估尾部風險。

## Rockafellar-Uryasev 線性規劃優化

2000 年 Rockafellar 和 Uryasev 證明 ES 可以轉化為線性規劃問題，這是 ES 在實務上被廣泛使用的關鍵突破：

$$\min_{w, z, \gamma} \gamma + \frac{1}{(1-\alpha)J} \sum_{j=1}^J z_j$$

subject to:
- $z_j \geq \ell(w, x_j) - \gamma$
- $z_j \geq 0$

其中 J 是模擬次數，ℓ 是損失函數，w 是組合權重。選擇線性損失函數後，整個問題變成標準線性規劃，可高效求解。

## 實戰應用

**1. 資本準備 (Capital Reserve)**
- Basel III 已用 ES(97.5%) 取代 VaR(99%) 作為銀行市場風險資本計提基礎
- ES 更保守，確保極端情境下資本充足

**2. 投資組合優化**
- 傳統均值-變異數優化只考慮前兩階動差，忽略偏態和峰度
- ES 優化直接考量尾部，適合非常態分配的資產組合
- 用蒙特卡洛模擬生成 J 個情境，再解線性規劃

**3. 風險預算與資本配置**
- 將 ES 分解到各資產貢獻，實現基於尾部風險的資本配置
- 比傳統變異數分配更保守，特別適合信用風險和尾部事件密集的組合

**4. 台股實戰考量**
- 台股在2026年7月費半跌20%、韓國槓桿ETF爆倉等事件中展現明顯厚尾特徵
- 常態分配假設下的 VaR 會嚴重低估此類情境的損失
- 使用歷史模擬法或 t 分配計算 ES 更貼近實際

## 與其他風險指標的關係

- **VaR → CVaR**：CVaR 是 VaR 的上推 (superquantile)，永遠 ≥ VaR
- **CVaR 與 [[風險管理/一致性風險測度Coherent-Risk-Measures|一致性風險測度]]**：CVaR 是最常用的一致性測度之一，滿足次可加性
- **CVaR 與 [[風險管理/光譜風險測度Spectral-Risk-Measure|光譜風險測度]]**：CVaR 是光譜測度的特例（等權重光譜）
- **CVaR 與 [[風險管理/索提諾比率進階實戰Sortino-Ratio-Advanced|Sortino 比率]]**：Sortino 只看下行波動，CVaR 更進一步只看尾部期望損失

## 注意事項

- **非時間一致性**：標準 ES 不是時間一致的風險測度，動態版本需要特殊處理
- **分配假設敏感**：連續分配下各定義等價，但離散分配（有原子）下定義可能不同
- **尾部估計不確定性**：ES 依賴尾部估計，而尾部數據本來就少，樣本 ES 有較大估計誤差
- **計算成本**：歷史模擬法需要足夠多的歷史數據，蒙特卡洛法需要大量模擬

## 來源
- Rockafellar & Uryasev (2000), "Optimization of conditional value-at-risk", Journal of Risk
- Acerbi & Tasche (2002), "Expected Shortfall: a natural coherent alternative to Value at Risk"
- Artzner, Delbaen, Eber & Heath (1999), "Coherent Measures of Risk"
- Basel Committee on Banking Supervision (2019), Basel III market risk framework (FRTB)

## 相關主題
- [[風險管理/一致性風險測度Coherent-Risk-Measures|一致性風險測度]]
- [[風險管理/光譜風險測度Spectral-Risk-Measure|光譜風險測度]]
- [[風險管理/通縮夏普比率Deflated-Sharpe-Ratio|通縮夏普比率]]
- [[風險管理/風險管理總論|風險管理總論]]
- [[風險管理/Copula連接函數與尾部相依性Copula-and-Tail-Dependence|Copula 連接函數與尾部相依性]]