#!/usr/bin/env python3
"""
股票學習筆記 - 增強版動態網站伺服器

功能：
- 學習進度儀表板
- 主題分類瀏覽
- 時間線視圖
- 知識圖譜
- 搜尋功能
"""

import os
import re
import json
from datetime import datetime, timedelta
from pathlib import Path
from flask import Flask, render_template_string, request, jsonify
import markdown

# 路徑配置
BASE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"

# Flask App
app = Flask(__name__)

# 主題對應
TOPICS = {
    "technical": {"name": "技術分析", "icon": "📊", "keywords": ["K線", "均線", "支撐", "壓力", "技術", "RSI", "MACD"]},
    "fundamental": {"name": "基本面分析", "icon": "💰", "keywords": ["財報", "營收", "EPS", "本益比", "基本面", "估值"]},
    "chips": {"name": "籌碼面分析", "icon": "🎲", "keywords": ["法人", "主力", "融資", "融券", "籌碼", "外資", "投信"]},
    "strategy": {"name": "操作策略", "icon": "🎯", "keywords": ["當沖", "波段", "價值投資", "策略", "停損", "停利"]},
    "risk": {"name": "風險管理", "icon": "⚠️", "keywords": ["風險", "倉位", "部位", "MDD", "回撤"]},
    "psychology": {"name": "交易心理", "icon": "🧠", "keywords": ["心理", "心態", "情緒", "紀律"]}
}

# 模板
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} | 股票學習筆記</title>
    <link rel="stylesheet" href="/static/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">
                <span class="logo-icon">📈</span>
                <h1>股票學習筆記</h1>
            </div>
            <nav>
                <a href="/" {% if page == 'index' %}class="active"{% endif %}>📊 儀表板</a>
                <a href="/knowledge" {% if page == 'knowledge' %}class="active"{% endif %}>📚 知識庫</a>
                <a href="/timeline" {% if page == 'timeline' %}class="active"{% endif %}>📅 時間線</a>
                <a href="/graph" {% if page == 'graph' %}class="active"{% endif %}>🔗 知識圖譜</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        {{ content | safe }}
    </div>
    
    <footer>
        <div class="footer-stats">
            <div class="footer-stat">
                <div class="footer-stat-value">{{ stats.total_sessions }}</div>
                <div class="footer-stat-label">學習回合</div>
            </div>
            <div class="footer-stat">
                <div class="footer-stat-value">{{ stats.total_topics }}</div>
                <div class="footer-stat-label">涵蓋主題</div>
            </div>
            <div class="footer-stat">
                <div class="footer-stat-value">{{ stats.days_streak }}</div>
                <div class="footer-stat-label">連續天數</div>
            </div>
        </div>
        <p>由妖姬西打龍 🐍 自動生成 | 最後更新：{{ last_update }}</p>
    </footer>
    
    <script>
        // 搜尋功能
        function handleSearch(query) {
            if (query.length < 2) return;
            window.location.href = '/search?q=' + encodeURIComponent(query);
        }
    </script>
