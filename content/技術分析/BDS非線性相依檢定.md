---
title: BDS非線性相依檢定
aliases: [BDS Test, Brock-Dechert-Scheinkman Test, Correlation Dimension Test, 非線性獨立性檢定]
category: 技術分析
date: 2026-08-24
---

# BDS非線性相依檢定

> BDS檢定追問的是「這串資料真的像獨立同分布嗎？」；拒絕後只知道還有結構，並不知道結構叫動量、波動率聚集還是混沌，別拿一個p值就封自己當非線性天才。

## 核心概念

BDS由Brock、Dechert、Scheinkman與LeBaron發展，是不預先指定對立模型形式的獨立同分布檢定。虛無假設為：

$$H_0:\{x_t\}\text{ is an i.i.d. sequence}$$

它先把一維序列重建成$m$維歷史向量：

$$x_t^m=(x_t,x_{t-1},\ldots,x_{t-m+1})$$

接著比較兩個$m$維向量在距離門檻$\varepsilon$內的比例，形成$m$維correlation integral $C_m(\varepsilon)$。若序列為i.i.d.，理論上應近似：

$$C_m(\varepsilon)\approx [C_1(\varepsilon)]^m$$

標準化後的BDS統計量概念式為：

$$W_{m,n}(\varepsilon)=\frac{\sqrt n\left[C_m(\varepsilon)-C_1(\varepsilon)^m\right]}{\hat\sigma_{m,n}(\varepsilon)}$$

在規則條件與虛無假設下，統計量漸近服從標準常態分布。

## 它抓到的是什麼

BDS拒絕i.i.d.可能來自：

- 線性自相關
- 波動率聚集
- 條件異質變異
- 結構轉折
- 非線性相依
- 季節性
- 離群值或資料錯誤
- 真正更複雜的動態結構

所以BDS是「煙霧警報器」，不是「火災鑑識報告」。它會告訴你房子裡有煙，不會自動說是廚房煎魚、電線走火還是鄰居又在亂燒東西。

## 為什麼要先過濾線性與波動結構

直接對股票原始報酬做BDS，拒絕i.i.d.很常見，但資訊含量有限。更有用的流程是：

1. 以AR或ARMA移除線性自相關
2. 以GARCH類模型處理條件波動率
3. 取得標準化殘差
4. 對標準化殘差做BDS
5. 若仍拒絕，才有較強理由懷疑剩餘非線性、結構轉折或模型遺漏

即使走完這套流程，仍不能把「拒絕i.i.d.」翻譯成「發現確定性混沌」。BDS對立假設沒有指定，統計學根本沒替你說那句話。

## Embedding Dimension與Epsilon

BDS結果依賴兩組設定：

- **嵌入維度$m$**：觀察連續多少期共同結構
- **距離門檻$\varepsilon$**：判定兩個向量是否足夠接近

常見實務會檢查多個$m$與以樣本標準差倍數表示的$\varepsilon$，但必須注意：

- $m$提高後有效向量數減少
- $\varepsilon$太小，近鄰太少且估計不穩
- $\varepsilon$太大，局部結構被沖淡
- 同時測太多組合會產生多重檢定問題
- 結果對設定敏感代表證據不穩，不是讓你挑最小p值那格貼金箔

## 交易研究SOP

1. 清理錯價、缺漏與非同步資料
2. 事前指定報酬頻率、$m$與$\varepsilon$集合
3. 先以線性模型處理均值結構
4. 再以波動模型取得標準化殘差
5. 對殘差執行BDS並完整報告所有規格
6. 若拒絕，依經濟機制提出門檻、體制或交互作用假說
7. 新模型必須重新做淨化後樣本外驗證
8. 最後才檢查成本後報酬、容量與實盤穩定性

## 實戰啟示

1. BDS是規格診斷工具，不是方向指標
2. 對原始報酬拒絕i.i.d.通常只是起點，對標準化殘差仍拒絕才更值得追
3. 線性、波動率、轉折與非線性會互相冒充，分析順序不能亂
4. 多個參數組都一致才算穩健，只有一格p值漂亮多半只是統計彩券
5. 發現殘差有結構不等於已找到能扣成本變現的交易規則

## 實戰應用

### 應用一：檢查技術訊號是否漏掉非線性

假設模型為：

$$r_{t+1}=\alpha+\beta_1\text{Momentum}_t+\beta_2\text{Volatility}_t+u_{t+1}$$

若$u_t$通過線性自相關診斷，卻在BDS仍顯著，可能表示：

- 訊號效果隨市場體制改變
- 上漲與下跌反應不對稱
- 波動率門檻造成非線性
- 多個技術指標存在交互作用
- 單一線性係數無法描述關係

下一步應提出可解釋的新模型並做封存樣本驗證，不是一路加神經網路加到回測變成人體藝術。

### 應用二：比較模型前後殘差

- 原始報酬BDS顯著
- ARMA殘差仍顯著
- ARMA-GARCH標準化殘差不顯著

這種結果表示原本的相依主要可由線性與條件波動率解釋，沒有必要硬扯神秘非線性alpha。

若ARMA-GARCH後仍顯著，才進一步檢查門檻模型、體制轉換、非線性均值或資料分段。

### 應用三：策略上線前的殘差閘門

對候選策略的樣本外殘差同時做：

- 線性自相關診斷
- BDS檢定
- 波動率聚集診斷
- 結構穩定檢定

四者分工不同。單一檢定通過不代表模型正確，全部通過也只代表目前沒抓到明顯規格錯誤，市場明天照樣可能翻桌。

## 注意事項

- **拒絕i.i.d.不等於發現非線性獲利機會**
- **拒絕不等於混沌**：要主張chaos還需要其他識別與穩健證據
- **先去除線性相關**：否則BDS只是重複抓到已知自相關
- **先處理異質變異**：波動率聚集本身就足以造成拒絕
- **對離群值敏感**：錯價與資料缺口會改變距離關係
- **高維與長樣本昂貴**：常見實作涉及$n\times n$距離矩陣
- **小樣本近似有限**：高$m$、小$\varepsilon$時尤其不穩
- **多重規格要校正**：跨$m$、$\varepsilon$、標的與頻率不能只報喜不報憂

## 相關主題

- [[技術分析/Ljung-Box自相關白噪音檢定]]
- [[技術分析/CUSUM累積和結構轉折檢定]]
- [[技術分析/赫斯特指數Hurst-Exponent]]
- [[技術分析/卡爾曼濾波器Kalman-Filter]]
- [[風險管理/波動率體制轉換模型Volatility-Regime-Switching-Model]]
- [[技術分析/技術分析回測方法與過度擬合Backtesting-and-Overfitting]]

## 來源

- Brock, W. A., Dechert, W. D., Scheinkman, J. A., & LeBaron, B. (1996). [A Test for Independence Based on the Correlation Dimension](https://doi.org/10.1080/07474939608800353). *Econometric Reviews*, 15(3), 197–235.
- statsmodels. [BDS Test Statistic for Independence of a Time Series](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.bds.html), version 0.14.6.
- LeBaron, B. (1992). [Some Relations Between Volatility and Serial Correlations in Stock Market Returns](https://doi.org/10.1086/296465). *Journal of Business*, 65(2), 199–219.

---

*最後更新：2026-08-24*
