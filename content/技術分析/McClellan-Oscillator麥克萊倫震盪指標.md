---
date: 2026-05-18
---

# McClellan Oscillator麥克萊倫震盪指標

> AD Line的MACD版——用19日EMA減39日EMA捕捉市場寬度動能，寬度推升是起漲訊號、背離是大盤反轉預警，搭配Summation Index看中長期趨勢

## 核心概念

**McClellan Oscillator**（麥克萊倫震盪指標）由Sherman和Marian McClellan夫婦開發，是將**淨漲跌家數**（Net Advances = 上漲家數 - 下跌家數）的19日EMA與39日EMA相減得出的市場寬度動能指標。

如果把AD Line（騰落指數）看成價格線，那McClellan Oscillator就是AD Line的MACD——它把市場寬度的動能變化可視化，讓你一眼看出多空力道是在加速還是減速。

### 公式

```
RANA（Ratio-Adjusted Net Advances）= (上漲家數 - 下跌家數) / (上漲家數 + 下跌家數) × 1000

McClellan Oscillator = RANA的19日EMA - RANA的39日EMA

19日EMA平滑係數 = 0.10（= 2/(19+1)）
39日EMA平滑係數 = 0.05（= 2/(39+1)）
```

**為什麼用比例調整（RANA）？**
NYSE在1990年交易約2000檔股票，2010年超過3600檔。如果直接用淨漲跌家數，不同時期的數值無法比較。RANA把淨漲跌家數轉成百分比，消除掛牌數量變動的影響，讓歷史數據可以公平對比。

### McClellan Summation Index（麥克萊倫累計指標）

McClellan Oscillator的累計版本：

```
今日MSI = 昨日MSI + 今日McClellan Oscillator
（第一天的MSI = 第一天的McClellan Oscillator）
```

**MSI vs McClellan Oscillator的關係**：
- McClellan Oscillator = **短期**市場寬度動能（像MACD柱狀圖）
- McClellan Summation Index = **中長期**市場寬度趨勢（像MACD的訊號線）

## 實戰判讀

### 三大訊號類型

**一、零軸穿越（Centerline Crossovers）**

| 訊號 | 含義 | 操作意義 |
|------|------|----------|
| 從負轉正（突破零軸） | 多方寬度動能增強 | 偏多操作 |
| 從正轉負（跌破零軸） | 空方寬度動能增強 | 偏空或觀望 |
| 長期在零軸上方 | 持續多頭寬度 | 做多為主 |
| 長期在零軸下方 | 持續空頭寬度 | 減碼或做空 |

**二、寬度推升（Breadth Thrusts）**

定義：McClellan Oscillator從極低值急速拉升至高值，典型是從-50以下飆升到+50以上（+100點推升）。

**特徵**：
- 通常標誌重要底部
- 如果前面有**多頭背離**，訊號更可靠
- 推升後指標回到正區但形成較低高點是正常的
- 只要維持在正區，多頭格局不變

**寬度推升實戰SOP**：
1. 觀察McClellan Oscillator是否從-50以下急速回升
2. 確認是否伴隨多頭背離（指數新低但Oscillator未新低）
3. 等推升完成後回測零軸不破，再加碼進場
4. 設停損在零軸下方

**三、背離（Divergences）**

| 背離類型 | 定義 | 可靠度 |
|----------|------|--------|
| 多頭背離 | 指數新低但McClellan Oscillator較高 | 高（特別是在極端負值後） |
| 空頭背離 | 指數新高但McClellan Oscillator較低 | 高（特別是在極端正值後） |

**背離確認條件**：
1. 背離必須明顯——兩個高點/低點之間的差異要肉眼可見
2. 背離需要伴隨強烈的方向性移動確認（多頭背離需突破零軸、空頭背離需跌破零軸）
3. 弱背離（差異微小）大多不會導致反轉

### McClellan Oscillator vs McClellan Summation Index搭配

| 狀態 | McClellan Oscillator | Summation Index | 解讀 | 操作 |
|------|---------------------|-----------------|------|------|
| 雙正 | 正值且上升 | 正值 | 強多頭 | 積極做多 |
| Osc正但Sum負 | 正值 | 負值 | 多頭動能初升 | 小部位試多 |
| Osc負但Sum正 | 負值 | 正值 | 多頭動能衰退 | 減碼 |
| 雙負 | 負值且下降 | 負值 | 強空頭 | 偏空或空手 |

