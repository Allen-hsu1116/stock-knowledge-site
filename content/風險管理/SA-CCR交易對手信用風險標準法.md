---
title: SA-CCR交易對手信用風險標準法
aliases: [SA-CCR, Standardised Approach for Counterparty Credit Risk, 交易對手信用風險標準法, 衍生品EAD]
category: 風險管理
date: 2026-09-05
---

# SA-CCR交易對手信用風險標準法

> SA-CCR不是拿衍生品名目本金直接當風險，而是按法律可執行的淨額結算組合，把當前重置成本與未來潛在曝險合併成EAD；公式很制式，但合約、擔保與淨額分錯組，後面算再漂亮也只是精裝版垃圾。

## 核心概念

### SA-CCR在算什麼

Basel的Standardised Approach for Counterparty Credit Risk適用於場外衍生品、交易所交易衍生品與長結算交易。沒有獲准使用內部模型法的銀行，需按每個netting set分別計算違約曝險額（Exposure at Default, EAD）：

$$EAD=\alpha\times(RC+PFE)$$

其中：

- $\alpha=1.4$：監理乘數，用來涵蓋模型簡化、相關性與未完全捕捉的風險。
- $RC$：Replacement Cost，交易對手現在違約時的當前重置成本。
- $PFE$：Potential Future Exposure，從現在到平倉或替代交易完成前，曝險可能增加的保守估計。

EAD是資本計提輸入，不是預測「一定會損失多少」，也不是[[風險管理/交易對手曝險曲線EE-PFE-EPE|PFE分位數曲線]]的同義詞。

### 法律淨額結算決定計算邊界

SA-CCR以netting set為單位。只有在違約與破產情境下仍可依法執行的雙邊淨額結算，正負市值才可放在同一組抵銷；否則每筆交易原則上各自成組。

這件事比公式重要，因為把不能抵銷的交易塞進同一組，會同時壓低RC與PFE。系統帳戶相同、交易員相同、甚至對手集團相同，都不自動等於法律上可淨額。

### 未保證金組合的RC

未受合格變動保證金協議涵蓋時，簡化重置成本為：

$$RC=\max(V-C,0)$$

其中 $V$ 是組合淨市值，$C$ 是經監理折扣後可認列的淨擔保品。若銀行欠對手錢，RC不會變成負數；超額擔保或負市值可透過PFE乘數提供部分保護，但不能把當前曝險算成負資產。

### 已保證金組合的RC

受雙向變動保證金協議涵蓋時，RC還要反映追繳門檻與最低移轉金額：

$$RC=\max(V-C,TH+MTA-NICA,0)$$

其中：

- $TH$：Threshold，達到此曝險才觸發保證金追繳。
- $MTA$：Minimum Transfer Amount，小於此金額暫不移轉。
- $NICA$：Net Independent Collateral Amount，可在對手違約時扣押的淨獨立擔保品。

$TH+MTA-NICA$代表在保證金機制下，仍可能不觸發追繳的最大缺口。單向協議若只有銀行付出VM、卻收不到VM，SA-CCR仍把它當未保證金組合；合約封面寫著margin，不代表風險就自動被施法消失。

### PFE的組成

SA-CCR將PFE寫成：

$$PFE=multiplier\times AddOn^{aggregate}$$

- **Aggregate Add-on**：先把交易轉成有效名目本金，再依利率、外匯、信用、股票與商品資產類別及hedging set聚合。
- **Multiplier**：未足額擔保時通常為1；超額擔保或組合淨市值為負時可下降，但監理下限為5%，因此PFE不會因今天價外或多收擔保品就直接歸零。
- **期限調整**：未保證金交易以剩餘期限與監理風險期間調整；已保證金交易改以Margin Period of Risk（MPOR）為核心。

RC在netting set層級計算，PFE先在各資產類別內聚合，再跨資產類別加總。這種跨類別較保守的處理，是防止拿「平常看起來負相關」替危機抵銷背書。

### 保證金不等於零風險

