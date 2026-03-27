#!/usr/bin/env python3
"""
股票學習筆記 - 靜態網站生成器（增強版）

功能：
- 美觀現代的 UI
- 完整的 Markdown 渲染（表格、代碼塊等）
- 響應式設計
- 搜尋功能
- 主題分類
"""

import os
import re
import json
from datetime import datetime, timedelta
from pathlib import Path
import html

# 路徑配置
BASE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"
OUTPUT_DIR = BASE_DIR / "docs"

# 主題對應
TOPICS = {
    "technical": {"name": "技術分析", "icon": "📊", "color": "#6366f1", "keywords": ["K線", "均線", "支撐", "壓力", "技術", "RSI", "MACD", "KD", "技術面"]},
    "fundamental": {"name": "基本面分析", "icon": "💰", "color": "#22c55e", "keywords": ["財報", "營收", "EPS", "本益比", "基本面", "估值", "ROE", "毛利率"]},
    "chips": {"name": "籌碼面分析", "icon": "🎲", "color": "#f97316", "keywords": ["法人", "主力", "融資", "融券", "籌碼", "外資", "投信", "自營商"]},
    "strategy": {"name": "操作策略", "icon": "🎯", "color": "#ec4899", "keywords": ["當沖", "波段", "價值投資", "策略", "停損", "停利", "操作", "交易"]},
    "risk": {"name": "風險管理", "icon": "⚠️", "color": "#ef4444", "keywords": ["風險", "倉位", "部位", "MDD", "回撤", "停損", "資金"]},
    "psychology": {"name": "交易心理", "icon": "🧠", "color": "#a855f7", "keywords": ["心理", "心態", "情緒", "紀律", "貪婪", "恐懼"]}
}

