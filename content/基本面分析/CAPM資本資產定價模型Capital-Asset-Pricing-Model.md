---
title: "CAPM資本資產定價模型 Capital Asset Pricing Model"
category: "基本面分析"
---

# CAPM資本資產定價模型 Capital Asset Pricing Model

> 一條公式告訴你承擔系統性風險應該獲得多少報酬——投資理論的基石，也是所有資產定價模型的起點

## 核心概念

CAPM（Capital Asset Pricing Model）是1960年代由Jack Treynor、William Sharpe、John Lintner和Jan Mossin獨立發展的資產定價模型，用來確定一個資產在充分分散的投資組合中，理論上應有的必要報酬率。模型只考慮資產對不可分散風險（系統性風險）的敏感度——即Beta（β）——以及市場的預期報酬和無風險利率。

Sharpe、Markowitz和Merton Miller因這項貢獻共同獲得1990年諾貝爾經濟學獎。Fischer Black（1972）後來發展了不假設無風險資產存在的Black CAPM（零Beta CAPM），在實證上更為穩健。

### CAPM公式

```
E(Ri) = Rf + βi × [E(Rm) - Rf]
```

- **E(Ri)**：資產i的預期報酬率
- **Rf**：無風險利率（如美國國庫券利率）
- **βi**：資產i的Beta係數，衡量對市場風險的敏感度
- **E(Rm)**：市場投資組合的預期報酬率
- **E(Rm) - Rf**：市場風險溢酬（Market Risk Premium）

### Beta的定義

```
βi = Cov(Ri, Rm) / Var(Rm) = ρi,m × σi × σm / σm²
```

Beta衡量個別資產報酬對市場報酬的敏感度：
- **β = 1**：與市場同步波動
- **β > 1**：比市場更波動（高系統性風險）
- **β < 1**：比市場更穩定（低系統性風險）
- **β = 0**：與市場無相關
- **β < 0**：與市場反向相關（極罕見）

### 風險的兩種類型

CAPM的核心假設是投資人只應為系統性風險獲得補償：

- **系統性風險（Systematic Risk）**：市場整體風險，無法透過分散消除。包括利率變動、經濟衰退、戰爭等宏觀因素。CAPM只補償這種風險。
- **非系統性風險（Unsystematic Risk）**：個別公司特有風險，可透過分散投資消除。持有30-40檔股票即可消除大部分非系統性風險。

## 證券市場線（SML）

CAPM的圖形表示就是證券市場線（Security Market Line, SML）：

- **X軸**：系統性風險（Beta）
- **Y軸**：預期報酬率
- **截距**：無風險利率Rf
- **斜率**：市場風險溢酬 E(Rm) - Rf

**SML的判讀**：
- 資產落在SML**上方** → 被低估（提供比系統性風險所要求的更高的報酬）
- 資產落在SML**下方** → 被高估（報酬不足以補償其系統性風險）
- 資產落在SML**上** → 合理定價

### Jensen's Alpha

當資產偏離SML時，偏離量就是Jensen's Alpha：

```
E(Ri) = Rf + βi × [E(Rm) - Rf] + αi
```

- **α > 0**：超額報酬，資產被低估
- **α = 0**：合理定價
- **α < 0**：報酬不足，資產被高估

> 相關頁面：[[風險管理/詹森Alpha與特雷諾比率Jensen-Alpha-and-Treynor-Ratio]] — Alpha的進階應用與績效評估

## CAPM的假設

CAPM建立在以下理想化假設上：

1. **投資人追求效用最大化**：都是理性的、風險趨避的
2. **充分分散投資**：投資人持有廣泛分散的投資組合
3. **價格接受者**：單一投資人無法影響價格
4. **無限借貸**：可以無風險利率無限借貸
5. **無交易成本與稅**：完美市場
6. **資產可無限分割**：所有資產完全可分割且流動
7. **同質預期**：所有投資人對未來有相同預期
8. **資訊同時可得**：所有投資人同時獲得所有資訊

## 實戰應用

### 1. 計算必要報酬率作為折現率

CAPM最常見的用途是計算股權資本成本（Cost of Equity），作為DCF估值的折現率：

```
股權成本 = Rf + β × (E(Rm) - Rf)
```

然後用這個折現率計算股票的內在價值：

```
PV = Σ E(CFt) / (1 + E(Ri))^t
```

- 計算出的PV > 市價 → 股票被低估
- 計算出的PV < 市價 → 股票被高估

> 相關頁面：[[基本面分析/現金流量折現法DCF估值]] — CAPM折現率是DCF估值的關鍵輸入

### 2. WACC的股權成本組件

