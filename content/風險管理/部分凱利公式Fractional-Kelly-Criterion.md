# 部分凱利公式 Fractional Kelly Criterion

> Full Kelly 是理論最優，Half Kelly 是實務最優。因為你永遠不知道真正的勝率和賠率到底對不對。

## 核心概念

[[風險管理/凱利公式部位最佳化Kelly-Criterion-Position-Sizing|凱利公式]]（Kelly Criterion）告訴你「在已知勝率和賠率下，每次下注佔總資金的多少比例可以讓長期幾何成長率最大化」。理論上很完美，實務上卻有三個致命問題：

1. **你不知道真正的勝率**——歷史回測的勝率是估計值，不是真實值
2. **你不知道真正的賠率**——市場報酬分佈不是靜態的
3. **Full Kelly 的回撤太深**——就算參數完美，Full Kelly 的預期最大回撤仍可達 50% 以上

部分凱利（Fractional Kelly）的解法簡單粗暴：**把凱利公式算出來的比例乘上一個分數**，通常是一半（Half Kelly）、四分之一（Quarter Kelly）或更小。

## 公式

### Full Kelly（回顧）

**二元結果版本：**

```
f* = (p × l - q × g) / (g × l)
```

其中 p = 勝率，q = 1-p，g = 贏的比例，l = 輸的比例。

**股市連續版本：**

```
f* = (μ - r) / σ²
```

其中 μ = 預期報酬率，r = 無風險利率，σ² = 報酬率變異數。

### Fractional Kelly

```
f_fractional = k × f*
```

其中 k 是分數係數，0 < k ≤ 1：
- **k = 1.0**：Full Kelly（理論最優成長率，但回撤巨大）
- **k = 0.5**：Half Kelly（最常用，成長率約為 Full Kelly 的 75%，但回撤大幅降低）
- **k = 0.25**：Quarter Kelly（保守型，適合參數不確定性高的場景）
- **k = 0.1**：十分之一 Kelly（極度保守，接近等比例下注）

## 為什麼 Half Kelly 是實務最優？

### 1. 成長率損失很小

Half Kelly 的長期幾何成長率約為 Full Kelly 的 **75%**——你只犧牲了 25% 的成長速度，卻換來大幅降低的波動和回撤。

數學上，幾何成長率 G 與下注比例 f 的關係近似：

```
G(f) ≈ r + f × (μ - r) - ½ × f² × σ²
```

Full Kelly 時 f* = (μ-r)/σ²，代入得 G_max = r + ½(μ-r)²/σ²

Half Kelly 時 f = f*/2，代入得 G_half = r + ¾ × ½(μ-r)²/σ² = r + ⅜(μ-r)²/σ²

所以 G_half / G_max = ¾ = 75%。

### 2. 回撤大幅降低

| 下注比例 | 預期最大回撤 | 相對成長率 |
|----------|-------------|-----------|
| Full Kelly | ~50-60% | 100% |
| 3/4 Kelly | ~35-45% | ~94% |
| Half Kelly | ~20-30% | ~75% |
| Quarter Kelly | ~10-15% | ~44% |

Half Kelly 把預期最大回撤從 50%+ 降到 20-30%，對大多數投資人來說「可承受」。

### 3. 參數誤差的緩衝

這是最重要的實務理由。假設你估計的 μ 和 σ 都有誤差：

- Full Kelly：如果真實 μ 比估計低 20%，你可能下注過重，長期反而虧損
- Half Kelly：就算估計偏差 50%，通常仍在安全範圍內

Thorp（1969）證明：**當參數存在不確定性時，Half Kelly 的期望效用在大多數情境下高於 Full Kelly**。

## 與其他部位控制方法的比較

- **[[風險管理/部位控制2%法則Position-Sizing-2-Percent-Rule|2%法則]]**：固定每筆交易風險佔總資金 2%，不考慮勝率賠率。簡單但不最優
- **[[風險管理/最適f理論Optimal-f-Position-Sizing|最適 f 理論]]**：Ralph Vince 的方法，類似 Kelly 但基於歷史交易結果的最佳化。容易過擬合
- **[[風險管理/反馬丁格爾策略Anti-Martingale|反馬丁格爾]]**：贏了加碼、輸了減碼，方向與 Kelly 一致但無公式，靠紀律執行
- **Fixed Fractional**：固定比例下注（如永遠 5%），不隨勝率調整

Fractional Kelly 的優勢在於它**有理論基礎**（最大化幾何成長率）**又有實務緩衝**（分數係數吸收參數誤差）。

## 多資產 Fractional Kelly

在多資產投資組合中，Kelly 公式推廣為：

```
F* = Σ⁻¹ × (μ - r·1)
```

