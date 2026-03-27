# 股票學習筆記

這是一個自動從學習記錄生成的靜態網站。

## 部署到 Vercel

1. 安裝 Vercel CLI：
```bash
npm install -g vercel
```

2. 登入 Vercel：
```bash
vercel login
```

3. 部署：
```bash
cd ~/.openclaw/workspace/stock-knowledge-site
vercel --prod
```

## 更新網站

每次學習記錄更新後，執行：
```bash
python3 generate_site.py && vercel --prod
```

## 自動更新

已設定 cron job 每小時更新網站。