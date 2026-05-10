# 選擇權Convexity凸性與非對稱收益Option-Convexity

> Long Option = Long Convexity = Long Gamma——賺的時候越賺越多、賠的時候越賠越少，這個非對稱收益就是選擇權最核心的特性，代價是你要付權利金和承受 Theta Decay

## 核心概念

Convexity（凸性）是選擇權最獨特也最重要的特性。數學上，Convexity 描述的是一條「斜率不斷上升」的曲線——曲線上任兩點連線的直線都高於曲線上的值。

對照選擇權：
- **Long Option = Long Convexity = Long Gamma**：收益曲線向上彎，賺越多賺越快
- **Short Option = Short Convexity = Concavity**：收益曲線向下彎，賠越多賠越快

### Delta 與 Convexity 的關係

Call 的 Delta 介於 0~1 之間，隨標的物價格上升，Delta 也越來越高。這正是「斜率不斷上升」的曲線：

- 深價外：Delta ≈ 0，對標的物 exposure 極小
- 價平：Delta ≈ 0.5，一半的敏感度
- 深價內：Delta ≈ 1，跟期貨同步

這條曲線意味著：**賺的時候越賺越多，賠的時候越賠越少**。

### 具體例子

假設你想用 Call 組合出 ETH 漲幅的 exposure（Delta = 1），可以買 2 個 ATM Call（每個 Delta 0.5）：

- **ETH 上漲 500**：你會賺超過 500，因為隨著 ETH 漲越多，Delta 從 1 變成 2，每漲一塊錢你的倉位漲兩塊
- **ETH 下跌 500**：你會損失少於 500，因為隨著 ETH 跌越多，Delta 從 1 變小，每跌一塊錢你的損失越來越少
- **最終**：ETH 跌到一定程度後，Call 幾乎價值歸零，不再繼續虧損

這就是 Convexity 的魔法——有限下檔、無限上檔的非對稱收益。

## 實戰應用

### Convexity 的代價

天下沒有白吃的午餐，Long Convexity 的代價：

1. **權利金**：買入選擇權時一次付清，這是獲得非對稱收益的門票
2. **Theta Decay**：隨時間流逝，選擇權價值不斷遞減，這是維持 Convexity 的持續成本

反過來，Short Convexity（賣方）的收益：

1. **收取權利金**：一開始就收到錢
2. **賺取 Theta**：時間流逝就是賣方的利潤
3. **但承擔無限下檔風險**：賺有限，賠無限

### Convexity 在投資組合中的運用

1. **凸性套利（Convexity Arbitrage）**：當市場定價的 Convexity 成本偏離合理值時，買入便宜的 Convexity、賣出昂貴的 Convexity

2. **對沖無常損失（IL Hedge）**：
   - Uniswap LP 是 Short Convexity（Short Gamma）
   - 選擇權是 Long Convexity（Long Gamma）
   - 用選擇權可以對沖 LP 的 Gamma 風險
   - 對沖後收益來源變簡單：手續費收入 vs 權利金支出

3. **槓桿放大**：
   - 買 2 個 ATM Call 可以獲得大於 1 倍的 Delta exposure
   - 在小區間內接近期貨效果，但大漲時槓桿自動加大
   - 大跌時損失有底線（權利金歸零）

### Gamma Scalping 與 Convexity

Long Gamma 的 Scalping 策略本質上就是在收割 Convexity：

- 買入 ATM Straddle（Long Gamma + Long Vega）
- 當價格上漲，Delta 變正，賣出期貨 Delta Neutral
- 當價格下跌，Delta 變負，買入期貨 Delta Neutral
- 每次調整都在「鎖定」Convexity 帶來的利潤
- 代價是每天支付 Theta（時間衰減）

**盈虧平衡點**：Gamma Scalping 利潤 = Theta 成本時，策略剛好打平

### 與其他金融商品的對比

| 商品 | Convexity | Gamma | 收益特性 |
|------|-----------|-------|---------|
| 現貨/期貨 | 無（線性） | 0 | 對稱收益 |
| Long Call/Put | 正（凸性） | > 0 | 非對稱：有限下檔、無限上檔 |
| Short Call/Put | 負（凹性） | < 0 | 非對稱：有限上檔、無限下檔 |
| Uniswap LP | 負（凹性） | < 0 | 無常損失 = Short Gamma |
| 鐵兀鷹賣方 | 負 | < 0 | 有限收益、有限風險 |

## 注意事項

1. **Convexity 不是免費的**：Long Convexity 要付權利金和承受 Theta Decay，這不是套利而是「付費買保險+槓桿」
2. **Short Convexity 風險無限**：賣方的收益曲線向下彎，意味著極端行情時虧損沒有上限
3. **Gamma 越大 Convexity 越強**：ATM 選擇權 Gamma 最大，Convexity 也最強，但 Theta 也最大
4. **到期前 Convexity 在變**：越接近到期，Gamma 越集中於 ATM 附近，Convexity 的效應越極端
5. **不要只看 Convexity 不看成本**：非對稱收益聽起來很美好，但權利金可能已經反映了這個優勢
6. **DeFi LP 的 Short Gamma 本質**：Uniswap LP 的無常損失本質就是 Short Convexity，需要手續費收入來彌補

## 相關主題

- [[選擇權Greeks希臘字母]]
- [[選擇權Greeks進階組合判讀與風險管理Option-Greeks-Advanced]]
- [[Black-Scholes定價模型]]
- [[選擇權四大基本策略]]
- [[選擇權組合策略]]
- [[波動率套利與Delta-Neutral策略Volatility-Arbitrage-and-Delta-Neutral]]
- [[波動率套利與Delta Neutral策略]]
- [[選擇權賣方收租策略Option-Seller-Rent-Collection]]

## 來源

- [Anton Cheng-選擇權的定價與避險參數](../raw/2026-05-10/Greeks進階-選擇權定價與避險參數.md)
- [OP凱文-Greeks風險儀表板](../raw/2026-05-10/Greeks基礎-Delta-Gamma-Vega-Theta開車比喻.md)