# 現代化 CSS
CSS = """
:root {
    --bg: #0f0f0f;
    --bg-secondary: #1a1a1f;
    --bg-tertiary: #252530;
    --card: #1e1e28;
    --card-hover: #282836;
    --text: #f0f0f5;
    --text-secondary: #a0a0b0;
    --text-muted: #707080;
    --border: #2a2a3a;
    --accent: #8b5cf6;
    --accent-light: #a78bfa;
    --gradient-1: linear-gradient(135deg, #8b5cf6 0%, #6366f1 50%, #3b82f6 100%);
    --gradient-card: linear-gradient(145deg, #1e1e28 0%, #252535 100%);
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    --radius: 12px;
    --radius-lg: 20px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    min-height: 100vh;
}

/* Container */
.container { max-width: 1200px; margin: 0 auto; padding: 24px; }

/* Header */
header {
    background: linear-gradient(180deg, var(--bg-secondary) 0%, transparent 100%);
    border-bottom: 1px solid var(--border);
    padding: 16px 0;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(20px);
}

.header-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}

.logo-icon {
    width: 40px;
    height: 40px;
    background: var(--gradient-1);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.logo-text {
    font-size: 1.25rem;
    font-weight: 700;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

nav {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

nav a {
    color: var(--text-secondary);
    text-decoration: none;
    padding: 10px 16px;
    border-radius: var(--radius);
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s;
}

nav a:hover {
    color: var(--text);
    background: var(--card);
}

nav a.active {
    color: var(--accent-light);
    background: rgba(139, 92, 246, 0.1);
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 32px 0;
}

.stat-card {
    background: var(--gradient-card);
    border-radius: var(--radius-lg);
    padding: 24px;
    border: 1px solid var(--border);
    transition: transform 0.3s, box-shadow 0.3s;
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow);
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 800;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stat-label {
    color: var(--text-muted);
    font-size: 0.9rem;
    margin-top: 4px;
}

.stat-icon {
    font-size: 1.5rem;
    margin-bottom: 8px;
}

/* Progress Section */
.progress-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin: 32px 0;
}

.progress-card {
    background: var(--card);
    border-radius: var(--radius);
    padding: 20px;
    border: 1px solid var(--border);
}

.progress-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}

.progress-icon {
    font-size: 1.5rem;
}

.progress-title {
    font-weight: 600;
}

.progress-count {
    color: var(--text-muted);
    font-size: 0.85rem;
}

.progress-bar-bg {
    height: 8px;
    background: var(--bg-tertiary);
    border-radius: 4px;
    overflow: hidden;
}

.progress-bar-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.5s ease;
}

/* Topic Cards */
.topic-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 24px 0;
}

.topic-card {
    background: var(--gradient-card);
    border-radius: var(--radius);
    padding: 20px;
    text-decoration: none;
    color: var(--text);
    border: 1px solid var(--border);
    transition: all 0.3s;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.topic-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: var(--shadow);
}

.topic-icon {
    font-size: 2rem;
    margin-bottom: 8px;
}

.topic-name {
    font-weight: 600;
    margin-bottom: 4px;
}

.topic-count {
    color: var(--text-muted);
    font-size: 0.85rem;
}

/* Timeline */
.timeline {
    position: relative;
    margin: 24px 0;
    padding-left: 28px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 8px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, var(--accent) 0%, var(--border) 100%);
}

.timeline-item {
    position: relative;
    background: var(--card);
    border-radius: var(--radius);
    padding: 20px;
    margin-bottom: 16px;
    border: 1px solid var(--border);
    transition: all 0.3s;
    text-decoration: none;
    color: var(--text);
    display: block;
}

.timeline-item:hover {
    border-color: var(--accent);
    transform: translateX(4px);
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -24px;
    top: 24px;
    width: 12px;
    height: 12px;
    background: var(--accent);
    border-radius: 50%;
    border: 3px solid var(--bg);
}

.timeline-date {
    color: var(--text-muted);
    font-size: 0.85rem;
    margin-bottom: 6px;
}

.timeline-title {
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 8px;
}

.timeline-excerpt {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-bottom: 12px;
}

/* Tags */
.tags {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
}

.tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
}

.tag.technical { background: rgba(99, 102, 241, 0.15); color: #a5b4fc; }
.tag.fundamental { background: rgba(34, 197, 94, 0.15); color: #86efac; }
.tag.chips { background: rgba(249, 115, 22, 0.15); color: #fdba74; }
.tag.strategy { background: rgba(236, 72, 153, 0.15); color: #f9a8d4; }
.tag.risk { background: rgba(239, 68, 68, 0.15); color: #fca5a5; }
.tag.psychology { background: rgba(168, 85, 247, 0.15); color: #d8b4fe; }

/* Content Card */
.content-card {
    background: var(--card);
    border-radius: var(--radius-lg);
    padding: 32px;
    border: 1px solid var(--border);
    margin: 24px 0;
}

.content-card h1 {
    font-size: 2rem;
    margin-bottom: 16px;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.content-card h2 {
    font-size: 1.5rem;
    color: var(--accent-light);
    margin: 32px 0 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}

.content-card h3 {
    font-size: 1.2rem;
    color: var(--text);
    margin: 24px 0 12px;
}

.content-card h4 {
    font-size: 1rem;
    color: var(--text-secondary);
    margin: 20px 0 8px;
}

.content-card p {
    color: var(--text-secondary);
    margin-bottom: 16px;
    line-height: 1.8;
}

.content-card ul, .content-card ol {
    margin: 0 0 16px 24px;
    color: var(--text-secondary);
}

.content-card li {
    margin-bottom: 8px;
}

/* Markdown Tables */
.content-card table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 0.95rem;
}

.content-card th, .content-card td {
    padding: 12px 16px;
    text-align: left;
    border: 1px solid var(--border);
}

.content-card th {
    background: var(--bg-tertiary);
    font-weight: 600;
    color: var(--text);
}

.content-card td {
    color: var(--text-secondary);
}

.content-card tr:hover td {
    background: var(--bg-secondary);
}

/* Code Blocks */
.content-card code {
    background: var(--bg-tertiary);
    padding: 3px 8px;
    border-radius: 4px;
    font-family: 'Fira Code', 'JetBrains Mono', monospace;
    font-size: 0.9em;
    color: var(--accent-light);
}

.content-card pre {
    background: var(--bg-tertiary);
    padding: 20px;
    border-radius: var(--radius);
    overflow-x: auto;
    margin: 16px 0;
}

.content-card pre code {
    background: none;
    padding: 0;
}

/* Blockquotes */
.content-card blockquote {
    border-left: 4px solid var(--accent);
    padding-left: 20px;
    margin: 16px 0;
    color: var(--text-secondary);
    font-style: italic;
}

/* Search */
.search-container {
    position: relative;
    margin: 24px 0;
}

.search-input {
    width: 100%;
    padding: 16px 20px 16px 48px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    font-size: 1rem;
    transition: all 0.2s;
}

.search-input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}

.search-icon {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.2rem;
}

/* Section Headers */
.section {
    margin: 40px 0;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Navigation Links */
.nav-links {
    display: flex;
    gap: 12px;
    margin: 24px 0;
    flex-wrap: wrap;
}

.nav-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 16px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    text-decoration: none;
    transition: all 0.2s;
}

.nav-link:hover {
    background: var(--accent);
    border-color: var(--accent);
}

/* Footer */
footer {
    margin-top: 60px;
    padding: 32px;
    background: var(--bg-secondary);
    border-top: 1px solid var(--border);
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
}

.footer-stats {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.footer-stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent);
}

.footer-stat-label {
    color: var(--text-muted);
    font-size: 0.85rem;
}

.footer-text {
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* Breadcrumb */
.breadcrumb {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 24px;
    color: var(--text-muted);
    font-size: 0.9rem;
}

.breadcrumb a {
    color: var(--text-secondary);
    text-decoration: none;
}

.breadcrumb a:hover {
    color: var(--accent-light);
}

/* Responsive */
@media (max-width: 768px) {
    .header-inner {
        flex-direction: column;
        gap: 16px;
    }
    
    nav {
        width: 100%;
        justify-content: center;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .container {
        padding: 16px;
    }
    
    .content-card {
        padding: 20px;
    }
    
    .content-card table {
        font-size: 0.85rem;
    }
    
    .content-card th, .content-card td {
        padding: 8px 12px;
    }
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeInUp 0.4s ease-out;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg);
}

::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}
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


def parse_markdown_file(filepath: Path) -> dict:
    """解析 Markdown 檔案"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return None
    
    # 提取日期
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else ""
    
    # 提取標題（第一個 # 標題）
    title_match = re.search(r"^#+\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    
    # 偵測主題
    topics = detect_topics(content)
    
    # 提取摘要
    summary = ""
    # 嘗試找第一個段落
    paras = re.split(r"\n\n+", content)
    for para in paras[1:4]:  # 跳過標題，取前幾段
        if para and not para.startswith("#"):
            summary = para[:200].replace("\n", " ").strip()
            break
    
    return {
        "date": date,
        "title": title,
        "content": content,
        "topics": topics,
        "summary": summary,
        "filename": filepath.stem,
    }


def markdown_to_html(content: str) -> str:
    """將 Markdown 轉換為 HTML（支援表格、代碼塊等）"""
    # 代碼塊
    content = re.sub(r"```(\w*)\n(.*?)\n```", r"<pre><code class=\"\1\">\2</code></pre>", content, flags=re.DOTALL)
    
    # 行內代碼
    content = re.sub(r"`([^`]+)`", r"<code>\1</code>", content)
    
    # 標題
    content = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", content, flags=re.MULTILINE)
    content = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", content, flags=re.MULTILINE)
    content = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", content, flags=re.MULTILINE)
    content = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", content, flags=re.MULTILINE)
    
    # 粗體和斜體
    content = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", content)
    content = re.sub(r"\*(.+?)\*", r"<em>\1</em>", content)
    
    # 引用
    content = re.sub(r"^>\s+(.+)$", r"<blockquote>\1</blockquote>", content, flags=re.MULTILINE)
    
    # 列表
    content = re.sub(r"^\*\s+(.+)$", r"<li>\1</li>", content, flags=re.MULTILINE)
    content = re.sub(r"(<li>.*</li>\n?)+", lambda m: f"<ul>{m.group(0)}</ul>", content)
    content = re.sub(r"^\d+\.\s+(.+)$", r"<li>\1</li>", content, flags=re.MULTILINE)
    
    # 表格
    def convert_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)
        
        # 解析表頭
        headers = [cell.strip() for cell in lines[0].split("|") if cell.strip()]
        
        # 解析分隔行（跳過）
        # 解析內容行
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split("|") if cell.strip()]
            if cells:
                rows.append(cells)
        
        html = "<table>\n<thead>\n<tr>\n"
        for h in headers:
            html += f"<th>{h}</th>\n"
        html += "</tr>\n</thead>\n<tbody>\n"
        for row in rows:
            html += "<tr>\n"
            for cell in row:
                html += f"<td>{cell}</td>\n"
            html += "</tr>\n"
        html += "</tbody>\n</table>"
        return html
    
    # 表格正則
    content = re.sub(r"(\|.+\|\n)+(\|[-:]+\|\n)(\|.+\|\n?)+", convert_table, content)
    
    # 段落
    paragraphs = content.split("\n\n")
    result = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith(("<h", "<ul", "<ol", "<table", "<pre", "<blockquote")):
            p = f"<p>{p}</p>"
        result.append(p)
    
    return "\n\n".join(result)


