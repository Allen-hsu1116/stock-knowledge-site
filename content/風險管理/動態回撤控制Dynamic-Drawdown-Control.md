# 動態回撤控制 Dynamic Drawdown Control

> 不只是看「回撤有多大」，而是在回撤發生時「動態縮減部位」，讓資金曲線的坑洞越挖越淺。

## 核心概念

傳統風控用 VaR、[[風險管理/VaR風險值Value-at-Risk|VaR]] 或[[風險管理/停損方法|停損]]來控制單筆交易的損失上限，但這些都是「靜態」的——設定一個數字就不動了。動態回撤控制（Dynamic Drawdown Control, DDC）的核心思想是：

**當回撤加深時，自動減少部位；當回撤恢復時，逐步加回部位。**

這不是新的停損方法，而是一個「部位調節器」，讓你的風險暴露隨著資金曲線的健康程度動態變化。

## 與相關策略的定位

動態回撤控制與以下概念有重疊但不同：

- **[[風險管理/CPPI固定比例投資組合保險策略|CPPI]]**：保護本金不低於某個地板，靠動態調整風險資產與無風險資產比例。DDC 不保護本金，而是控制「從高點往下的距離」
- **[[操作策略/波動率目標策略Volatility-Targeting|波動率目標]]**：根據波動率預測調整部位。DDC 根據已實現回撤調整，一個看未來波動、一個看過去回撤
- **[[風險管理/反馬丁格爾策略Anti-Martingale|反馬丁格爾]]**：贏了加碼、輸了減碼。DDC 更精細——不只看輸贏，而是看「從高點掉了多少」
- **[[風險管理/資金曲線管理Equity-Curve-Management|資金曲線管理]]**：DDC 是資金曲線管理的具體執行模組之一

## 控制機制設計

### 1. 回撤計算

首先定義「回撤」：

```
DD(t) = (Equity(t) - Peak(t)) / Peak(t)
```

其中 Peak(t) = max(Equity(0), Equity(1), ..., Equity(t))，即歷史最高資金。

### 2. 縮減函數

定義一個「部位縮減函數」f(DD)，將回撤深度映射到部位倍數：

**線性縮減（最常見）：**

```
f(DD) = max(0, 1 - DD / DD_max)
```

- DD = 0%（創新高）→ f = 1.0（滿部位）
- DD = 5% → f = 0.75（如果 DD_max = 20%）
- DD = 20% → f = 0（完全空倉）

**指數縮減（更平滑）：**

```
f(DD) = exp(-k × DD)
```

- k 越大，縮減越激進
- 不會突然歸零，適合不想完全空倉的策略

**分段縮減（實務常用）：**

- DD < 5%：100% 部位
- 5% ≤ DD < 10%：75% 部位
- 10% ≤ DD < 15%：50% 部位
- 15% ≤ DD < 20%：25% 部位
- DD ≥ 20%：0% 部位（暫停交易）

### 3. 恢復機制

回撤恢復後如何加回部位，是 DDC 最微妙的設計：

**立即恢復**：回撤縮小就馬上加碼。問題是可能在高波動期頻繁加減碼，交易成本高。

**滯後恢復（推薦）**：設定一個「恢復閾值」，只有回撤縮小到某個程度才開始加碼。例如：
- 縮減閾值：DD > 10% 開始減碼
- 恢復閾值：DD < 5% 才開始加碼
- 兩個閾值之間形成「不動區」，避免來回調整

**高點確認恢復**：必須創歷史新高才回到滿部位。最保守，但可能錯過反彈初期行情。

## 實戰參數設定

### 依策略類型調整 DD_max

- **趨勢追蹤策略**：DD_max = 15-25%（趨勢策略本來回撤就大，設太緊會頻繁暫停）
- **均值回歸策略**：DD_max = 8-12%（均值回歸回撤應該小，超過代表策略可能失效）
- **當沖策略**：DD_max = 5-8%（日內策略不應有大幅回撤）
- **多策略組合**：DD_max = 10-15%（分散後回撤應受控）

