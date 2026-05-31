# 階層式風險平價 HRP（Hierarchical Risk Parity）

> 用機器學習的聚類演算法把相關性矩陣從完全圖降維成樹狀結構，解決MPT對參數過度敏感的問題——第五代資產配置理論

## 核心概念

### 為什麼需要 HRP？

傳統馬可維茲投資組合理論（MPT/MVO）有一個致命缺陷：**對參數極度敏感**。稍微改變預期收益或相關係數，最終的配置比例就天差地別。

Lopez de Prado（2016）找到根本原因：相關係數矩陣的 **condition number** 過高。在圖論上，相關係數矩陣等價於 **complete graph**（完全圖）——每個節點和每個節點之間都有連線，太多不必要的 edges 導致過多雜訊。

HRP 的解法：把完全圖**剪枝降維成二叉樹**，只保留有層級結構的資訊。

### 資產配置理論的五個世代

| 世代 | 理論 | 核心思想 |
|------|------|----------|
| 第一代 | 1/N 均分 | 不考慮任何參數，平均分配 |
| 第二代 | MVO（馬可維茲） | 同時考量風險和報酬，最優化 |
| 第三代 | Black-Litterman | 合理化預期報酬，修正MVO |
| 第四代 | Risk Parity（風險平價） | 放棄預期收益，只從風險出發 |
| 第五代 | HRP（階層式風險平價） | 用聚類演算法降維相關性矩陣 |

### HRP 三大步驟

**Step 1: Tree Clustering（樹狀聚類）**
- 對相關係數矩陣執行聚類演算法
- 將資產依照相關性分成群組
- 產生樹狀結構（dendrogram）

**Step 2: Quasi-Diagonalization（準對角化）**
- 將相關係數矩陣依照 Step 1 的聚類結果重新排序
- 高相關的資產被排在一起
- 矩陣對角線附近聚集高相關區塊

**Step 3: Recursive Bisection（遞迴二分法）**
- 依照二叉樹結構迭代更新權重
- 從樹的頂端開始，每個節點將權重在左右子樹間分配
- 分配方式：根據兩側子樹的變異數反比分配
- 底層實作可用 bottom-up 遞迴法（比原論文的 top-down 方法更穩定）

### 數學基礎

**Long-Only 下的 IVP（反變異數組合）：**

在 long-only 約束下，MVO 的封閉解退化為反變異數組合：
- wᵢ ∝ 1/σᵢ²

**HRP 的權重分配：**

在二叉樹結構下，每個節點的權重分配：
- 左子樹權重 ∝ 1/σ²_left
- 右子樹權重 ∝ 1/σ²_right
- 正規化後分配到子樹中的各資產

## 實戰應用

### Python 實作（簡易版）

```python
import numpy as np
import seaborn as sns
from scipy.cluster.hierarchy import linkage, leaves_list

def hrp_weights(cov_matrix, corr_matrix):
    # Step 1 & 2: Clustering and Quasi-Diagonalization
    link = linkage(corr_matrix, method='ward')
    order = leaves_list(link)
    
    # Step 3: Recursive Bisection
    weights = recursive_bisection(cov_matrix, order)
    return weights

def recursive_bisection(cov, order):
    n = len(order)
    if n == 1:
        return pd.Series(1.0, index=[order[0]])
    
    mid = n // 2
    left_items = order[:mid]
    right_items = order[mid:]
    
    left_var = get_cluster_var(cov, left_items)
    right_var = get_cluster_var(cov, right_items)
    
    alpha = 1 - left_var / (left_var + right_var)
    
    left_weights = recursive_bisection(cov, left_items) * alpha
    right_weights = recursive_bisection(cov, right_items) * (1 - alpha)
    
    return pd.concat([left_weights, right_weights])
```

### 快速視覺化聚類

```python
import seaborn as sns
sns.clustermap(corr_matrix)  # 一行完成 Step 1 & 2
```

### HRP vs 其他配置方法

| 方法 | 優點 | 缺點 |
|------|------|------|
| 1/N | 簡單、穩健 | 完全忽略資產特性 |
| MVO | 理論最優 | 對參數極度敏感 |
| 風險平價/ERC | 分散風險 | 相關性高時失效 |
| HRP | 穩健、抗參數敏感性 | 實務驗證尚不足 |
| MinVar | 低波動 | 偏向低波動資產 |

### 蒙地卡羅模擬驗證

Lopez de Prado 原論文的模擬結果顯示：
- HRP 的表現優於 MVO 和 ERC
- Bottom-up 遞迴法比原論文的 top-down 方法至少好 10%
- 不論修改何種 Linkage 方法（Ward, Average, Complete 等），bottom-up 都勝出

## 注意事項

### 業界採用現況

- 目前業界仍以 **Barra Risk Model** 為主流風控工具
- Lopez de Prado 加入 AQR（量化界知名公司）後不到一年就離職，暗示理論與實務仍有差距
- HRP 在學術上具有突破性，但實際投資組合管理的採用率仍低

### 限制與挑戰

1. **聚類方法的選擇**：Ward、Average、Complete 等不同 linkage 方法會產生不同的樹狀結構
2. **歷史數據依賴**：相關係數矩陣仍基於歷史數據估算，未來可能不同
3. **再平衡成本**：頻繁調整權重產生交易成本
4. **缺乏預期收益**：和風險平價一樣，不考慮預期收益
5. **實務驗證不足**：雖然蒙地卡羅模擬表現好，但實盤數據有限

### 條件數問題的本質

相關係數矩陣的 condition number = 最大特徵值 / 最小特徵值

- Condition number 越大 → 矩陣越「病態」→ 小的參數變動造成大的權重變化
- HRP 透過聚類降維，實質上是在減少 condition number
- 這是為什麼 HRP 比 MVO 更穩健的數學根源

## 相關主題

- [[風險平價策略Risk-Parity]]
- [[風險預算Risk Budgeting]]
- [[投資組合相關性分析實戰Portfolio-Correlation-Analysis-in-Practice]]
- [[相關性風險Correlation-Risk]]
- [[模型風險Model Risk]]
- [[回測過擬合Backtest-Overfitting]]
- [[資產配置策略比較Asset-Allocation-Comparison]]
- [[分散投資七法與相關係數Diversification-Seven-Methods]]
- [[投資組合理論與分散投資的局限Portfolio-Theory-and-Diversification-Limits]]

## 來源

- [第五代資產配置理論：階層式風險平價 - Hayden海頓君](../raw/2026-05-15/階層式風險平價HRP-Hayden.md)
- [Risk Parity 策略和全天候基金 - 狂徒](../raw/2026-05-15/風險平價策略與全天候基金-狂徒.md)