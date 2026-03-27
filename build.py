#!/usr/bin/env python3
"""
股票學習筆記 - 簡潔版網站生成器
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
LEARNING_DIR = MEMORY_DIR / "stock-learning"
OUTPUT_DIR = BASE_DIR / "docs"

TOPICS = {
    "technical": {"name": "技術分析", "icon": "📊"},
    "fundamental": {"name": "基本面", "icon": "💰"},
    "chips": {"name": "籌碼面", "icon": "🎲"},
    "strategy": {"name": "操作策略", "icon": "🎯"},
    "risk": {"name": "風險管理", "icon": "⚠️"},
    "psychology": {"name": "交易心理", "icon": "🧠"}
}

# 簡潔 CSS
CSS = '''
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: system-ui, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; background: #fafafa; color: #333; }
a { color: #0366d6; text-decoration: none; }
a:hover { text-decoration: underline; }
nav { margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid #eee; }
nav a { margin-right: 20px; }
nav a.active { font-weight: bold; }
h1 { margin-bottom: 20px; color: #111; }
h2 { margin: 30px 0 15px; color: #222; border-bottom: 2px solid #ddd; padding-bottom: 8px; }
h3 { margin: 25px 0 12px; color: #333; }
p { margin-bottom: 15px; }
ul, ol { margin: 15px 0 15px 25px; }
li { margin-bottom: 8px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { padding: 12px; text-align: left; border: 1px solid #ddd; }
th { background: #f5f5f5; font-weight: 600; }
tr:hover { background: #fafafa; }
code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; }
pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; margin: 15px 0; }
pre code { background: none; padding: 0; }
blockquote { border-left: 4px solid #0366d6; padding-left: 20px; margin: 15px 0; color: #666; }
.tags { margin: 10px 0; }
.tag { display: inline-block; padding: 4px 10px; margin-right: 8px; border-radius: 15px; font-size: 12px; background: #e1e4e8; }
.meta { color: #666; font-size: 14px; margin-bottom: 20px; }
hr { border: none; border-top: 1px solid #eee; margin: 30px 0; }
'''

def detect_topics(content):
    found = []
    keywords = {
        "technical": ["K線", "均線", "支撐", "壓力", "技術", "RSI", "MACD"],
        "fundamental": ["財報", "營收", "EPS", "本益比", "基本面", "估值"],
        "chips": ["法人", "主力", "融資", "籌碼", "外資", "投信"],
        "strategy": ["當沖", "波段", "價值投資", "策略", "停損", "停利"],
        "risk": ["風險", "倉位", "部位", "MDD", "回撤"],
        "psychology": ["心理", "心態", "情緒", "紀律"]
    }
    for t, kws in keywords.items():
        for kw in kws:
            if kw in content and t not in found:
                found.append(t)
    return found

def md_to_html(content):
    # 代碼塊
    content = re.sub(r"```(\w*)\n(.*?)\n```", r"<pre><code>\2</code></pre>", content, flags=re.DOTALL)
    content = re.sub(r"`([^`]+)`", r"<code>\1</code>", content)
    # 標題
    content = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", content, flags=re.MULTILINE)
    content = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", content, flags=re.MULTILINE)
    content = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", content, flags=re.MULTILINE)
    content = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", content, flags=re.MULTILINE)
    # 粗體斜體
    content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", content)
    content = re.sub(r"\*(.+?)\*", r"<i>\1</i>", content)
    # 連結
    content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', content)
    # 列表
    content = re.sub(r"^\*\s+(.+)$", r"<li>\1</li>", content, flags=re.MULTILINE)
    content = re.sub(r"(^<li>.*</li>\n?)+", r"<ul>\g<0></ul>", content)
    # 表格
    def tbl(m):
        lines = m.group(0).strip().split('\n')
        if len(lines) < 2: return m.group(0)
        h = [c.strip() for c in lines[0].split('|') if c.strip()]
        rows = [[c.strip() for c in l.split('|') if c.strip()] for l in lines[2:] if l.strip()]
        html = '<table><thead><tr>' + ''.join(f'<th>{x}</th>' for x in h) + '</tr></thead><tbody>'
        for r in rows: html += '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
        return html + '</tbody></table>'
    content = re.sub(r"(\|.+\|\n)+(\|[-:]+\|\n)(\|.+\|\n?)+", tbl, content)
    # 段落
    paras = content.split('\n\n")
    return '\n\n'.join(f"<p>{p}</p>" if p.strip() and not p.strip().startswith(('<h','<ul','<ol','<table','<pre','<li')) else p for p in paras)

def parse_files():
    files = []
    for f in sorted(LEARNING_DIR.glob("*.md"), reverse=True):
        if "summary" in f.stem: continue
        with open(f, encoding="utf-8") as fp: content = fp.read()
        title = re.search(r"^#+\s+(.+)$", content, re.MULTILINE)
        date = re.search(r"(\d{4}-\d{2}-\d{2})", f.stem)
        files.append({
            "date": date.group(1) if date else "",
            "file": f.stem,
            "title": title.group(1) if title else f.stem,
            "content": content,
            "topics": detect_topics(content)
        })
    return files

def HTML(content, title="股票學習筆記"):
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head>
<body>
<h1>📈 {title}</h1>
<nav>
<a href="index.html">首頁</a>
<a href="knowledge.html">知識庫</a>
<a href="timeline.html">時間線</a>
</nav>
{content}
<hr>
<p style="color:#888;font-size:12px">由妖姬西打龍 🐍 自動生成 · {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
</body></html>'''

def main():
    print("生成簡潔版網站...")
    if OUTPUT_DIR.exists():
        import shutil
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    (OUTPUT_DIR/"history").mkdir()
    (OUTPUT_DIR/"topic").mkdir()
    
    files = parse_files()
    
    # 統計
    stats = {"total": len(files), "topics": {k: 0 for k in TOPICS}}
    for f in files:
        for t in f["topics"]:
            if t in stats["topics"]: stats["topics"][t] += 1
    
    # 首頁
    progress = "".join([f'<p><a href="topic/{k}.html">{v["icon"]} {v["name"]}：{stats["topics"][k]} 篇</a></p>' for k,v in TOPICS.items()])
    recent = "".join([f'<li><a href="history/{f["file"]}.html">{f["date"]} - {f["title"][:50]}</a></li>' for f in files[:10]])
    index_content = f'''
<h2>📊 統計</h2>
<p>學習回合：{stats["total"]} 篇</p>
<h2>📖 主題分類</h2>
{progress}
<h2>🕐 最近學習</h2>
<ol>{recent}</ol>
'''
    with open(OUTPUT_DIR/"index.html", "w", encoding="utf-8") as f:
        f.write(HTML(index_content, "股票學習筆記"))
    
    # 知識庫
    kf = MEMORY_DIR / "stock-knowledge.md"
    khtml = md_to_html(kf.read_text(encoding="utf-8")) if kf.exists() else "<p>知識庫尚未建立</p>"
    with open(OUTPUT_DIR/"knowledge.html", "w", encoding="utf-8") as f:
        f.write(HTML(f"<h1>📚 知識庫</h1>{khtml}", "知識庫"))
    
    # 時間線
    tlist = "".join([f'<li><a href="history/{x["file"]}.html">{x["date"]} - {x["title"][:50]}</a></li>' for x in files])
    with open(OUTPUT_DIR/"timeline.html", "w", encoding="utf-8") as f:
        f.write(HTML(f"<h1>📅 學習時間線</h1><p>共 {len(files)} 篇</p><ol>{tlist}</ol>", "時間線"))
    
    # 主題頁
    for k, v in TOPICS.items():
        items = [x for x in files if k in x["topics"]]
        tlist = "".join([f'<li><a href="../history/{x["file"]}.html">{x["date"]} - {x["title"][:50]}</a></li>' for x in items])
        with open(OUTPUT_DIR/"topic"/f"{k}.html", "w", encoding="utf-8") as f:
            f.write(HTML(f'<h1>{v["icon"]} {v["name"]}</h1><p>{len(items)} 篇相關學習</p><ol>{tlist}</ol>', v["name"]))
    
    # 文章頁
    for x in files:
        html = md_to_html(x["content"])
        tags = " ".join([f'<span class="tag">{TOPICS[t]["icon"]} {TOPICS[t]["name"]}</span>' for t in x["topics"]])
        with open(OUTPUT_DIR/"history"/f'{x["file"]}.html', "w", encoding="utf-8") as f:
            f.write(HTML(f'''
<p class="meta">{x["date"]} · {tags}</p>
<h1>{x["title"]}</h1>
{html}
<p><a href="../timeline.html">← 返回時間線</a></p>
''', x["title"][:50]))
    
    print(f"✅ 已生成 {len(files)} 篇文章")

if __name__ == "__main__":
    main()