#!/bin/bash
# 啟動股票學習筆記網站

cd ~/.openclaw/workspace/stock-knowledge-site

PORT=${1:-8080}

echo "啟動網站..."
echo "網址: http://localhost:$PORT"
echo "按 Ctrl+C 停止"
echo ""

python3 server.py --port $PORT