已每日交換VM的交易仍有PFE，因為對手違約後到最後一次保證金交換、部位終止、賣出擔保品與完成替代交易之間存在MPOR。這段期間價格照樣會跳、擔保品照樣會跌，法律爭議也不會因交易員下班就停止計時。

## 實戰應用

### 簡化EAD驗算

假設某已保證金netting set：

- 組合市值 $V=12$
- 可認列擔保品 $C=7$
- $TH=1$
- $MTA=0.5$
- $NICA=2$
- 聚合Add-on為8

則：

$$RC=\max(12-7,1+0.5-2,0)=5$$

目前仍未足額擔保，所以multiplier取1，PFE為8：

$$EAD=1.4\times(5+8)=18.2$$

這裡名目本金甚至沒有直接出現在最後一行；它先透過有效名目本金、監理因子、Delta、期限與hedging set影響Add-on。

### 對手曝險檢查SOP

1. 逐一確認交易產品是否納入SA-CCR。
2. 依主協議、終止淨額條款與司法管轄切分netting set。
3. 區分雙向VM、單向VM與完全未保證金交易。
4. 對市值與擔保品做幣別、折扣及可執行性調整後計算RC。
5. 將交易依資產類別、hedging set、方向、Delta與期限轉成有效名目本金。
6. 聚合Add-on並套用超額擔保乘數，得到PFE。
7. 乘以1.4得到EAD，再進入PD、LGD、風險權重與資本計算。
8. 另做[[風險管理/錯向風險Wrong-Way-Risk|錯向風險]]與流動性壓力測試，別把標準法當上帝視角。

### 股票投資人的用途

- **銀行與金控**：衍生品名目本金相近，不代表SA-CCR EAD與RWA相近；netting、VM、IM、期限與產品組合會大幅改變資本耗用。
- **券商與造市商**：客戶清算、選擇權及場外避險會同時占用交易對手限額、擔保品與資本。
- **壽險公司**：長天期利率與匯率避險可能有較長期限、集中對手與大量擔保需求，需把信用資本和流動性一起看。
- **財報閱讀**：關注衍生品正市值、netting benefit、可認列擔保品、EAD與RWA的變化，不能只被巨大名目本金嚇到或哄到。

## 注意事項

- **EAD不是預期損失**：預期損失還要結合PD與LGD；CVA則採風險中立信用與折現曝險邏輯。
- **PFE不是統計分位數**：SA-CCR的PFE是監理Add-on結果，與模擬出的95%或99% PFE用途不同。
- **法律意見不能省**：淨額協議在正常時可操作，不代表破產時一定可執行。
- **擔保品要折扣**：價格波動、幣別錯配、集中度與流動性會削弱擔保效果。
- **單向VM可能仍算未保證金**：判斷標準是對手是否有義務向銀行提供VM。
- **標準法不等於低風險**：集中度、跳空、模型風險及[[風險管理/錯向風險Wrong-Way-Risk|WWR]]仍需額外管理。
- **比較銀行要看實施口徑**：各地導入日期、過渡規定與揭露粒度可能不同。

## 相關主題

- [[風險管理/場外衍生品初始保證金與變動保證金|場外衍生品初始保證金與變動保證金]]
- [[風險管理/中央交易對手CCP與違約瀑布|中央交易對手CCP與違約瀑布]]
- [[風險管理/保證金順週期性與流動性螺旋|保證金順週期性與流動性螺旋]]
- [[風險管理/交易對手曝險曲線EE-PFE-EPE|交易對手曝險曲線EE、PFE與EPE]]
- [[風險管理/交易對手風險Counterparty-Risk|交易對手風險]]
- [[風險管理/信用估值調整CVA-Credit-Valuation-Adjustment|信用估值調整CVA]]
- [[風險管理/錯向風險Wrong-Way-Risk|錯向風險]]
- [[風險管理/信用風險Credit-Risk|信用風險]]

## 來源

- [Basel Framework CRE52原文摘錄](../../raw/2026-09-05/Basel-CRE52-SA-CCR.md)
- [Basel Framework CRE52：Standardised approach to counterparty credit risk](https://www.bis.org/committees/bcbs/basel-framework/standard/cre/52/inforce/2023-01-01/published/2020-06-05)
