# TED Spread 泰德利差

> 銀行間信用壓力的溫度計——當銀行開始不信任彼此，TED Spread 會先告訴你。

## 定義

**TED Spread**（泰德利差）是三個月期銀行間無擔保借貸利率與三個月期美國國庫券（T-Bill）利率之間的差值，以基點（bps）表示。

**公式：**

TED Spread = 3個月LIBOR（或SOFR） − 3個月T-Bill利率

- **T** = Treasury Bill（美國國庫券，被視為無風險）
- **ED** = Eurodollar（歐洲美元期貨合約代碼，代表銀行間借貸利率）

TED Spread 衡量的是：**銀行向彼此借錢的利率，比借給美國政府的利率高出多少？** 這個差距越大，代表市場認為銀行違約風險越高。

## 歷史演變

**原始版本（1987年前）：** 三個月T-Bill期貨減三個月Eurodollar期貨。CME在1987年黑色星期一股災後取消T-Bill期貨，改用LIBOR直接計算。

**LIBOR版本（1987-2021）：** 三個月LIBOR減三個月T-Bill利率。這是使用最久的版本，所有歷史數據與研究文獻都基於此。

**SOFR版本（2021後）：** LIBOR因操縱醜聞於2021年停用，由**SOFR（Secured Overnight Financing Rate）**取代。但SOFR追蹤的是**有擔保**借貸，LIBOR追蹤的是**無擔保**借貸，兩者不等價。SOFR版本的TED Spread對信用風險的敏感度降低，這是後LIBOR時代的一個測量盲區。

## 判讀標準

- **正常區間：** 10-50 bps（0.1%-0.5%），長期均值約30 bps
- **警戒區間：** 50-100 bps，信用壓力開始上升
- **危機區間：** >100 bps，銀行間信任嚴重崩壞
- **極端危機：** >200 bps，系統性流動性危機

Boudt、Paulus和Rosenthal（2017）的研究指出，TED Spread超過48 bps即指示經濟危機狀態。

## 歷史重大事件

**2008金融海嘯：**
- 2007次貸危機爆發，TED Spread升至150-200 bps
- 2008年9月17日（雷曼兄弟破產後一週），TED Spread突破300 bps，打破1987黑色星期一的歷史紀錄
- 2008年10月10日，TED Spread達到歷史最高457 bps
- 這意味著銀行寧願把錢塞在零風險的T-Bill裡，也不願借給同業

**2020疫情衝擊：**
- 3月全球美元荒期間TED Spread一度飆升至約130 bps
- 聯準會啟動FIMA回購機制與SWAP線解凍美元流動性

**2013年負值異常：**
- 10月因美國債務上限逼近違約恐慌，1個月期TED Spread首次出現負值
- T-Bill利率被恐慌推至接近零甚至負值，反轉了正常利差關係

## 實戰應用

### 1. 作為股市領先指標

TED Spread上升通常**領先**股市下跌。當利差從正常區間開始擴大，代表流動性正在被抽走，往往預示股市即將承壓。這不是因為股市本身出了問題，而是因為**銀行體系的信任崩潰會傳導到所有風險資產**。

### 2. 搭配其他信用指標

- **[[基本面分析/殖利率曲線分析Yield-Curve-Analysis|殖利率曲線]]：** 殖利率倒掛看經濟衰退預期，TED Spread看銀行間流動性壓力
- **[[風險管理/信用利差Credit-Spread|信用利差]]：** 信用利差看企業違約風險，TED Spread看銀行間違約風險
- **[[基本面分析/信用違約交換CDS-Credit-Default-Swap|CDS]]：** CDS看特定機構違約風險，TED Spread看整體銀行體系風險

### 3. 2026年的實戰連結

在2026年的AI資本支出泡沫論辯中，宏爺講股和股市好聲音頻道多次提及信用市場壓力——七巨頭CDS利差擴大、AI債券發行4890億美元創紀錄。如果TED Spread從低檔開始擴大，代表銀行體系開始感受到AI基建融資的壓力外溢，是比CDS更早的系統性預警。

## 後LIBOR時代的盲區

LIBOR停用後，TED Spread面臨兩個結構性問題：

1. **SOFR是有擔保利率：** SOFR基於國債回購市場，本身就帶有擔保品，信用敏感度遠低於無擔保的LIBOR。用SOFR算的TED Spread**低估了**真實的銀行間信用壓力。

2. **替代指標的興起：** 高盛在2016年就因LIBOR受SEC貨幣市場基金新規影響而將TED Spread從金融狀況指數中移除。現在市場更傾向用**FRA-OIS Spread**或**SOFR-OIS Spread**來衡量銀行間壓力。

儘管如此，TED Spread的歷史數據和概念框架仍然是理解信用壓力傳導的基礎工具。在危機時刻，追蹤SOFR-T-Bill Spread仍能提供有價值的系統性壓力訊號。

## 關鍵要點

- TED Spread = 銀行間借貸利率 − 無風險利率，衡量銀行間信任程度
- 正常10-50 bps，超過100 bps代表系統性壓力，2008年曾達457 bps
- TED Spread上升通常領先股市下跌，是流動性收縮的早期訊號
- LIBOR停用後SOFR替代，但因有擔保vs無擔保差異，新版敏感度降低
- 搭配殖利率曲線、信用利差、CDS使用，構成完整的信用壓力監測框架

## 相關頁面

- [[基本面分析/殖利率曲線分析Yield-Curve-Analysis|殖利率曲線分析]]
- [[風險管理/信用利差Credit-Spread|信用利差]]
- [[基本面分析/信用違約交換CDS-Credit-Default-Swap|信用違約交換CDS]]
- [[基本面分析/FOMC聯邦公開市場委員會與利率決策Federal-Open-Market-Committee|FOMC與利率決策]]
- [[基本面分析/QT量化緊縮與聯準會資產負債表Quantitative-Tightening|QT量化緊縮]]
- [[基本面分析/CPI消費者物價指數Consumer-Price-Index|CPI消費者物價指數]]

---
*學習日期：2026-07-31*
*資料來源：Wikipedia TED Spread、Bloomberg、St. Louis Fed、Boudt et al. (2017)*