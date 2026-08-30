---
title: 增量營業利益率Incremental-Operating-Margin
aliases: [Incremental Operating Margin, Incremental Margin, 增量利潤率, 邊際營業利益率, 增量EBIT率]
category: 基本面分析
date: 2026-08-26
---

# 增量營業利益率Incremental-Operating-Margin

> 一般營業利益率看整鍋湯有多濃，增量營業利益率看新加的一碗水到底變成多少料；營收成長很大聲，新增利潤小得像蚊子，規模經濟大概只活在法說會投影片。

## 核心概念

增量營業利益率衡量一段期間內，每增加一元營收帶來多少新增營業利益：

$$Incremental\ Operating\ Margin=\frac{EBIT_t-EBIT_{t-1}}{Revenue_t-Revenue_{t-1}}$$

一般營業利益率是存量比率：

$$Operating\ Margin_t=\frac{EBIT_t}{Revenue_t}$$

兩者差異在於：

- 一般營業利益率回答「目前每元營收留下多少EBIT」
- 增量營業利益率回答「新增每元營收留下多少新增EBIT」
- 前者容易被龐大既有業務平均，後者更敏感地顯示成長品質與成本結構變化

Wall Street Prep將增量利潤率定義為利潤指標變動除以營收變動，概念上就是「成長部分的利潤率」。

## 可拆成三層

不要只算最下面一層，可沿損益表逐層追蹤：

$$Incremental\ Gross\ Margin=\frac{\Delta Gross\ Profit}{\Delta Revenue}$$

$$Incremental\ EBITDA\ Margin=\frac{\Delta EBITDA}{\Delta Revenue}$$

$$Incremental\ Operating\ Margin=\frac{\Delta EBIT}{\Delta Revenue}$$

三層差異能定位問題：

- 增量毛利率高、增量EBITDA率低：新增毛利被SG&A或研發吃掉
- 增量EBITDA率高、增量EBIT率低：折舊攤銷上升，可能是新產能或併購無形資產負擔
- 三者同步上升：售價、產品組合與費用槓桿一起改善
- 增量毛利率先轉負：價格競爭、原料上漲或產品組合惡化已從最上游開咬

## 算例

假設營收由100億元增至130億元，EBIT由10億元增至16億元：

$$Incremental\ Operating\ Margin=\frac{16-10}{130-100}=20\%$$

原營業利益率為10%，新一期營業利益率約12.31%。增量率20%高於原有率10%，表示新增營收的獲利能力較高，會把整體率往上拉。

若營收增加20億元，EBIT反而由10億元降至8億元：

$$Incremental\ Operating\ Margin=\frac{8-10}{120-100}=-10\%$$

這種「營收成長、利潤倒退」通常比單看正營業利益更早暴露成本失控。公司還在賺錢沒錯，只是新增生意正在幫舊生意挖墳墓。

## 與營業槓桿的關係

高固定成本企業在營收跨過損益兩平點後，新增營收不必同比增加固定成本，因此增量營業利益率可能遠高於平均營業利益率。常見於：

- 晶圓製造與面板
- 航空與航運
- 飯店、電信與有線網路
- SaaS與數位平台
- 工廠自動化及高資本密集製造

但營業槓桿是雙面刃：

- 上行期：產能利用率提高，增量率暴升
- 下行期：營收下降但固定成本還在，增量率可能劇烈惡化
- 接近營收無變化時：分母很小，數字容易失真或爆表

因此增量率不是越高越安全。高固定成本公司會在多頭時看起來像印鈔機，反轉時才發現印的是催繳單。

## 如何判讀增量率高低

沒有跨產業通用門檻，應比較四組基準：

- **自身歷史**：3至5年與完整景氣循環
- **平均利潤率**：增量率高於平均，整體率傾向擴張
- **同業**：相同需求環境下誰能把新增營收留成更多利潤
- **管理層指引**：實際增量率是否符合毛利、費用率與產能利用率說法

判讀方向可簡化為：

- 增量率高於平均率且穩定：規模經濟或產品組合改善
- 增量率低於平均率但仍為正：成長仍獲利，但會稀釋整體率
- 增量率為負：新增營收伴隨利潤下降，需拆成本與一次性因素
- 增量率異常高：檢查低基期、補貼、迴轉利益、存貨跌價回升與延後費用

## 用季度、年度還是多年

### 單季同比

