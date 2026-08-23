---
title: "Gamma Scalping實戰策略 Gamma Scalping Strategy"
tags: [操作策略, 選擇權, Greeks, 波動率交易, Delta-Neutral]
created: 2026-07-05
---

# Gamma Scalping實戰策略 Gamma Scalping Strategy

> Long Gamma + Delta Neutral + 不斷再平衡 = 在波動中收割利潤。用Theta成本換Gamma收益的進階選擇權策略，本質是「用時間買波動」。

## 核心概念

**Gamma Scalping**是選擇權交易中最高階的操作手法之一。核心邏輯是：

1. 建立**Long Gamma**部位（買進選擇權）
2. 維持**Delta Neutral**（不賭方向，Delta≈0）
3. 價格上漲時賣出股票讓Delta回歸零（高賣）
4. 價格下跌時買回股票讓Delta回歸零（低買）
5. 不斷重複→ 在波動中「刮」出利潤

**本質**：你不是在賭漲跌，你是在賭**波動率**。只要標的資產波動夠大，Gamma Scalping就能獲利。代價是每天付出的**Theta（時間價值衰減）**。

### Gamma Scalping 的數學本質

每當價格移動ΔS，Long Gamma部位的利潤近似為：

$$\text{Gamma利潤} \approx \frac{1}{2} \times \Gamma \times (\Delta S)^2$$

累積N次再平衡後的總Gamma利潤：

$$\text{總Gamma利潤} = \frac{1}{2} \times \Gamma \times \sum_{i=1}^{N} (\Delta S_i)^2$$

而Theta成本是線性的：

$$\text{Theta成本} = |\Theta| \times T$$

**盈虧平衡波動率**（Breakeven Volatility）：當Gamma利潤 = Theta成本時的已實現波動率。如果實際波動 > 盈虧平衡波動率 → 獲利；反之 → 虧損。

## 操作步驟

### Step 1：建立Long Gamma + Delta Neutral部位

最常見的建倉方式是**買進跨式（[[跨式Straddle與勒式Strangle|Long Straddle]]）**：

- 買進ATM Call + 買進ATM Put（相同履約價、相同到期日）
- 初始Delta ≈ 0（Call的+0.5和Put的-0.5互相抵消）
- Gamma為正（兩邊都是Long Gamma）

**部位範例**：
- 買進1張台指期ATM Call（履約價23000），Delta=+0.50
- 買進1張台指期ATM Put（履約價23000），Delta=-0.50
- 組合Delta = 0, Gamma > 0, Theta < 0, Vega > 0

### Step 2：價格移動後再平衡

**情境A：指數從23000漲到23100**
- Call的Delta從0.50增加到約0.55（Gamma效應）
- Put的Delta從-0.50增加到約-0.45（Gamma效應）
- 組合Delta = 0.55 + (-0.45) = +0.10
- **動作**：賣出相當於Delta 0.10的小台指期貨 → Delta回到0
- 你在23100「賣出」——高賣

**情境B：指數從23100跌回23000**
- Call的Delta從0.55回到約0.50
- Put的Delta從-0.45回到約-0.50
- 組合Delta = 0.50 + (-0.50) + 賣出的-0.10 = -0.10
- **動作**：買回相當於Delta 0.10的小台指期貨 → Delta回到0
- 你在23000「買回」——低買

**淨效果**：你在23100賣出、在23000買回，賺了100點的價差。這就是Gamma Scalping——用再平衡製造「高賣低買」。

### Step 3：不斷重複

只要指數持續波動，就持續再平衡。每次再平衡都在「刮」一小層利潤。

### Step 4：管理Theta成本

每一天你的Long Straddle都在流失Theta：
- ATM選擇權最後30天Theta加速衰減
- 如果波動不夠大，Gamma利潤趕不上Theta流失
- **21 DTE Rule**：避免在到期前21天內建倉，Theta衰減太兇猛

## 關鍵參數判讀

### Gamma值

- Gamma越大 → 每次價格移動的再平衡利潤越大
- ATM選擇權Gamma最大
- 越接近到期日Gamma越大（但Theta也越大）
- **最佳平衡點**：30-60天到期，ATM或輕微OTM

### Theta值

- Theta是Gamma Scalping的「成本」
- ATM選擇權Theta最大（最不利）
- 需要實際波動 > 隱含波動才能覆蓋Theta成本
- **判斷公式**：所需日波動 ≈ √(2|Θ|/Γ)

### Vega值

- Long Straddle是Long Vega → IV上升有利
- 但Gamma Scalping的核心是已實現波動 vs 隱含波動
- 如果IV已經很高（VIX > 25），建倉成本昂貴，盈虧平衡波動率被拉高
- **最佳進場時機**：IV偏低但預期波動即將增加（例如重大事件前）

## 實戰策略變體

