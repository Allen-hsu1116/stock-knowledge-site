---
title: VaR回測Kupiec Christoffersen與Basel燈號
aliases: [VaR Backtesting, Kupiec POF, Christoffersen Conditional Coverage, Basel Traffic Light, VaR例外回測]
category: 風險管理
date: 2026-08-21
---

# VaR回測：Kupiec、Christoffersen與Basel燈號


> VaR 回測不是看預測線畫得漂不漂亮，而是逐日記錄實際損失是否超過昨日預測的 VaR：Kupiec 檢查例外率對不對，Christoffersen 再檢查例外有沒有群聚，Basel 燈號則把 250 日、99% VaR 的例外數分成綠黃紅三區。
## 核心概念
VaR 回測不是看預測線畫得漂不漂亮，而是逐日記錄實際損失是否超過昨日預測的 VaR：Kupiec 檢查例外率對不對，Christoffersen 再檢查例外有沒有群聚，Basel 燈號則把 250 日、99% VaR 的例外數分成綠黃紅三區。

## 為什麼VaR一定要回測

[[風險管理/VaR風險值Value-at-Risk|VaR]]是一個條件分位數預測。模型宣稱 99% 一日 VaR 為 100 萬元，意思是依模型與目前資訊，未來一天損失超過 100 萬元的機率應為 1%。

如果實際超標：

- 太頻繁：模型低估風險
- 太少：模型可能過度保守，也可能浪費資本
- 成群出現：模型沒有及時捕捉波動體制
- 幅度巨大：尾部分布、流動性或非線性風險漏掉

只算 VaR 不回測，跟裝煙霧偵測器但從不換電池一樣，平常很有安全感，出事只剩裝飾功能。

## 例外指標

令 $L_t$ 為第 $t$ 日實際損失，$\operatorname{VaR}_{t|t-1}$ 為前一日用當時資訊預測的 VaR：

$$I_t=\mathbf{1}\{L_t>\operatorname{VaR}_{t|t-1}\}$$

其中：

- $I_t=1$：發生例外或 breach
- $I_t=0$：損失未超過 VaR
- 信心水準為 $c$
- 理論例外機率 $p=1-c$
- 樣本數為 $n$
- 例外總數 $x=\sum_{t=1}^n I_t$

良好 VaR 模型至少需要：

1. **無條件覆蓋正確**：$P(I_t=1)=p$
2. **例外獨立**：$I_t$ 不應出現可預測群聚
3. **損益與預測口徑一致**：同持有期、同部位、同資料截止點

## 最基本的例外數檢查

若例外獨立且機率固定：

$$X=\sum_{t=1}^n I_t\sim\operatorname{Binomial}(n,p)$$

因此：

$$E[X]=np$$

$$\operatorname{Var}(X)=np(1-p)$$

例如 99% VaR、250 個交易日：

$$E[X]=250\times0.01=2.5$$

理論平均只有 2.5 次例外，這也說明高信心水準回測很缺資料。一年沒超標不代表模型宇宙第一，可能只是尾巴根本還沒輪到上班。

## Kupiec無條件覆蓋檢驗

Kupiec 的 Proportion of Failures test 檢驗：

$$H_0:\ \widehat p=\frac{x}{n}=p$$

似然比統計量：

$$LR_{uc}=-2\log\left[\frac{(1-p)^{n-x}p^x}{(1-\widehat p)^{n-x}\widehat p^x}\right]$$

在虛無假設下漸近服從：

$$LR_{uc}\sim\chi_1^2$$

解讀：

- 統計量小：實際例外率與目標例外率差異沒有足夠證據
- 統計量大：模型可能系統性高估或低估 VaR
- 不能只做單尾檢查，例外太少也可能代表模型過度保守

### Kupiec的弱點

假設 250 日內有 5 次例外：

- 模型A：分散在全年
- 模型B：全部擠在同一週

Kupiec 只看到「都是 5 次」，無法識別模型B在危機初期完全沒追上波動率。頻率對不代表時序對，這就是 Christoffersen 要補的洞。

## Christoffersen獨立性檢驗

建立例外狀態的一階 Markov 轉移計數：

- $N_{00}$：前日無例外、今日也無例外
- $N_{01}$：前日無例外、今日有例外
- $N_{10}$：前日有例外、今日無例外
- $N_{11}$：前日有例外、今日也有例外

條件例外機率：

$$\pi_{01}=\frac{N_{01}}{N_{00}+N_{01}}$$

$$\pi_{11}=\frac{N_{11}}{N_{10}+N_{11}}$$

不考慮前一日狀態的總體轉移例外率：

$$\pi=\frac{N_{01}+N_{11}}{N_{00}+N_{01}+N_{10}+N_{11}}$$

獨立性似然比：

