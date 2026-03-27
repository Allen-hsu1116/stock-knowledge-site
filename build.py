#!/usr/bin/env python3
"""股票學習筆記 - 專業版網站生成器（參考 Linear + Notion 設計）"""

import os
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"
OUTPUT_DIR = BASE_DIR / "docs"

TOPICS = {
    "technical": {"name": "技術分析", "icon": "📊", "desc": "K線、均線、技術指標"},
    "fundamental": {"name": "基本面分析", "icon": "💰", "desc": "財報、估值、產業分析"},
    "chips": {"name": "籌碼面分析", "icon": "🎲", "desc": "三大法人、主力動向"},
    "strategy": {"name": "操作策略", "icon": "🎯", "desc": "當沖、波段、價值投資"},
    "risk": {"name": "風險管理", "icon": "⚠️", "desc": "停損停利、倉位控制"},
    "psychology": {"name": "交易心理", "icon": "🧠", "desc": "心態建設、認知偏誤"}
}

# 專業版 CSS（參考 Linear + Notion）
CSS = '''
:root {
    --primary: #6366f1; --primary-light: #818cf8;
    --bg: #ffffff; --bg-secondary: #f9fafb; --bg-tertiary: #f3f4f6;
    --text: #111827; --text-secondary: #4b5563; --text-muted: #9ca3af;
    --border: #e5e7eb; --border-light: #f3f4f6;
    --shadow: 0 1px 3px rgba(0,0,0,0.1);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; }
.container { max-width: 1200px; margin: 0 auto; }

/* Header */
header { position: sticky; top: 0; background: var(--bg); border-bottom: 1px solid var(--border); z-index: 100; }
.header-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; max-width: 1200px; margin: 0 auto; }
.logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
.logo-icon { width: 36px; height: 36px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; }
.logo-text { font-size: 18px; font-weight: 600; color: var(--text); }
nav { display: flex; gap: 8px; }
nav a { padding: 8px 16px; border-radius: 8px; color: var(--text-secondary); text-decoration: none; font-size: 14px; font-weight: 500; transition: all 0.2s; }
nav a:hover { background: var(--bg-tertiary); color: var(--text); }
nav a.active { background: var(--primary); color: white; }

/* Main */
main { padding: 40px 24px; }

/* Hero */
.hero { text-align: center; padding: 60px 0 40px; }
.hero-title { font-size: 48px; font-weight: 700; margin-bottom: 16px; background: linear-gradient(135deg, var(--text), var(--text-secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-subtitle { font-size: 18px; color: var(--text-muted); margin-bottom: 32px; }

/* Stats */
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 48px; }
.stat-card { background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-align: center; transition: all 0.2s; }
.stat-card:hover { border-color: var(--primary); transform: translateY(-2px); }
.stat-value { font-size: 32px; font-weight: 700; color: var(--primary); }
.stat-label { font-size: 14px; color: var(--text-muted); margin-top: 8px; }

/* Topic Cards */
.topic-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 48px; }
.topic-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-decoration: none; color: var(--text); transition: all 0.2s; }
.topic-card:hover { border-color: var(--primary); box-shadow: var(--shadow); transform: translateY(-2px); }
.topic-icon { width: 48px; height: 48px; background: var(--bg-tertiary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px; }
.topic-name { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
.topic-desc { font-size: 14px; color: var(--text-secondary); }
.topic-count { font-size: 12px; color: var(--text-muted); margin-top: 12px; }

/* Section */
.section { margin-bottom: 48px; }
.section-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; }
.section-title { font-size: 24px; font-weight: 600; }
.section-link { color: var(--primary); text-decoration: none; font-size: 14px; }

/* Timeline */
.timeline { display: flex; flex-direction: column; gap: 12px; }
.timeline-item { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-decoration: none; color: var(--text); transition: all 0.2s; display: block; }
.timeline-item:hover { border-color: var(--primary); }
.timeline-date { font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }
.timeline-title { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.timeline-excerpt { font-size: 14px; color: var(--text-secondary); line-height: 1.5; }
.timeline-item:hover .timeline-title { color: var(--primary); }

/* Tags */
.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 12px; background: var(--bg-tertiary); border-radius: 16px; font-size: 12px; color: var(--text-secondary); }
.tag:hover { background: var(--primary); color: white; }

/* Content */
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

/* Breadcrumb */
.breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 14px; color: var(--text-muted); margin-bottom: 24px; }
.breadcrumb a { color: var(--text-secondary); text-decoration: none; }
.breadcrumb a:hover { color: var(--primary); }

/* Nav Links */
.nav-links { display: flex; gap: 12px; margin-bottom: 24px; }
.nav-link { display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; color: var(--text-secondary); text-decoration: none; font-size: 14px; transition: all 0.2s; }
.nav-link:hover { background: var(--bg-tertiary); color: var(--text); border-color: var(--primary); }

/* Footer */
footer { background: var(--bg-secondary); border-top: 1px solid var(--border); padding: 32px; margin-top: 48px; text-align: center; }
.footer-text { font-size: 14px; color: var(--text-muted); }

/* Responsive */
@media (max-width: 900px) {
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .topic-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .stats-grid { grid-template-columns: 1fr; }
    .topic-grid { grid-template-columns: 1fr; }
    .hero-title { font-size: 32px; }
    .content-card { padding: 24px; }
}
'''

