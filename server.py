#!/usr/bin/env python3
"""
股票學習筆記 - 動態網站伺服器

即時讀取 memory/stock-learning/*.md 和 memory/stock-knowledge.md
不需要預先生成 HTML

Usage:
    python3 server.py [--port 8080]
"""

import os
import re
import json
import markdown
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template_string, send_from_directory

# 路徑配置
BASE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"

# Flask App
app = Flask(__name__)

# 主題對應
TOPIC_MAP = {
    "技術分析": ("technical", "📊"),
    "技術面": ("technical", "📊"),
    "K線": ("technical", "📊"),
    "均線": ("technical", "📊"),
    "基本面": ("fundamental", "💰"),
    "財報": ("fundamental", "💰"),
    "估值": ("fundamental", "💰"),
    "籌碼": ("chips", "🎲"),
    "法人": ("chips", "🎲"),
    "主力": ("chips", "🎲"),
    "操作策略": ("strategy", "🎯"),
    "當沖": ("strategy", "🎯"),
    "波段": ("strategy", "🎯"),
    "風險管理": ("risk", "⚠️"),
    "停損": ("risk", "⚠️"),
    "交易心理": ("psychology", "🧠"),
    "心態": ("psychology", "🧠"),
}

# 模板
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - 股票學習筆記</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1>📈 股票學習筆記</h1>
        <p class="subtitle">朝股票操作大師邁進中</p>
        <nav>
            <a href="/" {% if page == 'index' %}class="active"{% endif %}>總覽</a>
            <a href="/knowledge" {% if page == 'knowledge' %}class="active"{% endif %}>知識庫</a>
            <a href="/history" {% if page == 'history' %}class="active"{% endif %}>學習記錄</a>
        </nav>
    </header>

    <main>
        {{ content | safe }}
    </main>

    <footer>
        <p>由妖姬西打龍 🐍 自動生成</p>
        <p>最後更新：{{ last_update }}</p>
    </footer>
</body>
</html>
"""


def parse_markdown(filepath: Path) -> dict:
    """解析 Markdown 檔案"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return {"title": "找不到內容", "content": "", "topics": []}
    
    # 提取標題
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    
    # 提取日期
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else ""
    
    # 提取主題
    topics = []
    for keyword, (tag, icon) in TOPIC_MAP.items():
        if keyword in content and tag not in topics:
            topics.append(tag)
    
    # 轉換為 HTML
    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    
    return {
        "title": title,
        "date": date,
        "content": html_content,
        "topics": topics,
        "filename": filepath.stem,
    }


def get_stats():
    """取得統計資料"""
    total_sessions = 0
    all_topics = set()
    recent = []
    
    if LEARNING_DIR.exists():
        for md_file in sorted(LEARNING_DIR.glob("*.md"), reverse=True):
            total_sessions += 1
            data = parse_markdown(md_file)
            all_topics.update(data["topics"])
            
            if len(recent) < 10:
                recent.append(data)
    
    return {
        "total_sessions": total_sessions,
        "total_topics": len(all_topics),
        "recent": recent,
    }


def get_topic_tag(topic: str) -> str:
    """取得主題標籤"""
    for keyword, (tag, icon) in TOPIC_MAP.items():
        if tag == topic:
            return f"{icon} {keyword}"
    return topic


