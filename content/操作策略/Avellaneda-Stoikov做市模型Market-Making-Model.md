---
title: "Avellaneda-Stoikov 做市模型 Avellaneda-Stoikov Market Making Model"
category: "操作策略"
---

# Avellaneda-Stoikov 做市模型 Avellaneda-Stoikov Market Making Model

> 經典做市商庫存管理模型，在風險中性和庫存風險之間找到最優報價。

## 核心概念

**Avellaneda-Stoikov 模型** 由 Marco Avellaneda 和 Sasha Stoikov 於 2008 年在 *High-Frequency Trading: A Practical Guide to Algorithmic Strategies and Trading Systems* 中提出。它是做市商定價的數學框架，解決一個核心問題：**做市商如何在提供流動性的同時管理庫存風險？**

## 做市商的基本困境

做市商靠買賣價差（bid-ask spread）賺錢，但面臨兩個對立風險：

1. **庫存風險（Inventory Risk）**：掛單被成交後持有部位，價格可能往不利方向移動
2. **機會成本（Missed Trades）**：報價太寬不成交，賺不到價差

Avellaneda-Stoikov 模型的核心貢獻是引入**效用函數**來動態調整報價，在兩者間取得最優平衡。

## 模型設定

### 基本假設

- 基礎價格 S(t) 服從布朗運動：dS = σdW
- 做市商目標是在時間 T 最大化期末財富的指數效用
- 效用函數：U(x) = -exp(-γx)，γ 為風險趨避係數
- 買單和賣單的到達服從泊松過程，強度與報價偏移量相關

### 最優報價公式

做市商的最優買賣報價為：

**買價（Bid）：** r_b = S - δ_b

**賣價（Ask）：** r_a = S + δ_a

其中偏移量：

**δ_b = δ_a = γσ²(T-t)/2 + (1/γ) × ln(1 + γ/κ)**

- **S**：參考價格（mid-price 或公允價值）
- **σ**：價格波動率
- **T-t**：剩餘時間
- **γ**：風險趨避係數
- **κ**：訂單到達強度對報價偏移的敏感度

## 關鍵洞察

### 1. 對稱報價 → 非對稱報價

基本模型在無庫存時報價對稱（δ_b = δ_a）。但模型的核心創新是引入**庫存因子**：

當做市商持有正庫存（做多）時：
- 賣價降低（更願意賣出平倉）
- 買價也降低（不願意繼續買入）

當做市商持有負庫存（做空）時：
- 買價升高（更願意買入平倉）
- 賣價也升高（不願意繼續賣出）

### 2. 庫存調整公式

引入庫存 q 後的最優報價：

**r_b = S - δ_b - q × γσ²(T-t)**

**r_a = S + δ_a - q × γσ²(T-t)**

- **q > 0**（多庫存）：整體報價下移，傾向賣出
- **q < 0**（空庫存）：整體報價上移，傾向買入
- **q = 0**（中性）：對稱報價

### 3. 時間效應

隨著 t → T（收盤逼近）：
- γσ²(T-t) → 0，庫存調整項消失
- 做市商在收盤前傾向清空庫存
- 報價回到接近對稱但偏移量增大（因 ln 項不變）

## 與其他做市模型比較

### vs Guéant-Tapia 模型
- Guéant-Tapia (2013) 是 Avellaneda-Stoikov 的簡化版本
- 提供封閉解近似，計算更快速
- 適合高頻交易的即時報價更新

### vs [[操作策略/高頻交易與做市策略High-Frequency-Trading-and-Market-Making|一般做市策略]]
- 一般做市策略用經驗法則設定價差和庫存限制
- Avellaneda-Stoikov 提供嚴格的數學最優化框架
- 實務中常混合使用：用 A-S 模型算基準報價，再用經驗法則微調

### vs [[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle's Lambda 模型]]
- Kyle 模型描述大單對價格的衝擊（執行面）
- Avellaneda-Stoikov 描述做市商如何報價（定價面）
- 兩者互補：Kyle 告訴你大單怎麼影響市場，A-S 告訴你做市商怎麼應對

## 數學推導簡述

1. 定義做市商財富過程 X(t) 和庫存 q(t)
2. 目標函數：maximize E[U(X(T) + q(T)×S(T))]
3. 用動態規劃求解 HJB 方程
4. 假設指數效用函數可得解析解
5. 最優報價為儲備價格 ± 偏移量 ± 庫存調整

完整的 HJB 方程推導涉及隨機控制理論，有興趣可參考原論文。

## 實戰應用

### 1. 參數估計
- **σ（波動率）**：用近期高頻數據估計，可用 ATR 或 realized volatility
- **κ（訂單強度）**：觀察歷史掛單成交率與報價偏移的關係
- **γ（風險趨避）**：主觀設定，γ 越大越保守，γ → 0 為風險中性
- **T（時間窗口）**：日內做市設為收盤時間，也可設滾動窗口

### 2. 散戶可以學到什麼
- **理解造市商行為**：當你看到買賣價突然不對稱，可能是造市商在調整庫存
- **流動性成本估算**：大型訂單執行時可參考 A-S 模型估算造市商會怎麼移動報價
- **搭配 [[操作策略/VWAP執行演算法與機構交易策略VWAP-Execution-Algorithms|VWAP 執行演算法]]**：了解做市商報價行為有助於優化大單執行策略
- **搭配 [[技術分析/訂單流失衡OFI-Order-Flow-Imbalance|訂單流失衡 OFI]]**：A-S 模型的庫存調整會在 OFI 上留下足跡

### 3. 限制與挑戰
- **假設過強**：布朗運動假設不適用跳空缺口和極端事件
- **對手風險**：模型假設對手方隨機到達，實際可能有知情交易者（adverse selection）
- **多做市商競爭**：模型只考慮單一做市商，實際市場中多個做市商競爭會壓縮價差
- **參數不穩定**：κ 和 σ 在不同市場狀態下波動劇烈
- **結算風險**：收盤強制清倉假設不適用可隔夜持有的策略

## 注意事項

### 在台股的應用限制
- 台股無正式做市商制度（除少數權證造市）
- 但可應用於：
  - **選擇權造市**：期貨商自營部門可參考 A-S 模型管理選擇權部位
  - **ETF 套利**：創造/贖回機制中的報價可參考
  - **了解外資行為**：外資大單執行時的造市商反應可預測
- 台股漲跌幅限制（10%）使模型中的波動率假設需要修正
- 處置股制度抽流動性，與 A-S 模型的連續交易假設衝突（可參考 [[YouTube頻道/股癌-Gooaye/EP684-Situational-Awareness清算事件與流動性陷阱|股癌 EP684 流動性陷阱]]）

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Avellaneda, M. & Stoikov, S. (2008). "High-frequency trading in a limit order book." *Quantitative Finance*, 8(3), 217-224.
- Guéant, O. & Tapia, M. (2013). "Dealing with the inventory risk: a solution to the market making problem." *Mathematics and Financial Economics*, 7(4), 477-507.
- Cartea, Á., Jaikumar, S. & Penalva, J. (2015). *Algorithmic and High-Frequency Trading*. Cambridge University Press.

---

*學習日期：2026-08-12*