### 1. 純Gamma Scalping（Long Straddle + 期貨再平衡）

- 最直接的版本
- 適合：預期高波動但不確定方向
- 風險：Theta消耗，波動不夠就虧

### 2. Gamma Scalping with IV Edge

- 在IV低於歷史平均時建倉
- 同時賺Gamma Scalping利潤 + IV回升的Vega利潤
- 雙重獲利來源降低Theta風險

### 3. 日內Gamma Scalping

- 當天建倉當天平倉
- 避免隔夜Theta成本
- 適合：預期單日高波動（例如FOMC當天）
- 需要極低交易成本才有可行性

### 4. 寬幅Gamma Scalping

- 不每5點再平衡，而是等價格移動20-50點才再平衡
- 減少再平衡次數→降低手續費侵蝕
- 但每次再平衡利潤更大
- **關鍵trade-off**：再平衡頻率 vs 手續費

## 台股實戰可行性

### 有利因素

- 台指選擇權流動性佳，買賣價差窄
- 小台指期貨流動性足夠做再平衡
- 台股日內波動常有200-500點，足以覆蓋Theta

### 不利因素

- **手續費侵蝕**：每次再平衡都有成本，頻繁再平衡手續費可能吃掉Gamma利潤
- **隔夜風險**：台股跳空開盤常見，隔夜部位可能被跳空直接打到停損
- **交易稅**：選擇權交易稅0.1%，期貨交易稅更複雜
- **保證金需求**：Long Straddle需要全額權利金，資金效率低

### 實務建議

- 再平衡間隔設為ATR的0.5-1倍，而非固定點數
- 用[[ATR平均真實波幅-Average-True-Range|ATR]]動態設定再平衡閾值
- 避開最後30天（Theta加速期）
- 選擇IV低於20日歷史波動率的時機建倉
- 總部位不超過帳戶的10-15%

## 常見誤區

**誤區1：Gamma Scalping穩賺**
→ 如果波動不夠大，Theta會吃光所有利潤。Gamma Scalping的勝率取決於實際波動 vs 隱含波動的差距。

**誤區2：越頻繁再平衡越好**
→ 理論上連續再平衡最優，但手續費讓連續再平衡變成虧損策略。存在最佳再平衡頻率。

**誤區3：只看Gamma不看Theta**
→ Gamma/Theta比值是核心指標。Gamma/|Theta| > 5才算有利的Gamma Scalping環境。

**誤區4：方向不重要**
→ 雖然Delta Neutral不賭方向，但強趨勢日（單邊大漲或大跌）的Gamma Scalping效果遠不如震盪日。趨勢日你只在單邊再平衡，錯過另一邊的利潤。

## 與其他策略的關係

- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral|波動率套利與Delta Neutral]] — Gamma Scalping是波動率套利的具體實作方式
- [[選擇權Convexity凸性與非對稱收益Option-Convexity|選擇權Convexity]] — Gamma Scalping本質就是收割Convexity
- [[選擇權Greeks希臘字母|Greeks]] — Gamma和Theta是核心參數
- [[選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced|Greeks進階]] — 多維Greeks管理
- [[跨式Straddle與勒式Strangle|Straddle]] — Gamma Scalping最常見的建倉工具
- [[Theta時間衰減實戰|Theta時間衰減]] — Theta是Gamma Scalping的敵人
- [[隱含波動率IV與歷史波動率HV實戰判讀|IV vs HV]] — IV/HV差距決定Gamma Scalping可行性
- [[波動率風險溢價Volatility-Risk-Premium|波動率風險溢價]] — Gamma Scalping本質是做空波動率風險溢價
- [[鐵兀鷹Iron-Condor]] — 反向策略：Short Gamma收Theta
- [[VIX恐慌指數實戰判讀|VIX]] — VIX水位判斷建倉時機

## 策略總結

Gamma Scalping是選擇權交易「聖盃級」的策略——理論上完美（不賭方向只賺波動），實務上極難（Theta成本+手續費+跳空風險）。

**核心公式**：
- 獲利條件 = 已實現波動率 > 盈虧平衡波動率
- 盈虧平衡波動率 ≈ √(2|Θ|/Γ) × √(252)
- 最佳環境 = 低IV + 高實際波動 + 震盪市

**不是每個人都該做Gamma Scalping**——它需要：
1. 對Greeks有深入理解
2. 低交易成本的券商帳戶
3. 能即時監控部位再平衡
4. 能承受Theta每天燃燒的心理壓力

但理解Gamma Scalping的邏輯，即使不做，也能幫助你理解選擇權定價的本質——**時間和波動率的永恆交易**。

## 實戰應用

（待補充）

## 注意事項

（待補充）

## 相關主題

（待補充）

## 來源

- 待補：本頁目前沒有可核對的原始來源連結。
