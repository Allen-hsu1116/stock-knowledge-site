---
title: "Beneish M-Score 盈餘操縱偵測模型"
category: "基本面分析"
---

# Beneish M-Score 盈餘操縱偵測模型

> 8個財報比率，一個公式，算出公司有沒有在做假帳——康乃爾學生靠它在1998年就抓出安隆。

## 核心概念

**Beneish M-Score** 是 Indiana University 會計教授 Messod D. Beneish 於1999年在論文 *"The Detection of Earnings Manipulation"* 中提出的統計模型，用8個財務比率計算出一個分數，判斷公司是否很可能在操縱盈餘。

與 [[基本面分析/Piotroski-F-Score財務品質評分模型|Piotroski F-Score]] 評估基本面好壞不同，M-Score 專門抓「盈餘操縱」（earnings manipulation）——也就是公司透過會計手段讓財報看起來比實際好。

## 八大變數與公式

### 8個財務比率

1. **DSRI（應收帳款天數指數）** — (Net Receivables_t / Sales_t) / (Net Receivables_{t-1} / Sales_{t-1})
   - 應收帳款佔營收比重異常上升 = 可能虛增營收

2. **GMI（毛利率指數）** — [毛利率_{t-1}] / [毛利率_t]
   - 毛利率惡化時 > 1，公司有動機做手腳撐住數字

3. **AQI（資產品質指數）** — [1-(流動資產+不動產+證券)/總資產]_t / [1-(流動資產+不動產+證券)/總資產]_{t-1}
   - 非正常資產比例上升 = 可能將費用資本化

4. **SGI（營收成長指數）** — Sales_t / Sales_{t-1}
   - 高成長公司操縱盈餘的壓力更大

5. **DEPI（折舊指數）** — [折舊_{t-1}/(PP&E_{t-1}+折舊_{t-1})] / [折舊_t/(PP&E_t+折舊_t)]
   - > 1 表示折舊率下降 = 可能改變折舊年限拉高利潤

6. **SGAI（SG&A費用指數）** — (SG&A/Sales)_t / (SG&A/Sales)_{t-1}
   - 銷管費用佔營收比上升 = 營運效率惡化，可能掩蓋問題

7. **LVGI（槓桿指數）** — [(流動負債+長期負債)/總資產]_t / [(流動負債+長期負債)/總資產]_{t-1}
   - 槓桿上升 = 壓力增大，操縱誘因更強

8. **TATA（總應計項目/總資產）** — (營業利益-營業現金流)/總資產
   - 應計項目佔比越高 = 盈餘品質越差

### M-Score 公式

```
M-Score = -4.84 + 0.92×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI 
         + 0.115×DEPI - 0.172×SGAI + 4.679×TATA - 0.327×LVGI
```

## 經典案例：安隆（Enron）

1998年，康乃爾大學的學生使用 Beneish M-Score 分析安隆財報，正確判定安隆在操縱盈餘。當時華爾街分析師仍然推薦買進安隆股票。三年後安隆爆發會計醜聞倒閉，成為美國史上最大企業醜聞之一（直到後來被世界通訊超越）。

這個案例證明：M-Score 能在傳統分析師還沒察覺時，就從財報數字中嗅出異常。

## 聚合M-Score與經濟預測

2023年 Beneish 等人的研究發現，將多家公司的 M-Score 聚合計算，可以預測美國經濟衰退和GDP成長。2023年初的聚合M-Score達到約40年來最高水準，暗示盈餘操縱的普遍性上升可能是經濟即將惡化的先行指標。

## 與其他模型比較

- **[[基本面分析/Piotroski-F-Score財務品質評分模型|Piotroski F-Score]]**：評估財報品質是否在改善 → 選好公司
- **M-Score**：偵測財報是否被操縱 → 避地雷
- **[[基本面分析/Altman-Z-Score破產預測模型|Altman Z-Score]]**：預測破產風險 → 避倒閉
- **[[基本面分析/Ohlson-O-Score破產預測模型|Ohlson O-Score]]**：另一種破產預測模型

三者互補：F-Score找好公司、M-Score確認沒做假帳、Z-Score確認不會倒。

## 實戰應用

### 判讀標準
- **M-Score > -1.78**：公司很可能在操縱盈餘 ⚠️
- **M-Score < -1.78**：公司不太可能操縱盈餘 ✅

例如 M-Score = -2.50 → 低操縱風險；M-Score = -1.50 → 高操縱風險。



1. **定期健檢持股**：每季財報出來後算一次M-Score，監控是否有惡化趨勢
2. **新股IPO篩選**：上市櫃前幾年財報用M-Score檢驗，避免踩到作帳上市的雷
3. **搭配F-Score使用**：F-Score高但M-Score也高（> -1.78）的公司，可能是靠會計手段改善的假象
4. **關注DSRI和TATA**：這兩個變數權重最高（0.92和4.679），是M-Score中最敏感的指標

台股常見的盈餘操縱手法包括：年底衝刺營收認列、存庫減損提列不足、關係人交易虛增營收、費用資本化等，這些都能在M-Score的8個變數中留下痕跡。

## 注意事項
1. **機率模型非確定**：M-Score是統計模型，無法100%準確偵測操縱
2. **不適用金融機構**：銀行保險靠利息和手續費賺錢，沒有傳統的「應收帳款」和「銷貨成本」，M-Score的關鍵變數無意義
3. **只能抓會計操縱**：合法但激進的會計政策（如改變折舊年限）可能被偵測為操縱，但未必違法
4. **無法偵測表外操作**：如SPE特殊目的實體等表外融資手段，M-Score不一定能抓到
5. **數據探勘風險**：模型基於歷史操縱案例建立，新型態的操縱可能逃過偵測

## 相關主題
- [[基本面分析/Piotroski-F-Score財務品質評分模型]] — 財務品質評分
- [[基本面分析/Altman-Z-Score破產預測模型]] — 破產預測
- [[基本面分析/Ohlson-O-Score破產預測模型]] — 破產預測
- [[基本面分析/信用評等與公司債違約風險判讀Credit-Rating-and-Default-Risk]] — 信用風險

## 來源
- Beneish, Messod D. (1999). "The Detection of Earnings Manipulation"
- Beneish, Lee & Nichols (2013). "Year-end Shifting and the Performance of the Beneish Model"
- Beneish & Vorst (2020). "The Cost of Being Good: The Returns to ESG Investing"
- Wikipedia: Beneish M-score
