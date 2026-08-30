---
title: Romano-Wolf重抽樣逐步多重檢定
aliases: [Romano-Wolf Stepdown, Romano-Wolf多重檢定, Bootstrap Stepdown, 重抽樣Stepdown]
category: 風險管理
date: 2026-08-23
---

# Romano-Wolf重抽樣逐步多重檢定


> Romano-Wolf Stepdown在同時檢定多個策略時，用重抽樣估計「剩餘假設最大統計量」的聯合虛無分布，再從最強訊號逐步往下檢定，控制至少誤報一次的機率，又比無視策略相關性的Bonferroni和Holm通常更有檢定力。

## 核心概念
Romano-Wolf Stepdown在同時檢定多個策略時，用重抽樣估計「剩餘假設最大統計量」的聯合虛無分布，再從最強訊號逐步往下檢定，控制至少誤報一次的機率，又比無視策略相關性的Bonferroni和Holm通常更有檢定力。

## 問題從哪裡來

同時測$m$個策略，每個都用5%單一顯著水準。即使全部沒有alpha，至少出現一個假陽性的機率會隨$m$增加。

若檢定彼此獨立：

$$P(\text{至少一次誤報})=1-(1-\alpha)^m$$

測100個策略時還拿$p<0.05$當通行證，跟發100張彩券後驚呼「天啊居然有人中獎」差不多蠢。

## FWER是什麼

令：

- $V$：被錯誤拒絕的真虛無假設數
- $R$：全部被拒絕的假設數

Familywise Error Rate（FWER）定義為：

$$FWER=P(V\ge1)$$

### 弱控制

只在所有虛無假設都為真時控制FWER。

### 強控制

在任何真假假設組合下都控制：

$$FWER\le\alpha$$

Romano-Wolf的目標是強FWER控制。對要投入真金白銀、錯選一個高槓桿策略就會出事的研究，這種嚴格標準有其價值。

## 策略假設怎麼設

對策略$j$的成本後報酬，可設單尾假設：

$$H_j:E[r^{net}_{j,t}]\le0$$

$$H'_j:E[r^{net}_{j,t}]>0$$

個別studentized統計量可寫為：

$$T_j=\frac{\sqrt n\,\bar r^{net}_j}{\widehat\omega_j}$$

其中$\widehat\omega_j$是考慮時間相依的長期標準差估計。

也能檢定：

- 因子alpha是否大於零
- 預測模型是否降低損失
- 新策略是否優於既有基準
- 多個事件研究效果是否非零
- 多個交易成本改善是否顯著

檢定方向、績效口徑與基準必須事前寫死。看完正負號才決定單尾方向，叫作弊，不叫彈性。

## 為何不只用Bonferroni或Holm

### Bonferroni

每個假設使用：

$$\alpha_j=\frac{\alpha}{m}$$

優點是通用簡單，缺點是忽略假設間相關性。100個策略其實只是同一均線參數的近親，Bonferroni仍把它們當100個陌生人處罰，保守到訊號都被勒死。

### Holm Stepdown

先排序p值，再逐步使用：

$$\frac{\alpha}{m},\frac{\alpha}{m-1},\ldots,\alpha$$

Holm比單步Bonferroni強，但仍不直接利用檢定統計量的聯合依賴結構。

### Romano-Wolf

直接用同步重抽樣估計最大統計量分布。候選高度相關時，有效獨立試驗數可能遠小於$m$，因此通常能比Bonferroni與Holm保留更多檢定力，同時維持FWER控制。

## Stepdown核心流程

令尚未拒絕的假設索引集合為$K_s$。

### 第一步：排序觀測統計量

$$T_{r_1}\ge T_{r_2}\ge\cdots\ge T_{r_m}$$

較大的$T$對虛無假設提供較強反證。

### 第二步：建立第一階段最大值虛無分布

在每次重抽樣$b$中，對所有假設同步計算中心化統計量$T_j^{*,b}$，並取：

$$M_{K_1}^{*,b}=\max_{j\in K_1}T_j^{*,b}$$

以其$1-\alpha$分位數作臨界值：

$$c_{K_1}(1-\alpha)$$

### 第三步：檢定目前最強訊號

若：

$$T_{r_1}>c_{K_1}(1-\alpha)$$

則拒絕$H_{r_1}$，把它移出集合；否則停止並保留全部剩餘假設。

### 第四步：縮小集合後重算

令：

$$K_2=K_1\setminus\{r_1\}$$

重新使用$\max_{j\in K_2}T_j^{*}$的分布檢定$T_{r_2}$。因最強訊號已移除，臨界值通常下降，這就是stepdown比單步maxT更有力的來源。

### 第五步：直到第一次無法拒絕

一旦某階段無法拒絕目前最大統計量，所有剩餘假設停止拒絕。不要跳過失敗者繼續挑後面較小的統計量，否則stepdown的錯誤控制結構被你自己踹爛。

## 調整p值

對排序後第$s$個假設，可先估計該階段重抽樣p值：

$$\widehat p_{r_s}^{raw}=\frac{1}{B}\sum_{b=1}^{B}\mathbf 1\left\{\max_{j\in K_s}T_j^{*,b}\ge T_{r_s}\right\}$$

為維持stepdown單調性，調整p值取累積最大：

$$\widehat p_{r_s}^{adj}=\max_{u\le s}\widehat p_{r_u}^{raw}$$

實作常使用加一修正避免有限次重抽剛好得到零p值；重點不是小數點裝得多精緻，而是重抽樣次數足以讓結論穩定。

## 金融時間序列怎麼重抽