# 路由
@app.route("/")
def index():
    """首頁"""
    stats = get_stats()
    
    # 統計卡片
    stats_html = f"""
    <section class="stats">
        <div class="stat-card">
            <h3>學習回合</h3>
            <p>{stats['total_sessions']}</p>
        </div>
        <div class="stat-card">
            <h3>涵蓋主題</h3>
            <p>{stats['total_topics']}</p>
        </div>
        <div class="stat-card">
            <h3>最新學習</h3>
            <p>{stats['recent'][0]['date'] if stats['recent'] else '--'}</p>
        </div>
    </section>
    """
    
    # 主題卡片
    topics_html = """
    <section class="topics">
        <h2>📚 依主題瀏覽</h2>
        <div class="topic-grid">
            <a href="/topic/technical" class="topic-card">
                <h3>📊 技術分析</h3>
                <p>K線、均線、支撐壓力</p>
            </a>
            <a href="/topic/fundamental" class="topic-card">
                <h3>💰 基本面分析</h3>
                <p>財報、估值、產業</p>
            </a>
            <a href="/topic/chips" class="topic-card">
                <h3>🎲 籌碼面分析</h3>
                <p>法人、主力、融資券</p>
            </a>
            <a href="/topic/strategy" class="topic-card">
                <h3>🎯 操作策略</h3>
                <p>當沖、波段、價值投資</p>
            </a>
            <a href="/topic/risk" class="topic-card">
                <h3>⚠️ 風險管理</h3>
                <p>停損停利、倉位控制</p>
            </a>
            <a href="/topic/psychology" class="topic-card">
                <h3>🧠 交易心理</h3>
                <p>心態建設、認知偏誤</p>
            </a>
        </div>
    </section>
    """
    
    # 最近列表
    recent_html = "<ul>"
    for r in stats['recent'][:10]:
        topics_tags = "".join([f'<span class="tag {t}">{t}</span>' for t in r['topics'][:2]])
        recent_html += f"""
        <li>
            <a href="/history/{r['filename']}">{r['date']} - {r['title'][:30]}</a>
            {topics_tags}
        </li>
        """
    recent_html += "</ul>"
    
    content = f"""
    {stats_html}
    {topics_html}
    <section class="recent">
        <h2>🕐 最近學習</h2>
        {recent_html}
    </section>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title="首頁",
        page="index",
        content=content,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/knowledge")
def knowledge():
    """知識庫"""
    knowledge_file = MEMORY_DIR / "stock-knowledge.md"
    data = parse_markdown(knowledge_file)
    
    topics_tags = "".join([f'<span class="tag {t}">{t}</span>' for t in data['topics']])
    
    content = f"""
    <div class="content">
        <h1>{data['title']}</h1>
        <p class="meta">{topics_tags}</p>
        {data['content']}
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title="知識庫",
        page="knowledge",
        content=content,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/history")
def history():
    """學習記錄列表"""
    stats = get_stats()
    
    content = "<div class='history-list'><h2>📅 所有學習記錄</h2><ul>"
    for r in stats['recent']:
        topics_tags = "".join([f'<span class="tag {t}">{t}</span>' for t in r['topics'][:2]])
        content += f"""
        <li>
            <a href="/history/{r['filename']}">{r['date']}</a>
            <span class="title">{r['title'][:50]}</span>
            {topics_tags}
        </li>
        """
    content += "</ul></div>"
    
    return render_template_string(
        BASE_TEMPLATE,
        title="學習記錄",
        page="history",
        content=content,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/history/<filename>")
def history_detail(filename):
    """學習記錄詳情"""
    md_file = LEARNING_DIR / f"{filename}.md"
    if not md_file.exists():
        return "找不到此記錄", 404
    
    data = parse_markdown(md_file)
    topics_tags = "".join([f'<span class="tag {t}">{t}</span>' for t in data['topics']])
    
    content = f"""
    <div class="content">
        <p><a href="/history">← 返回列表</a></p>
        <h1>{data['title']}</h1>
        <p class="meta">{data['date']} {topics_tags}</p>
        {data['content']}
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title=data['title'],
        page="history",
        content=content,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/topic/<topic>")
def topic(topic):
    """主題分類"""
    topic_names = {
        "technical": "技術分析",
        "fundamental": "基本面分析",
        "chips": "籌碼面分析",
        "strategy": "操作策略",
        "risk": "風險管理",
        "psychology": "交易心理",
    }
    
    stats = get_stats()
    filtered = [r for r in stats['recent'] if topic in r['topics']]
    
    content = f"""
    <div class='topic-page'>
        <p><a href="/">← 返回首頁</a></p>
        <h2>📚 {topic_names.get(topic, topic)}</h2>
        <ul>
    """
    
    for r in filtered:
        content += f"""
        <li>
            <a href="/history/{r['filename']}">{r['date']}</a>
            <span class="title">{r['title'][:50]}</span>
        </li>
        """
    
    content += "</ul></div>"
    
    return render_template_string(
        BASE_TEMPLATE,
        title=topic_names.get(topic, topic),
        page="index",
        content=content,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/static/style.css")
def style():
    return send_from_directory(BASE_DIR, "style.css")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    
    print(f"啟動網站伺服器：http://localhost:{args.port}")
    print("按 Ctrl+C 停止")
    
    app.run(host="0.0.0.0", port=args.port, debug=False)