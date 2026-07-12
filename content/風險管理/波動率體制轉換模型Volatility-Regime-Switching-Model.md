# 波動率體制轉換模型 Volatility Regime Switching Model

> 市場有兩種人格——有時平靜如湖，有時狂暴如海。你不能用同一套策略對付兩種人格。波動率體制轉換模型用統計方法自動辨識市場現在是哪種人格，讓你知道何時該順勢、何時該反轉。

## 核心概念

波動率體制（Volatility Regime）是指市場在一段時間內維持的波動率水準。市場不是在「高波動」和「低波動」之間隨機跳動，而是傾向於在某一體制內停留一段時間後才轉換到另一體制。

這種「粘性」現象在學術上稱為波動率叢聚（Volatility Clustering）——高波動後面跟著高波動，低波動後面跟著低波動。Mandelbrot 早在 1963 年就觀察到這個現象。

### 兩大體制

- **低波動體制（Calm/Low-Vol Regime）**：波動率低於長期均值，市場趨勢明確，適合趨勢追蹤策略
- **高波動體制（Volatile/High-Vol Regime）**：波動率高於長期均值，市場震盪劇烈，適合均值回歸策略或降低部位

### 體制轉換的觸發因素
- 重大經濟事件（利率決策、非農數據、地緣政治）
- 市場結構性變化（流動性枯竭、槓桿清洗）
- 黑天鵝事件（COVID-19、金融危機）
- 有時候沒有明顯原因，純粹是市場情緒週期

> 相關頁面：[[風險管理/市場情緒週期與反脆弱交易系統Market-Sentiment-Cycle-and-Antifragile-System|市場情緒週期與反脆弱交易系統]]

## Markov 體制轉換模型

最經典的波動率體制轉換模型是 Hamilton (1989) 提出的 Markov Regime-Switching Model。

### 核心概念

假設市場有 K 個體制（通常 K=2），市場在每個時刻處於某一體制，且服從 Markov 隨機過程——下一期的體制只取決於當前體制，與更早的歷史無關。

### 轉換概率矩陣

以兩體制模型為例：

```
        下一期低波動    下一期高波動
當期低波動    p(LL)         p(LH)
當期高波動    p(HL)         p(HH)
```

- **p(LL)**：今天低波動，明天繼續低波動的機率（持續性）
- **p(LH)**：今天低波動，明天轉高波動的機率（轉換機率）
- **p(HL)**：今天高波動，明天轉低波動的機率
- **p(HH)**：今天高波動，明天繼續高波動的機率

通常 p(LL) 和 p(HH) 都很高（如 0.90-0.98），代表體制有粘性。p(LH) 和 p(HL) 很低（如 0.02-0.10），代表轉換不常發生。

### 期望持續時間

在某一體制的期望停留時間 = 1 / (1 - p(自轉機率))

- 若 p(LL) = 0.95，低波動體制平均持續 1 / (1 - 0.95) = 20 天
- 若 p(HH) = 0.90，高波動體制平均持續 1 / (1 - 0.90) = 10 天

這個數字對部位管理至關重要——如果知道高波動體制平均只持續 10 天，就能設定合理的「等待回歸」期限。

## 實務辨識方法

### 方法一：滾動波動率 + 門檻

最簡單的方法：

1. 計算 N 日滾動標準差（通常 N=20 或 60）
2. 設定門檻：高於長期均值的 1.5 倍 = 高波動體制
3. 低於長期均值 = 低波動體制

優點：簡單直觀
缺點：門檻選擇主觀，滾動窗口有滯後

### 方法二：VIX 分位數

用 VIX 指數的歷史分位數判斷：

- VIX < 15（歷史 25th percentile）→ 低波動體制
- VIX 15-25 → 中波動體制
- VIX > 25（歷史 75th percentile）→ 高波動體制

台股可用台指 VIX 或 TCRI 指數替代。

> 相關頁面：[[風險管理/VIX恐慌指數實戰判讀|VIX 恐慌指數實戰判讀]]

### 方法三：GARCH 模型

GARCH（Generalized Autoregressive Conditional Heteroskedasticity）模型可以估計條件波動率，並預測未來波動率。GARCH(1,1) 是最常用版本：

```
σ²_t = ω + α × ε²_{t-1} + β × σ²_{t-1}
```

當 GARCH 估計的條件波動率超過長期無條件波動率的某個倍數，判定為高波動體制。

### 方法四：HMM 隱馬爾可夫模型

用 Hidden Markov Model 直接擬合收益序列，模型自動估計體制數量和轉換概率。Python 的 `hmmlearn` 套件可以實作。