- 能消除部分季節性
- 轉折較快
- 容易受認列時點、匯率與單季費用干擾

### 年度

- 適合營運穩定企業
- 噪音較低
- 可能晚一年才看見惡化

### 3年累積

$$Incremental\ Margin_{3Y}=\frac{EBIT_t-EBIT_{t-3}}{Revenue_t-Revenue_{t-3}}$$

- 適合建廠、擴店與SaaS規模化分析
- 可降低單季雜訊
- 仍需處理併購與業務組合改變

最實用做法不是選一個數字信到底，而是同時看單季同比、TTM與3年累積；如果三條線一起轉弱，還硬說只是短期因素，通常只是投資人開始替管理層兼職公關。

## 與ROIIC交叉驗證

Morgan Stanley指出，高ROIIC常來自資本效率或營業槓桿，而營業槓桿可用營業利益變動除以銷售變動觀察。兩者一起看可分辨：

- 增量率高、ROIIC高：新增營收轉成利潤，且沒有吞太多資本
- 增量率高、ROIIC低：利潤率不差，但成長需大量廠房、設備或營運資金
- 增量率低、ROIIC高：可能分母投入資本被低估，或資產處分、費用化無形投資造成失真
- 兩者都低：成長既不賺錢又吃資本，完整的資本配置車禍

## 實戰啟示

1. 增量營業利益率比平均率更早揭露成長品質
2. 增量率高於平均率，整體率才有持續擴張的數學基礎
3. 從毛利到EBIT逐層算，才能知道新增利潤死在哪一段
4. 高固定成本企業的增量率上下波動都會放大，不能只愛上行不看下行
5. 最有價值的訊號不是某季爆高，而是跨季度、TTM與全週期都能維持

## 實戰應用

1. 使用相同會計口徑的營收、毛利、EBITDA與EBIT
2. 優先做季度同比，避免旺季對淡季亂比
3. 另算TTM及3年累積增量率
4. 標註併購、處分、匯率、補貼、存貨跌價與一次性費用
5. 將增量毛利率、EBITDA率與營業利益率逐層拆解
6. 對照產能利用率、ASP、產品組合、員工與折舊增幅
7. 與同業在同一景氣階段比較
8. 再搭配ROIIC、自由現金流與營運資金，確認利潤有沒有變成現金
9. 把可持續增量率放入財測，對高低情境做敏感度分析

## 注意事項

- **營收變動太小**：分母接近零時比率沒有判讀價值
- **營收下降時符號反直覺**：收入與EBIT同降可能算出正值，不代表經營變好
- **低基期灌水**：前期虧損或一次性費用可讓後期增量率異常漂亮
- **景氣循環失真**：高峰價格與利用率不能外推成永久率
- **併購改變組合**：營收與利潤不是同一業務有機增加時，增量率會混入收購效果
- **會計分類差異**：公司調整成本、費用或折舊分類會破壞可比性
- **EBITDA可能遮住資本成本**：增量EBITDA率高，不代表重資產擴產有經濟價值
- **降本有上限**：裁員、砍研發與延後維修能短期提高增量率，但可能掏空未來
- **不是邊際貢獻率**：公開財報的增量率混合價格、數量、產品組合與成本變化，不等於管理會計的單位貢獻毛利

## 相關主題

- [[基本面分析/損益表結構與獲利比率判讀]]
- [[基本面分析/毛利率分析實戰判讀]]
- [[基本面分析/營業槓桿與財務槓桿聯合槓桿判讀Operating-Financial-Combined-Leverage]]
- [[基本面分析/ROIC投入資本報酬率]]
- [[基本面分析/ROIIC增量投入資本報酬率Return-on-Incremental-Invested-Capital]]
- [[基本面分析/再投資率與基本面成長率Reinvestment-Rate-and-Fundamental-Growth]]

## 來源

- Wall Street Prep. [Incremental Margin: Formula and Calculation Guide](https://www.wallstreetprep.com/knowledge/incremental-margin/), updated February 20, 2024.
- Mauboussin, M. J., & Callahan, D. (2022). [Return on Invested Capital: How to Calculate ROIC and Handle Common Issues](https://www.morganstanley.com/im/publication/insights/articles/article_returnoninvestedcapital.pdf), Counterpoint Global Insights, p. 23.
- Damodaran, A. [Estimating Growth](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/growth.pdf), NYU Stern valuation lecture notes, pp. 30–33.

---

*最後更新：2026-08-26*
