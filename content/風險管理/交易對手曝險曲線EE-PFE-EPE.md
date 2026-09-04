---
title: 交易對手曝險曲線EE、PFE與EPE
aliases: [Expected Exposure, Potential Future Exposure, Expected Positive Exposure, Effective EPE, 交易對手曝險曲線]
category: 風險管理
date: 2026-09-04
---

# 交易對手曝險曲線EE、PFE與EPE

> 衍生品的信用曝險不是固定本金，而是一條會隨市場價格、時間、淨額結算與擔保品變動的未來正曝險曲線；EE看平均、PFE看高分位、EPE則把整段時間壓成資本計算尺度。

## 核心概念

### 為什麼不能拿名目本金當曝險

普通貸款撥款後本金大致已知，衍生品的[[風險管理/交易對手風險Counterparty-Risk|交易對手風險]]則隨市價雙向變動。合約名目本金可能很大，但真正會因對手違約而損失的是當時的正重置價值：

$$Exposure(t)=\max\bigl(V_{net}(t)-C(t),0\bigr)$$

其中 $V_{net}(t)$ 是同一可執行淨額結算組合的淨市值，$C(t)$ 是可認列擔保品。若市值為負，違約時通常是自己欠對方，不構成對該對手的正信用曝險。

### Current Exposure與曝險分配

**Current Exposure（CE）**又稱Replacement Cost，是對手現在立刻違約、假設零回收時會失去的正市值。

未來市價尚未發生，因此每個未來日期不是一個曝險點，而是一個機率分配。利率、匯率、股價、商品價格與波動率路徑都可能改變合約價值。

### EE：每個未來日期的平均曝險

在未來日期 $t$，Expected Exposure為正曝險分配的平均：

$$EE(t)=E\left[\max\bigl(V_{net}(t)-C(t),0\bigr)\right]$$

把多個日期的EE連起來就是曝險曲線。交換合約可能先升後降；選擇權因單向正值與波動率效果，曲線形狀又不同。只看今天CE，會漏掉明天合約變成價內後的曝險。

### PFE：未來曝險的高分位數

Potential Future Exposure通常取某日期曝險分配的95%或99%分位數：

$$PFE_q(t)=Quantile_q\bigl(Exposure(t)\bigr)$$

EE回答「平均會曝險多少」，PFE回答「在給定信賴水準下可能高到多少」。PFE適合設定交易對手限額與峰值監控，但不是最大可能損失；超過99%分位後仍有尾巴，市場從來不會因報表欄位填滿就停止作妖。

### EPE與Effective EPE

Expected Positive Exposure（EPE）是EE在第一年內的時間加權平均；若全部合約不到一年，則平均到最長到期日：

$$EPE=\frac{1}{T}\sum_k EE(t_k)\Delta t_k$$

Basel另定義不下降的Effective EE：

$$Effective\ EE(t_k)=\max\bigl(Effective\ EE(t_{k-1}),EE(t_k)\bigr)$$

再將第一年內Effective EE時間加權平均，得到Effective EPE。它不允許曝險曲線後段自然下降立即抵銷前段峰值，因此比普通EPE保守。

內部模型法的簡化監理曝險額為：

$$EAD=\alpha\times Effective\ EPE$$

Basel監理值 $\alpha=1.4$；此乘數用來涵蓋跨對手相關性、模型簡化與未完全捕捉的風險。

### 淨額結算與擔保品改變的是整條曲線

- **淨額結算**：同一法律可執行的netting set內，正負市值可抵銷。
- **變動保證金**：降低目前市值曝險，但存在追繳頻率與爭議風險。
- **初始保證金**：用來吸收平倉期間潛在未來價格變化。
- **保證金風險期間MPOR**：對手違約後到部位平倉或重新避險完成的時間，期間越長，殘餘PFE通常越高。

## 實戰應用

### 一年期簡化驗算

