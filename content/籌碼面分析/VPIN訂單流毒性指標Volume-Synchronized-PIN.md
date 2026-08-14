# VPIN訂單流毒性指標 Volume-Synchronized PIN

> 2010年閃電崩盤前一小時，VPIN 就已經發出了警報。Easley, López de Prado & O'Hara 用成交量時間取代時鐘時間，量化「知情交易者」何時大舉進場——這是市場微結構中最具實戰價值的毒性預警指標。

## 核心概念

**VPIN（Volume-Synchronized Probability of Informed Trading）** 是 Easley, López de Prado & O'Hara（2012）在《Flow Toxicity and Liquidity in a High-Frequency World》中提出的訂單流毒性即時指標。它是經典 PIN 模型的改良版，解決了 PIN 估計需要長期歷史數據、無法即時計算的問題。

**訂單流毒性（Flow Toxicity）** 指的是知情交易者（informed traders）佔總交易的比例。當知情交易者活躍時，造市商被「毒」到（adverse selection）——他們在不知情下提供了流動性，卻被知情者「收割」。毒性越高，造市商越傾向撤退，流動性枯竭，閃電崩盤風險升高。

## PIN 到 VPIN 的演進

### 經典 PIN 模型

Easley & O'Hara（1992） original PIN 模型：
- 假設每天有 α 機率發生資訊事件
- 知情交易者以 μ 速率交易
- 不知情交易者以 ε 速率買賣
- **PIN = αμ / (αμ + 2ε)**：知情交易佔總交易的比例
- 缺點：需要最大概似估計（MLE），用數月數據估計一個靜態 PIN，無法即時反映毒性變化

### VPIN 的突破

VPIN 用三個創新解決 PIN 的即時性問題：

**1. 成交量時間（Volume Time）取代時鐘時間**
- 將交易數據按「成交量切片」而非「時間切片」
- 每個切片 = 固定數量的成交量（Volume Bucket, V）
- 在成交量時間中，知情交易均勻分布的假設更合理
- 解決了時鐘時間下交易不均勻的問題（開盤收盘密集、中午稀疏）

**2. 一致性買賣壓力（Order Imbalance）**
- 每個成交量切片內計算買賣壓力：VBS（Volume Buy Side）- VSS（Volume Sell Side）
- 用 Bulk Volume Classification（BVC）分類：基於切片內價格變動方向判定買賣主導
- BVC 優勢：不需逐筆成交數據，用分K或Tick數據即可計算

**3. 滾動窗口計算**
- 用最近 N 個成交量切片計算 VPIN
- VPIN = Σ|VBS_i - VSS_i| / (N × V)
- 可以逐分鐘更新，實現即時毒性監控

## 計算流程

```
步驟一：設定參數
  V = 每個切片的成交量（例如每日成交量的 1/50）
  N = 切片數量（通常 50）

步驟二：成交量切片
  將交易數據按累積成交量 V 切分
  每個切片包含剛好 V 的成交量

步驟三：分類買賣壓力
  BVC方法：
  σ = 切片內價格變動標準差
  Z = 切片內價格變動 / σ
  VBS = V × Φ(Z)  （買方成交量）
  VSS = V × (1 - Φ(Z))  （賣方成交量）
  Φ = 標準常態分配 CDF

步驟四：計算 VPIN
  VPIN = (1/N) × Σ_{i=1}^{N} |VBS_i - VSS_i| / V
  範圍：0 到 1
  越高代表訂單流毒性越強
```

## 閃電崩盤預警

### 2010年5月6日閃電崩盤（Flash Crash）

VPIN 最著名的實戰案例：

- **事件**：道瓊指數在5分鐘內暴跌近1000點，市值蒸發約1兆美元，隨後迅速反彈
- **VPIN 預警**：Easley et al.（2012）回測顯示，VPIN 在閃崩前**一小時**就開始攀升
- **臨界值**：VPIN 超過 0.9 時，閃崩風險急劇上升
- **機制**：知情交易者（可能為高頻交易商）大量進場→造市商被毒→撤單→流動性蒸發→價格失序

### 2026年台股的 VPIN 應用

台股雖然沒有公開 VPIN 數據，但可以用以下代理變數近似：

- **大單占比異常上升**：當大單（>500張）佔比突然攀升，可能代表知情交易者進場
- **買賣壓力極端失衡**：連續多筆大單同方向，類似 VPIN 的 order imbalance 訊號
- **內外盤比極端值**：與[[技術分析/內外盤比與五檔報價判讀InOut-Disk-Ratio-and-Order-Book|內外盤比與五檔報價判讀]]直接關聯
- **法人買賣超與價格背離**：法人買超但價格不漲=知情者可能在賣給法人