### 依時間框架調整

- **日線級別**：用每日收盤資金計算回撤，調整頻率為每日
- **週線級別**：用每週收盤計算，適合波段策略，避免日內雜訊
- **月線級別**：適合長期投資組合，但反應太慢可能來不及控制風險

## 與其他風控工具的組合

DDC 很少單獨使用，通常與以下工具疊加：

- **DDC + [[風險管理/停損方法|單筆停損]]**：DDC 控制組合層面的回撤，停損控制單筆交易的損失
- **DDC + [[風險管理/部位控制2%法則Position-Sizing-2-Percent-Rule|2%法則]]**：2% 法則設定單筆最大虧損，DDC 在累積虧損後進一步縮減
- **DDC + [[風險管理/波動率目標策略Volatility-Targeting|波動率目標]]**：波動率目標控制預期風險，DDC 控制已實現回撤，雙重調節
- **DDC + [[風險管理/蒙地卡羅模擬交易驗證Monte-Carlo-Simulation|蒙地卡羅模擬]]**：用模擬測試 DDC 參數在各種路徑下的效果

## 優缺點

**優點：**
- 直覺性強——「輸越多下越小」符合常識
- 數學上可證明能降低[[風險管理/MDD最大回撤計算與恢復難度|最大回撤]]和[[風險管理/破產風險Risk-of-Ruin|破產風險]]
- 與幾乎任何策略兼容，不改變進出場邏輯只調部位
- 可量化回測，參數優化空間大

**缺點：**
- **反覆假動作**：回撤接近閾值時來回觸發，可能在高波動期不斷縮減又加碼
- **復利拖累**：回撤後縮減部位，反彈時獲利速度也變慢，拉長回撤恢復時間
- **參數過擬合**：DD_max 和恢復閾值如果用歷史數據優化，容易[[風險管理/回測過擬合Backtest-Overfitting|過擬合]]
- **不防閃崩**：單日暴跌 20% 時 DDC 來不及反應（除非用日內監控）

## 台股實戰考量

台股有獨特的回撤控制需求：

- **漲跌幅限制 10%**：單日極端回撤有上限，DDC 用日線計算相對安全
- **處置股制度**：當個股被處置時流動性驟降，DDC 應額外考慮「處置風險」
- **除權息季節**：7-8 月除權息密集，指數自然回落不算真實回撤，DDC 計算應使用還原股價
- **外資期貨空單**：外資空單高位時市場波動加劇，可作為 DDC 的領先指標提前縮減

## 程式化實作概念

```python
class DynamicDrawdownControl:
    def __init__(self, dd_max=0.15, recovery_threshold=0.05):
        self.dd_max = dd_max
        self.recovery_threshold = recovery_threshold
        self.peak_equity = 0
        self.current_scale = 1.0
        self.is_reducing = False
    
    def update(self, equity):
        if equity > self.peak_equity:
            self.peak_equity = equity
        
        dd = (equity - self.peak_equity) / self.peak_equity
        
        if dd <= 0:  # 創新高
            self.current_scale = 1.0
            self.is_reducing = False
        elif self.is_reducing:
            if abs(dd) < self.recovery_threshold:
                self.is_reducing = False
                self.current_scale = 1.0
            else:
                self.current_scale = max(0, 1 - abs(dd) / self.dd_max)
        else:
            if abs(dd) > self.recovery_threshold:
                self.is_reducing = True
                self.current_scale = max(0, 1 - abs(dd) / self.dd_max)
        
        return self.current_scale
```

## 參考來源

- Schwartz, B. (2010). "The Emotion Machine: Managing Drawdowns in Trading"
- 系統化交易回撤控制框架可參考 [[風險管理/回撤分析進階Drawdown-Analysis-Advanced|回撤分析進階]] 與 [[風險管理/動態部位管理Dynamic-Position-Sizing|動態部位管理]]
- 回撤恢復數學基礎見 [[風險管理/回撤恢復數學與帳戶生存Drawdown-Recovery-Math|回撤恢復數學]]