假設目前正曝險為2，未來四個等距季度的EE依序為5、4、3、1：

- EPE =（5 + 4 + 3 + 1）÷ 4 = 3.25
- Effective EE依序為5、5、5、5
- Effective EPE = 5
- 以 $\alpha=1.4$ 計算，EAD = 7

期末EE只剩1，不代表中間沒有衝到5。用期末點代替整條曲線，就是把電影最後一幕截圖當完整劇情。

### 實務監控SOP

1. 先確認交易是否可依法淨額結算，不能只因系統畫面放在同一帳戶就當作可抵銷。
2. 依交易、netting set、交易對手與集團四層彙總正曝險。
3. 模擬所有重要市場因子的聯合路徑，產生各日期曝險分配。
4. 同時查看CE、EE曲線、95%與99% PFE、EPE及Effective EPE。
5. 納入擔保品門檻、最低轉移金額、追繳頻率、MPOR與保證金爭議。
6. 用壓力波動率與壓力相關性重跑，不拿平靜期參數替危機背書。
7. 對一年後仍上升的長天期曝險另設限額，監理平均期限不是風險消失期限。

### 股票投資人的用途

- **銀行與券商**：衍生品正曝險、netting benefit、擔保品與PFE決定交易對手資本需求。
- **壽險與金控**：長天期利率、匯率避險可能在壓力時同時推高曝險與保證金流動性需求。
- **一般企業**：遠期外匯、利率交換與商品避險若集中單一銀行，正曝險是公司對金融機構的隱性無擔保債權。
- **平台與發行商產品**：ETN、結構債或場外商品除了標的方向，還要問正市值最終向誰收錢。

## 注意事項

- **EE不是尾部**：平均曝險不能取代PFE與壓力測試。
- **PFE不是最大損失**：信賴水準外仍可能更慘，也未直接乘入PD與LGD。
- **EPE壓縮時間資訊**：相同EPE可能來自短期尖峰或長期平緩曝險，管理方式不同。
- **實際與風險中立分配不同**：資本、限額與定價使用的機率測度可能不同，不能混著抄數字。
- **淨額結算依賴法律可執行性**：跨法人、跨司法管轄或破產程序可能讓帳面抵銷失效。
- **擔保品也會失靈**：價格跳空、錯誤估值、折扣不足與追繳爭議都會留下殘餘曝險。
- **肥尾不可省略**：Basel要求曝險分配適當納入非常態與厚尾。
- **信用與市場不能分家**：若曝險上升時對手信用同步惡化，普通EE模型會低估聯合損失。

## 相關主題

- [[風險管理/信用估值調整CVA-Credit-Valuation-Adjustment|信用估值調整CVA]]
- [[風險管理/錯向風險Wrong-Way-Risk|錯向風險]]
- [[風險管理/交易對手風險Counterparty-Risk|交易對手風險]]
- [[風險管理/信用風險Credit-Risk|信用風險]]
- [[基本面分析/違約損失率LGD與回收率Recovery-Rate|違約損失率LGD與回收率]]
- [[風險管理/蒙地卡羅模擬交易驗證Monte-Carlo-Simulation|蒙地卡羅模擬]]
- [[風險管理/情境分析與壓力測試框架Scenario-Analysis-Framework|情境分析與壓力測試框架]]
- [[風險管理/相關性風險Correlation-Risk|相關性風險]]

## 來源

- [Basel Framework CRE50：Counterparty credit risk definitions and terminology](https://www.bis.org/committees/bcbs/basel-framework/standard/cre/50/inforce/2019-12-15/published/2024-07-05)
- [Basel Framework CRE53：Internal models method for counterparty credit risk](https://www.bis.org/committees/bcbs/basel-framework/standard/cre/53/inforce/2023-01-01/published/2020-06-05)
- [本次來源學習紀錄](../../raw/2026-09-04/Basel-交易對手曝險與錯向風險學習紀錄.md)