def get_all_learning() -> list:
    """取得所有學習記錄"""
    files = []
    if LEARNING_DIR.exists():
        for f in sorted(LEARNING_DIR.glob("*.md"), reverse=True):
            data = parse_markdown_file(f)
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
        "total": len(learnings),
        "topics": len(TOPICS),
        "topic_counts": topic_counts,
        "streak": streak,
    }


def generate_index(learnings: list, stats: dict) -> str:
    """生成首頁"""
    # 進度卡片
    progress_cards = ""
    for topic_key, count in sorted(stats["topic_counts"].items(), key=lambda x: -x[1]):
        topic = TOPICS[topic_key]
        pct = min(100, count * 10)
        progress_cards += f"""
        <div class="progress-card">
            <div class="progress-header">
                <span class="progress-icon">{topic['icon']}</span>
                <div>
                    <div class="progress-title">{topic['name']}</div>
                    <div class="progress-count">{count} 篇學習</div>
                </div>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: {pct}%; background: {topic['color']}"></div>
            </div>
        </div>
        """
    
    # 最近學習
    timeline_html = ""
    for l in learnings[:8]:
        tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in l["topics"][:3]])
        timeline_html += f"""
        <a href="history/{l['filename']}.html" class="timeline-item fade-in">
            <div class="timeline-date">{l['date']}</div>
            <div class="timeline-title">{html.escape(l['title'][:50])}</div>
            <div class="timeline-excerpt">{html.escape(l['summary'][:100])}...</div>
            <div class="tags">{tags}</div>
        </a>
        """
    
    # 主題卡片
    topic_cards = ""
    for topic_key, topic in TOPICS.items():
        count = stats["topic_counts"].get(topic_key, 0)
        topic_cards += f"""
        <a href="topic/{topic_key}.html" class="topic-card">
            <span class="topic-icon">{topic['icon']}</span>
            <div class="topic-name">{topic['name']}</div>
            <div class="topic-count">{count} 篇</div>
        </a>
        """
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>股票學習筆記</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">📈</div>
                <span class="logo-text">股票學習筆記</span>
            </a>
            <nav>
                <a href="index.html" class="active">儀表板</a>
                <a href="knowledge.html">知識庫</a>
                <a href="timeline.html">時間線</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <!-- 統計儀表板 -->
        <div class="stats-grid">
            <div class="stat-card fade-in">
                <div class="stat-icon">📚</div>
                <div class="stat-value">{stats['total']}</div>
                <div class="stat-label">學習回合</div>
            </div>
            <div class="stat-card fade-in">
                <div class="stat-icon">🎯</div>
                <div class="stat-value">{stats['topics']}</div>
                <div class="stat-label">涵蓋主題</div>
            </div>
            <div class="stat-card fade-in">
                <div class="stat-icon">🔥</div>
                <div class="stat-value">{stats['streak']}</div>
                <div class="stat-label">連續天數</div>
            </div>
            <div class="stat-card fade-in">
                <div class="stat-icon">📊</div>
                <div class="stat-value">{stats['total'] // max(1, stats['streak'])}</div>
                <div class="stat-label">平均每天</div>
            </div>
        </div>
        
        <!-- 學習進度 -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">📊 學習進度</h2>
            </div>
            <div class="progress-section">
                {progress_cards}
            </div>
        </div>
        
        <!-- 主題分類 -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">📖 主題分類</h2>
            </div>
            <div class="topic-grid">
                {topic_cards}
            </div>
        </div>
        
        <!-- 最近學習 -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">🕐 最近學習</h2>
                <a href="timeline.html" class="nav-link">查看全部 →</a>
            </div>
            <div class="timeline">
                {timeline_html}
            </div>
        </div>
    </div>
    
    <footer>
        <div class="footer-content">
            <div class="footer-stats">
                <div class="footer-stat">
                    <div class="footer-stat-value">{stats['total']}</div>
                    <div class="footer-stat-label">學習回合</div>
                </div>
                <div class="footer-stat">
                    <div class="footer-stat-value">{stats['topics']}</div>
                    <div class="footer-stat-label">涵蓋主題</div>
                </div>
                <div class="footer-stat">
                    <div class="footer-stat-value">{stats['streak']}</div>
                    <div class="footer-stat-label">連續天數</div>
                </div>
            </div>
            <p class="footer-text">由妖姬西打龍 🐍 自動生成</p>
            <p class="footer-text">最後更新：{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </div>
    </footer>
</body>
</html>"""


def generate_knowledge() -> str:
    """生成知識庫頁面"""
    knowledge_file = MEMORY_DIR / "stock-knowledge.md"
    
    if not knowledge_file.exists():
        html_content = "<div class='content-card'><h1>知識庫尚未建立</h1></div>"
    else:
        with open(knowledge_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        html_content = markdown_to_html(content)
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>知識庫 - 股票學習筆記</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">📈</div>
                <span class="logo-text">股票學習筆記</span>
            </a>
            <nav>
                <a href="index.html">儀表板</a>
                <a href="knowledge.html" class="active">知識庫</a>
                <a href="timeline.html">時間線</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="breadcrumb">
            <a href="index.html">首頁</a>
            <span>›</span>
            <span>知識庫</span>
        </div>
        
        <div class="content-card">
            <h1>📚 知識庫</h1>
            {html_content}
        </div>
    </div>
    
    <footer>
        <div class="footer-content">
            <p class="footer-text">由妖姬西打龍 🐍 自動生成</p>
        </div>
    </footer>
</body>
</html>"""


def generate_timeline(learnings: list) -> str:
    """生成時間線頁面"""
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
        
        # 計算星期
        weekday = ""
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
            weekdays = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
            weekday = weekdays[dt.weekday()]
        except:
            pass
        
        items_html = ""
        for l in items:
            tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in l["topics"][:3]])
            items_html += f"""
            <a href="history/{l['filename']}.html" class="timeline-item">
                <div class="timeline-title">{html.escape(l['title'][:60])}</div>
                <p class="timeline-excerpt">{html.escape(l['summary'][:150])}...</p>
                <div class="tags">{tags}</div>
            </a>
            """
        
        timeline_html += f"""
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">📅 {date} {weekday}</h2>
                <span style="color: var(--text-muted)">{len(items)} 篇</span>
            </div>
            {items_html}
        </div>
        """
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>時間線 - 股票學習筆記</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">📈</div>
                <span class="logo-text">股票學習筆記</span>
            </a>
            <nav>
                <a href="index.html">儀表板</a>
                <a href="knowledge.html">知識庫</a>
                <a href="timeline.html" class="active">時間線</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="breadcrumb">
            <a href="index.html">首頁</a>
            <span>›</span>
            <span>時間線</span>
        </div>
        
        <div class="content-card">
            <h1>📅 學習時間線</h1>
            <p style="color: var(--text-secondary)">共 {len(learnings)} 篇學習記錄</p>
        </div>
        
        {timeline_html}
    </div>
    
    <footer>
        <div class="footer-content">
            <p class="footer-text">由妖姬西打龍 🐍 自動生成</p>
        </div>
    </footer>
