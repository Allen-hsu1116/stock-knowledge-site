#!/usr/bin/env python3
"""
股票學習筆記 - 網站生成器
從 memory/stock-learning/*.md 生成靜態網站到 docs/

使用方式：
    python3 stock-knowledge-site-build.py

此腳本由每天的凌晨統整任務自動執行，
執行後會自動推送到 GitHub。
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# 路徑設定
WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"
REPO_DIR = WORKSPACE / "stock-knowledge-site"
OUTPUT_DIR = REPO_DIR / "docs"

TOPICS = {
    "technical": {"name": "技術分析", "icon": "📊", "desc": "K線、均線、技術指標"},
    "fundamental": {"name": "基本面分析", "icon": "💰", "desc": "財報、估值、產業分析"},
    "chips": {"name": "籌碼面分析", "icon": "🎲", "desc": "三大法人、主力動向"},
    "strategy": {"name": "操作策略", "icon": "🎯", "desc": "當沖、波段、價值投資"},
    "risk": {"name": "風險管理", "icon": "⚠️", "desc": "停損停利、倉位控制"},
    "psychology": {"name": "交易心理", "icon": "🧠", "desc": "心態建設、認知偏誤"}
}

CSS = '''
:root {
    --primary: #6366f1; --primary-light: #818cf8; --primary-dark: #4f46e5;
    --bg: #ffffff; --bg-secondary: #f9fafb; --bg-tertiary: #f3f4f6;
    --text: #111827; --text-secondary: #4b5563; --text-muted: #9ca3af;
    --border: #e5e7eb; --shadow: 0 1px 3px rgba(0,0,0,0.1);
    --success: #10b981; --warning: #f59e0b; --danger: #ef4444;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; }
.container { max-width: 1200px; margin: 0 auto; }

header { position: sticky; top: 0; background: var(--bg); border-bottom: 1px solid var(--border); z-index: 100; }
.header-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; max-width: 1200px; margin: 0 auto; }
.logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
.logo-icon { width: 36px; height: 36px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; }
.logo-text { font-size: 18px; font-weight: 600; color: var(--text); }
nav { display: flex; gap: 8px; }
nav a { padding: 8px 16px; border-radius: 8px; color: var(--text-secondary); text-decoration: none; font-size: 14px; font-weight: 500; transition: all 0.2s; }
nav a:hover { background: var(--bg-tertiary); color: var(--text); }
nav a.active { background: var(--primary); color: white; }

main { padding: 40px 24px; }

.hero { text-align: center; padding: 60px 0 40px; }
.hero-title { font-size: 48px; font-weight: 700; margin-bottom: 16px; background: linear-gradient(135deg, var(--text), var(--text-secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-subtitle { font-size: 18px; color: var(--text-muted); }

.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 48px; }
.stat-card { background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-align: center; transition: all 0.2s; }
.stat-card:hover { border-color: var(--primary); transform: translateY(-2px); }
.stat-value { font-size: 32px; font-weight: 700; color: var(--primary); }
.stat-label { font-size: 14px; color: var(--text-muted); margin-top: 8px; }

.topic-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 48px; }
.topic-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-decoration: none; color: var(--text); transition: all 0.2s; }
.topic-card:hover { border-color: var(--primary); box-shadow: var(--shadow); transform: translateY(-2px); }
.topic-icon { width: 48px; height: 48px; background: var(--bg-tertiary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px; }
.topic-name { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
.topic-desc { font-size: 14px; color: var(--text-secondary); }
.topic-count { font-size: 12px; color: var(--text-muted); margin-top: 12px; }

.section { margin-bottom: 48px; }
.section-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; }
.section-title { font-size: 24px; font-weight: 600; }
.section-link { color: var(--primary); text-decoration: none; font-size: 14px; }

.date-group { margin-bottom: 32px; }
.date-header { font-size: 18px; font-weight: 600; color: var(--text); margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid var(--primary); }
.date-header .date { color: var(--primary); }
.date-header .weekday { color: var(--text-muted); font-size: 14px; margin-left: 8px; }

.session-list { display: flex; flex-direction: column; gap: 12px; margin-bottom: 16px; }
.session-item { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 16px 20px; text-decoration: none; color: var(--text); transition: all 0.2s; display: flex; flex-direction: column; gap: 8px; }
.session-item:hover { border-color: var(--primary); }
.session-time { font-size: 12px; color: var(--text-muted); }
.session-title { font-size: 16px; font-weight: 600; }
.session-item:hover .session-title { color: var(--primary); }
.session-excerpt { font-size: 14px; color: var(--text-secondary); line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

.tags { display: flex; flex-wrap: wrap; gap: 6px; }
.tag { display: inline-flex; align-items: center; gap: 4px; padding: 2px 10px; background: var(--bg-tertiary); border-radius: 12px; font-size: 12px; color: var(--text-secondary); }

.summary-card { background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 12px; padding: 20px; margin-top: 16px; }
.summary-card a { color: white; text-decoration: none; display: block; }
.summary-card:hover { opacity: 0.95; }
.summary-title { font-size: 14px; opacity: 0.9; }
.summary-link { font-size: 16px; font-weight: 600; margin-top: 4px; }

.content { background: var(--bg); max-width: 900px; margin: 0 auto; }
.content-card { background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 16px; padding: 40px; margin-bottom: 24px; }
.content h1 { font-size: 32px; font-weight: 700; margin-bottom: 24px; }
.content h2 { font-size: 24px; font-weight: 600; margin: 32px 0 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border); }
.content h3 { font-size: 20px; font-weight: 600; margin: 24px 0 12px; }
.content h4 { font-size: 16px; font-weight: 600; margin: 20px 0 8px; color: var(--text-secondary); }
.content p { margin-bottom: 16px; color: var(--text-secondary); }
.content ul, .content ol { margin: 0 0 16px 24px; color: var(--text-secondary); }
.content li { margin-bottom: 8px; }
.content a { color: var(--primary); text-decoration: none; }
.content a:hover { text-decoration: underline; }
.content code { background: var(--bg-tertiary); padding: 2px 8px; border-radius: 4px; font-family: monospace; font-size: 14px; }
.content pre { background: var(--bg-tertiary); border-radius: 8px; padding: 16px; overflow-x: auto; margin: 16px 0; }
.content pre code { background: none; padding: 0; }
.content blockquote { border-left: 4px solid var(--primary); padding-left: 16px; margin: 16px 0; color: var(--text-muted); }
.content table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }
.content th { background: var(--bg-tertiary); padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid var(--border); }
.content td { padding: 12px; border-bottom: 1px solid var(--border-light); color: var(--text-secondary); }
.content tr:hover td { background: var(--bg-secondary); }
.content .meta { font-size: 14px; color: var(--text-muted); margin-bottom: 16px; }

.knowledge-nav { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 32px; }
.knowledge-nav a { padding: 8px 16px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 20px; color: var(--text-secondary); text-decoration: none; font-size: 14px; transition: all 0.2s; }
.knowledge-nav a:hover { background: var(--primary); color: white; border-color: var(--primary); }

.breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 14px; color: var(--text-muted); margin-bottom: 24px; }
.breadcrumb a { color: var(--text-secondary); text-decoration: none; }
.breadcrumb a:hover { color: var(--primary); }

.nav-links { display: flex; gap: 12px; margin-bottom: 24px; }
.nav-link { display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; color: var(--text-secondary); text-decoration: none; font-size: 14px; transition: all 0.2s; }
.nav-link:hover { background: var(--bg-tertiary); color: var(--text); border-color: var(--primary); }

footer { background: var(--bg-secondary); border-top: 1px solid var(--border); padding: 32px; margin-top: 48px; text-align: center; }
.footer-text { font-size: 14px; color: var(--text-muted); }

@media (max-width: 900px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } .topic-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { .stats-grid { grid-template-columns: 1fr; } .topic-grid { grid-template-columns: 1fr; } .hero-title { font-size: 32px; } .content-card { padding: 24px; } }
'''

def detect_topics(content):
    keywords = {
        "technical": ["K線", "均線", "支撐", "壓力", "技術", "RSI", "MACD", "KD", "移動平均", "趨勢線"],
        "fundamental": ["財報", "營收", "EPS", "本益比", "基本面", "估值", "ROE", "殖利率", "股息"],
        "chips": ["法人", "主力", "融資", "籌碼", "外資", "投信", "自營商", "大戶"],
        "strategy": ["當沖", "波段", "價值投資", "策略", "停損", "停利", "選擇權", "加碼", "部位"],
        "risk": ["風險", "倉位", "部位控制", "MDD", "回撤", "凱利", "資金管理"],
        "psychology": ["心理", "心態", "情緒", "紀律", "偏誤", "行為", "FOMO", "貪婪", "恐懼"]
    }
    found = []
    for t, kws in keywords.items():
        for kw in kws:
            if kw in content and t not in found:
                found.append(t)
    return found

def md_to_html(text):
    """Convert Markdown to HTML with proper line breaks"""
    # Save code blocks
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f"\n__CODE{len(code_blocks)-1}__\n"
    text = re.sub(r"```[\s\S]*?```", save_code, text)
    
    # Tables
    def make_table(m):
        lines = m.group(0).strip().split('\n')
        if len(lines) < 2: return m.group(0)
        h = [c.strip() for c in lines[0].split('|') if c.strip()]
        rows = [[c.strip() for c in l.split('|') if c.strip()] for l in lines[2:] if l.strip()]
        return '<table><thead><tr>' + ''.join(f'<th>{x}</th>' for x in h) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows) + '</tbody></table>'
    text = re.sub(r"(\|.+\|\n)+(\|[-:| ]+\|\n)(\|.+\|[\s\S]*?)(?=\n\n|\n*$)", make_table, text)
    
    # Split into blocks
    lines = text.split('\n')
    blocks = []
    current_block = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        is_header = re.match(r'^#{1,4}\s+', stripped)
        is_list_item = re.match(r'^[-*]\s+', stripped)
        is_hr = stripped == '---'
        is_empty = not stripped
        is_table_row = stripped.startswith('|')
        is_code_placeholder = '__CODE' in stripped
        
        if is_list_item:
            if not in_list and current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            in_list = True
            current_block.append(line)
        elif in_list and not is_list_item and not is_empty:
            blocks.append('\n'.join(current_block))
            current_block = [line]
            in_list = False
        elif is_empty:
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            in_list = False
        else:
            current_block.append(line)
    
    if current_block:
        blocks.append('\n'.join(current_block))
    
    # Process each block
    result = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        if re.match(r'^#{4}\s+', block):
            result.append(re.sub(r'^#{4}\s+(.+)$', r'<h4>\1</h4>', block))
        elif re.match(r'^#{3}\s+', block):
            result.append(re.sub(r'^#{3}\s+(.+)$', r'<h3>\1</h3>', block))
        elif re.match(r'^#{2}\s+', block):
            result.append(re.sub(r'^#{2}\s+(.+)$', r'<h2>\1</h2>', block))
        elif re.match(r'^#\s+', block):
            result.append(re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', block))
        elif block == '---':
            result.append('<hr>')
        elif re.match(r'^[-*]\s+', block, re.MULTILINE):
            items = re.findall(r'^[-*]\s+(.+)$', block, re.MULTILINE)
            def format_item(item):
                item = re.sub(r'`([^`]+)`', r'<code>\1</code>', item)
                item = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', item)
                item = re.sub(r'\*(.+?)\*', r'<i>\1</i>', item)
                item = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', item)
                return item
            html = '<ul>\n' + '\n'.join(f'<li>{format_item(item)}</li>' for item in items) + '\n</ul>'
            result.append(html)
        elif block.startswith('<table>'):
            result.append(block)
        elif '__CODE' in block:
            result.append(block)
        else:
            block = re.sub(r'`([^`]+)`', r'<code>\1</code>', block)
            block = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', block)
            block = re.sub(r'\*(.+?)\*', r'<i>\1</i>', block)
            block = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', block)
            lines_in_block = [l.strip() for l in block.split('\n') if l.strip()]
            if lines_in_block:
                result.append('<p>' + '<br>\n'.join(lines_in_block) + '</p>')
    
    text = '\n\n'.join(result)
    
    for i, block in enumerate(code_blocks):
        block = re.sub(r'^```\w*\n', '<pre><code>', block)
        block = re.sub(r'\n```$', '</code></pre>', block)
        text = text.replace(f'__CODE{i}__', block)
    
    return text

def parse_session(content, session_num):
    # 新格式：## 第 N 回合學習 - Title 或 ## 第 N 回合學習 — Title
    title_match = re.search(r"^##\s*第\s*(\d+)\s*回合學習\s*[-–—]\s*(.+)$", content, re.MULTILINE)
    if title_match:
        title = title_match.group(2).strip()
    else:
        # 舊格式：#1 - Title
        title_match = re.search(r"^#\s*(\d+)\s*[-–]\s*(.+)$", content, re.MULTILINE)
        if not title_match:
            title_match = re.search(r"^#\s*[\d-]+\s+[\d:]+\s*[-–](.+)$", content, re.MULTILINE)
        title = title_match.group(2).strip() if title_match else f"學習回合 {session_num}"
    
    # 時間格式：**時間**：01:09 或舊格式
    time_match = re.search(r"\*\*時間\*\*[：:]\s*(\d{1,2}:\d{2})", content)
    if not time_match:
        time_match = re.search(r"(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{2})", content)
    session_time = time_match.group(1) if time_match else ""
    
    return {
        "num": session_num,
        "title": title,
        "time": session_time,
        "content": content,
        "topics": detect_topics(content)
    }

def parse_daily_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else ""
    
    if "summary" in filepath.stem:
        return None
    
    # 新格式：## 第 N 回合學習 - Title
    # 舊格式：# 2026-04-03 00:08 - Title
    session_pattern = r"(^##\s*第\s*\d+\s*回合學習\s*[-–—].+?$|^#\s*\d{4}-\d{2}-\d{2}\s+\d{1,2}:\d{2}\s*[-–—].+?$)"
    session_starts = list(re.finditer(session_pattern, content, re.MULTILINE))
    
    sessions = []
    if session_starts:
        for i, match in enumerate(session_starts):
            start = match.start()
            end = session_starts[i + 1].start() if i + 1 < len(session_starts) else len(content)
            session_content = content[start:end].strip()
            sessions.append(parse_session(session_content, i + 1))
    else:
        sessions.append({
            "num": 1,
            "title": f"{date} 學習記錄",
            "time": "",
            "content": content,
            "topics": detect_topics(content)
        })
    
    first_title = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    day_title = first_title.group(1) if first_title else date
    
    return {
        "date": date,
        "file": filepath.stem,
        "title": day_title,
        "sessions": sessions,
        "topics": detect_topics(content)
    }

def get_weekday(date_str):
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        weekdays = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
        return weekdays[d.weekday()]
    except:
        return ""

def HTML(body, title="股票學習筆記", depth=""):
    nav_links = f'''
    <nav>
        <a href="{depth}index.html">首頁</a>
        <a href="{depth}knowledge.html">知識庫</a>
        <a href="{depth}timeline.html">時間線</a>
    </nav>'''
    
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head>
<body>
<header><div class="header-inner"><a href="{depth}index.html" class="logo"><div class="logo-icon">📈</div><div class="logo-text">學習筆記</div></a>{nav_links}</div></header>
<main class="container">{body}</main>
<footer><p class="footer-text">由妖姬西打龍 🐍 自動生成</p></footer>
</body></html>'''

def main():
    print("生成網站...")
    
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    (OUTPUT_DIR/"session").mkdir()
    (OUTPUT_DIR/"topic").mkdir()
    
    # Parse all learning records
    all_files = sorted(LEARNING_DIR.glob("*.md"), reverse=True)
    daily_data = []
    all_sessions = []
    
    for f in all_files:
        if "summary" in f.stem:
            continue
        data = parse_daily_file(f)
        if data:
            daily_data.append(data)
            for s in data["sessions"]:
                all_sessions.append({
                    **s,
                    "date": data["date"],
                    "day_file": data["file"],
                    "day_title": data["title"]
                })
    
    # Stats
    stats = {
        "total_sessions": len(all_sessions),
        "total_days": len(daily_data),
        "topics": {k: 0 for k in TOPICS}
    }
    
    for s in all_sessions:
        for t in s["topics"]:
            if t in stats["topics"]:
                stats["topics"][t] += 1
    
    # Index page
    stats_html = f'''
    <div class="stat-card"><div class="stat-value">{stats["total_sessions"]}</div><div class="stat-label">學習回合</div></div>
    <div class="stat-card"><div class="stat-value">{stats["total_days"]}</div><div class="stat-label">學習天數</div></div>
    <div class="stat-card"><div class="stat-value">{len(TOPICS)}</div><div class="stat-label">主題分類</div></div>
    <div class="stat-card"><div class="stat-value">{sum(1 for s in all_sessions if len(s["topics"]) > 1)}</div><div class="stat-label">跨主題學習</div></div>
    '''
    
    topics_html = ""
    for k, v in TOPICS.items():
        count = stats["topics"].get(k, 0)
        topics_html += f'<a href="topic/{k}.html" class="topic-card"><div class="topic-icon">{v["icon"]}</div><div class="topic-name">{v["name"]}</div><div class="topic-desc">{v["desc"]}</div><div class="topic-count">{count} 回合</div></a>'
    
    recent_html = ""
    for day in daily_data[:5]:
        weekday = get_weekday(day["date"])
        recent_html += f'<div class="date-group"><div class="date-header"><span class="date">{day["date"]}</span><span class="weekday">{weekday}</span> · {len(day["sessions"])} 回合</div><div class="session-list">'
        
        for s in day["sessions"]:
            tags = "".join([f'<span class="tag">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in s["topics"] if t in TOPICS])
            recent_html += f'<a href="session/{day["file"]}_{s["num"]}.html" class="session-item"><div class="session-time">#{s["num"]} {s["time"]}</div><div class="session-title">{s["title"][:50]}</div><div class="tags">{tags}</div></a>'
        
        summary_file = LEARNING_DIR / f"{day['date']}-summary.md"
        if summary_file.exists():
            recent_html += f'<div class="summary-card"><a href="session/{day["date"]}-summary.html"><div class="summary-title">📅 當日總結</div><div class="summary-link">查看 {day["date"]} 學習總結 →</div></a></div>'
        
        recent_html += '</div></div>'
    
    index_html = f'''
    <div class="hero"><h1 class="hero-title">股票學習筆記</h1><p class="hero-subtitle">朝股票操作大師邁進中</p></div>
    <div class="stats-grid">{stats_html}</div>
    <section class="section"><div class="section-header"><h2 class="section-title">📖 學習主題</h2></div><div class="topic-grid">{topics_html}</div></section>
    <section class="section"><div class="section-header"><h2 class="section-title">🕐 最近學習</h2><a href="timeline.html" class="section-link">查看全部 →</a></div>{recent_html}</section>
    '''
    
    with open(OUTPUT_DIR/"index.html", "w", encoding="utf-8") as f:
        f.write(HTML(index_html))
    
    # Knowledge page
    kf = MEMORY_DIR / "stock-knowledge.md"
    khtml = md_to_html(kf.read_text(encoding="utf-8")) if kf.exists() else "<p>知識庫尚未建立</p>"
    
    nav_html = '<div class="knowledge-nav">'
    for k, v in TOPICS.items():
        nav_html += f'<a href="#{k}">{v["icon"]} {v["name"]}</a>'
    nav_html += '</div>'
    
    knowledge_html = f'<div class="content"><div class="content-card"><h1>📚 知識庫</h1>{nav_html}{khtml}</div></div>'
    
    with open(OUTPUT_DIR/"knowledge.html", "w", encoding="utf-8") as f:
        f.write(HTML(knowledge_html, "知識庫"))
    
    # Timeline page
    timeline_html = f'<div class="content"><div class="content-card"><h1>📅 學習時間線</h1><p>共 {len(all_sessions)} 回合學習記錄</p></div></div>'
    
    for day in daily_data:
        weekday = get_weekday(day["date"])
        timeline_html += f'<div class="date-group"><div class="date-header"><span class="date">{day["date"]}</span><span class="weekday">{weekday}</span> · {len(day["sessions"])} 回合</div><div class="session-list">'
        
        for s in day["sessions"]:
            tags = "".join([f'<span class="tag">{TOPICS[t]["icon"]}</span>' for t in s["topics"][:3] if t in TOPICS])
            timeline_html += f'<a href="session/{day["file"]}_{s["num"]}.html" class="session-item"><div class="session-time">#{s["num"]} {s["time"]}</div><div class="session-title">{s["title"][:60]}</div><div class="tags">{tags}</div></a>'
        
        summary_file = LEARNING_DIR / f"{day['date']}-summary.md"
        if summary_file.exists():
            timeline_html += f'<div class="summary-card"><a href="session/{day["date"]}-summary.html"><div class="summary-title">📅 當日總結</div><div class="summary-link">查看 {day["date"]} 學習總結 →</div></a></div>'
        
        timeline_html += '</div></div>'
    
    with open(OUTPUT_DIR/"timeline.html", "w", encoding="utf-8") as f:
        f.write(HTML(timeline_html, "時間線"))
    
    # Topic pages
    for k, v in TOPICS.items():
        related = [s for s in all_sessions if k in s["topics"]]
        titems = ""
        for s in related:
            titems += f'<a href="../session/{s["day_file"]}_{s["num"]}.html" class="session-item"><div class="session-time">{s["date"]} #{s["num"]}</div><div class="session-title">{s["title"][:60]}</div></a>'
        
        topic_html = f'<div class="content"><div class="content-card"><h1>{v["icon"]} {v["name"]}</h1><p>{v["desc"]}</p><p style="color:var(--text-muted);margin-top:12px">{len(related)} 回合相關學習</p></div></div><section class="section"><div class="session-list">{titems}</div></section>'
        
        with open(OUTPUT_DIR/"topic"/f"{k}.html", "w", encoding="utf-8") as f:
            f.write(HTML(topic_html, v["name"], "../"))
    
    # Session pages
    for day in daily_data:
        for s in day["sessions"]:
            html = md_to_html(s["content"])
            tags = "".join([f'<span class="tag">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in s["topics"] if t in TOPICS])
            
            session_html = f'''
            <div class="content">
                <div class="breadcrumb"><a href="../index.html">首頁</a><span>/</span><a href="../timeline.html">時間線</a><span>/</span><span>{day["date"]}</span></div>
                <div class="nav-links"><a href="../timeline.html" class="nav-link">← 返回時間線</a></div>
                <div class="content-card">
                    <div class="meta">{day["date"]} #{s["num"]} · {tags}</div>
                    <h1>{s["title"]}</h1>
                    {html}
                </div>
            </div>
            '''
            
            with open(OUTPUT_DIR/"session"/f"{day['file']}_{s['num']}.html", "w", encoding="utf-8") as f:
                f.write(HTML(session_html, s["title"][:50], "../"))
    
    # Summary pages
    for f in all_files:
        if "summary" in f.stem:
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", f.stem)
            date = date_match.group(1) if date_match else ""
            
            content = f.read_text(encoding="utf-8")
            html = md_to_html(content)
            
            summary_html = f'''
            <div class="content">
                <div class="breadcrumb"><a href="../index.html">首頁</a><span>/</span><a href="../timeline.html">時間線</a><span>/</span><span>{date}</span></div>
                <div class="nav-links"><a href="../timeline.html" class="nav-link">← 返回時間線</a></div>
                <div class="content-card">
                    <h1>📅 {date} 學習總結</h1>
                    {html}
                </div>
            </div>
            '''
            
            with open(OUTPUT_DIR/"session"/f"{date}-summary.html", "w", encoding="utf-8") as fh:
                fh.write(HTML(summary_html, f"{date} 學習總結", "../"))
    
    print(f"✅ 已生成 {len(all_sessions)} 個學習回合（{len(daily_data)} 天）")

if __name__ == "__main__":
    main()