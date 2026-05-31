# Elder-Ray牛熊力量指標

> 市場的X光機，看穿K線皮膚底下多頭貪婪與空頭恐懼的真實骨架

## 核心概念

艾爾德射線 (Elder-Ray Index)，又稱牛熊力量指標 (Bull & Bear Power)，由傳奇交易員 Alexander Elder 博士發明。

命名由來：「Ray」代表X光射線。K線圖是市場的皮膚，這套指標是市場的X光機，能看穿多頭（貪婪）與空頭（恐懼）的真實力量。

### 三個行為金融學假設

1. **價值共識 (Value Consensus)**：13日 EMA 代表多空雙方妥協後的「合理價值」
2. **Bull Power（多頭力量）**：最高價與EMA的距離
   - 公式：Bull Power = High – 13日 EMA
   - 意義：多頭能把價格拉離價值共識多遠
3. **Bear Power（空頭力量）**：最低價與EMA的距離
   - 公式：Bear Power = Low – 13日 EMA
   - 意義：空頭能把價格壓離價值共識多深

## 實戰應用

### 最高勝率買點：多頭趨勢中的「空頭力竭」
- **前提**：13日 EMA 趨勢向上（大方向多頭）
- **觸發**：Bear Power 在零軸之下（股價回檔），但柱狀體開始縮短、向上勾頭
- **解讀**：空頭砸盤力量耗盡，順勢拉回買點
- **這就是 [[多時間框架分析]] 的精髓**：大方向多頭 + 短期空頭力竭 = 進場

### 最高勝率空點：空頭趨勢中的「多頭力竭」
- **前提**：13日 EMA 趨勢向下
- **觸發**：Bull Power 在零軸之上，但柱狀體開始縮短、向下彎折
- **解讀**：反彈中多頭力盡，極佳的反彈空點

### 終極反轉訊號：力量背離 (Power Divergence)
- **頂背離**：股價創新高，Bull Power 比前一波低 → 多頭耗竭，即將見頂
- **底背離**：股價創新低，Bear Power 負值比前一波淺 → 空頭耗竭，即將見底

### 與三重濾網系統搭配
Elder-Ray 是 [[三重濾網交易系統]] 中第二重濾網的理想工具：
- 第一重：週線 MACD 判斷大方向
- 第二重：日線 Elder-Ray 找空頭力竭買點
- 第三重：60分鐘線確認突破進場

## XScript 指標腳本

```
// 指標名稱：Elder-Ray Index (艾爾德射線 / 牛熊力量指標)
// 理論基礎：Dr. Alexander Elder
Input: Length(13, "EMA 計算週期");
Variable: ValueEMA(0), BullPower(0), BearPower(0);

// 1. 計算市場價值共識 (13 日 EMA)
ValueEMA = XAverage(Close, Length);

// 2. 計算多頭力量與空頭力量
BullPower = High - ValueEMA;
BearPower = Low - ValueEMA;

// 3. 繪圖輸出
Plot1(BullPower, "多頭力量(Bull)");
Plot2(BearPower, "空頭力量(Bear)");
Plot3(0, "價值共識(零軸)");
```

## 注意事項

- **EMA 方向是前提**：不看EMA方向就讀Bull/Bear Power毫無意義，多頭趨勢中看空頭力竭，空頭趨勢中看多頭力竭
- **Bear Power 在零軸下是正常的**：不代表一定看空，關鍵是「柱狀體縮短」的力竭訊號
- **力量背離比絕對值更重要**：不要纠结Bull Power數字多大，要看趨勢變化
- **盤整區間無效**：EMA走平時Bull/Bear Power失去方向性參考價值
- **單獨使用風險高**：一定要搭配趨勢判斷和其他指標確認
- **精神醫學視角**：Elder有精神科醫師背景，指標設計核心是量化貪婪（Bull Power）與恐懼（Bear Power）的心理狀態

## 相關主題

- [[三重濾網交易系統]] - Elder-Ray的發明者Elder設計的多時間框架系統
- [[多時間框架分析]] - Elder-Ray適合放在中間層級使用
- [[背離Divergence進階實戰]] - Power Divergence是背離的一種
- [[順勢交易]] - Elder-Ray是順勢交易找進場點的最佳工具
- [[背離Divergence進階實戰]] - 其他背離指標可交叉驗證
- [[MACD指標實戰判讀]] - 第一重濾網常用指標

## 來源

- [Elder-Ray Index - XQ官方部落格](../raw/2026-04-30/Elder-Ray-Index牛熊力量指標.md)
- [Elder-Ray Index 進階 - XQ官方部落格](../raw/2026-05-11/Elder-Ray-Index牛熊力量指標.md)