</body>
</html>"""


def generate_topic_page(topic_key: str, learnings: list) -> str:
    """生成主題頁面"""
    topic = TOPICS[topic_key]
    related = [l for l in learnings if topic_key in l["topics"]]
    
    timeline_html = ""
    for l in related[:20]:
        tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]}</span>' for t in l["topics"]])
        timeline_html += f"""
        <a href="../history/{l['filename']}.html" class="timeline-item">
            <div class="timeline-date">{l['date']}</div>
            <div class="timeline-title">{html.escape(l['title'][:50])}</div>
            <div class="tags">{tags}</div>
        </a>
        """
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic['name']} - 股票學習筆記</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="../index.html" class="logo">
                <div class="logo-icon">📈</div>
                <span class="logo-text">股票學習筆記</span>
            </a>
            <nav>
                <a href="../index.html">儀表板</a>
                <a href="../knowledge.html">知識庫</a>
                <a href="../timeline.html">時間線</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="breadcrumb">
            <a href="../index.html">首頁</a>
            <span>›</span>
            <span>{topic['name']}</span>
        </div>
        
        <div class="content-card">
            <h1>{topic['icon']} {topic['name']}</h1>
            <p style="color: var(--text-secondary)">{len(related)} 篇相關學習</p>
        </div>
        
        <div class="timeline">
            {timeline_html}
        </div>
    </div>
    
    <footer>
        <div class="footer-content">
            <p class="footer-text">由妖姬西打龍 🐍 自動生成</p>
        </div>
    </footer>
</body>
</html>"""