</body>
</html>
"""


def detect_topics(content: str) -> list:
    """從內容偵測主題"""
    topics = []
    for topic_key, topic_info in TOPICS.items():
        for keyword in topic_info["keywords"]:
            if keyword in content:
                if topic_key not in topics:
                    topics.append(topic_key)
                break
    return topics


def parse_learning_file(filepath: Path) -> dict:
    """解析學習檔案"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return None
    
    # 提取日期
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else ""
    
    # 提取標題
    title_match = re.search(r"^#+\s*(.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    
    # 偵測主題
    topics = detect_topics(content)
    
    # 提取重點（第一個 ## 後的內容）
    summary = ""
    summary_match = re.search(r"##[^#].+?\n(.+?)(?=\n##|\n#|$)", content, re.DOTALL)
    if summary_match:
        summary = summary_match.group(1).strip()[:200] + "..."
    
    return {
        "date": date,
        "title": title,
        "content": content,
        "topics": topics,
        "summary": summary,
        "filename": filepath.stem,
    }


def get_all_learning() -> list:
    """取得所有學習記錄"""
    files = []
    if LEARNING_DIR.exists():
        for f in sorted(LEARNING_DIR.glob("*.md"), reverse=True):
            data = parse_learning_file(f)
            if data:
                files.append(data)
    return files


def get_stats() -> dict:
    """取得統計資料"""
    learnings = get_all_learning()
    
    # 計算主題分佈
    topic_counts = {k: 0 for k in TOPICS}
    for l in learnings:
        for t in l["topics"]:
            if t in topic_counts:
                topic_counts[t] += 1
    
    # 計算連續天數
    streak = 0
    dates = set(l["date"] for l in learnings if l["date"])
    today = datetime.now().date()
    for i in range(365):
        check_date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        if check_date in dates:
            streak += 1
        else:
            break
    
    return {
        "total_sessions": len(learnings),
        "total_topics": len(TOPICS),
        "topic_counts": topic_counts,
        "days_streak": streak,
        "recent": learnings[:5],
    }


def get_knowledge_graph() -> dict:
    """構建知識圖譜"""
    learnings = get_all_learning()
    
    # 主題關聯
    topic_links = {}
    for l in learnings:
        topics = l["topics"]
        for i, t1 in enumerate(topics):
            for t2 in topics[i+1:]:
                key = tuple(sorted([t1, t2]))
                topic_links[key] = topic_links.get(key, 0) + 1
    
    # 每個主題的文章數
    topic_articles = {}
    for topic_key in TOPICS:
        topic_articles[topic_key] = [l for l in learnings if topic_key in l["topics"]]
    
    return {
        "topics": TOPICS,
        "links": topic_links,
        "articles": topic_articles,
    }


# 路由
@app.route("/")
def index():
    """儀表板首頁"""
    stats = get_stats()
    
    # 進度條
    progress_bars = ""
    for topic_key, count in stats["topic_counts"].items():
        topic_info = TOPICS[topic_key]
        pct = min(100, count * 10)  # 每10篇算100%
        progress_bars += f"""
        <div class="stat-card">
            <div class="topic-icon">{topic_info['icon']}</div>
            <div class="topic-name">{topic_info['name']}</div>
            <div class="topic-count">{count} 篇學習</div>
            <div class="topic-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pct}%"></div>
                </div>
            </div>
        </div>
        """
    
    # 最近學習時間線
    timeline = ""
    for l in stats["recent"]:
        tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' 
                       for t in l["topics"][:3]])
        timeline += f"""
        <div class="timeline-item fade-in">
            <div class="timeline-date">{l['date']}</div>
            <div class="timeline-title">{l['title'][:50]}</div>
            <div class="timeline-tags">{tags}</div>
        </div>
        """
    
    content = f"""
    <!-- 搜尋框 -->
    <div class="search-container">
        <span class="search-icon">🔍</span>
        <input type="text" class="search-input" placeholder="搜尋學習筆記..." 
               onkeyup="if(event.key==='Enter')handleSearch(this.value)">
    </div>
    
    <!-- 統計儀表板 -->
    <div class="stats-dashboard">
        <div class="stat-card">
            <div class="stat-icon">📚</div>
            <div class="stat-value">{stats['total_sessions']}</div>
            <div class="stat-label">學習回合</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🎯</div>
            <div class="stat-value">{stats['total_topics']}</div>
            <div class="stat-label">涵蓋主題</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🔥</div>
            <div class="stat-value">{stats['days_streak']}</div>
            <div class="stat-label">連續天數</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">📈</div>
            <div class="stat-value">{int(stats['total_sessions']/max(1, stats['days_streak']))}</div>
            <div class="stat-label">平均每天</div>
        </div>
    </div>
    
    <!-- 主題進度 -->
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>📖</span> 學習進度</div>
        </div>
        <div class="topic-grid">
            {progress_bars}
        </div>
    </div>
    
    <!-- 最近學習 -->
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>🕐</span> 最近學習</div>
            <a href="/timeline" class="action-btn">查看全部 →</a>
        </div>
        <div class="timeline">
            {timeline}
        </div>
    </div>
    
    <!-- 快捷入口 -->
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>⚡</span> 快捷入口</div>
        </div>
        <div class="quick-actions">
            <a href="/knowledge" class="action-btn">📚 知識庫</a>
            <a href="/graph" class="action-btn">🔗 知識圖譜</a>
            <a href="/topic/technical" class="action-btn">📊 技術分析</a>
            <a href="/topic/strategy" class="action-btn">🎯 操作策略</a>
        </div>
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title="儀表板",
        page="index",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/knowledge")
def knowledge():
    """知識庫"""
    knowledge_file = MEMORY_DIR / "stock-knowledge.md"
    
    if not knowledge_file.exists():
        content = "<div class='content-card'><h2>知識庫尚未建立</h2></div>"
    else:
        with open(knowledge_file, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'toc'])
        
        # 添加 TOC
        toc_html = "<div class='content-card'><h2>📑 目錄</h2><ul>"
        for line in md_content.split('\n'):
            if line.startswith('## '):
                title = line[3:].strip()
                toc_html += f"<li><a href='#section-{title}'>{title}</a></li>"
        toc_html += "</ul></div>"
        
        content = f"""
        <div class="section">
            <div class="section-header">
                <div class="section-title"><span>📚</span> 知識庫</div>
            </div>
            {toc_html}
            <div class="content-card">
                {html_content}
            </div>
        </div>
        """
    
    stats = get_stats()
    return render_template_string(
        BASE_TEMPLATE,
        title="知識庫",
        page="knowledge",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/timeline")
def timeline():
    """時間線視圖"""
    learnings = get_all_learning()
    stats = get_stats()
    
    # 按日期分組
    by_date = {}
    for l in learnings:
        date = l["date"] or "未知日期"
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(l)
    
    timeline_html = ""
    for date in sorted(by_date.keys(), reverse=True):
        items = by_date[date]
        items_html = ""
        for l in items:
            tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' 
                           for t in l["topics"][:3]])
            items_html += f"""
            <div class="timeline-item">
                <div class="timeline-title">{l['title'][:60]}</div>
                <div class="timeline-tags">{tags}</div>
                <p style="color: var(--text-muted); margin-top: 8px; font-size: 0.9rem;">{l['summary'][:150]}...</p>
                <a href="/history/{l['filename']}" class="action-btn" style="margin-top: 8px; padding: 6px 12px;">閱讀全文 →</a>
            </div>
            """
        
        # 星期幾
        weekday = ""
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
            weekdays = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
            weekday = weekdays[dt.weekday()]
        except:
            pass
        
        timeline_html += f"""
        <div class="section">
            <div class="section-header">
                <div class="section-title"><span>📅</span> {date} {weekday}</div>
            </div>
            {items_html}
        </div>
        """
    
    content = f"""
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>📅</span> 學習時間線</div>
            <span style="color: var(--text-muted);">共 {len(learnings)} 篇學習記錄</span>
        </div>
    </div>
    {timeline_html}
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title="時間線",
        page="timeline",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/graph")
