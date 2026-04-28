#!/usr/bin/env python3
"""
股票知識庫 - 網站生成器
從 stock-knowledge-base/wiki/ 生成靜態網站到 docs/

使用方式：
    python3 build.py

此腳本由每天的學習任務自動執行，
執行後會自動推送到 GitHub。
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# 路徑設定
WORKSPACE = Path.home() / ".openclaw" / "workspace"
WIKI_DIR = WORKSPACE / "stock-knowledge-base" / "wiki"
RAW_DIR = WORKSPACE / "stock-knowledge-base" / "raw"
REPO_DIR = WORKSPACE / "stock-knowledge-site"
OUTPUT_DIR = REPO_DIR / "docs"

# 主題對應
TOPICS = {
    "技術分析": {"id": "technical", "icon": "📊", "desc": "K線、均線、技術指標"},
    "基本面分析": {"id": "fundamental", "icon": "💰", "desc": "財報、估值、產業分析"},
    "籌碼面分析": {"id": "chips", "icon": "🎲", "desc": "三大法人、主力動向"},
    "操作策略": {"id": "strategy", "icon": "🎯", "desc": "當沖、波段、價值投資"},
    "風險管理": {"id": "risk", "icon": "⚠️", "desc": "停損停利、倉位控制"},
}

# 中文標題對應英文 slug
TITLE_SLUGS = {
    "K線型態": "k-patterns",
    "均線判斷": "moving-averages",
    "支撐壓力": "support-resistance",
    "財報假帳偵測": "financial-fraud-detection",
    "盈餘品質分析": "earnings-quality",
    "三大法人特性": "institutional-investors",
    "當沖操作": "day-trading",
    "停損方法": "stop-loss",
    "停利方法": "take-profit",
    "倉位管理": "position-sizing",
    "期貨未平倉量判讀": "futures-open-interest",
    "外資期貨未平倉判讀": "foreign-futures-oi",
    "作帳行情": "quarterly-window-dressing",
    "融資維持率與斷頭": "margin-maintenance-calls",
}

CSS = '''
:root {
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --bg: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-tertiary: #f3f4f6;
    --text: #111827;
    --text-secondary: #4b5563;
    --text-muted: #9ca3af;
    --border: #e5e7eb;
    --shadow: 0 1px 3px rgba(0,0,0,0.1);
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
.hero-title { font-size: 48px; font-weight: 700; margin-bottom: 16px; }
.hero-subtitle { font-size: 18px; color: var(--text-muted); }

.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 48px; }
.stat-card { background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-align: center; }
.stat-value { font-size: 32px; font-weight: 700; color: var(--primary); }
.stat-label { font-size: 14px; color: var(--text-muted); margin-top: 8px; }

.topic-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 48px; }
.topic-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-decoration: none; color: var(--text); transition: all 0.2s; }
.topic-card:hover { border-color: var(--primary); transform: translateY(-2px); }
.topic-icon { width: 48px; height: 48px; background: var(--bg-tertiary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px; }
.topic-name { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
.topic-desc { font-size: 14px; color: var(--text-secondary); }
.topic-count { font-size: 12px; color: var(--text-muted); margin-top: 12px; }

.section { margin-bottom: 48px; }
.section-title { font-size: 24px; font-weight: 600; margin-bottom: 24px; }

.article-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 16px; }
.article-card:hover { border-color: var(--primary); }
.article-title { font-size: 20px; font-weight: 600; margin-bottom: 12px; }
.article-title a { color: var(--text); text-decoration: none; }
.article-title a:hover { color: var(--primary); }
.article-excerpt { font-size: 14px; color: var(--text-secondary); margin-bottom: 16px; }
.article-meta { display: flex; gap: 16px; font-size: 12px; color: var(--text-muted); }

.wikilink { color: var(--primary); text-decoration: none; }
.wikilink:hover { text-decoration: underline; }

.article-content { max-width: 800px; }
.article-content h2 { font-size: 24px; margin: 32px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
.article-content h3 { font-size: 18px; margin: 24px 0 12px; }
.article-content p { margin-bottom: 16px; }
.article-content ul { margin: 16px 0; padding-left: 24px; }
.article-content li { margin-bottom: 8px; }
.article-content table { width: 100%; border-collapse: collapse; margin: 16px 0; }
.article-content th, .article-content td { padding: 12px; border: 1px solid var(--border); text-align: left; }
.article-content th { background: var(--bg-secondary); }
.article-content code { background: var(--bg-tertiary); padding: 2px 6px; border-radius: 4px; font-family: 'SF Mono', Consolas, monospace; }
.article-content pre { background: var(--bg-tertiary); padding: 16px; border-radius: 8px; overflow-x: auto; }
.article-content blockquote { border-left: 4px solid var(--primary); padding-left: 16px; margin: 16px 0; color: var(--text-secondary); }

footer { background: var(--bg-secondary); border-top: 1px solid var(--border); padding: 24px; text-align: center; color: var(--text-muted); font-size: 14px; }
'''


def get_slug(title: str) -> str:
    """取得標題對應的英文 slug"""
    return TITLE_SLUGS.get(title, title.lower().replace(" ", "-").replace("/", "-"))


def parse_wiki_article(filepath: Path) -> dict:
    """解析 wiki 文章"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取標題
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    
    # 提取摘要（> 開頭的行）
    summary_match = re.search(r'^> (.+)$', content, re.MULTILINE)
    summary = summary_match.group(1) if summary_match else ""
    
    # 提取關鍵字
    keywords = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    return {
        "title": title,
        "summary": summary,
        "keywords": keywords,
        "content": content,
        "filename": get_slug(title),  # 使用英文 slug
        "original_filename": filepath.stem,  # 保留原始檔名
        "category": filepath.parent.name
    }