def generate_history_page(l: dict, all_learnings: list) -> str:
    """生成學習詳情頁面"""
    html_content = markdown_to_html(l["content"])
    tags = "".join([f'<span class="tag {t}">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in l["topics"]])
    
    # 找上一篇/下一篇
    prev_link = ""
    next_link = ""
    for i, item in enumerate(all_learnings):
        if item["filename"] == l["filename"]:
            if i > 0:
                prev_link = f'<a href="{all_learnings[i-1]["filename"]}.html" class="nav-link">← 上一篇</a>'
            if i < len(all_learnings) - 1:
                next_link = f'<a href="{all_learnings[i+1]["filename"]}.html" class="nav-link">下一篇 →</a>'
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(l['title'])} - 股票學習筆記</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="../index.html" class="logo">
                <div class="logo-icon">📈</div>
                <span class="logo-text">股票學習筆記</span>
            </a>
            <nav>
                <a href="../index.html">儀表板</a>
                <a href="../knowledge.html">知識庫</a>
                <a href="../timeline.html">時間線</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="breadcrumb">
            <a href="../index.html">首頁</a>
            <span>›</span>
            <a href="../timeline.html">時間線</a>
            <span>›</span>
            <span>{l['date']}</span>
        </div>
        
        <div class="nav-links">
            <a href="../timeline.html" class="nav-link">← 返回時間線</a>
            {prev_link}
            {next_link}
        </div>
        
        <div class="content-card">
            <h1>{html.escape(l['title'])}</h1>
            <p style="color: var(--text-muted); margin-bottom: 24px;">
                {l['date']} · {tags}
            </p>
            {html_content}
        </div>
    </div>
    
    <footer>
        <div class="footer-content">
            <p class="footer-text">由妖姬西打龍 🐍 自動生成</p>
        </div>
    </footer>
</body>
</html>"""


def main():
    """主程式"""
    print("生成網站...")
    
    # 清理並建立輸出目錄
    if OUTPUT_DIR.exists():
        import shutil
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    # 建立子目錄
    (OUTPUT_DIR / "history").mkdir(exist_ok=True)
    (OUTPUT_DIR / "topic").mkdir(exist_ok=True)
    
    # 取得所有學習記錄
    learnings = get_all_learning()
    stats = get_stats()
    
    print(f"  學習記錄: {len(learnings)} 篇")
    print(f"  涵蓋主題: {stats['topics']} 個")
    
    # 複製 CSS
    css_path = BASE_DIR / "style-new.css"
    if css_path.exists():
        import shutil
        shutil.copy(css_path, OUTPUT_DIR / "style.css")
    else:
        # 使用內建的 CSS
        with open(OUTPUT_DIR / "style.css", "w", encoding="utf-8") as f:
            f.write(CSS)
    
    # 生成首頁
    with open(OUTPUT_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_index(learnings, stats))
    print("  ✓ index.html")
    
    # 生成知識庫
    with open(OUTPUT_DIR / "knowledge.html", "w", encoding="utf-8") as f:
        f.write(generate_knowledge())
    print("  ✓ knowledge.html")
    
    # 生成時間線
    with open(OUTPUT_DIR / "timeline.html", "w", encoding="utf-8") as f:
        f.write(generate_timeline(learnings))
    print("  ✓ timeline.html")
    
    # 生成主題頁面
    for topic_key in TOPICS:
        with open(OUTPUT_DIR / "topic" / f"{topic_key}.html", "w", encoding="utf-8") as f:
            f.write(generate_topic_page(topic_key, learnings))
    print(f"  ✓ {len(TOPICS)} 主題頁面")
    
    # 生成學習詳情頁面
    for l in learnings:
        with open(OUTPUT_DIR / "history" / f"{l['filename']}.html", "w", encoding="utf-8") as f:
            f.write(generate_history_page(l, learnings))
    print(f"  ✓ {len(learnings)} 學習頁面")
    
    print(f"\n✅ 網站已生成到 {OUTPUT_DIR}")
    print(f"   最後更新：{datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()