def graph():
    """知識圖譜"""
    kg = get_knowledge_graph()
    stats = get_stats()
    
    # 主題卡片
    topic_cards = ""
    for topic_key, topic_info in TOPICS.items():
        articles = kg["articles"].get(topic_key, [])
        article_count = len(articles)
        
        # 最近的文章
        recent = ""
        for a in articles[:3]:
            recent += f"<li>{a['date']}: {a['title'][:30]}</li>"
        
        topic_cards += f"""
        <div class="knowledge-node">
            <h4>{topic_info['icon']} {topic_info['name']}</h4>
            <p style="color: var(--accent); font-weight: 600;">{article_count} 篇學習</p>
            <ul>{recent}</ul>
        </div>
        """
    
    content = f"""
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>🔗</span> 知識圖譜</div>
        </div>
        <div class="knowledge-graph">
            {topic_cards}
        </div>
    </div>
    
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>📊</span> 學習分佈</div>
        </div>
        <div class="content-card">
            <p>各主題學習次數：</p>
            <ul>
                {''.join([f'<li>{TOPICS[t]["icon"]} {TOPICS[t]["name"]}: {stats["topic_counts"][t]} 次</li>' for t in TOPICS])}
            </ul>
        </div>
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title="知識圖譜",
        page="graph",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/topic/<topic>")
def topic_page(topic):
    """主題頁面"""
    if topic not in TOPICS:
        return "主題不存在", 404
    
    learnings = get_all_learning()
    stats = get_stats()
    topic_info = TOPICS[topic]
    
    # 過濾相關文章
    related = [l for l in learnings if topic in l["topics"]]
    
    timeline = ""
    for l in related[:20]:
        tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' 
                       for t in l["topics"]])
        timeline += f"""
        <div class="timeline-item">
            <div class="timeline-date">{l['date']}</div>
            <div class="timeline-title">{l['title'][:50]}</div>
            <div class="timeline-tags">{tags}</div>
            <a href="/history/{l['filename']}" class="action-btn" style="margin-top: 8px; padding: 6px 12px;">閱讀 →</a>
        </div>
        """
    
    content = f"""
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>{topic_info['icon']}</span> {topic_info['name']}</div>
            <span style="color: var(--text-muted);">{len(related)} 篇相關學習</span>
        </div>
    </div>
    
    <div class="section">
        <div class="timeline">
            {timeline}
        </div>
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title=f"{topic_info['name']} - 學習記錄",
        page="index",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/history/<filename>")
