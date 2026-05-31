# 最適f理論Optimal-f-Position-Sizing

> 用歷史交易資料找出讓資金成長最快的下注比例——Kelly的實戰版，但最大虧損是它的錨點

## 核心概念

最適 f 理論（Optimal f）由 Ralph Vince 在1990年提出，是凱利公式在交易實務上的改良版。Kelly 假設你知道機率分布，但現實中你只有歷史交易資料。Optimal f 直接用歷史交易的淨利淨損序列，找出讓最終財富幾何成長率最大的下注比例。

### Kelly vs Optimal f 的根本差異

| 比較項目 | Kelly Criterion | Optimal f (Vince) |
|---------|---------------|-------------------|
| 損失定義 | 固定比例損失 | 歷史最大單筆損失 |
| 計算基礎 | 機率分布已知 | 歷史交易資料序列 |
| 輸入參數 | 勝率+盈虧比 | 每筆交易的損益金額 |
| 適用場景 | 理論最適比例 | 實際交易最適比例 |
| 破產考量 | 不直接考慮 | 以最大虧損為分母 |
| 資金成長 | 幾何成長率最大 | 終端財富幾何平均最大 |

**核心差異**：Kelly 用機率，Optimal f 用實際交易結果。Optimal f 把歷史最大單筆虧損當作分母的基礎，這代表它天生比 Kelly 更重視最壞情況。

### Optimal f 公式

**HPR(i) = 1 + f × (-Trade(i) / BiggestLoss)**

**TWR = HPR(1) × HPR(2) × ... × HPR(n)**

**Geometric Mean = TWR^(1/n)**

其中：
- f = 下注比例（0到1之間）
- Trade(i) = 第 i 筆交易的損益
- BiggestLoss = 歷史最大單筆虧損（負數）
- HPR = Holding Period Return（持有期間報酬）
- TWR = Terminal Wealth Relative（終端財富比）
- 最適 f = 讓 Geometric Mean 最大的 f 值

### 計算範例

**交易序列**：+500, -300, +800, -200, +600（最大虧損 = -300）

嘗試 f = 0.25：
- HPR(1) = 1 + 0.25 × (500/300) = 1.417
- HPR(2) = 1 + 0.25 × (-300/300) = 0.750
- HPR(3) = 1 + 0.25 × (800/300) = 1.667
- HPR(4) = 1 + 0.25 × (-200/300) = 0.833
- HPR(5) = 1 + 0.25 × (600/300) = 1.500

TWR = 1.417 × 0.750 × 1.667 × 0.833 × 1.500 = 2.219
Geometric Mean = 2.219^(1/5) = 1.173 → 17.3% / 交易

逐一嘗試不同 f 值，找到讓 Geometric Mean 最大的 f，就是 Optimal f。

## 實戰應用

### Secure Fraction（安全比例）

Vince 建議使用 Optimal f 的一個分數，而非完整比例：

| 比例 | 風險等級 | 適用對象 |
|------|---------|---------|
| Full Optimal f | 極高風險 | 純理論，不建議實戰 |
| 50% Optimal f | 高風險 | 極有經驗的交易者 |
| 33% Optimal f | 中風險 | 一般交易者 |
| 25% Optimal f | 低風險 | 保守型交易者 |

### 部位計算實務

**合約數 = (帳戶淨值 × Secure Fraction × Optimal f) / |最大虧損|**

例如：
- 帳戶淨值：100萬
- Optimal f：0.35
- Secure Fraction：0.33
- 最大虧損：每口3萬

合約數 = (1,000,000 × 0.33 × 0.35) / 30,000 = 3.85 → **3口**

### 與Kelly的選擇策略

| 情境 | 選擇 | 原因 |
|------|------|------|
| 策略有明確勝率盈虧比 | Kelly | 參數穩定可估計 |
| 只有回測交易資料 | Optimal f | 直接用歷史損益 |
| 策略參數不穩定 | 保守打折 | 兩者都不精確 |
| 新策略剛上線 | 固定比例法 | 先求穩再求好 |

## 注意事項

### 四大致命陷阱

1. **歷史最大虧損未來可能被打破**：Optimal f 的分母是歷史最大虧損，但黑天鵝事件可以產生更大的虧損，導致部位過大
2. **過度擬合歷史資料**：Optimal f 完全依賴歷史交易序列，不同期間的結果可能天差地遠
3. **Full Optimal f 的回撤極大**：理論最適比例的回撤可達50-80%，多數人心理無法承受
4. **樣本數不足時不適用**：至少需要30筆以上交易才能計算，太少會嚴重偏誤

### 三個安全措施

1. **用歷史最大虧損的2倍當分母**：預留黑天鵝的空間
2. **只用 Secure Fraction**：永遠不用 Full Optimal f
3. **定期重新計算**：每季用最新交易資料重新計算 Optimal f

### 和固定比例法的比較

| 比較項目 | Optimal f | 固定比例法（1-2%） |
|---------|---------|-----------------|
| 理論基礎 | 數學最佳化 | 經驗法則 |
| 部位調整 | 隨策略績效動態調整 | 固定百分比 |
| 獲利時加碼 | 是（複利效果） | 是（但幅度較小） |
| 虧損時縮碼 | 是 | 是 |
| 心理負擔 | 高（部位波動大） | 低（部位穩定） |
| 適合階段 | 成熟策略 | 所有階段 |

## 相關主題

- [[凱利公式部位最佳化Kelly-Criterion-Position-Sizing]]
- [[倉位管理]]
- [[MDD最大回撤計算與恢復難度]]
- [[蒙地卡羅模擬交易驗證Monte-Carlo-Simulation]]
- [[回測過擬合Backtest-Overfitting]]
- [[破產風險Risk-of-Ruin]]
- [[風險報酬比]]
- [[交易期望值Trading-Expectancy]]
- [[財務槓桿風險管理Leverage-Risk-Management]]

## 來源

- [Kelly Criterion - Wikipedia](../raw/2026-05-09/Kelly-Criterion-Wikipedia.md)
- Ralph Vince, "Portfolio Management Formulas" (1990)
- Ralph Vince, "The Mathematics of Money Management" (1992)