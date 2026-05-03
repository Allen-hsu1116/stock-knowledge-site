# Aroon 阿隆指標實戰判讀

> 用「多久以前創新高/低」來判斷趨勢強弱——Aroon-Up 100 代表剛創新高、Aroon-Down 100 代表剛創新低，交叉是轉折訊號，盤整是最大剋星

## 核心概念

Aroon 指標由 Tushar Chande 於 1995 年發明，核心邏輯不是看「漲多少跌多少」，而是看「距離上次創新高/新低已經過了多久」。如果剛創新高，Aroon-Up 接近 100，代表多方力道強；如果已經很久沒創新高，Aroon-Up 接近 0，代表趨勢正在失去動力。

### 計算公式

- **Aroon-Up** = ((N - 創N日最高價到今天的天數) / N) × 100
- **Aroon-Down** = ((N - 創N日最低價到今天的天數) / N) × 100
- **Aroon-Osc** = Aroon-Up - Aroon-Down

預設 N = 25 日。

### 數值意義

| 數值區間 | 意義 |
|----------|------|
| Aroon-Up = 100 | 剛創25日新高，多方最強 |
| Aroon-Up 70~100 | 上升趨勢強勁 |
| Aroon-Up 跌破 50 | 上升趨勢失去動力 |
| Aroon-Down = 100 | 剛創25日新低，空方最強 |
| Aroon-Down 70~100 | 下降趨勢強勁 |
| Aroon-Down 跌破 50 | 下降趨勢失去動力 |
| 兩線都低於 30 | 盤整無趨勢 |

## 實戰應用

### 交叉訊號

- **黃金交叉**：Aroon-Up 往上穿越 Aroon-Down → 行情轉強，偏多訊號
- **死亡交叉**：Aroon-Down 往上穿越 Aroon-Up → 行情轉弱，偏空訊號

### Aroon-Osc 判讀

- **正數**：創高日較近、創低日較遠 → 多方主導
- **負數**：創低日較近、創高日較遠 → 空方主導
- **接近 0**：無趨勢特徵，盤整階段

### TEJ 回測策略條件

**進場**：Aroon-Up > 80 且 Aroon-Down < 45 → 買進
**出場**：Aroon-Down > 55 且 Aroon-Up < 45 且差距 > 15 → 賣出
**加碼**：Aroon-Up > 55 且 Aroon-Down < 45 且差距 > 15 且投入本金 ≤ 20%本金

### FinLab 回測結果

aroonup > aroondown 條件回測年化報酬約 6%，與其他動能策略相比效果遜色。市場一般參數使用下效果有限，需搭配其他指標優化。

## 注意事項

1. **盤整是最大剋星**：兩線都低時訊號無效，交叉頻繁產生假訊號
2. **落後性**：基於「多久以前創新高」計算，屬於落後指標，轉折判斷會慢半拍
3. **單獨使用效果有限**：回測顯示年化報酬偏低，需搭配 ADX、成交量等指標過濾盤整
4. **參數敏感度低**：N=25 是常用值，調整效果不明顯
5. **與 ADX 互補**：ADX 判斷趨勢有無、Aroon 判斷趨勢方向，搭配使用效果更好

## 相關主題

- [[ADX趨勢強度過濾盤整]]
- [[DMI動向指標與DI方向判斷]]
- [[MACD指標實戰判讀]]
- [[背離Divergence進階實戰]]
- [[多時間框架分析]]
- [[MTM動量指標Momentum-Index]]
- [[ROC變動率指標Rate-of-Change]]

## 來源

- [阿隆 Aroon 指標－快速抓出轉折與趨勢](../raw/2026-05-04/Aroon阿隆指標實戰判讀.md)
- [Aroon Up Down Strategy - TEJ](https://www.tejwin.com/en/insight/%E3%80%90quant%E3%80%91aroon-up-down-strategy/)
- [技術指標教室｜動量指標 AROON - FinLab](https://www.finlab.tw/aroon_indicator/)