def detect_topics(content):
    keywords = {
        "technical": ["K線", "均線", "支撐", "壓力", "技術", "RSI", "MACD", "KD"],
        "fundamental": ["財報", "營收", "EPS", "本益比", "基本面", "估值", "ROE"],
        "chips": ["法人", "主力", "融資", "籌碼", "外資", "投信"],
        "strategy": ["當沖", "波段", "價值投資", "策略", "停損", "停利"],
        "risk": ["風險", "倉位", "部位", "MDD", "回撤"],
        "psychology": ["心理", "心態", "情緒", "紀律"]
    }
    found = []
    for t, kws in keywords.items():
        for kw in kws:
            if kw in content and t not in found:
                found.append(t)
    return found

def md_to_html(content):
    content = re.sub(r"```(\w*)\n(.*?)\n```", r"<pre><code>\2</code></pre>", content, flags=re.DOTALL)
    content = re.sub(r"`([^`]+)`", r"<code>\1</code>", content)
    content = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", content, flags=re.MULTILINE)
    content = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", content, flags=re.MULTILINE)
    content = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", content, flags=re.MULTILINE)
    content = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", content, flags=re.MULTILINE)
    content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", content)
    content = re.sub(r"\*(.+?)\*", r"<i>\1</i>", content)
    content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', content)
    content = re.sub(r"^\*\s+(.+)$", r"<li>\1</li>", content, flags=re.MULTILINE)
    content = re.sub(r"(^<li>.*</li>\n?)+", r"<ul>\g<0></ul>", content)
    def tbl(m):
        lines = m.group(0).strip().split('\n')
        if len(lines) < 2: return m.group(0)
        h = [c.strip() for c in lines[0].split('|') if c.strip()]
        rows = [[c.strip() for c in l.split('|') if c.strip()] for l in lines[2:] if l.strip()]
        return '<table><thead><tr>' + ''.join(f'<th>{x}</th>' for x in h) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows) + '</tbody></table>'
    content = re.sub(r"(\|.+\|\n)+(\|[-:]+\|\n)(\|.+\|\n?)+", tbl, content)
    paras = content.split('\n\n')
    return '\n\n'.join(f"<p>{p}</p>" if p.strip() and not p.strip().startswith(('<h','<ul','<ol','<table','<pre','<li')) else p for p in paras)

def parse_files():
    files = []
    for f in sorted(LEARNING_DIR.glob("*.md"), reverse=True):
        if "summary" in f.stem: continue
        with open(f, encoding="utf-8") as fp: content = fp.read()
        title = re.search(r"^#+\s+(.+)$", content, re.MULTILINE)
        date = re.search(r"(\d{4}-\d{2}-\d{2})", f.stem)
        files.append({"date": date.group(1) if date else "", "file": f.stem, "title": title.group(1) if title else f.stem, "content": content, "topics": detect_topics(content)})
    return files

def HTML(body, title="股票學習筆記"):
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head>
<body>
<header><div class="header-inner"><a href="index.html" class="logo"><div class="logo-icon">📈</div><div class="logo-text">學習筆記</div></a><nav><a href="index.html">首頁</a><a href="knowledge.html">知識庫</a><a href="timeline.html">時間線</a></nav></div></header>
<main class="container">{body}</main>
<footer><p class="footer-text">由妖姬西打龍 🐍 自動生成</p></footer>
</body></html>'''

def main():
    print("生成專業版網站...")
    import shutil
    if OUTPUT_DIR.exists(): shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    (OUTPUT_DIR/"history").mkdir()
    (OUTPUT_DIR/"topic").mkdir()
    
    files = parse_files()
    stats = {"total": len(files), "topics": {k: 0 for k in TOPICS}}
    for f in files:
        for t in f["topics"]:
            if t in stats["topics"]: stats["topics"][t] += 1
    
    # 首頁
    stats_html = ''.join([f'<div class="stat-card"><div class="stat-value">{v}</div><div class="stat-label">{{"total":"學習回合","topics":"主題數"}[k]}</div></div>' for k,v in [("total",stats["total"]),("topics",len(TOPICS))]])
    topics_html = ''.join([f'<a href="topic/{k}.html" class="topic-card"><div class="topic-icon">{v["icon"]}</div><div class="topic-name">{v["name"]}</div><div class="topic-desc">{v["desc"]}</div><div class="topic-count">{stats["topics"][k]} 篇</div></a>' for k,v in TOPICS.items()])
    recent_html = ''.join([f'<a href="history/{f["file"]}.html" class="timeline-item"><div class="timeline-date">{f["date"]}</div><div class="timeline-title">{f["title"][:60]}</div><div class="tags">{"".join([f"<span class=\"tag\">{TOPICS[t][\"icon\"]}</span>" for t in f["topics"][:3]])}</div></a>' for f in files[:8]])
    
    with open(OUTPUT_DIR/"index.html", "w", encoding="utf-8") as f:
        f.write(HTML(f'''