其中 F* 是各資產最適權重向量，Σ 是報酬率協方差矩陣，μ 是預期報酬向量。

實務上這個公式極度不穩定——Σ 的估計誤差會被反矩陣放大，導致權重爆炸。因此多資產 Fractional Kelly 通常配合：

1. **貝葉斯收縮**（Bayesian Shrinkage）：把估計值往先驗（如市場均衡權重）收縮，這正是[[操作策略/Black-Litterman模型結合觀點與市場均衡Black-Litterman-Model|Black-Litterman 模型]]的做法
2. **嶺回歸正則化**：在 Σ 上加一個對角矩陣 λI，降低反矩陣的敏感度
3. **直接用 Half Kelly**：算出 F* 後整體乘 0.5

## 實戰計算範例

### 單一股票

假設你回測一個交易策略：
- 勝率 p = 55%
- 平均獲利 g = 3%（贏的時候賺 3%）
- 平均虧損 l = 2%（輸的時候虧 2%）

```
Full Kelly f* = (0.55 × 0.02 - 0.45 × 0.03) / (0.03 × 0.02)
              = (0.011 - 0.0135) / 0.0006
              = -0.0025 / 0.0006
              = -0.42
```

結果是負的——代表這個策略沒有正期望值！Full Kelly 告訴你不該交易。這就是 Kelly 公式的另一個價值：**先檢驗策略是否有正期望值**。

換一個有正期望值的例子：
- 勝率 p = 60%，g = 4%，l = 3%

```
f* = (0.60 × 0.03 - 0.40 × 0.04) / (0.04 × 0.03)
   = (0.018 - 0.016) / 0.0012
   = 0.002 / 0.0012
   = 1.67
```

Full Kelly 說下注 167%（要用槓桿），Half Kelly 就是 83%，Quarter Kelly 就是 42%。

### 股市版本

假設 S&P 500：
- 預期年報酬 μ = 10%
- 無風險利率 r = 4%
- 年化波動率 σ = 16%，σ² = 0.0256

```
Full Kelly f* = (0.10 - 0.04) / 0.0256 = 2.34（234%）
Half Kelly  f = 1.17（117%）
Quarter Kelly f = 0.59（59%）
```

Thorp 估計美股市場的 Kelly 比例約 117%，Half Kelly 約 59%——對大多數投資人來說 60% 股票部位是合理的。

## 常見誤區

- **「Half Kelly 永遠是最好的」**：不是。如果你的參數估計很精確（如套利策略），可以接近 Full Kelly。如果估計很不確定，甚至該用 Quarter Kelly
- **「Kelly 公式保證不破產」**：Full Kelly 理論上不會歸零，但回撤可以非常深（50%+），且參數估計錯誤時可能破產
- **「Kelly 適用於所有市場」**：Kelly 假設報酬分佈已知且穩定，肥尾市場（如加密貨幣）需要額外的[[風險管理/極端值理論EVT量化肥尾風險|極端值理論]]修正
- **「可以直接用回測勝率代入」**：回測勝率是樣本估計，樣本外可能完全不同。應該用貝葉斯方法或保守折扣

## 與行為財務學的關聯

投資人對回撤的心理反應是 Kelly 分數選擇的隱藏變數：

- **[[風險管理/損失厭惡Loss-Aversion處置效應過度自信FOMO|損失厭惡]]**：多數人對 50% 回撤的痛苦是 25% 回撤的 4 倍以上，Half Kelly 的情感可承受度遠高於 Full Kelly
- **[[風險管理/前景理論Prospect-Theory|前景理論]]**：Kahneman-Tversky 的 S 型效用函數暗示，投資人的最適分數應該低於 Full Kelly
- **[[風險管理/回撤恢復數學與帳戶生存Drawdown-Recovery-Math|回撤恢復數學]]**：跌 50% 要漲 100% 才回本，降低回撤深度比追求最大成長率更重要

## 參考來源

- Kelly, J.L. (1956). "A New Interpretation of Information Rate." *Bell System Technical Journal*
- Thorp, E.O. (1969). "Optimal Gambling Systems for Favorable Games." *Review of the International Statistical Institute*
- MacLean, L.C., Thorp, E.O. & Ziemba, W.T. (2011). *The Kelly Capital Growth Investment Criterion*
- Wikipedia: [Kelly criterion - Full Kelly, fractional Kelly, and more than Kelly](https://en.wikipedia.org/wiki/Kelly_criterion)
- 相關主題：[[風險管理/凱利公式部位最佳化Kelly-Criterion-Position-Sizing|凱利公式部位最佳化]]、[[風險管理/最適f理論Optimal-f-Position-Sizing|最適 f 理論]]、[[風險管理/破產風險Risk-of-Ruin|破產風險]]