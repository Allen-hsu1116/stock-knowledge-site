---
title: "波動率期限結構與曲面演化Volatility-Term-Structure-and-Surface-Evolution"
date: 2026-06-27
category: "操作策略"
---

# 波動率期限結構與曲面演化 Volatility Term Structure & Surface Evolution

> 波動率微笑只看單一到期日——加上期限結構就變成三維曲面，理解曲面的時間演化（Sticky Strike vs Sticky Delta）才能動態管理選擇權部位

## 核心概念

### 從微笑到曲面

波動率分析有三個層次：
1. **波動率微笑/偏斜**：同一到期日，不同履約價的 IV 分布（二維曲線）
2. **波動率期限結構**：同一履約價（通常 ATM），不同到期日的 IV 分布（二維曲線）
3. **波動率曲面**：履約價 × 到期日 × IV 的三維整合圖景

### 期限結構的驅動因素

#### 事件驅動型
- **財報前 IV 上升**：市場預期財報日波動加大，近月 IV 比遠月高
- **財報後 IV 崩跌**：資訊被吸收，IV 快速回落（Vol Crush）
- **央行會議前**：利率決策前後 IV 波動加劇
- **選舉、政策公告**：不確定性事件推升前端 IV

#### 結構型
- **正常型態（Contango）**：遠月 IV > 近月 IV，市場穩定時常見
- **反向型態（Backwardation）**：近月 IV > 遠月 IV，危機或事件前常見
- **駝峰型**：中間到期 IV 最高，特定事件落在中間月份時出現

#### Vol of Vol
- 近月選擇權的 IV 波動幅度遠大於遠月
- 短期事件對近月 IV 的衝擊更劇烈
- 遠月 IV 相對穩定，反映長期波動率預期

### 波動率曲面結構

三維曲面的三個維度：
- **X 軸**：到期時間（Days to Maturity, DTM）
- **Y 軸**：履約價（Strike）或 Delta/Moneyness
- **Z 軸**：隱含波動率（IV）

兩種座標系：
- **絕對曲面**：以履約價 K 為座標，適合單一標的分析
- **相對曲面**：以 Moneyness/Delta 為座標，適合跨標的比較

### 曲面演化：Sticky Strike vs Sticky Delta

曲面的靜態快照描述某一時點的 IV 分布，但標的價格移動時曲面如何變化？

#### Sticky Strike（黏性履約價）
- 標的價格變動時，特定履約價的 IV 不變
- 例如標的從 $100 漲到 $120，$120 履約價的 IV 維持不變（雖然從 OTM 變成 ATM）
- 適用於流動性高、履約價密集的市場

#### Sticky Delta / Sticky Moneyness（黏性 Delta）
- 標的價格變動時，特定 Moneyness/Delta 的 IV 不變
- 例如標的從 $100 漲到 $120，ATM 的 IV（現在是 $120 履約價）= 之前 $100 履約價的 ATM IV
- 適用於偏斜穩定、曲面隨標的移動的市場

#### 實戰判斷
- **股市通常介於兩者之間**：短期接近 Sticky Strike，長期接近 Sticky Delta
- **Sticky Delta 意味著偏斜跟著標的移動**：看跌保護的 IV 溢價不因價格上漲而消失
- **錯判演化模式會導致避險失誤**：用 Sticky Strike 假設但市場走 Sticky Delta，Delta 和 Vega 避險都會偏離

### Risk Reversal 與 Butterfly 的曲面分解

市場實務用三個報價建構曲面：
- **ATM**：ATM Forward 的 IV
- **Risk Reversal (RR)**：Call(x) IV − Put(x) IV，衡量偏斜方向
- **Butterfly (Fly)**：0.5 × (Call(x) + Put(x)) IV − ATM IV，衡量微笑程度

公式：
- Call(x) = ATM + 0.5 × RR(x) + Fly(x)
- Put(x) = ATM − 0.5 × RR(x) + Fly(x)

x 通常取 25 Delta。這三個參數就能重建整條微笑曲線。

### 風險中性隱含機率分布

