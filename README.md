# 股票學習筆記網站

自動從學習記錄生成的靜態網站。

## 網址

GitHub Pages: https://allen-hsu1116.github.io/stock-knowledge-site

## 設定步驟

1. 到 GitHub repo → Settings → Pages
2. Source 選擇 **GitHub Actions**
3. 等待部署完成（約 1-2 分鐘）

## 自動更新

每次 push 到 main 分支，GitHub Actions 會自動：
1. 執行 `generate_site_v2.py` 生成網站
2. 部署到 GitHub Pages

## 本地預覽

```bash
python3 generate_site_v2.py
cd docs && python3 -m http.server 8080
# 開啟 http://localhost:8080
```