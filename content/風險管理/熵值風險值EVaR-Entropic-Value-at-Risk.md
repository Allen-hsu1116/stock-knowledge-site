---
title: 熵值風險值EVaR (Entropic Value-at-Risk)
aliases: [Entropic Value-at-Risk, EVaR, 熵風險值]
category: 風險管理
date: 2026-08-21
---

# 熵值風險值EVaR (Entropic Value-at-Risk)


> 熵值風險值 EVaR 用損失分布的指數動差與 Chernoff bound 衡量尾部風險；它是一致性風險測度、同信心水準下通常比 VaR 與 CVaR 更保守，並可解讀為在 Kullback-Leibler 相對熵限制內尋找最壞期望損失。

## 核心概念
熵值風險值 EVaR 用損失分布的指數動差與 Chernoff bound 衡量尾部風險；它是一致性風險測度、同信心水準下通常比 VaR 與 CVaR 更保守，並可解讀為在 Kullback-Leibler 相對熵限制內尋找最壞期望損失。

## 為什麼還需要EVaR

[[風險管理/VaR風險值Value-at-Risk|VaR]]只告訴你某個分位數門檻，不告訴你超過門檻後會摔多深，而且一般情況下不滿足次可加性。

[[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall|CVaR或Expected Shortfall]]對最差尾部取平均，已經比 VaR 合理，也滿足[[風險管理/一致性風險測度Coherent-Risk-Measures|一致性風險測度]]四大公理。

EVaR 再往前一步：

- 使用整個指數動差，不只截取一段尾部樣本
- 是 Chernoff inequality 對 VaR 與 CVaR 可給出的最緊上界
- 同一信心水準下通常滿足 $\operatorname{VaR}\le\operatorname{CVaR}\le\operatorname{EVaR}$
- 對可微凸損失可形成可微凸最佳化問題
- 對偶表示帶有 KL divergence，可自然連到分布魯棒最佳化

代價也很直白：它通常更保守，而且對動差母函數是否存在非常挑剔。數學不是免費保險，保守到最後也可能只剩現金抱著哭。

## 定義與符號慣例

令 $L$ 為「損失」隨機變數，越大越糟；信心水準為 $c\in(0,1)$，尾部機率為 $\alpha=1-c$。

EVaR 定義為：

$$\operatorname{EVaR}_{c}(L)=\inf_{z>0}\frac{\log E[e^{zL}]-\log(1-c)}{z}$$

或用尾部機率表示：

$$\operatorname{EVaR}_{1-\alpha}(L)=\inf_{z>0}\frac{\log E[e^{zL}]-\log\alpha}{z}$$

其中：

- $z>0$ 是需要最佳化的傾斜參數
- $E[e^{zL}]$ 是損失的動差母函數
- $\log E[e^{zL}]$ 是 cumulant-generating function
- $-\log\alpha$ 會隨信心水準提高而增加

文獻有時用報酬而非損失、也有人把 $\alpha$ 當信心水準。抄公式前先看符號，不然 99% 風控會被你寫成只管最好的 99%，這種低級錯誤特別有金融業傳統。

## Chernoff上界從哪裡來

對任意 $z>0$，Markov inequality 給出：

$$P(L\ge x)=P(e^{zL}\ge e^{zx})\le e^{-zx}E[e^{zL}]$$

若希望右側不超過尾部機率 $\alpha$，則：

$$x\ge\frac{\log E[e^{zL}]-\log\alpha}{z}$$

對所有 $z>0$ 取最小值，就得到 EVaR。

所以 EVaR 不是憑空發明一個更大的數字，而是把「指數尾界」調到最緊。它控制的是機率上界，不是預言明天一定不會超過。

## 與VaR和CVaR的關係

### VaR

- 只看分位數門檻
- 不描述超標後的損失幅度
- 對離散或非凸分布可能違反次可加性
- 最佳化常不平滑且難解

### CVaR

- 衡量超過 VaR 後的平均損失
- 是一致性風險測度
- 樣本式線性組合最佳化可轉成線性規劃
- 輔助變數與限制式通常隨情境數增加

### EVaR

- 用所有樣本的指數加權資訊
- 是一致性風險測度
- 通常是 VaR 與 CVaR 的上界
- 在可微凸條件下可用平滑凸最佳化
- 樣本數增加主要增加函數評估成本，不必等比例增加最佳化變數與限制式
- 對極端損失的權重成指數增加，因此會比 CVaR 更敏感

三者不是誰把誰淘汰。VaR 適合溝通門檻，CVaR 適合直接描述尾部平均損失，EVaR 適合保守上界、凸最佳化與分布魯棒解讀。

## 常態分布例子

若損失：

$$L\sim N(\mu,\sigma^2)$$

則：

$$\log E[e^{zL}]=\mu z+\frac12\sigma^2z^2$$

代入 EVaR：

$$\operatorname{EVaR}_{c}(L)=\inf_{z>0}\left(\mu+\frac12\sigma^2z-\frac{\log(1-c)}{z}\right)$$

一階條件得到：

$$z^*=\frac{\sqrt{-2\log(1-c)}}{\sigma}$$

因此：

$$\operatorname{EVaR}_{c}(L)=\mu+\sigma\sqrt{-2\log(1-c)}$$

在常態世界裡，EVaR 最後仍是「平均加波動率倍數」。但真實市場偏態、肥尾、跳空和流動性斷裂一個都不肯配合常態世界演戲，所以別看到封閉解就感動到失去戒心。

## KL相對熵的魯棒解讀

EVaR 的對偶表示可概念化為：

$$\operatorname{EVaR}_{1-\alpha}(L)=\sup_{Q:\,D_{KL}(Q\|P)\le-\log\alpha}E_Q[L]$$

其中：

