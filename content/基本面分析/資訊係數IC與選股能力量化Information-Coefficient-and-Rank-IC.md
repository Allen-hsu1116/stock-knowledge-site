---
title: "資訊係數IC與選股能力量化 Information Coefficient & Rank IC"
category: "基本面分析"
---

# 資訊係數IC與選股能力量化 Information Coefficient & Rank IC

> 量化選股能力的標準答案——IC衡量預測與實際報酬的相關性，Rank IC更穩健地用Spearman等級相關避開極端值干擾，IR=IC×√BR揭示選股能力×交易頻率的乘法關係

## 核心定義

**資訊係數（Information Coefficient, IC）** 衡量預測值與實際結果之間的線性相關程度，是量化投資中衡量選股預測能力的核心指標

- IC 範圍 -1 到 +1
- IC=0：預測無效（沒有選股能力）
- IC=+1：完美正相關（預測完全準確）
- IC=-1：完美負相關（預測完全反向）

**Rank IC** 是 IC 的穩健版本，用 Spearman 等級相關取代 Pearson 相關，對極端值不敏感

## Pearson IC vs Rank IC

### Pearson IC（傳統IC）
$$IC_{Pearson} = \text{corr}(\hat{R}_i, R_i)$$

- $\hat{R}_i$ = 預測報酬率
- $R_i$ = 實際報酬率
- 計算所有股票預測值和實際值的 Pearson 相關係數

**問題**：極端值影響大——一檔股票暴漲200%會嚴重扭曲結果

### Rank IC（Spearman IC）
$$IC_{Rank} = \text{corr}(\text{rank}(\hat{R}_i), \text{rank}(R_i))$$

- 先把預測值和實際值轉換為排名
- 再計算排名的 Pearson 相關（等於 Spearman 相關）
- 對極端值免疫——第1名就是第1名不管贏多少

**為什麼量化基金偏好 Rank IC**：
- 金融報酬率分佈有肥尾，極端值頻繁
- 選股只關心排序（買前10%賣後10%），不關心絕對報酬率
- Rank IC 更穩定、更可重現

## IC 值的判讀標準

| IC 範圍 | 選股能力 | 說明 |
|---------|----------|------|
| |IC| < 0.02 | 無能力 | 與隨機選股無異 |
| 0.02 ≤ |IC| < 0.05 | 弱 | 有微弱訊號但交易成本可能吃掉 |
| 0.05 ≤ |IC| < 0.10 | 中等 | 專業量化基金常見水準 |
| 0.10 ≤ |IC| < 0.15 | 強 | 優秀量化基金水準 |
| |IC| ≥ 0.15 | 極強 | 頂級或可能過度擬合 |

**重要提醒**：
- IC=0.05 看起來很低，但在幾千檔股票中已經是顯著的選股能力
- IC>0.15 在實務中極為罕見，回測中出現通常意味過度擬合
- 正IC = 做多預測高分、做空預測低分
- 負IC = 預測完全反向（反向操作或訊號定義錯誤）

## IC 的時間序列分析

### IC 的穩定性
單期IC無意義，必須看IC的時間序列：
- **IC均值**：長期平均預測能力
- **IC標準差**：預測能力的穩定性
- **ICIR（IC Information Ratio）** = IC均值 / IC標準差
- ICIR > 0.5 算穩健的策略

### IC 衰減 Decay
- 預測能力隨時間衰減是常態
- 短期IC（1週）vs 長期IC（3個月）反映不同因子特性
- 動能因子短期IC高、價值因子長期IC高
- IC 衰減曲線是策略容量規劃的關鍵輸入

## IR = IC × √BR

**信息比率（Information Ratio, IR）** 與 IC 的數學關係：

$$IR = IC \times \sqrt{BR}$$

- **BR（Breadth）** = 每年獨立預測的次數
- IC=0.05、每年預測200次 → IR = 0.05 × √200 = 0.71
- IC=0.10、每年預測50次 → IR = 0.10 × √50 = 0.71

**啟示**：
- 低IC可以靠高頻率補償（高頻交易邏輯）
- 高IC可以靠低頻率達成（深度價值投資）
- 兩者殊途同歸到相同的IR
- 詳見 [[風險管理/信息比率與追蹤誤差Information-Ratio-and-Tracking-Error|信息比率與追蹤誤差]]

## 主動管理基本法則 Fundamental Law of Active Management

Grinold & Kahn 的主動管理基本法則：

$$IR = IC \times \sqrt{BR} \times \sqrt{TC}$$

