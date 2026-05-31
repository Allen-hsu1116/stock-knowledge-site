# Walk-Forward Analysis 滾動前進驗證

> 把歷史數據切成訓練和測試窗口，逐步前移——模擬真實交易中的決策過程，戳破「回測完美等於實戰完美」的幻想

## 核心概念

Walk-Forward Analysis（WFA，滾動前進驗證/前向優化）是解決回測過擬合問題的核心方法。它通過將歷史數據分為多個訓練窗口（樣本內）和測試窗口（樣本外），在每個訓練窗口優化參數，然後在對應的測試窗口驗證表現，滾動前進重複此過程。

### 為什麼需要 WFA？

傳統回測的致命問題：
- **全樣本優化**：用整段歷史數據找最佳參數，等於用未來資訊做決策
- **過度擬合**：策略過於「贴合」歷史數據，捕捉噪音而非規律
- **缺乏適應性驗證**：歷史表現好不代表未來也好

WFA 的核心思想：**模擬真實交易環境中的決策過程——你只能用當時已知的數據做決策，不能用未來數據。**

### WFA 流程圖解

```
時間軸：|====訓練1====|==測試1==|====訓練2====|==測試2==|====訓練3====|==測試3==|
         ← 優化參數 →  ← 驗證 →  ← 優化參數 →  ← 驗證 →  ← 優化參數 →  ← 驗證 →
```

每個窗口：
1. **訓練期（In-Sample）**：優化策略參數，找到最佳組合
2. **測試期（Out-of-Sample）**：用訓練期最佳參數在未見數據上驗證
3. **窗口前移**：訓練和測試窗口同時向右移動，重複上述步驟
4. **彙整所有樣本外結果**：拼接成完整的實戰模擬績效

## 實戰應用

### Step 1：選擇數據

- 必須包含不同市場條件（牛市、熊市、橫盤市）
- 數據長度至少覆蓋完整市場週期
- 台股建議至少5年以上數據，涵蓋多空循環

### Step 2：定義參數和指標

**優化參數**（舉例）：
- 移動平均線長度（如 10, 20, 30）
- 停損百分比（如 3%, 5%, 8%）
- RSI 門檻值（如 30/70, 25/75）

**績效指標**：
- 利潤因子（Profit Factor）
- 夏普比率（Sharpe Ratio）
- 最大回撤（MDD）
- 期望值（Expected Value）

### Step 3：設置窗口比例

**常見窗口設定**：

| 交易週期 | 訓練期 | 測試期 | 比例 |
|----------|--------|--------|------|
| 日內交易 | 6個月 | 1個月 | 6:1 |
| 波段交易 | 2年 | 6個月 | 4:1 |
| 長期投資 | 5年 | 1年 | 5:1 |

**原則**：訓練期至少是測試期的3-5倍，確保有足夠數據優化。

### Step 4：執行優化與測試

```
對每個窗口：
  1. 在訓練期優化參數 → 得到最佳參數組合
  2. 將最佳參數應用於測試期 → 記錄績效
  3. 窗口前移 → 進入下一個窗口
彙整所有測試期結果 → 得到真實績效估計
```

### Step 5：分析結果

**健康的 WFA 結果**：
- 樣本外表現 ≥ 樣本內表現的 50%（Walk-Forward Efficiency ≥ 50%）
- 所有窗口都有正期望值（不要求每個窗口都賺，但不能大虧）
- 最佳參數在不同窗口間穩定變化（而非跳來跳去）

**危險信號**：
- 樣本外表現遠低於樣本內 → 過度擬合
- 不同窗口最佳參數差異極大 → 策略不穩健
- 某些窗口大幅虧損 → 策略不適應某些市況

### WFA 效率比（Walk-Forward Efficiency）

$$WFE = \frac{\text{樣本外年化報酬}}{\text{樣本內年化報酬}} \times 100\%$$

- WFE > 50%：策略穩健，值得實戰
- WFE 30-50%：策略可能需要簡化
- WFE < 30%：策略過度擬合，需要重新設計

## 注意事項

### 計算強度問題
- WFA 需要大量計算資源和時間
- 參數越多，組合越多，計算時間指數增長
- 建議先用粗略參數範圍快速篩選，再用精細參數深入優化

### 窗口長度選擇
- 訓練期太短：參數不穩定，容易受噪音影響
- 訓練期太長：無法適應市場結構變化
- 測試期太短：統計顯著性不足
- 測試期太長：市場可能已經發生結構性變化

### 數據品質
- 必須使用 Point-in-Time 數據
- 修正後的財報數據會引入前瞻偏差
- 確保訓練集和測試集不重疊（數據洩露）

### 避免數據洩露
- 訓練集和測試集嚴格不可重疊
- 不用測試期數據來選擇策略類型
- 不反覆修改策略直到樣本外「好看」——這只是換個方式過擬合

### WFA 不是萬能的
- 即使 WFA 通過，實盤仍可能失敗（制度變化、流動性枯竭等）
- WFA 驗證的是「策略在過去市場環境下的適應性」，不保證未來
- 需要搭配 [[蒙地卡羅模擬交易驗證Monte-Carlo-Simulation|蒙地卡羅模擬]] 做壓力測試

## Python 實作框架

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import ParameterGrid

def walk_forward_analysis(data, strategy_func, param_grid, 
                          train_size, test_size):
    """Walk-Forward Analysis 基本框架"""
    results = []
    train_start = 0
    
    while train_start + train_size + test_size <= len(data):
        train_end = train_start + train_size
        test_end = train_end + test_size
        
        train_data = data[train_start:train_end]
        test_data = data[train_end:test_end]
        
        # 在訓練期找最佳參數
        best_params = None
        best_score = -np.inf
        for params in ParameterGrid(param_grid):
            score = strategy_func(train_data, **params)
            if score > best_score:
                best_score = score
                best_params = params
        
        # 用最佳參數在測試期驗證
        test_score = strategy_func(test_data, **best_params)
        
        results.append({
            'train_period': (train_start, train_end),
            'test_period': (train_end, test_end),
            'best_params': best_params,
            'train_score': best_score,
            'test_score': test_score
        })
        
        # 窗口前移
        train_start += test_size
    
    return pd.DataFrame(results)

# 使用範例
results = walk_forward_analysis(
    data=price_data,
    strategy_func=ma_crossover_strategy,
    param_grid={'fast': [5,10,20], 'slow': [30,50,60]},
    train_size=500,
    test_size=100
)

# 計算 WFA 效率比
wfe = results['test_score'].mean() / results['train_score'].mean()
print(f"WFA Efficiency: {wfe:.1%}")
```

## 相關主題

- [[回測框架與偏差防範Backtesting-Framework-and-Bias-Prevention|回測框架與偏差防範]]
- [[回測過擬合Backtest-Overfitting|回測過擬合]]
- [[過度擬合Overfitting量化判斷|過度擬合量化判斷]]
- [[蒙地卡羅模擬交易驗證Monte-Carlo-Simulation|蒙地卡羅模擬]]
- [[策略壓力測試Stress-Testing|策略壓力測試]]
- [[交易策略回測與過擬合Backtesting-and-Overfitting|交易策略回測與過擬合]]
- [[交易系統Trading-System設計與迷思|交易系統設計與迷思]]
- [[交易策略開發流程Trading-Strategy-Development-Workflow|交易策略開發流程]]

## 來源

- [Walk Forward Optimization 讓回測與實戰永不脫節 - 老余的智能顧投](../raw/2026-05-10/Walk-Forward-Optimization前向優化.md)
- [回測框架與偏差防範](../raw/2026-05-02/交易策略開發流程與回測框架.md)