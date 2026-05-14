# Chandelier Exit 吊燈出場指標

> 用 ATR 動態設定追蹤停損的出場指標，像吊燈從最高點懸掛下來，波動大距離遠、波動小距離近，自動適應不同股票的波動性

## 核心概念

Chandelier Exit 由 Charles Le Beau 開發、Alexander Elder 推廣，是一種基於 ATR 的追蹤停損指標。

**計算公式**：
- 做多：Chandelier Exit = 最高價 - ATR(n) × 乘數
- 做空：Chandelier Exit = 最低價 + ATR(n) × 乘數

**常用參數**：ATR 期間 22、乘數 3（三倍 ATR）

**核心邏輯**：結合「趨勢極值」（最高/最低價）和「波動度量」（ATR），停損距離自動隨波動調整。波動大的股票停損遠一點不怕被洗，波動小的股票停損近一點避免回吐太多。

**與固定%追蹤停損的差異**：固定%追蹤停損不考慮個股波動性，高波動股容易被洗、低波動股回吐太多。Chandelier Exit 用 ATR 解決這個問題。

## 實戰應用

### 出場判斷
- 做多：收盤價跌破 Chandelier Exit → 多頭出場
- 做空：收盤價漲破 Chandelier Exit → 空頭出場
- Chandelier Exit 只會往有利方向移動（做多時只上移、做空時只下移），確保鎖住利潤

### 輔助進場
- 價格突破長期下降的 Chandelier Exit → 趨勢反轉做多
- 價格跌破長期上升的 Chandelier Exit → 趨勢反轉做空

### 參數調整
- **ATR 期間**：22（月線）是預設，短線用 10-14，長線用 50
- **乘數**：3 是預設，加大→停損寬鬆（少被洗但回吐多），縮小→停損緊（鎖利快但易被洗）
- **調整原則**：先看標的最近 3 個月 ATR 均值，確保乘數×ATR 大於常見回檔幅度

### 與其他追蹤停損比較

| 方法 | 基準點 | 距離計算 | 適合場景 |
|------|--------|----------|----------|
| 固定%追蹤停損 | 最高價 | 固定百分比 | 簡單直覺，波動性相近的標的 |
| [[SAR拋物線指標Parabolic-SAR]] | 極值點 | 加速因子 | 趨勢明確的市場 |
| Chandelier Exit | 最高價 | ATR×乘數 | 波動差異大的多標的操作 |

## 注意事項

- **極端行情**：跳空漲停時 ATR 暴增，停損點突然變遠，可能回吐大量利潤
- **盤整市**：雖然比 SAR 好，但盤整中仍會被來回洗
- **只提供出場**：不提供進場訊號，需搭配其他指標
- **參數無一體適用**：不同標的需要不同參數，要先觀察再設定
- **與 [[移動停利停損Trailing-Stop]] 的關係**：Chandelier Exit 是 Trailing Stop 的 ATR 進階版，用波動度取代固定百分比

## 相關主題

- [[移動停利停損Trailing-Stop]]
- [[ATR平均真實波幅-Average-True-Range]]
- [[SAR拋物線指標Parabolic-SAR]]
- [[海龜交易法則]]
- [[進場SOP交易紀律完整框架]]
- [[Chande-Kroll-Stop錢德克羅停損指標]]

## 來源

- [Chandelier Exit 吊燈式追蹤出場](../raw/2026-05-07/Chandelier-Exit吊燈式追蹤出場.md)
- [OANDA: Chandelier Stop](https://www.oanda.com/bvi-ft/lab-education/technical_analysis/chandelier-stop/)
- [出場策略(2)：Chandelier Exit - Trading with Technical Analysis](../raw/2026-05-11/Chandelier-Exit吊燈出場法.md)
- [運用ATR決定獲利結算目標 - OANDA Lab](../raw/2026-05-11/ATR停利停損目標策略-OANDA.md)
- [吊燈式追蹤停損 Chandelier Stop OANDA（更新版）](../raw/2026-05-14/吊燈式追蹤停損Chandelier-Stop-OANDA.md)