在加權平均資本成本（WACC）中，股權成本用CAPM計算：

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - T)
```

其中Re = CAPM計算的股權成本。

> 相關頁面：[[基本面分析/WACC加權平均資本成本]] — CAPM是WACC中股權成本的標準計算法

### 3. 績效評估基準

CAPM是評估基金經理和投資策略績效的基準模型。將實際報酬與CAPM預測的必要報酬比較，超出部分就是Jensen's Alpha。

### 4. 台股實務

- **無風險利率**：用台灣10年期公債殖利率，約1.2-1.5%
- **市場風險溢酬**：台股歷史市場溢酬約5-7%
- **Beta估算**：用台股加權指數作為市場代理，回歸過去2-5年月報酬
- **台積電Beta**：通常在0.8-1.2之間，因佔大盤權重過高，Beta估算有自我相關問題
- **金融股Beta**：通常<1，防禦性較強
- **AI概念股Beta**：通常>1.5，高系統性風險高報酬

## CAPM的局限與批評

### 1. 實證失敗

Fama和French（2004）在回顧中指出「CAPM在實證測試中的失敗意味著該模型的大多數應用都是無效的」：

- **低波動異象**：低Beta股票的報酬比CAPM預測的更高，SML比理論更平坦
- **規模與價值效應**：小型股和價值股的超額報酬無法用單一Beta解釋
- **Beta不穩定**：Beta並非常數，會隨市場週期變化

> 相關頁面：[[基本面分析/Fama-French多因子模型Fama-French-Multi-Factor-Model]] — CAPM的升級版，加入規模和價值因子

### 2. 理論缺陷

- **Roll批評**：真正的「市場組合」應包含所有資產（房地產、人力資本等），用股價指數代理會導致錯誤推論
- **循環論證**：總風險的價格是協方差風險的函數，存在循環邏輯
- **風險衡量**：用變異數衡量風險，忽略下行風險和偏態

### 3. 假設不切實際

- 無交易成本和稅？現實中台股交易稅0.3% + 手續費0.1425%
- 無限借貸？散戶融資受限、券商有額度上限
- 同質預期？看多看空永遠存在分歧

### 4. 行為財務學的挑戰

CAPM假設投資人完全理性，但行為財務學證明投資人系統性地做出非理性決策，這些偏差影響價格和報酬，CAPM的線性框架無法捕捉。

> 相關頁面：[[風險管理/行為財務學總論Behavioral-Finance-Overview]] — CAPM理性假設的系統性挑戰

## CAPM的延伸模型

為了解決CAPM的局限，學界發展了多個延伸模型：

- **Black CAPM（零Beta CAPM）**：用零Beta投資組合報酬取代無風險利率，不需假設無風險資產存在
- **跨期CAPM（ICAPM）**：Merton（1973）允許多期投資和投資組合再平衡
- **消費CAPM（CCAPM）**：用資產與總消費的共變異取代與市場的共變異
- **Fama-French三因子/五因子模型**：加入規模、價值、獲利能力、投資因子
- **套利定價理論（APT）**：Ross（1976）的多因子模型，不要求CAPM的嚴格假設

> 相關頁面：[[操作策略/Black-Litterman模型結合觀點與市場均衡Black-Litterman-Model]] — 在CAPM基礎上加入投資人觀點的資產配置模型

## 散戶實戰要點

1. **Beta不是萬能指標**：高Beta不代表一定高報酬，CAPM只是理論框架
2. **用CAPM計算折現率**：估計股票內在價值時，CAPM是計算股權成本的標準方法
3. **分散投資消除非系統性風險**：持有30-40檔不同產業股票，非系統性風險基本消除
4. **Beta會變**：用歷史Beta預測未來有風險，牛市和熊市的Beta可能不同
5. **市場溢酬是主觀估計**：不同人用不同市場溢酬會得到完全不同的必要報酬率
6. **CAPM是起點不是終點**：理解CAPM才能理解Fama-French等更進階的模型

## 相關頁面

- [[風險管理/Beta係數實戰判讀]] — Beta的實戰判讀與台股應用
- [[風險管理/詹森Alpha與特雷諾比率Jensen-Alpha-and-Treynor-Ratio]] — CAPM框架下的績效評估指標
- [[基本面分析/Fama-French多因子模型Fama-French-Multi-Factor-Model]] — CAPM的多因子升級版
- [[基本面分析/現金流量折現法DCF估值]] — CAPM折現率在DCF估值中的應用
- [[基本面分析/WACC加權平均資本成本]] — CAPM股權成本是WACC的核心組件
- [[操作策略/Black-Litterman模型結合觀點與市場均衡Black-Litterman-Model]] — CAPM均衡的資產配置延伸
- [[操作策略/Black-Scholes定價模型]] — 與CAPM同時代的定價理論基石
- [[風險管理/投資組合理論與分散投資的局限Portfolio-Theory-and-Diversification-Limits]] — CAPM建立在MPT之上
- [[風險管理/風險調整報酬指標夏普比率與索提諾比率]] — CAPM框架下的風險調整報酬
- [[風險管理/行為財務學總論Behavioral-Finance-Overview]] — CAPM理性假設的系統性挑戰

## 來源
- [Capital asset pricing model - Wikipedia](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)
- Sharpe, William F. (1964). "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk". Journal of Finance. 19 (3): 425–442.
- Lintner, John (1965). "The Valuation of Risk Assets and the Selection of Risky Investments in Stock Portfolios and Capital Budgets". Review of Economics and Statistics. 47 (1): 13–37.
- Black, Fischer (1972). "Capital Market Equilibrium with Restricted Borrowing". Journal of Business. 45 (3): 444–454.
- Fama, E. F.; French, K. R. (2004). "The Capital Asset Pricing Model: Theory and Evidence". Journal of Economic Perspectives. 18 (3): 25–46.

## 注意事項
（待補充）


## 相關主題
（待補充）