<div class="hero"><h1 class="hero-title">股票學習筆記</h1><p class="hero-subtitle">朝股票操作大師邁進中</p></div>
<div class="stats-grid">{stats_html}</div>
<section class="section"><div class="section-header"><h2 class="section-title">📖 學習主題</h2></div><div class="topic-grid">{topics_html}</div></section>
<section class="section"><div class="section-header"><h2 class="section-title">🕐 最近學習</h2><a href="timeline.html" class="section-link">查看全部 →</a></div><div class="timeline">{recent_html}</div></section>
'''))

    # 知識庫
    kf = MEMORY_DIR / "stock-knowledge.md"
    khtml = md_to_html(kf.read_text(encoding="utf-8")) if kf.exists() else "<p>知識庫尚未建立</p>"
    with open(OUTPUT_DIR/"knowledge.html", "w", encoding="utf-8") as f:
        f.write(HTML(f'<div class="content"><div class="content-card"><h1>📚 知識庫</h1>{khtml}</div></div>', "知識庫"))

    # 時間線
    titems = ''.join([f'<a href="history/{x["file"]}.html" class="timeline-item"><div class="timeline-date">{x["date"]}</div><div class="timeline-title">{x["title"][:60]}</div><div class="tags">{"".join([f"<span class=\"tag\">{TOPICS[t][\"icon\"]}</span>" for t in x["topics"]])}</div></a>' for x in files])
    with open(OUTPUT_DIR/"timeline.html", "w", encoding="utf-8") as f:
        f.write(HTML(f'<div class="content"><div class="content-card"><h1>📅 學習時間線</h1><p>共 {len(files)} 篇學習記錄</p></div></div><section class="section"><div class="timeline">{titems}</div></section>', "時間線"))

    # 主題頁
    for k, v in TOPICS.items():
        items = [x for x in files if k in x["topics"]]
        titems = ''.join([f'<a href="../history/{x["file"]}.html" class="timeline-item"><div class="timeline-date">{x["date"]}</div><div class="timeline-title">{x["title"][:60]}</div></a>' for x in items])
        with open(OUTPUT_DIR/"topic"/f"{k}.html", "w", encoding="utf-8") as f:
            f.write(HTML(f'<div class="content"><div class="content-card"><h1>{v["icon"]} {v["name"]}</h1><p>{v["desc"]}</p><p style="color:var(--text-muted);margin-top:12px">{len(items)} 篇相關學習</p></div></div><section class="section"><div class="timeline">{titems}</div></section>', v["name"]))

    # 文章頁
    for x in files:
        html = md_to_html(x["content"])
        tags = "".join([f'<span class="tag">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in x["topics"]])
        idx = next((i for i, f in enumerate(files) if f["file"] == x["file"]), -1)
        prev = f'<a href="{files[idx-1]["file"]}.html" class="nav-link">← 上一篇</a>' if idx > 0 else ""
        next_ = f'<a href="{files[idx+1]["file"]}.html" class="nav-link">下一篇 →</a>' if idx < len(files)-1 else ""
        with open(OUTPUT_DIR/"history"/f'{x["file"]}.html', "w", encoding="utf-8") as f:
            f.write(HTML(f'''
<div class="content">
<div class="breadcrumb"><a href="../index.html">首頁</a><span>/</span><a href="../timeline.html">時間線</a><span>/</span><span>{x["date"]}</span></div>
<div class="nav-links"><a href="../timeline.html" class="nav-link">← 返回時間線</a>{prev}{next_}</div>
<div class="content-card"><div class="meta">{x["date"]} · {tags}</div><h1>{x["title"]}</h1>{html}</div>
</div>
''', x["title"][:50]))
    
    print(f"✅ 已生成 {len(files)} 篇文章")

if __name__ == "__main__":
    main()