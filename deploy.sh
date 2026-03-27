#!/bin/bash
# 部署股票學習筆記到 Vercel

cd ~/.openclaw/workspace/stock-knowledge-site

# 檢查 Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "請先安裝 Vercel CLI:"
    echo "npm install -g vercel"
    echo ""
    echo "然後執行: vercel login"
    exit 1
fi

# 生成網站
echo "生成網站..."
python3 generate_site.py

# 部署
echo "部署到 Vercel..."
vercel --prod

echo ""
echo "✅ 部署完成！"