$$LR_{ind}=-2\log\left[\frac{(1-\pi)^{N_{00}+N_{10}}\pi^{N_{01}+N_{11}}}{(1-\pi_{01})^{N_{00}}\pi_{01}^{N_{01}}(1-\pi_{11})^{N_{10}}\pi_{11}^{N_{11}}}\right]$$

虛無假設為：

$$H_0:\ \pi_{01}=\pi_{11}$$

漸近分布：

$$LR_{ind}\sim\chi_1^2$$

若 $\pi_{11}$ 明顯高於 $\pi_{01}$，表示昨天超標後今天更容易繼續超標，例外正在群聚。

## Christoffersen條件覆蓋檢驗

把正確例外率與獨立性合併：

$$LR_{cc}=LR_{uc}+LR_{ind}$$

漸近分布：

$$LR_{cc}\sim\chi_2^2$$

這個聯合檢驗要求模型同時做到：

- 長期例外比例正確
- 例外不群聚

但聯合檢驗通過不代表模型完美，因為：

- 小樣本檢驗力不足
- 只看有沒有超標，不看超標多少
- 一階 Markov 只抓最簡單的群聚
- 結構性斷點可能被平均掉

## Basel交通燈框架

Basel 1996 文件以最近 250 個交易日、99% 一日 VaR 為例：

- **綠燈：0至4次例外**
- **黃燈：5至9次例外**
- **紅燈：10次以上例外**

### 綠燈

結果與正確 99% 覆蓋模型相容，不代表模型保證正確，只是沒有足夠警訊。

### 黃燈

可能是模型不準，也可能是統計運氣。需要檢查：

- 例外發生時間
- 例外幅度
- 是否集中在單一交易單位
- 波動率與相關性是否更新過慢
- 是否漏掉風險因子
- 實際損益是否被盤中交易污染

### 紅燈

對正確 99% 模型而言極不尋常，原則上應推定模型存在問題並立即調查。

燈號門檻只適用特定樣本數與信心水準。拿 95% VaR 或 500 日樣本照抄 0至4、5至9、10以上，這不是 Basel，是數字角色扮演。

## 假設損益與實際損益

### Hypothetical P&L

固定昨日收盤部位，只套用今日市場變動：

- 較乾淨地檢驗 VaR 模型
- 排除盤中換倉與新交易
- 適合確認風險因子、估值與市場資料是否正確

### Actual P&L

使用真實交易結果：

- 包含盤中交易
- 可能包含費用與價差收入
- 反映真實帳戶結果
- 但不一定與昨日 VaR 的靜態部位假設一致

Basel 文件建議兩種口徑都有價值。只用 actual P&L，模型錯誤可能被穩定手續費收入遮住；只用 hypothetical P&L，又可能漏掉交易執行與盤中風險。

## 例外原因分類

每一次 breach 都應有事件紀錄，而不是在試算表多塗一格紅色就下班。

### 資料與系統完整性

- 持倉漏載
- 價格錯誤
- 公司行動未調整
- 波動率或相關性計算程式錯誤
- 時區與資料截止點不一致

### 模型規格不足

- 漏掉 basis、spread 或 volatility risk
- 選擇權只用 Delta 近似
- 曲面節點太少
- 相關性固定
- 未納入跳空與流動性

### 市場體制改變

- 波動率突然上升
- 相關性崩潰
- 政策或事件跳躍
- 停牌、熔斷、流動性枯竭

### 交易活動污染

- 盤中新增大部位
- 交易員改變方向
- 手續費或新產品收入
- 收盤標記與實際成交落差

## 超標幅度不能忽略

標準覆蓋檢驗把下列兩件事都記成 $I_t=1$：

- 損失比 VaR 多 1 元
- 損失是 VaR 的 5 倍

因此風險儀表板還應追蹤：

$$M_t=\max(0,L_t-\operatorname{VaR}_{t|t-1})$$

以及：

- 平均超標幅度
- 最大超標倍數
- 例外日 Expected Shortfall
- 累計例外損失
- 例外與流動性、VIX、相關性的關係

頻率檢驗是必要條件，不是完整尾部風控。

## 小樣本與檢驗力

高信心水準的尷尬是例外很少：

- 95% VaR、250日：預期 12.5 次例外
- 99% VaR、250日：預期 2.5 次例外
- 99.9% VaR、250日：預期 0.25 次例外

信心水準越高，傳統二元回測越沒力。

改善方式：

- 延長樣本，但注意市場結構過時
- 同時回測多個分位數
- 使用 duration-based test
- 檢查完整預測分布或 probability integral transform
- 對 Expected Shortfall 使用適合的聯合回測框架
- 結合壓力測試與情境分析

「沒有拒絕模型」只代表證據不足，不能翻譯成「模型已證明正確」。統計課最愛被金融簡報這樣糟蹋。