Black-Scholes 假設標的報酬為常態分配（log-normal），但真實市場的隱含分配有胖尾和偏斜：
- **曲面非平坦** = 隱含分配偏離 log-normal
- **左端 IV 高** = 隱含分配左偏（市場給大跌更高機率）
- **兩端 IV 都高** = 隱含分配有胖尾（極端事件機率被放大）
- **從曲面反推機率分布**：Breeden-Litzenberger 公式用 Call 價格對履約價的二階偏導數推算風險中性機率密度

## 實戰應用

### 期限結構交易策略

1. **Calendar Spread（時間價差）**：賣近月買遠月，賺近月 IV 衰減
   - 財報前近月 IV 飆高時特別有效
   - 財報後近月 IV 崩跌，遠月相對穩定

2. **反向期限結構交易**：近月 IV 遠高於遠月時
   - 賣近月買遠月，賭期限結構正常化
   - 危機後近月 IV 回落，價差收斂獲利

3. **Diagonal Spread（對角價差）**：不同履約價 + 不同到期日
   - 利用曲面三維結構的不對稱
   - 看多偏斜 + 看空期限結構的組合

### 曲面套利

1. **曲面凸點/凹陷**：某履約價-到期日組合的 IV 明顯偏離周圍
   - 賣高 IV 合約、買低 IV 合約
   - 用 Delta/Gamma 中性消除方向風險

2. **跨期限偏斜套利**：某到期偏斜異常陡峭而鄰近到期正常
   - 做空異常端偏斜、做多正常端

3. **離差交易（Dispersion Trading）**：
   - 指數選擇權 IV 偏斜通常比成分股更陡
   - 賣指數選擇權（收高溢價）+ 買成分股選擇權（付低溢價）
   - 賭指數成分股相關性下降

### 曲面判讀信號

- **曲面整體上抬**：市場恐慌上升，所有 IV 同步走高
- **前端升幅遠大於長端**：短期不確定性劇增（事件驅動）
- **偏斜陡峭化**：市場防跌意識增強（左端 IV 上升更快）
- **偏斜平坦化**：市場對下跌風險的擔憂降低
- **期限結構反轉**：近月 IV > 遠月 IV，危機訊號或事件前兆
- **曲面扭曲**：特定區域 IV 異常，可能反映局部供需失衡或套利機會

### 模型校準

曲面建模的主要方法：
- **局部波動率模型（Local Volatility）**：Dupire 公式從曲面反推標的波動率函數
- **隨機波動率模型**：SABR、Heston 模型用少量參數擬合整個曲面
- **SVI（Stochastic Volatility Inspired）**：Gatheral 提出的參數化方法，高效擬合微笑曲線
- **Vanna-Volga 方法**：用 ATM + RR + Fly 三點建構微笑曲線的近似方法

## 注意事項

- **曲面是快照不是預測**：曲面反映當前市場定價，不預測未來波動率走向
- **Sticky 假設不完美**：真實市場的曲面演化介於 Sticky Strike 和 Sticky Delta 之間，過度依賴任一假設都會產生避險誤差
- **流動性影響曲面形狀**：OTM 和遠月選擇權流動性差，IV 報價可能不反映真實市場預期
- **台股曲面特性**：造市制度使 IV 黏度高，曲面形狀不如美股自由市場豐富
- **模型校準風險**：擬合曲面用複雜模型可能過度擬合，參數不穩定
- **Breeden-Litzenberger 限制**：反推機率分布需要密集的履約價數據，實務上數據有限

## 相關主題

- [[技術分析/波動率微笑曲線與偏態Volatility-Smile-and-Skew]]
- [[技術分析/隱含波動率IV與歷史波動率HV實戰判讀]]
- [[操作策略/價內程度Moneyness實戰判讀]]
- [[操作策略/二階與三階Greeks進階Vanna-Vomma-Charm]]
- [[操作策略/Black-Scholes定價模型]]
- [[操作策略/波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[操作策略/時間價差Calendar-Spread]]
- [[操作策略/對角價差Diagonal-Spread]]
- [[風險管理/VIX恐慌指數實戰判讀]]

## 來源

- [Volatility Smile & Surface - Wikipedia](../raw/2026-06-27/Volatility-Smile-Surface-Wikipedia.md)