優點：最統計嚴謹
缺點：計算複雜、需要專業知識、過擬合風險

> 相關頁面：[[技術分析/赫斯特指數Hurst-Exponent|赫斯特指數 Hurst Exponent]] — 另一個判斷市場體制的工具

## 不同體制的策略選擇

### 低波動體制 → 趨勢追蹤

- **適用策略**：突破交易、動能策略、趨勢線操作
- **部位管理**：可放大部位（波動率目標策略下，低波動 → 高曝險）
- **停損設定**：可用較窄停損（ATR 較小）
- **指標選擇**：[[技術分析/SuperTrend超級趨勢指標|SuperTrend]]、[[技術分析/唐奇安通道Donchian-Channel|唐奇安通道]]、[[操作策略/海龜交易法則|海龜交易法則]]

### 高波動體制 → 均值回歸或降部位

- **適用策略**：均值回歸、選擇權賣方（高 IV）、配對交易
- **部位管理**：縮小部位（波動率目標策略下，高波動 → 低曝險）
- **停損設定**：必須放寬（ATR 較大，窄停損會被洗出）
- **指標選擇**：[[操作策略/均值回歸策略|均值回歸策略]]、[[操作策略/網格交易Grid-Trading|網格交易]]、[[技術分析/布林通道Bollinger-Bands三軌八型態|布林通道]]

> 相關頁面：[[操作策略/交易系統體制適應策略Adaptive-Trading-System|交易系統體制適應策略]]、[[風險管理/波動率目標策略Volatility-Targeting|波動率目標策略]]

## 體制轉換的預警訊號

### 1. VIX Term Structure 倒掛

正常情況下 VIX 期限結構正斜率（遠月 > 近月），當近月 VIX > 遠月 VIX 時稱為倒掛，是市場即將進入高波動體制的強烈預警。

> 相關頁面：[[操作策略/波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution|波動率期限結構與曲面演化]]

### 2. VVIX 飆升

VVIX（VIX 的 VIX）衡量波動率本身的波動率。VVIX 飆升代表波動率體制正在轉換中。

> 相關頁面：[[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|波動率的波動率 VVIX]]

### 3. 相關性崩潰

平時不相關的資產突然齊漲齊跌（相關性趨近 1），是高波動體制的典型特徵。

> 相關頁面：[[風險管理/相關性崩潰Correlation-Breakdown|相關性崩潰]]

### 4. ATR 急速擴張

ATR 在短時間內擴張 2 倍以上，代表波動率正在從低體制轉向高體制。

> 相關頁面：[[技術分析/ATR平均真實波幅-Average-True-Range|ATR 平均真實波幅]]

## 部位管理的體制適應

### 波動率目標策略

目標：讓組合每天承受固定的波動率（如年化 10%）。

- 低波動體制：σ = 8%，目標 10% → 槓桿 10/8 = 1.25x
- 高波動體制：σ = 25%，目標 10% → 槓桿 10/25 = 0.40x

這樣不管市場體制如何，組合的預期波動率都維持在 10% 左右。

> 相關頁面：[[風險管理/波動率目標策略Volatility-Targeting|波動率目標策略]]

### Kelly 公式動態調整

Kelly 公式的下注比例與波動率成反比：

```
f* = (μ - r) / σ²
```

高波動體制下 σ² 變大，f* 自然變小，Kelly 公式自動建議降低部位。

> 相關頁面：[[操作策略/凱利公式Kelly-Criterion最佳下注比例|凱利公式]]、[[風險管理/凱利公式部位最佳化Kelly-Criterion-Position-Sizing|凱利公式部位最佳化]]

### 最大回撤防禦

高波動體制下 MDD 風險急劇上升。建議在高波動體制觸發時：
- 總部位降低至 50% 以下
- 單筆風險從 2% 降到 1%
- 啟動保護性賣權或減倉

> 相關頁面：[[風險管理/MDD最大回撤進階實戰各資產歷史回撤與管理方法|MDD 最大回撤進階實戰]]、[[風險管理/保護性賣權與Collar避險策略Protective-Put-and-Collar|保護性賣權與 Collar 避險策略]]

## 台股實戰框架

### 體制判斷儀表板

每日計算以下指標判斷當前體制：

1. **台指 VIX**：< 15 低波動，> 25 高波動
2. **20 日 ATR / 指數**：< 1.2% 低波動，> 2.5% 高波動
3. **融資維持率大盤均值**：> 165% 低波動（安全感高），< 150% 高波動（恐慌）
4. **外資期貨未平倉**：大量翻空可能是體制轉換前兆