def generate_index_page(articles: list) -> str:
    """生成首頁"""
    # 統計各類別文章數
    category_counts = {}
    for article in articles:
        cat = article["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    # 生成主題卡片
    topic_cards = ""
    for cat_name, info in TOPICS.items():
        count = category_counts.get(cat_name, 0)
        topic_cards += f'''
        <a href="{info["id"]}.html" class="topic-card">
            <div class="topic-icon">{info["icon"]}</div>
            <div class="topic-name">{cat_name}</div>
            <div class="topic-desc">{info["desc"]}</div>
            <div class="topic-count">{count} 篇文章</div>
        </a>'''
    
    # 生成最新文章列表
    recent_articles = ""
    for article in articles[:10]:
        cat_info = TOPICS.get(article["category"], {"id": "other", "icon": "📄"})
        recent_articles += f'''
        <div class="article-card">
            <div class="article-title">
                <a href="{cat_info["id"]}/{article["filename"]}.html">{article["title"]}</a>
            </div>
            <div class="article-excerpt">{article["summary"]}</div>
            <div class="article-meta">
                <span>{cat_info["icon"]} {article["category"]}</span>
                {f'<span>相關：{", ".join(article["keywords"][:3])}</span>' if article["keywords"] else ''}
            </div>
        </div>'''
    
    total_articles = len(articles)
    
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>股票知識庫</title>
    <style>{CSS}</style>
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">📈</div>
                <div class="logo-text">股票知識庫</div>
            </a>
            <nav>
                <a href="index.html" class="active">首頁</a>
                <a href="https://github.com/" target="_blank">GitHub</a>
            </nav>
        </div>
    </header>
    <main class="container">
        <div class="hero">
            <h1 class="hero-title">股票操作知識庫</h1>
            <p class="hero-subtitle">成為股票操作大師的路上，每一步都算數</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{total_articles}</div>
                <div class="stat-label">篇文章</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{len(TOPICS)}</div>
                <div class="stat-label">個主題</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{sum(len(a["keywords"]) for a in articles)}</div>
                <div class="stat-label">個關鍵字</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">24</div>
                <div class="stat-label">小時更新</div>
            </div>
        </div>
        
        <section class="section">
            <h2 class="section-title">主題分類</h2>
            <div class="topic-grid">{topic_cards}</div>
        </section>
        
        <section class="section">
            <h2 class="section-title">最新文章</h2>
            {recent_articles}
        </section>
    </main>
    <footer>
        <p>股票知識庫 · 每小時自動學習，每天自動編譯</p>
        <p>最後更新：{datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
    </footer>
</body>
</html>'''


def generate_category_page(category: str, articles: list) -> str:
    """生成類別頁面"""
    cat_articles = [a for a in articles if a["category"] == category]
    cat_info = TOPICS.get(category, {"id": "other", "icon": "📄", "desc": ""})
    
    article_list = ""
    for article in cat_articles:
        article_list += f'''
        <div class="article-card">
            <div class="article-title">
                <a href="{cat_info["id"]}/{article["filename"]}.html">{article["title"]}</a>
            </div>
            <div class="article-excerpt">{article["summary"]}</div>
            <div class="article-meta">
                {f'<span>相關：{", ".join([f"<a class=\"wikilink\" href=\"{get_slug(k)}.html\">{k}</a>" for k in article["keywords"][:3]])}</span>' if article["keywords"] else ''}
            </div>
        </div>'''
    
    if not article_list:
        article_list = '<div class="article-card"><p>尚無文章</p></div>'
    
    nav_items = ""
    for cat_name, info in TOPICS.items():
        active = " active" if cat_name == category else ""
        nav_items += f'<a href="{info["id"]}.html" class="{active}">{cat_name}</a>'
    
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category} - 股票知識庫</title>
    <style>{CSS}</style>
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="index.html" class="logo">
                <div class="logo-icon">📈</div>
                <div class="logo-text">股票知識庫</div>
            </a>
            <nav>{nav_items}</nav>
        </div>
    </header>
    <main class="container">
        <h1 class="section-title">{cat_info["icon"]} {category}</h1>
        <p style="color: var(--text-muted); margin-bottom: 32px;">{cat_info["desc"]}</p>
        <div class="section">
            {article_list}
        </div>
    </main>
    <footer>
        <p>股票知識庫 · 每小時自動學習，每天自動編譯</p>
    </footer>
</body>
</html>'''


def markdown_to_html(content: str) -> str:
    """將 Markdown 轉換為 HTML（簡化版）"""
    # 標題
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    
    # 引用
    content = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', content, flags=re.MULTILINE)
    
    # 粗體
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    
    # 連結
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', content)
    
    # wiki 連結 [[主題]] - 使用英文 slug
    def replace_wikilink(match):
        title = match.group(1)
        slug = get_slug(title)
        return f'<a class="wikilink" href="{slug}.html">{title}</a>'
    
    content = re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, content)
    
    # 無序列表
    content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'(<li>.*</li>\n)+', r'<ul>\g<0></ul>\n', content)
    
    # 表格（簡化）
    def replace_table(match):
        table_content = match.group(1)
        rows = table_content.strip().split('\n')
        html = '<table>'
        for i, row in enumerate(rows):
            cells = row.split('|')
            cells = [c.strip() for c in cells if c.strip()]
            if cells:
                tag = 'th' if i == 0 else 'td'
                html += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
        html += '</table>'
        return html
    
    content = re.sub(r'\|(.+)\|\n(\|.+\|\n)+', replace_table, content)
    
    # 程式碼區塊
    content = re.sub(r'```(\w+)?\n(.+?)```', r'<pre><code class="\1">\2</code></pre>', content, flags=re.DOTALL)
    
    # 行內程式碼
    content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
    
    # 段落
    paragraphs = content.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # 如果已經是 HTML 標籤，就不加 <p>
        if not re.match(r'^<(h[1-6]|ul|ol|li|table|blockquote|pre)', p):
            p = f'<p>{p}</p>'
        html_paragraphs.append(p)
    
    return '\n\n'.join(html_paragraphs)


