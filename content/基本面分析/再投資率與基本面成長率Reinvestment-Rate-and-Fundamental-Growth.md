---
title: 再投資率與基本面成長率Reinvestment-Rate-and-Fundamental-Growth
aliases: [Reinvestment Rate, Fundamental Growth, 基本面成長率, 可持續成長率, 再投資效率]
category: 基本面分析
date: 2026-08-25
---

# 再投資率與基本面成長率Reinvestment-Rate-and-Fundamental-Growth

> 成長不是營收年增率自己從土裡冒出來，而是公司把多少錢丟回生意、每一塊新資本能賺多少的乘積；只喊高成長不談再投資效率，跟只報馬力不講油耗一樣會騙到自己。

## 核心概念

企業基本面成長可拆成兩個引擎：

1. **投入多少**：再投資率
2. **投得多有效**：投入資本報酬率

在投入資本報酬率穩定的簡化情況下，Damodaran將營業利益基本面成長寫成：

$$g_{EBIT}=\text{Reinvestment Rate}\times\text{Return on Capital}$$

這個公式把「成長」和「資本配置」綁在一起。企業不能永遠靠簡報、題材或一次性效率改善長大；長期成長最終要由新增資本與新增資本報酬支撐。

## EPS成長：保留盈餘比率乘ROE

若公司不發行新股，ROE保持穩定，EPS長期成長可近似：

$$g_{EPS}=b\times ROE$$

其中：

$$b=1-\text{Payout Ratio}$$

$b$是保留盈餘比率。假設公司保留60%盈餘、ROE為18%，則：

$$g_{EPS}=60\%\times18\%=10.8\%$$

這不是預言，而是一致性檢查。若分析師假設EPS永久成長20%，公司ROE只有12%，又固定配出一半盈餘，那個模型不是樂觀，是數學在加班替故事擦屁股。

## EBIT成長：再投資率乘ROC

以稅後營業利益NOPAT為基礎：

$$\text{Reinvestment Rate}=\frac{\text{Net CapEx}+\Delta\text{Noncash Working Capital}}{NOPAT}$$

其中：

$$\text{Net CapEx}=\text{CapEx}-\text{Depreciation}$$

投入資本報酬率為：

$$ROC=\frac{NOPAT}{\text{Invested Capital}}$$

因此：

$$g_{EBIT}=\text{Reinvestment Rate}\times ROC$$

若NOPAT為100億元，淨資本支出加營運資金增量為60億元，再投資率為60%；若ROC為15%，則基本面成長率為：

$$g_{EBIT}=60\%\times15\%=9\%$$

## 為什麼高成長不一定創造價值

成長是否增加企業價值，還要比較ROC與WACC：

- **ROC大於WACC**：每投入一塊錢創造正經濟利潤，成長通常增加價值
- **ROC等於WACC**：成長只擴大規模，沒有創造超額價值
- **ROC小於WACC**：公司越積極擴張，價值毀損越快

所以真正想要的是：

$$\text{Value-Creating Growth}=\text{High Reinvestment Opportunity}+ROC>WACC$$

「高成長、低回報」是資本市場最常見的煙火，亮的時候大家拍照，掉下來的灰都是股東掃。

## 公司成長與每股成長別混淆

公司可以靠發行新股、併購或舉債讓總營收與總淨利增加，但舊股東關心的是每股價值：

- 淨利成長20%，股數增加25%，EPS反而下降
- 回購使股數下降，EPS可高於淨利成長
- 併購帶來營收成長，若支付過高或ROIC低於WACC，每股內在價值仍可能下滑

因此研究流程應同時看：

- 營收與NOPAT總額成長
- 流通股數變化
- EPS成長
- 每股自由現金流成長
- 新增投入資本報酬率

## ROE或ROC改變時

若既有資產效率提高，短期成長還多一項「效率改善」：

$$g\approx\text{Reinvestment Rate}\times ROC_{new}+\text{Efficiency Change}$$

例如產能利用率由低檔回升、毛利率改善或費用率下降，盈餘可在幾乎不增加資本下快速成長。但這種來源有上限：

- 產能利用率不可能超過物理極限
- 毛利率不可能永久每年擴張
- ROE不可能無限上升
- 景氣谷底反彈不是永久成長率

短期轉機可以靠效率，長期複利必須靠再投資。把一次性回升塞進終值，DCF會長出比宇宙還大的公司，然後Excel還是一臉無辜。

## 實戰應用：四象限

### 高再投資率、高ROC

- 最理想的複利型企業
- 必須確認市場空間與護城河足以容納新增資本
- 觀察新增產能的邊際ROIC是否開始下滑

### 低再投資率、高ROC

- 成熟現金牛
- 現有業務優秀但成長空間有限
- 應把多餘現金合理配息、回購或尋找高報酬新用途

### 高再投資率、低ROC

- 價值毀損型成長
- 營收可能很漂亮，FCF與經濟利潤卻持續惡化
- 常見於過度擴產、搶市占與高價併購

### 低再投資率、低ROC

- 缺乏成長也缺乏回報
- 若還不願返還現金，資本配置通常更糟
- 除非有可信轉機，不然多半只是便宜有原因

## 台股實戰SOP

1. 用3至5年NOPAT與投入資本計算全週期ROC
2. 計算淨CapEx與非現金營運資金增量
3. 估算再投資率並處理併購、資產處分與一次性大額建廠
4. 用再投資率乘ROC估基本面成長率
5. 與公司指引、法人EPS預估及市場隱含成長比較
6. 檢查流通股數，確認公司成長是否轉成每股成長
7. 將ROC與WACC比較，判斷成長創造還是毀損價值
8. 對ROC均值回歸、再投資率與終值成長做敏感度測試

## 注意事項與常見陷阱

- **用平均ROIC代替邊際ROIC**：舊專案很賺，不代表新廠也一樣賺
- **忽略營運資金**：存貨與應收一起膨脹，成長會吞掉現金
- **把併購當有機成長**：總額長大不代表單位資本效率改善
- **高ROE可能來自槓桿**：應同時看ROC與負債
- **負再投資率未必壞**：成熟公司處分低效資產、釋放營運資金可能提高價值
- **週期高峰失真**：高峰NOPAT會把ROC與可持續成長一起灌胖
- **終值不一致**：永久高成長必須對應合理再投資，不能憑空生出現金流
- **成長率不是報酬率**：好成長若已被股價透支，投資報酬照樣難看

## 實戰啟示

1. 長期成長率不是外生假設，而是再投資率與資本報酬的結果
2. 高ROIC企業若沒有再投資空間，會變成現金牛而不是高速成長股
3. 高再投資率若配低ROIC，越努力通常越慘
4. 淨利總額成長必須經過股數調整，才知道舊股東有沒有真的變富
5. DCF成長假設必須和CapEx、營運資金、ROIC與WACC彼此一致

## 相關主題

- [[基本面分析/ROIC投入資本報酬率]]
- [[基本面分析/資本支出CapEx與自由現金流判讀]]
- [[基本面分析/FCF估值模型自由現金流15公式與選股實戰]]
- [[基本面分析/現金流量折現法DCF估值]]
- [[基本面分析/ROE杜邦分析淨利率資產週轉率權益乘數]]
- [[基本面分析/WACC加權平均資本成本]]

## 來源

- Damodaran, A. [Estimating Growth](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/growth.pdf), NYU Stern valuation lecture notes.
- Damodaran, A. [Valuation Questions: Growth](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/growth.htm).

---

*最後更新：2026-08-25*