def history_detail(filename):
    """學習詳情"""
    md_file = LEARNING_DIR / f"{filename}.md"
    
    if not md_file.exists():
        return "找不到此記錄", 404
    
    data = parse_learning_file(md_file)
    stats = get_stats()
    
    html_content = markdown.markdown(data["content"], extensions=['tables', 'fenced_code'])
    tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' 
                   for t in data["topics"]])
    
    # 上一篇/下一篇
    learnings = get_all_learning()
    prev_link = ""
    next_link = ""
    for i, l in enumerate(learnings):
        if l["filename"] == filename:
            if i > 0:
                prev_link = f'<a href="/history/{learnings[i-1]["filename"]}" class="action-btn">← 上一篇</a>'
            if i < len(learnings) - 1:
                next_link = f'<a href="/history/{learnings[i+1]["filename"]}" class="action-btn">下一篇 →</a>'
    
    content = f"""
    <div class="section">
        <div class="quick-actions">
            <a href="/timeline" class="action-btn">← 返回時間線</a>
            {prev_link}
            {next_link}
        </div>
    </div>
    
    <div class="content-card">
        <h1>{data['title']}</h1>
        <p class="meta" style="color: var(--text-muted); margin-bottom: 16px;">
            {data['date']} {tags}
        </p>
        {html_content}
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title=data['title'],
        page="history",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/search")
def search():
    """搜尋"""
    query = request.args.get("q", "").lower()
    learnings = get_all_learning()
    stats = get_stats()
    
    if query:
        results = [l for l in learnings 
                   if query in l["title"].lower() or query in l["content"].lower()]
    else:
        results = []
    
    result_html = ""
    for l in results[:20]:
        tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]}</span>' for t in l["topics"][:3]])
        result_html += f"""
        <div class="timeline-item">
            <div class="timeline-date">{l['date']}</div>
            <div class="timeline-title">{l['title'][:50]}</div>
            <div class="timeline-tags">{tags}</div>
            <a href="/history/{l['filename']}" class="action-btn" style="margin-top: 8px; padding: 6px 12px;">閱讀 →</a>
        </div>
        """
    
    if not results and query:
        result_html = f"<p style='color: var(--text-muted);'>找不到與「{query}」相關的內容</p>"
    
    content = f"""
    <div class="section">
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" class="search-input" placeholder="搜尋學習筆記..." 
                   value="{query}" onkeyup="if(event.key==='Enter')handleSearch(this.value)">
        </div>
    </div>
    
    <div class="section">
        <div class="section-header">
            <div class="section-title"><span>🔍</span> 搜尋結果</div>
            <span style="color: var(--text-muted);">找到 {len(results)} 筆結果</span>
        </div>
        <div class="timeline">
            {result_html}
        </div>
    </div>
    """
    
    return render_template_string(
        BASE_TEMPLATE,
        title=f"搜尋: {query}" if query else "搜尋",
        page="index",
        content=content,
        stats=stats,
        last_update=datetime.now().strftime("%Y-%m-%d %H:%M")
    )


@app.route("/static/style.css")
def style():
    return open(BASE_DIR / "style-new.css").read(), 200, {'Content-Type': 'text/css'}


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    
    print(f"🚀 啟動股票學習筆記網站...")
    print(f"📊 統計: {len(get_all_learning())} 篇學習記錄")
    print(f"🌐 網址: http://localhost:{args.port}")
    print(f"")
    print(f"按 Ctrl+C 停止")
    
    app.run(host="0.0.0.0", port=args.port, debug=False)