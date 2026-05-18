# Aroon 阿隆指標

> 用「距離最近新高/新低的天數」衡量趨勢強度與方向，0~100 區間，100 代表剛創新高/低，0 代表很久沒創新高/低。交叉是轉折訊號，盤整是最大剋星。

## 核心概念

Aroon 指標由 Tushar Chande 於 1995 年發明，「Aroon」是梵文「黎明前的曙光」，暗示其趨勢發現能力。核心邏輯不是看「漲多少跌多少」，而是看「距離上次創新高/新低已經過了多久」。指標由三個部分構成：

**1. Aroon Up（阿隆上升線）**
- 公式：`Aroon Up = ((N - 距創N期最高價的天數) / N) × 100`
- 衡量多近創過新高。值越接近 100 表示越近期創過新高

**2. Aroon Down（阿隆下降線）**
- 公式：`Aroon Down = ((N - 距創N期最低價的天數) / N) × 100`
- 衡量多近創過新低。值越接近 100 表示越近期創過新低

**3. Aroon Oscillator（阿隆震盪指標）**
- 公式：`Aroon Oscillator = Aroon Up - Aroon Down`
- 正值代表偏多，負值代表偏空

**常用參數**：25 天（原始設計）或 14 天（TA-Lib 預設）

### 數值判讀

| 數值區間 | 意義 |
|----------|------|
| Aroon Up = 100 | 剛創25日新高，多方最強 |
| Aroon Up 70~100 | 上升趨勢明確/強勁 |
| Aroon Up 跌破 50 | 上升趨勢失去動力 |
| Aroon Down = 100 | 剛創25日新低，空方最強 |
| Aroon Down 70~100 | 下降趨勢強勁 |
| Aroon Down 跌破 50 | 下降趨勢失去動力 |
| 兩線都低（<30） | 盤整無趨勢 |

## 實戰應用

### 1. 交叉訊號
- **黃金交叉**：Aroon Up 向上穿越 Aroon Down → 行情轉強，潛在買點
- **死亡交叉**：Aroon Down 向上穿越 Aroon Up → 行情轉弱，潛在賣點

### 2. 趨勢強度確認
- Aroon Up > 70 且 Aroon Down < 30：強勢上漲趨勢
- Aroon Down > 70 且 Aroon Up < 30：強勢下跌趨勢
- 兩線在 50 附近交叉：趨勢不明

### 3. Aroon Oscillator 搭配
- Oscillator > 0：偏多
- Oscillator < 0：偏空
- Oscillator 在 0 附近：典型無趨勢特徵，盤整階段

### 4. TEJ 回測策略條件

**進場**：Aroon-Up > 80 且 Aroon-Down < 45 → 買進
**出場**：Aroon-Down > 55 且 Aroon-Up < 45 且差距 > 15 → 賣出
**加碼**：Aroon-Up > 55 且 Aroon-Down < 45 且差距 > 15 且投入本金 ≤ 20%本金

### 5. FinLab 回測結果
- 條件：aroonup > aroondown，週期 25 日
- 結果：年化報酬約 6%，效果有限
- 與創新高延續度動能策略相比遜色
- **結論**：Aroon 單獨使用效果不佳，建議搭配其他指標（如均線、MACD、ADX）作為趨勢確認輔助

## 注意事項

1. **盤整是最大剋星**：兩線都低時訊號無效，交叉頻繁產生假訊號
2. **滯後性**：計算基於「距離創高低的天數」，本身有延遲，轉折確認較慢
3. **單獨使用效果有限**：FinLab 回測年化僅 6%，需搭配 ADX、成交量等指標過濾盤整
4. **不提供超買超賣訊號**：Aroon 衡量趨勢強度，不是震盪指標
5. **參數敏感度低**：N=25 是常用值，調整效果不明顯
6. **與 ADX 互補**：ADX 判斷趨勢有無、Aroon 判斷趨勢方向，搭配使用效果更好

## 相關主題

- [[技術分析/ADX趨勢強度過濾盤整]]
- [[技術分析/DMI動向指標與DI方向判斷]]
- [[技術分析/MACD指標實戰判讀]]
- [[技術分析/背離Divergence進階實戰]]
- [[技術分析/多時間框架分析]]
- [[操作策略/量價關係實戰操作SOP]]
- [[操作策略/順勢交易]]

## 來源

- [QuantPass 阿隆 Aroon 指標](https://quantpass.org/aroon/)
- [FinLab 技術指標教室 AROON](https://www.finlab.tw/aroon_indicator/)
- [TradingView 阿隆指標](https://tw.tradingview.com/support/solutions/43000501801/)
- [MBA智库百科 阿隆指標](https://wiki.mbalib.com/zh-tw/%E9%98%BF%E9%9A%86%E6%8C%87%E6%A0%87)
- [TEJWIN Aroon Up Down Strategy](https://www.tejwin.com/en/insight/%E3%80%90quant%E3%80%91aroon-up-down-strategy/)