- $P$ 是基準機率分布
- $Q$ 是候選扭曲分布
- $D_{KL}(Q\|P)$ 衡量 $Q$ 偏離 $P$ 的相對熵
- 半徑 $-\log\alpha$ 隨信心水準提高而放大

直覺是：不要只信基準模型 $P$，而是在一群「不能離它太遠」的分布中找最壞平均損失。

這讓 EVaR 同時具備：

- 尾部風險測度
- 指數效用與 large deviations 結構
- 分布魯棒最佳化意義
- 可用凸最佳化處理的形式

## 樣本估計

給定 $N$ 個損失樣本 $L_1,\ldots,L_N$，經驗 EVaR 可寫成：

$$\widehat{\operatorname{EVaR}}_c=\inf_{z>0}\frac{\log\left(\frac1N\sum_{i=1}^Ne^{zL_i}\right)-\log(1-c)}{z}$$

實作時不能直接計算巨大指數，應使用 log-sum-exp 技巧：

$$\log\sum_i e^{a_i}=m+\log\sum_i e^{a_i-m},\qquad m=\max_i a_i$$

否則極端樣本乘上大 $z$ 後 overflow，風險引擎會先於投資組合爆炸。

## 投資組合最佳化

令權重為 $w$，損失情境為 $L_i(w)$，可建立：

$$\min_w\ \widehat{\operatorname{EVaR}}_c(L(w))$$

並加入：

- 權重總和等於 1
- 單一資產與產業上限
- 目標報酬下限
- 週轉率與交易成本
- 流動性限制
- 槓桿與放空限制

若 $L_i(w)$ 對 $w$ 為凸函數，EVaR 目標通常保留凸性。與 CVaR 的情境式線性規劃相比，EVaR 可用一個額外的 $z$ 配合平滑凸目標，不必為每個樣本增加一個尾部鬆弛變數。

## 實戰檢查清單

- 隨機變數定義為損失還是報酬
- $\alpha$ 是尾部機率還是信心水準
- 動差母函數是否在某個 $z>0$ 有限
- 經驗估計是否使用 log-sum-exp
- $z$ 的搜尋區間與停止條件是否穩定
- 是否比較 VaR、CVaR、EVaR 三者排序
- 是否做 bootstrap 檢查樣本不確定性
- 是否對最大幾個損失做 leave-one-out 敏感度
- 是否加入流動性、交易成本與持有期調整
- 是否用樣本外資料驗證最佳化組合

## 關鍵啟示

1. EVaR 是 VaR 與 CVaR 的 Chernoff 最緊上界，不是另一個換名字的分位數
2. 它滿足一致性風險測度公理，且與 KL 相對熵下的最壞期望損失等價
3. 可微凸結構讓大樣本投資組合最佳化更方便，但保守性也更高
4. MGF 不存在時 EVaR 可能無限大，這是數學邊界，不是程式 bug
5. EVaR 應與 CVaR、壓力測試及流動性情境並用，別把一個漂亮公式當防彈背心

## 實戰應用

### 實戰用途
### 保守尾部風險預算

把組合 EVaR 限制在帳戶淨值的一定比例，適合：

- 高槓桿組合
- 選擇權賣方
- 信用與跳躍風險部位
- 多策略資金配置
- 對尾部模型不確定性特別敏感的帳戶

### VaR與CVaR的壓力上界

同時計算 VaR、CVaR 與 EVaR：

- 三者接近：尾部相對溫和或樣本模型接近橢圓分布
- EVaR 遠高於 CVaR：極端樣本、重尾或指數動差敏感度正在放大
- 跨日差距突然擴張：可能是新離群值、波動體制切換或資料錯誤

### 模型風險比較

在歷史模擬、GARCH、跳躍模型和壓力情境下分別計算 EVaR。不同模型的差距可作為[[風險管理/模型風險Model Risk|模型風險]]區間，而不是假裝單一數字有神諭能力。

## 注意事項
- **MGF可能不存在**：Student-t、Pareto 等重尾分布的正向 MGF 可能對所有 $z>0$ 都發散，EVaR 會變成無限大
- **極端樣本敏感**：指數加權會讓少數大損失支配結果
- **有限樣本偏差**：高信心水準需要大量尾部資料，否則數字只是精密包裝的樣本偶然
- **基準分布風險**：KL ball 仍圍繞基準分布，基準模型漏掉停牌或流動性枯竭時，魯棒也可能魯錯方向
- **過度保守**：EVaR 高於 CVaR，直接拿來最佳化可能把組合推向現金或低波動集中
- **參數與符號混亂**：$c$、$\alpha$、loss、return 的文獻慣例不一
- **不含路徑資訊**：EVaR 是終值分布風險，不直接衡量回撤持續時間、保證金追繳順序或停損滑價
- **不是最大損失**：它仍是機率風險測度，不是損失上限保證

## 相關主題
- [[風險管理/VaR風險值Value-at-Risk]]
- [[風險管理/條件風險價值CVaR與期望短缺Expected-Shortfall]]
- [[風險管理/一致性風險測度Coherent-Risk-Measures]]
- [[風險管理/光譜風險測度Spectral-Risk-Measure]]
- [[風險管理/模型風險Model Risk]]
- [[風險管理/策略壓力測試Stress-Testing]]

## 來源
- Ahmadi-Javid, A. (2012). "Entropic Value-at-Risk: A New Coherent Risk Measure." *Journal of Optimization Theory and Applications*, 155, 1105–1123. https://doi.org/10.1007/s10957-011-9968-2
- Ahmadi-Javid, A., & Fallah-Tafti, M. (2019). "Portfolio Optimization with Entropic Value-at-Risk." *European Journal of Operational Research*, 279(1), 225–241. https://arxiv.org/abs/1708.05713

---

*最後更新：2026-08-21*
