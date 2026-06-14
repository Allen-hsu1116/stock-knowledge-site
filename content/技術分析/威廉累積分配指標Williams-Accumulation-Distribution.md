---
category: "技術分析"
title: 威廉累積分配指標 Williams Accumulation/Distribution
date: 2026-05-31
---

# 威廉累積分配指標 Williams Accumulation/Distribution

> Larry Williams 設計的量價累積指標，用「真實高低的範圍」衡量多空力量，比 OBV 更精確地反映資金流向——價格創新高但 WA/D 不創新高，就是頂部背離警訊

## 核心概念

### 什麼是威廉累積分配？

 Williams Accumulation/Distribution（簡稱 WA/D 或 Williams A/D）是 Larry Williams 在 1972 年開發的量價累積指標。它不像 OBV 只看漲跌方向加減成交量，而是用「真實範圍」（True Range）的概念來衡量每天的多空力量分配。

**核心邏輯**：價格在某個範圍內波動，收盤價落在範圍的哪個位置，決定了當天多空力量的強弱。

### 計算公式

**步驟一：計算真實高低（True Range High/Low）**
```
True Range High = MAX(High, 前日Close)
True Range Low  = MIN(Low, 前日Close)
```

**步驟二：計算多空力量值**
- 如果收盤價 > 前日收盤價（上漲日）：
  ```
  多空值 = Close - True Range Low +（Close - Open）/ 2
  ```
- 如果收盤價 ≤ 前日收盤價（下跌日）：
  ```
  多空值 = Close - True Range High -（Open - Close）/ 2
  ```

**步驟三：累積計算**
```
WA/D = 前日WA/D + 多空值 × 成交量
```

### 與 OBV 和 Chaikin A/D 的比較

| 指標 | 計算邏輯 | 優點 | 缺點 |
|------|---------|------|------|
| OBV | 漲加量、跌減量 | 最簡單直觀 | 忽略日內價格位置 |
| Chaikin A/D | CLV × Volume 累積 | 考慮收盤位置 | 忽略跳空缺口 |
| Williams A/D | 真實範圍 × 成交量 | 處理跳空、更精確 | 計算較複雜 |

**Williams A/D 比 OBV 好在哪**：
- OBV 今天漲1點跟漲100點加的量一樣，Williams A/D 會區分程度
- OBV 不考慮跳空，Williams A/D 用 True Range 處理了跳空問題

**Williams A/D 比 Chaikin A/D 好在哪**：
- Chaikin A/D 碰到跳空開盤會失真（開盤跳空高開但收盤在低點，CLV 可能仍為正）
- Williams A/D 用 True Range High/Low 修正了跳空問題

## 實戰應用

### 1. 背離判讀（最重要的應用）

**頂部背離（看跌）**：
- 價格創新高，但 WA/D 沒有創新高
- 含義：上漲缺少成交量支撐，多頭力量在衰退
- 操作：考慮減碼或設緊停損

**底部背離（看漲）**：
- 價格創新低，但 WA/D 沒有創新低
- 含義：下跌缺量，空頭力量在衰退
- 操作：觀察其他指標確認，準備進場

**背離確認三步驟**：
1. 價格與 WA/D 出現背離
2. 等待 WA/D 轉折（方向改變）
3. 價格突破趨勢線確認

### 2. 趨勢確認

- WA/D 與價格同方向創新高新低 → 趨勢健康，可續抱
- WA/D 突破前高 → 量能支撐趨勢，偏多訊號
- WA/D 跌破前低 → 量能反轉，偏空訊號

### 3. 趨勢線與支撐壓力

- 在 WA/D 上畫趨勢線比在 OBV 上更有意義（因為包含價格位置資訊）
- WA/D 突破趨勢線的訊號比價格突破早 1-3 天（量先價行）

### 4. 搭配其他指標

**黃金組合：Williams A/D + [[RSI相對強弱指標|RSI]]**
- RSI 背離 + Williams A/D 背離 → 雙重確認，勝率顯著提升
- RSI 超買/超賣 + WA/D 方向轉折 → 進出場時機

**組合：Williams A/D + [[MACD指標實戰判讀|MACD]]**
- MACD 金叉/死叉 + WA/D 方向一致 → 確認趨勢啟動
- MACD 交叉但 WA/D 不確認 → 可能是假突破

### 5. 台股實戰注意事項

- 台股有涨跌幅限制（±10%），極端行情下 WA/D 效果減弱
- 開盤跳空是常態（受美股影響），Williams A/D 的 True Range 處理比 OBV 和 Chaikin A/D 更適合台股
- 盤整時 WA/D 會平緩，需要搭配趨勢指標過濾

## 注意事項

### 1. 計算複雜度高
Williams A/D 的計算步驟比 OBV 多，程式化交易時需要確認計算邏輯無誤。很多看盤軟體的 WA/D 演算法不一致，使用前要先確認軟體是用哪一版公式。

### 2. 單獨使用效果有限
WA/D 本身是輔助指標，不提供明確的買賣訊號（沒有超買超賣區間），必須搭配價格型態或其他指標。最佳使用方式是看背離和趨勢線突破。

### 3. 極端量能會扭曲結果
單日爆量漲停或跌停會讓 WA/D 劇烈跳動，可能產生假訊號。遇到除權息、處置股等特殊交易日需要排除或調整。

### 4. 盤整市失效
所有量價累積指標在盤整市中都容易產生假訊號，Williams A/D 也不例外。搭配 [[ADX趨勢強度過濾盤整|ADX]] 或 [[斬波指標Choppiness-Index|CHOP]] 過濾盤整市是必要的。

### 5. 與 Williams %R 的差異
Larry Williams 還開發了 [[威廉指標Williams-%R|Williams %R]] 擺盪指標，但兩者完全不同：
- Williams A/D 是量價累積指標（看長期趨勢）
- Williams %R 是動量擺盪指標（看短期超買超賣）
- 不要搞混了

## 相關主題

- [[OBV能量潮指標量價趨勢判讀|OBV能量潮指標]] — 最簡單的量價累積指標，漲加量跌減量
- [[AD累積分配指標收盤位置加權|AD累積分配指標]] — OBV的改良版，用收盤位置加權取代二元漲跌
- [[Chaikin-Money-Flow佳慶資金流量指標|Chaikin Money Flow]] — A/D線的震盪版本，背離是轉勢最強訊號
- [[Chaikin-Oscillator佳慶震盪指標|Chaikin Oscillator]] — A/D線的MACD版，偵測資金動能轉折
- [[量價關係九種型態高低檔判讀|量價關係九種型態]] — 量價基礎判讀
- [[成交量確認原則Volume-Confirmation|成交量確認原則]] — 沒有量能支持的突破都是假突破

## 來源

- Larry Williams, "How I Made One Million Dollars Last Year Trading Commodities" (1972) — Williams A/D 原始提出
- Larry Williams, "Long-Term Secrets to Short-Term Trading" — Williams A/D 實戰應用
- Alexander Elder, "Trading for a Living" — Williams A/D 與其他量價指標的比較