def generate_article_page(article: dict, all_articles: list) -> str:
    """生成文章頁面"""
    cat_info = TOPICS.get(article["category"], {"id": "other", "icon": "📄"})
    html_content = markdown_to_html(article["content"])
    
    # 相關文章
    related = ""
    for keyword in article["keywords"][:5]:
        for a in all_articles:
            if a["filename"] != article["filename"] and keyword in a["keywords"]:
                related += f'<a href="../{TOPICS.get(a["category"], {"id": "other"})["id"]}/{a["filename"]}.html" class="wikilink">{a["title"]}</a>, '
                break
    
    if related:
        related = f'<h2>相關主題</h2><p>{related.rstrip(", ")}</p>'
    
    nav_items = ""
    for cat_name, info in TOPICS.items():
        active = " active" if cat_name == article["category"] else ""
        nav_items += f'<a href="../{info["id"]}.html" class="{active}">{cat_name}</a>'
    
    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article["title"]} - 股票知識庫</title>
    <style>{CSS}</style>
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="../index.html" class="logo">
                <div class="logo-icon">📈</div>
                <div class="logo-text">股票知識庫</div>
            </a>
            <nav>{nav_items}</nav>
        </div>
    </header>
    <main class="container">
        <article class="article-content">
            <h1>{article["title"]}</h1>
            {html_content}
            {related}
        </article>
    </main>
    <footer>
        <p>股票知識庫 · <a href="../index.html">返回首頁</a></p>
    </footer>
</body>
</html>'''


def main():
    """主程式"""
    print("📊 股票知識庫網站生成器")
    print("=" * 50)
    
    # 清空輸出目錄
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    # 讀取所有 wiki 文章
    articles = []
    
    for category in TOPICS.keys():
        cat_dir = WIKI_DIR / category
        if cat_dir.exists():
            for filepath in cat_dir.glob("*.md"):
                article = parse_wiki_article(filepath)
                articles.append(article)
    
    print(f"找到 {len(articles)} 篇文章")
    
    # 生成首頁
    index_html = generate_index_page(articles)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding='utf-8')
    print("✅ 生成首頁")
    
    # 生成類別頁面
    for category, info in TOPICS.items():
        cat_dir = OUTPUT_DIR / info["id"]
        cat_dir.mkdir(exist_ok=True)
        
        # 類別索引頁
        cat_html = generate_category_page(category, articles)
        (OUTPUT_DIR / f"{info['id']}.html").write_text(cat_html, encoding='utf-8')
        
        # 類別內文章頁面
        for article in articles:
            if article["category"] == category:
                article_html = generate_article_page(article, articles)
                (cat_dir / f"{article['filename']}.html").write_text(article_html, encoding='utf-8')
        
        print(f"✅ 生成 {category} ({len([a for a in articles if a['category'] == category])} 篇)")
    
    print(f"\n🎉 網站生成完成！輸出目錄：{OUTPUT_DIR}")
    print(f"   - 首頁：{OUTPUT_DIR / 'index.html'}")
    print(f"   - 文章數：{len(articles)}")


if __name__ == "__main__":
    main()