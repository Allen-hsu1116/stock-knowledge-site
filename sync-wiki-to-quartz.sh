#!/bin/bash
# sync-wiki-to-quartz.sh
# 從 stock-knowledge-base/wiki/ 同步內容到 Quartz 專案的 content/ 目錄

QUARTZ_DIR="$(cd "$(dirname "$0")" && pwd)"
WIKI_DIR="$QUARTZ_DIR/../stock-knowledge-base/wiki"

echo "🔄 同步 stock wiki → Quartz content/"
echo "   來源: $WIKI_DIR"
echo "   目標: $QUARTZ_DIR/content/"

if [ ! -d "$WIKI_DIR" ]; then
  echo "❌ 找不到 wiki 目錄: $WIKI_DIR"
  exit 1
fi

rsync -av --delete \
  --exclude='SCHEMA.md' \
  --exclude='SKILL.md' \
  --exclude='.obsidian' \
  --exclude='templates' \
  --exclude='private' \
  "$WIKI_DIR/" "$QUARTZ_DIR/content/"

echo "✅ 同步完成"
echo ""
echo "📊 同步統計:"
echo "   檔案數: $(find "$QUARTZ_DIR/content/" -name "*.md" | wc -l | tr -d ' ')"
echo ""
echo "接下來可以："
echo "  1. cd $QUARTZ_DIR && npx quartz build --serve  # 本地預覽"
echo "  2. cd $QUARTZ_DIR && npx quartz sync            # 推送到 GitHub"