策略報酬可能存在：

- 自相關
- 波動率聚集
- 持有期重疊
- 共同市場曝險
- 同期流動性衝擊

因此應同步重抽整個策略報酬向量，並使用適合的時間序列方法，例如：

- Moving Block Bootstrap
- Stationary Bootstrap
- Circular Block Bootstrap
- 在條件成立時使用其他bootstrap或subsampling

不能每個策略各抽各的，也不能逐日獨立洗牌。那會抹掉策略相關性與時間相依，讓最大統計量臨界值失真。

## 和White RC與SPA的差別

[[風險管理/White-Reality-Check與Hansen-SPA多重策略檢定|White Reality Check與Hansen SPA]]主要檢定：

$$H_0:\max_j\mu_j\le0$$

若拒絕，只能說候選集合中至少一個策略優於基準，不會自動告訴你哪些個別策略通過。

Romano-Wolf則對多個個別假設做逐步調整，在FWER控制下識別可拒絕者。

實務可採：

1. RC或SPA先做集合層級的存在性檢定
2. Romano-Wolf再做個別策略識別
3. 之後才進封存樣本與經濟顯著性審查

但若兩階段都是看完結果才臨時加的篩選，整體研究流程仍可能產生額外選擇偏差。

## FWER還是FDR

FWER適合：

- 錯選任何一個策略代價都高
- 高槓桿或重大資金配置
- 確認性研究
- 風控模型與監管用途

若只是大量探索候選、可以容忍少量誤報以避免漏掉太多真訊號，FDR可能更合適。先決定錯誤成本，再選方法；不是哪個p值比較小就信哪個。

## 實戰檢查清單

- 是否定義要控制FWER而非只看個別p值
- 是否使用強控制觀念
- 假設方向是否事前指定
- 是否把所有試過的策略納入研究家族
- 是否同步重抽保留策略相關性
- 是否使用區塊方法保留時間相依
- 是否對每輪剩餘集合重算最大統計量
- 調整p值是否保持單調
- 結論是否經封存樣本與成本驗證
- 是否避免把統計通過講成未來獲利保證

## 實戰啟示

1. 多策略研究要控制的是整個家族的誤報風險，不是每個策略各自裝無辜
2. Romano-Wolf利用策略間相關性，通常比Bonferroni與Holm少浪費檢定力
3. Stepdown每移除一個強訊號就縮小最大值比較範圍，讓後續真訊號有機會被看見
4. 金融資料必須同步區塊重抽，獨立亂抽只是把麻煩藏起來
5. 調整後顯著只代表統計第一關通過，離能下單還隔著成本、容量、體制與實盤四座山

## 實戰應用
### 研究前凍結

- 所有候選策略與參數
- 每個虛無與替代假設
- 單尾或雙尾方向
- 報酬、alpha或損失定義
- 交易成本與滑價
- 樣本期間與資產池
- 顯著水準
- bootstrap方法與區塊長度

### 建立同步資料矩陣

每列是一個日期，每欄是一個策略或假設。所有欄位必須：

- 使用相同時間索引
- 相同無風險利率與基準
- 相同成本口徑
- 一致處理缺值
- 避免前瞻與生存者偏差

### 計算觀測統計量

使用能處理異質變異與時間相依的標準誤，且所有策略採相同原則。

### 同步重抽並Stepdown

- 每次重抽保留整個橫斷面向量
- 每個階段對剩餘集合取最大值
- 保存原始p值、調整p值、拒絕順序與臨界值
- 變更區塊長度與隨機種子做敏感度檢查

### 進入實盤前再驗證

通過Romano-Wolf仍需：

- 封存樣本
- Walk-Forward
- 參數鄰域穩定性
- 容量與交易成本壓力測試
- 市場體制拆解
- 回撤與尾部風險檢查

## 注意事項
- **很嚴格**：FWER只要出現一次誤報就算失敗，候選很多時檢定力仍可能不足
- **依賴估計品質**：區塊長度與重抽方法錯誤會污染聯合虛無分布
- **有限樣本不保證神奇**：理論漸近有效不代表200筆資料就突然很可靠
- **研究宇宙要完整**：漏報失敗策略仍會低估多重比較
- **統計顯著不等於可交易**：alpha小到不夠付成本照樣沒用
- **共同偏差無法修復**：全部策略共用污染資料，嚴謹檢定只是在垃圾場精準分類
- **結構轉折風險**：歷史聯合依賴不一定延續到下一個市場體制

## 相關主題
- [[風險管理/White-Reality-Check與Hansen-SPA多重策略檢定]]
- [[風險管理/通縮夏普比率Deflated-Sharpe-Ratio]]
- [[風險管理/Purged-K-Fold交叉驗證與Embargo防洩漏]]
- [[風險管理/回測過擬合Backtest-Overfitting]]
- [[風險管理/回測框架與偏差防範Backtesting-Framework-and-Bias-Prevention]]
- [[操作策略/Walk-Forward-Analysis滾動前進驗證]]

## 來源
- Romano, J. P., & Wolf, M. (2005). [Exact and Approximate Stepdown Methods for Multiple Hypothesis Testing](https://doi.org/10.1198/016214504000000539). *Journal of the American Statistical Association*, 100(469), 94–108. [公開工作論文PDF](https://econ-papers.upf.edu/papers/727.pdf)
- Stanford University. [Exact and Approximate Stepdown Methods for Multiple Hypothesis Testing](https://statistics.stanford.edu/technical-reports/exact-and-approximate-stepdown-methods-multiple-hypothesis-testing).

---

*最後更新：2026-08-23*
