---
title: "二階與三階Greeks進階 Vanna Vomma Charm"
date: 2026-06-27
---

# 二階與三階 Greeks 進階：Vanna、Vomma、Charm

> 一階 Greeks（Delta/Vega/Theta）只是起點——Vanna 衡量波動率變化對 Delta 的影響、Vomma 衡量 Vega 的凸性、Charm 衡量 Delta 的時間衰減，高階 Greeks 是專業選擇權交易者管理複雜部位的必修課

## 核心概念

### Greeks 階層體系

- **一階 Greeks**：Delta（∂V/∂S）、Vega（∂V/∂σ）、Theta（−∂V/∂τ）、Rho（∂V/∂r）
- **二階 Greeks**：Gamma、Vanna、Charm、Vomma、Veta、Vera
- **三階 Greeks**：Speed、Zomma、Color、Ultima、Parmicharma

二階 Greeks 是一階 Greeks 的偏微分，三階 Greeks 是二階的偏微分。每一階都捕捉更細微的風險變化。

### 二階 Greeks 詳解

#### Gamma（Γ）— Delta 的變化率
- Γ = ∂Δ/∂S = ∂²V/∂S²
- Long option 正 Gamma，Short option 負 Gamma
- ATM 時 Gamma 最大，越 ITM 或 OTM 越小
- Gamma 避險確保 Delta 避險在更大價格範圍內有效

#### Vanna — Delta 對波動率的敏感度
- Vanna = ∂Δ/∂σ = ∂Vega/∂S = ∂²V/∂S∂σ
- 又稱 DvegaDspot 或 DdeltaDvol
- 衡量：波動率變動 1% 時 Delta 變化多少
- **實戰意義**：Delta 避險部位在波動率變動時，避險比例需要調整的幅度
- Vanna 在偏斜環境下特別重要——偏斜變化會改變各履約價的 Delta

#### Charm — Delta 的時間衰減
- Charm = −∂Δ/∂τ = ∂Θ/∂S = −∂²V/∂τ∂S
- 又稱 Delta Decay 或 DdeltaDtime
- 衡量：時間流逝 1 天 Delta 讘化多少
- **實戰意義**：週末過後 Delta 自動漂移的幅度，Delta 避險部位需定期重新平衡的依據
- 近到期日 Charm 變化劇烈，日估不準確

#### Vomma — Vega 的凸性
- Vomma = ∂Vega/∂σ = ∂²V/∂σ²
- 又稱 Volga、Vega Convexity、DvegaDvol
- 衡量：波動率變動 1% 時 Vega 變化多少
- 正 Vomma = 波動率上升時部位自動變 Long Vega（類似 Long Gamma 的效果）
- OTM 選擇權 Vomma 為正，離開 ATM 後隨距離增加（但 Vega 衰減後最終下降）
- **實戰意義**：偏斜交易中管理 Vega 隨波動率變化的風險

#### Veta — Vega 的時間衰減
- Veta = ∂Vega/∂τ = ∂²V/∂σ∂τ
- 又稱 Vega Decay 或 DvegaDtime
- 衡量：時間流逝對 Vega 的影響
- **實戰意義**：長期選擇權的 Vega 較穩定，短期選擇權 Vega 隨到期接近快速衰減

#### Vera — Rho 對波動率的敏感度
- Vera = ∂Rho/∂σ = ∂²V/∂σ∂r
- 衡量：波動率變動對 Rho 的影響
- 利率敏感度在短期選擇權中通常不重要，Vera 實戰中使用頻率最低

### 三階 Greeks 詳解

#### Speed — Gamma 的變化率
- Speed = ∂Γ/∂S = ∂³V/∂S³
- 又稱 Gamma of Gamma 或 DgammaDspot
- **實戰意義**：標的價格大幅移動時 Gamma 本身變化的速度，Gamma 避險部位的動態調整依據

#### Zomma — Gamma 對波動率的敏感度
- Zomma = ∂Γ/∂σ = ∂Vanna/∂S = ∂³V/∂S²∂σ
- 又稱 DgammaDvol
- **實戰意義**：波動率變動時 Gamma 避險有效性的變化，偏斜環境下管理 Gamma 部位的關鍵

#### Color — Gamma 的時間衰減
- Color = ∂Γ/∂τ = ∂³V/∂S²∂τ
- 又稱 Gamma Decay 或 DgammaDtime
- **實戰意義**：Gamma 部位隨時間流逝的變化，近到期 Gamma 衝高但維持時間極短