### 關鍵數值參考（NYSE歷史經驗）

| 數值區間 | 含義 |
|----------|------|
| > +100 | 極度多頭寬度，可能過熱 |
| +50 ~ +100 | 健康多頭 |
| -50 ~ +50 | 中性區間，震盪 |
| -100 ~ -50 | 空頭動能增強 |
| < -100 | 極度空頭寬度，可能超賣 |

⚠️ 以上是NYSE歷史經驗值，台股需要自行回測調整。

## 台股應用注意事項

1. **數據來源**：台灣證券交易所每日公布漲跌家數，可計算加權指數的McClellan Oscillator。櫃買指數建議分開計算。

2. **參數調整**：19日和39日是原始設計參數，對應約1個月和2個月的交易天數。台股可以考慮用20日和40日（整數更容易計算）。

3. **搭配TRIN使用**：McClellan Oscillator只看家數不看量，TRIN同時看家數和量。兩者搭配：
   - McClellan Oscillator正 + TRIN < 1 = 最強多頭確認
   - McClellan Oscillator負 + TRIN > 1 = 最強空頭確認
   - 兩者矛盾時 = 結構性分化，需進一步分析

4. **搭配ADL使用**：McClellan Oscillator是ADL的動能版本。ADL看長期趨勢方向，McClellan Oscillator看動能轉折點。

5. **寬度推升的台股特徵**：台股底部常出現寬度推升，但推升幅度可能不如美股劇烈。觀察從-40以下推升至+40以上即可視為有效推升。

6. **背離的時間框架**：日線背離看1-2週轉折，週線背離看1-3個月轉折。短線操作用日線，波段操作用週線。

7. **Summation Index趨勢線**：在MSI上畫趨勢線，跌破上升趨勢線是中期空頭訊號，突破下降趨勢線是中期多頭訊號。

## 與MACD的類比理解

| 概念 | MACD（個股） | McClellan Oscillator（大盤） |
|------|-------------|------------------------------|
| 原始數據 | 股價 | 淨漲跌家數 |
| 快線 | 12日EMA | 19日EMA |
| 慢線 | 26日EMA | 39日EMA |
| 柱狀圖 | DIF - DEA | McClellan Oscillator值 |
| 累計版本 | MACD本身 | Summation Index |
| 零軸穿越 | 多空轉換 | 寬度多空轉換 |
| 背離 | 價格背離 | 大盤背離 |
| 推升 | — | 寬度推升（特有） |

## 注意事項

- **McClellan Oscillator只看家數不看個股權重**：這是寬度指標的優勢也是劣勢——不會被大型股掩蓋，但也無法反映大型股的影響力
- **波動大是正常**：和MACD一樣，McClellan Oscillator產生很多潛在訊號，但不是每個都有效
- **背離很多但大多不會反轉**：只關注明顯的、尖銳的背離，忽略微弱的背離
- **寬度推升後的較低高點是正常的**：不要期待Oscillator永遠維持在+50以上，只要維持正區即可
- **不同市場基準值不同**：NYSE、NASDAQ、台股的極端值區間不同，必須回測
- **順大趨勢操作**：多頭市場偏用超賣訊號做多，空頭市場偏用超買訊號減碼

## 相關主題
- [[技術分析/TRIN阿姆氏指標Arms-Index]]
- [[技術分析/騰落指數ADL判讀]]
- [[技術分析/大盤強弱判讀與市場寬度]]
- [[技術分析/MACD指標實戰判讀]]
- [[技術分析/MACD進階實戰柱狀圖背離零軸交易與雙背離確認]]
- [[技術分析/背離Divergence進階實戰]]
- [[技術分析/量價關係九種型態高低檔判讀]]
- [[技術分析/多指標共振交易系統Multi-Indicator-Confluence]]

## 來源
- [McClellan Oscillator - StockCharts ChartSchool](../raw/2026-05-18/TRIN阿姆氏指標與麥克萊倫震盪指標.md)
- [McClellan Summation Index - StockCharts ChartSchool](../raw/2026-05-18/TRIN阿姆氏指標與麥克萊倫震盪指標.md)
- [市場寬度 - Finetic](../raw/2026-05-18/TRIN阿姆氏指標與麥克萊倫震盪指標.md)
- [TRIN 交易者指數 - taindicators](../raw/2026-05-18/TRIN阿姆氏指標與麥克萊倫震盪指標.md)