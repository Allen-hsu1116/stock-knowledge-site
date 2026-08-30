---
title: "平方根法則與市場衝擊 Square Root Law of Market Impact"
category: "操作策略"
---

# 平方根法則與市場衝擊 Square Root Law of Market Impact

> 你買越多，價格衝擊越大——但不是線性放大，而是按成交量的平方根成長。買2倍的量，衝擊只增加√2≈1.41倍。這條經驗法則跨越股票、債券、期貨、外匯，是全球市場微結構中最穩健的實證規律之一。

## 核心概念

**平方根法則（Square Root Law）** 描述交易量與市場衝擊之間的非線性關係：市場衝擊與交易量的平方根成正比。

**核心公式**：

$$\Delta P \propto \sigma \cdot \sqrt{\frac{Q}{V}}$$

其中：
- ΔP = 價格衝擊
- σ = 日波動率
- Q = 訂單量（Order Size）
- V = 日成交量（Daily Volume）
- Q/V = 參與率（Participation Rate）

**含義**：
- 買2倍量 → 衝擊 √2 ≈ 1.41倍（不是2倍）
- 買4倍量 → 衝擊 2倍
- 買9倍量 → 衝擊 3倍
- 衝擊隨量增加但增速遞減——這就是「平方根」的力量

## 為什麼是平方根？

### 理論解釋

平方根法則沒有單一的理論推導，但多個微結構模型自然產生平方根關係：