- **TC（Transfer Coefficient）**：預測轉化為實際部位的效率
- TC=1 代表完全執行預測信號
- TC<1 代表有限制（流動性、風險控管、交易成本）
- 實務中 TC 通常 0.3-0.7

**核心洞見**：選股能力（IC）× 交易廣度（BR）× 執行效率（TC）三者缺一不可

## 實戰應用

### 1. 因子選股能力評估
- 計算每個因子的月度 Rank IC 時間序列
- 比較不同因子的IC穩定性（ICIR）
- 價值因子（PBR、PER）→ 長期IC穩定
- 動能因子（12個月動能）→ 短期IC爆發但衰減快
- 品質因子（ROE、GPA）→ 中期IC穩定
- 詳見 [[基本面分析/基本面因子選股總論Quantitative-Fundamental-Factors|基本面因子選股總論]]

### 2. 分析師預測能力評估
- 分析師預測的 IC 是其專業能力的量化
- 追蹤IC時間序列找出持續有能力的分析師
- 詳見 [[基本面分析/盈餘修正比率與分析師預估修正Earnings-Revision-Ratio|盈餘修正比率與分析師預估修正]]

### 3. 策略組合優化
- 不同因子IC的相關性 → 多因子組合
- 低相關IC的因子組合分散效果最好
- 詳見 [[操作策略/Smart-Beta因子投資策略|Smart Beta 因子投資策略]]

### 4. 台股實戰
- 月營收公告後的IC分析：營收動能因子在公告後3-5天IC最高
- 法說會預期差的IC：超預期的公司在之後1個月有正IC
- 詳見 [[基本面分析/盈餘公告後價格漂移PEAD|盈餘公告後價格漂移PEAD]]

## IC 的局限與陷阱

### 1. 線性假設
- Pearson IC 只衡量線性關係
- 非線性關係（如U型因子）IC可能接近零但實際有用
- 解法：用機器學習模型或分段計算IC

### 2. 倖存者偏差
- 退市公司的預測和報酬率被排除
- 退市公司通常是預測失敗的 → 高估IC
- 解法：使用包含退市公司的完整數據庫

### 3. 前瞻偏差
- 回測中使用未來資訊計算IC
- 如用年報數據在公告日前就計算IC
- 解法：嚴格使用 point-in-time 數據

### 4. 因子擁擠
- 高IC因子被發現後資金湧入 → IC衰減
- 詳見 [[風險管理/因子衰退Factor-Decay|因子衰退]]
- 監控IC時間序列是偵測因子擁擠的即時指標

### 5. 樣本不足
- 台股約1500檔，單月IC的統計顯著性低
- 需要至少3-5年月度IC才能判斷穩定性
- 新上市公司的IC數據不足

## IC 與其他績效指標的關係

| 指標 | 衡量什麼 | 與IC的關係 |
|------|----------|-----------|
| IR | 主動報酬/追蹤誤差 | IR = IC × √BR |
| Sharpe | 超額報酬/總風險 | 高IC策略通常高Sharpe |
| Hit Rate | 預測正確比例 | IC高不代表Hit Rate高 |
| 回測報酬 | 策略絕對報酬 | IC是報酬的因，報酬是果 |

## 相關連結

- [[風險管理/信息比率與追蹤誤差Information-Ratio-and-Tracking-Error|信息比率與追蹤誤差]]
- [[基本面分析/基本面因子選股總論Quantitative-Fundamental-Factors|基本面因子選股總論]]
- [[基本面分析/Fama-French多因子模型Fama-French-Multi-Factor-Model|Fama-French多因子模型]]
- [[操作策略/Smart-Beta因子投資策略|Smart Beta 因子投資策略]]
- [[基本面分析/盈餘公告後價格漂移PEAD|盈餘公告後價格漂移PEAD]]
- [[基本面分析/盈餘修正比率與分析師預估修正Earnings-Revision-Ratio|盈餘修正比率與分析師預估修正]]
- [[風險管理/因子衰退Factor-Decay|因子衰退]]
- [[風險管理/回測績效評估完整體系Backtest-Performance-Evaluation|回測績效評估完整體系]]

---

**來源**: Wikipedia Information Coefficient 條目；Grinold & Kahn《Active Portfolio Management》；量化投資實務
**建立日期**: 2026-07-23

## 核心概念
（待補充）


## 注意事項
（待補充）


## 相關主題
（待補充）

## 來源

- 待補：本頁目前沒有可核對的原始來源連結。