## VPIN 與相關指標的關聯

- **與[[技術分析/Kyle-Lambda與價格衝擊模型Price-Impact-Model|Kyle's Lambda]]**：Lambda 衡量單位交易量的價格衝擊，VPIN 衡量知情交易比例——兩者都反映市場微結構的資訊不對稱程度
- **與[[風險管理/Amihud非流動性指標Amihud-Illiquidity-Measure|Amihud 非流動性指標]]**：Amihud 衡量流動性，VPIN 衡量毒性——高 VPIN 常伴隨高 Amihud
- **與[[操作策略/高頻交易與做市策略High-Frequency-Trading-and-Market-Making|高頻交易與做市策略]]**：VPIN 是做市商決定是否提供流動性的核心指標，毒性過高時做市商撤單
- **與[[技術分析/訂單流失衡OFI-Order-Flow-Imbalance|訂單流失衡 OFI]]**：OFI 量化買賣壓力失衡，VPIN 將失衡轉化為毒性機率
- **與[[技術分析/技術分析與市場微結構融合Microstructure-Informed-Technical-Analysis|技術分析與市場微結構融合]]**：VPIN 是微結構訊號融入技術分析的橋樑
- **與[[風險管理/市場微結構與流動性定價Market-Microstructure-and-Liquidity-Pricing|市場微結構與流動性定價]]**：VPIN 量化逆向選擇風險，是流動性定價的核心輸入
- **與[[操作策略/Avellaneda-Stoikov做市模型Market-Making-Model|Avellaneda-Stoikov 做市模型]]**：做市商可根據 VPIN 動態調整報價寬度——毒性高時加寬價差

## 批評與限制

### Andersen & Bondarenko（2014）的質疑

- **「機械幻覺」批評**：Andersen & Bondarenko 認為 VPIN 的預警能力部分來自計算方法的機械性，而非真正的資訊含量
- **反饋迴路缺陷**：VPIN 上升→造市商撤單→波動增加→VPIN 再上升，形成自我實現的循環
- **集中市場 vs 碎裂市場**：VPIN 在碎裂市場（多個交易場所）中的表現不如集中市場

### 實務限制

- **數據要求高**：精確計算需要 Tick 級數據或至少分K數據
- **參數敏感**：V 和 N 的選擇影響結果，沒有普適最優值
- **台股適用性**：台股無逐筆成交公開數據（僅有最佳五檔），精確 VPIN 計算困難
- **高頻時代的有效性**：隨著 HFT 佔比提升，VPIN 的訊號可能被噪音淹沒

## 散戶實戰用法

散戶無法精確計算 VPIN，但可以觀察其代理訊號：

1. **盤中異常大單方向一致性**：連續大單同方向→毒性升高→趨勢可能加速
2. **法人買賣超與價格方向**：法人買超但價格不漲=有更聰明的賣方在出貨
3. **買賣價差突然擴大**：造市商感受到毒性撤退的訊號
4. **委買委賣比極端值**：與 VPIN 的 order imbalance 概念相通
5. **結算日前後毒性變化**：法人可能利用結算日集中操作，毒性通常升高

## YouTube 學習來源

- **"Order Flow Toxicity Explained: A Complete Guide to VPIN"**（WaveLabs 頻道）- 7分40秒，詳細解釋 VPIN 如何在 2010 閃崩前一小時發出預警，涵蓋 Volume Time vs Clock Time、0.9 警戒線、做市商實務應用與批評者觀點
- **"The VPIN Flow Toxicity metric and liquidity crashes"**（QuantCongressUSA2011）- Easley 團隊親自解說 VPIN 與流動性危機的關聯

## 參考文獻

- Easley, D., López de Prado, M. M. & O'Hara, M. (2012). "Flow Toxicity and Liquidity in a High-Frequency World." *Review of Financial Studies*, 25(5), 1457-1493.
- Easley, D. & O'Hara, M. (1992). "Time and the Process of Trade Evolution." *Journal of Finance*, 47(2), 577-605.
- Andersen & Bondarenko (2014). "VPIN and the Flash Crash." *Journal of Financial Economics*.
- Easley, D., López de Prado, M. M. & O'Hara, M. (2011). "The Microstructure of the Flash Crash." *Journal of Portfolio Management*.

---

*學習日期：2026-08-14*
*來源：Easley et al. (2012) 學術論文、YouTube WaveLabs "Order Flow Toxicity Explained"、QuantCongressUSA2011 演講*