**1. Kyle（1985）模型推導**
- [[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle's Lambda]] 線性模型中 ΔP = λQ
- 但 Kyle 模型的 λ 本身取決於交易者信號品質和成交量
- 當考慮 λ 的內生性時，淨效果接近平方根

**2. Almgren-Chriss 模型**
- [[操作策略/Almgren-Chriss最優執行模型Almgren-Chriss-Optimal-Execution|Almgren-Chriss 模型]]將衝擊分為永久和暫時兩部分
- 永久衝擊 η × Q 線性、暫時衝擊 ε × √Q 非線性
- 實證中暫時衝擊主導，淨效果接近平方根

**3. 隨機遊走解釋**
- 價格變動本質上具有隨機遊走特性
- N 筆交易的累積價格變動標準差 = σ × √N
- 大訂單拆成 N 筆執行，總衝擊自然呈 √N 規模

**4. 流動性提供者行為**
- 大訂單消耗限價單簿的流動性
- 每多執行一筆，消耗的流動性越深層（距中間價越遠）
- 限價單簿的形狀決定了非線性衝擊，平方根是最佳擬合

## 實證驗證

### Almgren et al.（2005）的開創性實證

- 分析美國股票市場大量機構交易數據
- 確認衝擊與 √Q 的關係在 0.5-0.7 指數範圍內最穩健
- 不同市值、不同流動性的股票都服從平方根法則

### Zarinelli et al.（2015）的修正

- 超過15萬筆大單實證發現，平方根法則在中等規模交易中最準確
- 小型交易（Q/V < 1%）的衝擊可能低於平方根預測（線性更接近）
- 超大交易（Q/V > 30%）的衝擊可能高於平方根預測（對數關係更好）
- 但在 1%-30% 參與率區間，平方根法則是最佳近似

### 跨市場驗證

平方根法則已在以下市場驗證：
- 美股（Almgren et al. 2005）
- 歐股（Donier 2015）
- 日本股市（Tóth et al. 2015）
- 外匯市場（Gabaix et al. 2006）
- 加密貨幣（Kyle et al. 2021）
- 台股（雖無正式學術研究，但法人實務經驗一致）

## 衝擊係數估計

```
衝擊成本（以 bps 為單位）≈ c × σ × √(Q/V)

其中 c 為市場特定常數：
  - 大型流動性好的股票：c ≈ 0.5-1.0
  - 中型股：c ≈ 1.0-2.0
  - 小型股/流動性差：c ≈ 2.0-5.0
  - 台股加權指數期貨：c ≈ 0.3-0.5

範例：
  台積電日成交量 50,000 張，日波動率 2%
  買入 5,000 張（參與率 10%）
  衝擊 ≈ 1.0 × 2% × √(5000/50000) = 1.0 × 2% × 0.447 = 0.89%
  即約 89 bps 的價格衝擊
```

## 與相關概念的關聯

- **與[[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle's Lambda]]**：Lambda 是線性衝擊模型，平方根法則是非線性修正——Lambda 衡量 ΔP/Q，平方根法則衡量 ΔP/√Q
- **與[[操作策略/Almgren-Chriss最優執行模型Almgren-Chriss-Optimal-Execution|Almgren-Chriss 模型]]**：平方根法則是 Almgren-Chriss 暫時衝擊項的實證基礎
- **與[[操作策略/交易成本分析Transaction-Cost-Analysis|交易成本分析 TCA]]**：平方根法則是衝擊成本預估的核心工具
- **與[[風險管理/Amihud非流動性指標Amihud-Illiquidity-Measure|Amihud 非流動性指標]]**：Amihud 衡量每單位成交金額的價格衝擊，與平方根法則的 c 係數直接相關
- **與[[風險管理/流動性風險Liquidity-Risk|流動性風險]]**：平方根法則的 c 係數越高，流動性風險越大
- **與[[風險管理/滑價與交易執行風險|滑價與交易執行風險]]**：滑價的根源就是市場衝擊，平方根法則提供滑價的量化預估
- **與[[操作策略/高頻交易與做市策略High-Frequency-Trading-and-Market-Making|高頻交易與做市策略]]**：HFT 做市商利用平方根法則定價——大單的衝擊讓他們在價差中獲利更多
- **與[[基本面分析/流動性溢價Liquidity-Premium|流動性溢價]]**：平方根法則解釋了為什麼低流動性資產要求更高報酬——高衝擊成本是流動性溢價的微觀來源

## 歷史背景

- **Kyle（1985）**：線性衝擊模型的奠基，為平方根法則提供理論起點
- **Almgren & Chriss（1999/2000）**：最優執行模型將非線性衝擊正式納入
- **Almgren et al.（2005）**：首次大規模實證確認平方根法則，被業界廣泛採用
- **Bouchaud et al.（2004）**：從統計物理角度解釋平方根的來源
- **Gabaix et al.（2006）**：提出基於冪律分佈的理論框架解釋平方根法則的普適性
- **Zarinelli et al.（2015）**：用更大數據修正，指出對數關係在極端交易中更優

## 實戰應用

### 散戶的隱形成本意識

散戶訂單通常 Q/V < 0.1%，平方根法則預測的衝擊微乎其微。但以下情境需注意：

1. **小型股大單**：日成交量100張的冷門股，一次買50張=50%參與率，衝擊可達 3-5%
2. **處置股交易**：處置股流動性極差，即使小單衝擊也被放大
3. **隔夜跳空後搶進**：開盤前五分鐘大量限價單被吃光，實際衝擊遠超預期
4. **融資斷頭潮**：大量強制平倉同方向湧出，市場衝擊非線性暴增

### 法人執行策略

平方根法則直接決定法人的拆單策略：

- **VWAP 執行**：按成交量分佈分配，最小化 Q/V 的尖峰——與[[操作策略/VWAP執行演算法與機構交易策略VWAP-Execution-Algorithms|VWAP 執行演算法]]直接關聯
- **TWAP 執行**：時間均分，適合成交量平穩時段
- **IS 執行**：動態平衡衝擊成本與時間風險——與[[操作策略/實施短缺與最佳執行Implementation-Shortfall-and-Best-Execution|實施短缺與最佳執行]]關聯
- **參與率上限**：機構通常限制 Q/V < 10-15% 避免衝擊失控

### 交易成本預估公式

```
總成本（bps）= 手續費 + 衝擊成本 + 滑價

手續費 = 固定（台股 0.1425% = 14.25 bps）
衝擊成本 ≈ c × σ × √(Q/V) × 10000 bps
滑價 = 0.5 × 衝擊成本（保守估計）

範例：買台積電 1000 張
  日成交量 50000 張，σ = 2%，c = 1.0
  衝擊 = 1.0 × 2% × √(1000/50000) = 1.0 × 2% × 0.141 = 0.283% = 28.3 bps
  滑價 ≈ 14 bps
  總成本 ≈ 14.25 + 28.3 + 14 = 56.6 bps
  若台積電 1000 元，每張 1000 股 = 100 萬
  1000 張 × 100 萬 × 0.566% = 566 萬的交易成本
```

## 注意事項
- **僅適用正常市場條件**：在極端壓力下（如2020年3月COVID拋售），衝擊可能遠超平方根預測
- **不考慮方向性資訊**：平方根法則假設訂單無資訊含量，但知情交易者的衝擊遠大於不知情——需搭配[[籌碼面分析/VPIN訂單流毒性指標Volume-Synchronized-PIN|VPIN]]過濾
- **市場碎裂影響**：同一標的在多個場所交易時，單一場所的 V 被高估，衝擊預測偏低
- **非線性區間限制**：超大交易（Q/V > 30%）的衝擊偏離平方根（Zarinelli et al. 2015 指出可能更接近對數）
- **台股特殊性**：漲跌幅限制 10%、處置股制度、盤中瞬間價格穩定措施等都會扭曲平方根法則的適用性

## 相關主題

- [[操作策略/操作策略總論]]

## 來源
- Almgren, R., Thum, C., Hauptmann, E. & Li, H. (2005). "Direct Estimation of Equity Market Impact." *Risk*, 18(7), 57-62.
- Bouchaud, J.P., Gefen, Y., Potters, M. & Wyart, M. (2004). "Fluctuations and Response in Financial Markets." *Quantitative Finance*, 4(2), 176-190.
- Gabaix, X., Gopikrishnan, P., Plerou, V. & Stanley, H.E. (2006). "Institutional Investors and Stock Market Volatility." *Quarterly Journal of Economics*, 121(2), 461-504.
- Kyle, A. (1985). "Continuous Auctions and Insider Trading." *Econometrica*, 53(6), 1315-1335.
- Zarinelli, E., Treccani, M., Farmer, J.D. & Lillo, F. (2015). "Beyond the Square Root: Evidence for Logarithmic Dependence of Market Impact on Size and Participation Rate." *Market Microstructure and Liquidity*, 1(2), 1550004.

---

*學習日期：2026-08-14*
*來源：Wikipedia Market Impact、Almgren et al. (2005) 學術論文、Zarinelli et al. (2015) 修正研究*
