---
title: "EP310 蘋果WWDC、Anthropic最強模型與SpaceX AI衛星——端側AI到太空資料中心"
category: "YouTube頻道"
---

# EP310 蘋果WWDC、Anthropic最強模型與SpaceX AI衛星——端側AI到太空資料中心

> M觀點把本集拆成三條科技主線：蘋果用 Google 技術補 AI 作業、Anthropic 新模型靠高價與安全控管重回前沿模型王座，SpaceX AI-1 衛星則讓太空資料中心從故事變成可驗證的工程題。

## 影片資訊

- **頻道**：M觀點
- **上傳日期**：2026-06-11
- **影片連結**：[YouTube](https://www.youtube.com/watch?v=2F98tMvzm14)
- **時效性**：本篇內容基於 2026-06-11 的市場觀點，僅供當時參考

## 核心觀點

**1. 蘋果 WWDC 交出的是及格 AI 作業，不是驚艷答案**
蘋果發表 Apple Foundation Model（AFM）系列，包含手機端小模型、Core Advanced、Private Cloud Compute、Cloud Pro 與影像模型。M觀點認為蘋果不是直接拿 Gemini 改皮，而是用 Google 技術與訓練方法從零訓練，再用 Gemini 類似蒸餾方式增強；這讓蘋果至少能交出合理 AI 方案，但分數大概只有 70 分。

**2. AFM Core Advanced 的重點是用 NAND Flash 補 DRAM 不足**
蘋果手機記憶體有限，20B 參數的 MoE 模型理論上放不進 DRAM，因此蘋果把權重放在 NAND Flash，需要時只載入被啟動的 1B 到 4B 參數到 DRAM。這做法很 Apple：省成本、有工程巧思，但因每個 prompt 大致只選一次專家，效能與彈性不會像傳統 MoE 那麼漂亮。

**3. 新 Siri 若能控制手機與 App，就是保底；但不會讓蘋果拿高分**
新 Siri 方向包含 personal context、on-screen awareness、App Intents 與多層模型調度：手機小模型解不了就上 Core Advanced，再上 Apple 私有雲，最後接 Cloud Pro 或外部 Gemini、ChatGPT、Claude。這能補足「能操作手機的 ChatGPT」需求，但 M觀點認為手機仍會賣得動，AI 只是保底，不是重新定價蘋果的爆點。

**4. Anthropic 新模型重新登上王座，但 30 天資料保留是企業採用地雷**
M觀點認為 Anthropic 新模型在多個 benchmark（AI intelligence index、SW Bench Pro、GPT Val、Humanity’s Last Exam、Terminal Bench）明顯超過 GPT-5.5 與 Opus 4.8，且網路早期使用者評價很好，唯一明顯缺點是貴。但因高風險安全監控需要保留資料 30 天，很多大企業與政府機構可能無法接受，反而給 OpenAI、Google、Microsoft 自有模型留下空間。

**5. SpaceX AI-1 衛星讓太空資料中心變成工程問題，不只是太空夢**
SpaceX 公布 AI-1 衛星設計：150kW 峰值發電、70 公尺級太陽能翼、液冷輻射散熱，剛好對應一組 NVIDIA GB300 NVL72 機櫃用電。M觀點認為散熱不是科學不可行，而是工程題；若 Starship 2026 年多次成功、2027 年進入商業任務，AI-1 衛星有機會在 2027 年形成小型太空資料中心 cluster。

## 實戰重點

- **蘋果 AI 先看 Siri 交付，不要只看 WWDC 簡報**：目前只是告訴市場如何交卷，真正分數要等新 Siri 與 AFM 實際落地。
- **端側 AI 會拉動記憶體與儲存需求**：MoE 權重放 NAND Flash 的做法若成趨勢，手機儲存容量、DRAM 與端側推論最佳化都會變重要。
- **Anthropic 模型優勢短期明確，但企業市場看資安政策**：模型最強不等於企業一定能用，資料保留、合規與機密風險會決定採用速度。
- **AI 模型競賽觀察節奏**：OpenAI 可能 7-8 月才有真正對抗版本；Google 可能落後 5-6 個月；xAI 1.5T 版本短期未必能追上最前沿模型。
- **SpaceX 估值要拆成 Starlink、Starship 與太空資料中心**：就算太空資料中心成真，M觀點仍認為 1.7 兆美元估值偏高；不要把夢全部用最高倍數折現。
- **太空 AI 供應鏈看三種算力版本**：NVIDIA GPU 版、Google TPU 版、Tesla AI5/AI6 ASIC 版都可能出現；能源效率越高，越適合上太空。

## 注意事項

- 本集 Whisper 語音辨識有大量專有名詞誤差，AFM、Gemini、Anthropic、Claude、SpaceX、Starship、NVL72、GB300 等已依語境校正。
- Apple AFM 與新 Siri 多數仍是規劃與預告，實際產品體驗、延遲與可用性要等正式推出。
- Anthropic 模型表現基於當時 benchmark 與早期使用心得，模型競賽變化極快，可能數週內被追上。
- SpaceX AI-1 的時間表高度依賴 Starship 發射穩定度；若發射事故或監管延誤，2027 年商業 cluster 推估會延後。

## 相關主題
- [[YouTube頻道/M觀點/EP309-Google租xAI算力-微軟NAI模型與股市修正終於來了嗎]]
- [[產業地圖/AI伺服器｜ODM與GPU運算平台]]
- [[產業地圖/網通衛星｜低軌衛星通訊系統]]
- [[YouTube頻道/周刊投資/SpaceX最大IPO與低軌衛星AI算力-台廠供應鏈升級戰]]

## 來源
- [EP310. 蘋果 WWDC 重點、Anthropic 最強模型、SpaceX AI 衛星 | M觀點](https://www.youtube.com/watch?v=2F98tMvzm14)