## 動態模型的回測

對 GARCH 或[[風險管理/波動率體制轉換模型Volatility-Regime-Switching-Model|體制轉換模型]]，每日 VaR 應使用當日可得資訊滾動產生：

1. 在 $t-1$ 日收盤估計模型
2. 產生 $t$ 日 VaR
3. 到 $t$ 日收盤取得損益
4. 記錄是否超標
5. 不得用 $t$ 日資料回頭修正昨日預測
6. 重複整個樣本外期間

如果回測中每一天都用全期間參數，未來資訊已經偷渡進模型。結果再漂亮也只是穿越時空作弊。

## 與FHS的關係

普通歷史模擬、參數法與[[風險管理/過濾歷史模擬Filtered-Historical-Simulation|FHS]]都必須用同一套回測框架比較：

- 例外率
- 例外群聚
- 超標幅度
- VaR穩定度
- 資本或部位調整頻率
- 危機期反應速度

模型越複雜，越不能只看樣本內擬合。[[風險管理/回測驗證Backtesting陷阱|回測陷阱]]在風險模型一樣會咬人，而且咬的通常不是學術分數，是你的錢。

## 實戰應用

### 實戰監控SOP
### 每日

- 保存昨日 VaR 與部位快照
- 計算 hypothetical P&L 與 actual P&L
- 判斷是否 breach
- 記錄超標幅度與初步原因
- 檢查資料、估值與持倉完整性

### 每月

- 更新滾動例外率
- 計算 Kupiec $LR_{uc}$
- 檢查連續例外與轉移計數
- 按策略、資產與風險因子拆解例外
- 比較 VaR 與 Expected Shortfall

### 每季

- 執行 Christoffersen independence 與 conditional coverage
- 檢查 Basel 燈號或依自身樣本重算二項門檻
- 做模型版本比較
- 進行壓力測試與反向壓力測試
- 決定是否調整限額、參數或模型

## 注意事項
- **檢驗力不足**：一年樣本對 99% VaR 太短
- **二元資訊損失**：不看超標幅度
- **例外非獨立**：傳統二項假設在波動率聚集下容易失效
- **P&L口徑污染**：盤中交易與費用收入可能掩蓋模型問題
- **多重檢定**：同時測很多模型與分位數會提高誤判率
- **模型選擇偏差**：挑回測最好看的版本再報告，照樣是過度擬合
- **結構性斷點**：長樣本提高統計力，也混入過時體制
- **VaR通過不等於ES正確**：分位數對了，尾部平均仍可能嚴重低估
- **燈號不是通用真理**：Basel門檻依特定 $n$ 與 $c$ 設定

## 實戰檢查清單

- VaR與P&L是否同為一日持有期
- 預測是否只使用當時可得資料
- 損失正負號與超標條件是否一致
- 是否同時計算 hypothetical 和 actual P&L
- 例外率是否接近 $1-c$
- 例外是否群聚
- 是否記錄超標幅度與原因
- 是否依正確樣本數重算二項門檻
- 是否檢查 Expected Shortfall 與壓力情境
- 模型調整後是否保留版本與樣本外驗證

## 關鍵啟示

1. Kupiec回答「例外總數對不對」，Christoffersen回答「例外有沒有群聚」
2. 條件覆蓋必須同時滿足正確頻率與獨立性
3. Basel 0至4、5至9、10以上只適用250日與99% VaR
4. 假設損益檢驗模型，實際損益檢驗真實帳戶，兩者都要看
5. 回測通過只代表尚未抓到足夠證據，不代表尾部風險從此被馴服

## 相關主題
- [[風險管理/VaR風險值Value-at-Risk]]
- [[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall]]
- [[風險管理/GARCH模型與波動率預測GARCH-Model-and-Volatility-Forecasting]]
- [[風險管理/波動率體制轉換模型Volatility-Regime-Switching-Model]]
- [[風險管理/模型風險Model Risk]]
- [[風險管理/回測驗證Backtesting陷阱]]
- [[風險管理/風險儀表板與每日風控檢查Risk-Dashboard]]
- [[風險管理/過濾歷史模擬Filtered-Historical-Simulation]]

## 來源
- Zhang, Y., & Nadarajah, S. (2018). "A review of backtesting for value at risk." *Communications in Statistics - Theory and Methods*. https://doi.org/10.1080/03610926.2017.1361984
- Christoffersen, P. F. (1998). "Evaluating Interval Forecasts." *International Economic Review*, 39(4), 841–862. https://doi.org/10.2307/2527341
- Basel Committee on Banking Supervision (1996). "Supervisory framework for the use of backtesting in conjunction with the internal models approach to market risk capital requirements." https://www.bis.org/publ/bcbs22.pdf

---

*最後更新：2026-08-21*