### 體制適應操作規則

**低波動體制（3 個以上指標確認）：**
- 部位上限：80%
- 策略偏好：趨勢追蹤、突破買進
- 停損：1.5 ATR
- 槓桿：可適度使用融資（不超過 1.2x）

**中波動體制：**
- 部位上限：60%
- 策略偏好：波段操作
- 停損：2 ATR
- 槓桿：不使用

**高波動體制（3 個以上指標確認）：**
- 部位上限：30%
- 策略偏好：均值回歸、選擇權賣方
- 停損：3 ATR（或改用時間停損）
- 槓桿：嚴禁加槓桿，考慮降槓桿

> 相關頁面：[[籌碼面分析/融資維持率與斷頭|融資維持率與斷頭]]、[[籌碼面分析/外資期貨未平倉判讀|外資期貨未平倉判讀]]

## Python 實作參考

### 簡易滾動波動率體制判斷

```python
import numpy as np
import pandas as pd

def volatility_regime(returns, window=20, threshold_mult=1.5):
    """
    判斷波動率體制
    returns: 日報酬序列
    window: 滾動窗口
    threshold_mult: 高波動門檻倍數（相對於長期均值）
    """
    rolling_vol = returns.rolling(window).std()
    long_term_vol = returns.expanding().std().mean()
    
    regime = pd.Series(index=returns.index, dtype=str)
    regime[rolling_vol < long_term_vol] = 'Low'
    regime[rolling_vol >= long_term_vol * threshold_mult] = 'High'
    regime[(rolling_vol >= long_term_vol) & 
           (rolling_vol < long_term_vol * threshold_mult)] = 'Medium'
    
    return regime, rolling_vol, long_term_vol
```

### HMM 體制識別

```python
from hmmlearn.hmm import GaussianHMM
import numpy as np

# 準備收益率數據
returns = np.array(daily_returns).reshape(-1, 1)

# 擬合 2 狀態 HMM
model = GaussianHMM(n_components=2, covariance_type="full", 
                     n_iter=1000, random_state=42)
model.fit(returns)

# 預測隱藏狀態
hidden_states = model.predict(returns)

# state 0 和 1 哪個是高波動看 variance
# variance 大的是高波動體制
```

## 模型的局限

### 1. 體制數量選擇
真實市場可能不止兩個體制，三分法（低/中/高）或四分法更接近現實，但更多體制 = 更多參數 = 更容易過擬合。

### 2. 轉換概率不穩定
歷史估計的轉換概率在不同市場環境下可能差異很大。2008 年前的轉換概率不適用於 2020 年的市場結構。

### 3. 滯後性
所有體制判斷方法都有滯後——等你確認進入高波動體制時，可能已經跌了 10%。預警訊號比確認訊號更有價值。

### 4. 過度依賴可能導致僵化
機械化的體制判斷可能在特殊情境下失靈（如政策干預導致波動率被壓制）。永遠保留主觀判斷的空間。

> 相關頁面：[[風險管理/過度擬合Overfitting量化判斷|過度擬合量化判斷]]、[[風險管理/模型風險Model Risk|模型風險]]

## 相關頁面

- [[風險管理/波動率的波動率VVIX-Volatility-of-Volatility|波動率的波動率 VVIX]] — 體制轉換的前瞻訊號
- [[風險管理/VIX恐慌指數實戰判讀|VIX 恐慌指數實戰判讀]] — 最常用的體制判斷工具
- [[風險管理/波動率目標策略Volatility-Targeting|波動率目標策略]] — 體制適應的部位管理
- [[操作策略/交易系統體制適應策略Adaptive-Trading-System|交易系統體制適應策略]] — 體制適應策略框架
- [[操作策略/市場體制識別Market-Regime-Detection|市場體制識別]] — 體制識別基礎
- [[操作策略/波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution|波動率期限結構與曲面演化]] — Term structure 倒掛預警
- [[風險管理/相關性崩潰Correlation-Breakdown|相關性崩潰]] — 高波動體制的特徵
- [[技術分析/赫斯特指數Hurst-Exponent|赫斯特指數 Hurst Exponent]] — 判斷趨勢vs均值回歸體制
- [[風險管理/動態部位管理Dynamic-Position-Sizing|動態部位管理]] — 根據體制動態調整部位
- [[風險管理/市場微結構與流動性定價Market-Microstructure-and-Liquidity-Pricing|市場微結構與流動性定價]] — 流動性與波動率的關係

---
*學習日期：2026-07-03*

## 實戰應用

（待補充）

## 注意事項

（待補充）

## 相關主題

（待補充）