#### Ultima — Vomma 的變化率
- Ultima = ∂Vomma/∂σ = ∂³V/∂σ³
- 又稱 DvommaDvol
- **實戰意義**：極端波動率環境下 Vega 凸性的變化，高階波動率交易使用

#### Parmicharma — Charm 的時間衰減
- Parmicharma = −∂Charm/∂τ = ∂³V/∂τ²∂S
- 又稱 DcharmDtime
- **實戰意義**：Charm 本身隨時間變化，長期 Delta 避險部位需要考量

### 多資產 Greeks

當選擇權價值依賴多個標的時，Greeks 延伸出交叉效應：
- **Correlation Delta（CEGA）**：對標的間相關性變動的敏感度
- **Cross Gamma**：一個標的的 Delta 對另一標的價格變動的變化率
- **Cross Vanna**：一個標的的 Vega 對另一標的價格的變化率
- **Cross Volga**：一個標的的 Vega 對另一標的波動率的變化率

## 實戰應用

### Vanna 管理實戰

1. **Delta 避險 + 波動率變動**：Delta 中性部位若 Vanna 很大，波動率跳升時 Delta 會偏離中性
2. **偏斜交易的 Vanna 風險**：做多 OTM Put、賣 ATM Put 的偏斜交易，Vanna 暴露在偏斜變化的風險中
3. **Vanna 中性策略**：同時管理 Delta 和 Vanna，讓部位在波動率和價格變動下都保持中性

### Charm 管理實戰

1. **週末 Delta 漂移**：週五收盤到週一開盤的 3 天 Charm 效應，Delta 避險部位需預先調整
2. **近到期 Charm 加速**：接近到期時 Charm 變化劇烈，每日 Delta 調整幅度增大
3. **Charm-Adjusted Delta**：用 Charm 修正 Delta 避險，預判隔日 Delta 變化提前調整

### Vomma 管理實戰

1. **Vega 中性 + Vomma 偏多**：構建 Vega 中性但 Vomma 正的部位，在不承擔方向性波動率風險下賺波動率凸性
2. **波動率暴漲保護**：正 Vomma 部位在波動率暴漲時自動增加 Vega 暴露，類似 Gamma 的效果
3. **不同履約價組合**：用不同履約價的比率組合構建目標 Vomma 暴露

### 高階 Greeks 的聯動管理

實務上很少單獨管理某一個高階 Greek，而是建立 Greeks 矩陣：
- **Delta 中性 + Gamma 中性**：標準做市商部位
- **Delta + Gamma + Vanna 中性**：考慮波動率對 Delta 的影響
- **Vega + Vomma 中性**：考慮波動率凸性
- **全中性 + 方向性暴露**：剝離所有二階風險，純粹押注方向

### 台股實戰注意

- 台指選擇權造市商制度使 IV 變動相對黏著，Vanna 和 Vomma 的影響不如美股明顯
- 但結算前後 Charm 效應顯著，隔日沖部位需特別注意 Delta 漂移
- 深度 OTM 選擇權的 Vomma 在極端行情中可能讓賣方部位 Vega 暴露暴增

## 注意事項

- **高階 Greeks 計算依賴模型**：所有公式都基於 Black-Scholes 假設，真實市場的偏斜和胖尾會使高階 Greeks 的精確度下降
- **近到期日不穩定**：Charm、Color 等時間相關的高階 Greeks 在接近到期時變化劇烈，日估不準確
- **不要過度優化**：散戶交易者管理到 Gamma 和 Vanna 已足夠，三階 Greeks 主要為機構做市商使用
- **交叉偏導數對稱性**：Vanna = ∂Δ/∂σ = ∂Vega/∂S（Schwarz 定理），同一 Greek 有兩種解讀方式
- **模型風險**：使用局部波動率或隨機波動率模型時，高階 Greeks 的數值可能與 BS 模型顯著不同

## 相關主題

- [[操作策略/選擇權Greeks希臘字母]]
- [[操作策略/選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]
- [[操作策略/價內程度Moneyness實戰判讀]]
- [[操作策略/Black-Scholes定價模型]]
- [[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew]]
- [[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[操作策略/選擇權Convexity凸性與非對稱收益Option-Convexity]]
- [[風險管理/選擇權Greeks風險判讀]]

## 來源

- [Greeks (Finance) - Wikipedia](../raw/2026-06-27/Greeks-Second-Third-Order-Wikipedia.md)