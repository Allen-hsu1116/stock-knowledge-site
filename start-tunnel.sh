#!/bin/bash
# 啟動股票學習筆記網站 + Cloudflare Tunnel

cd ~/.openclaw/workspace/stock-knowledge-site

# 停止舊的進程
pkill -f "server.py --port 8080" 2>/dev/null
pkill -f "cloudflared tunnel" 2>/dev/null
sleep 1

# 啟動網站
echo "啟動網站..."
python3 server.py --port 8080 > /tmp/stock-site.log 2>&1 &
sleep 2

# 啟動 Cloudflare Tunnel
echo "啟動 Cloudflare Tunnel..."
cloudflared tunnel --url http://localhost:8080 > /tmp/cloudflared.log 2>&1 &

sleep 3

# 取得網址
URL=$(grep -o 'https://[^.]*\.trycloudflare\.com' /tmp/cloudflared.log 2>/dev/null | head -1)

if [ -n "$URL" ]; then
    echo ""
    echo "✅ 網站已啟動！"
    echo ""
    echo "本地網址: http://localhost:8080"
    echo "外網網址: $URL"
    echo ""
    echo "按 Ctrl+C 停止（會繼續在背景運行）"
    echo "完全停止: pkill -f 'server.py\|cloudflared'"
else
    echo "⚠️ Cloudflare Tunnel 啟動中，請稍候..."
    echo "檢查日誌: cat /tmp/cloudflared.log"
fi