#!/usr/bin/env python3
"""
從學習記錄生成網站

Usage:
    python generate_site.py
"""

import os
import re
import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path

SITE_DIR = Path(__file__).parent
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
OUTPUT_DIR = SITE_DIR / "docs"

# 主題對應表
TOPIC_MAP = {
    "技術分析": "technical",
    "技術面": "technical",
    "K線": "technical",
    "均線": "technical",
    "支撐壓力": "technical",
    "基本面": "fundamental",
    "財報": "fundamental",
    "估值": "fundamental",
    "籌碼": "chips",
    "法人": "chips",
    "主力": "chips",
    "融資券": "chips",
    "操作策略": "strategy",
    "當沖": "strategy",
    "波段": "strategy",
    "價值投資": "strategy",
    "風險管理": "risk",
    "停損": "risk",
    "倉位": "risk",
    "交易心理": "psychology",
    "心態": "psychology",
}


def parse_markdown(filepath: Path) -> dict:
    """解析 Markdown 檔案"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 提取標題
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    
    # 提取日期
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    date = date_match.group(1) if date_match else ""
    
    # 提取主題標籤
    topics = []
    for keyword, tag in TOPIC_MAP.items():
        if keyword in content:
            topics.append(tag)
    topics = list(set(topics))
    
    return {
        "title": title,
        "date": date,
        "content": content,
        "topics": topics,
        "filename": filepath.stem,
    }


def generate_html(data: dict, template_type: str = "content") -> str:
    """生成 HTML"""
    
    # 將 Markdown 轉換為簡單 HTML
    content = data["content"]
    content = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", content, flags=re.MULTILINE)
    content = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", content, flags=re.MULTILINE)
    content = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", content, flags=re.MULTILINE)
    content = re.sub(r"^\*\*(.+?)\*\*", r"<strong>\1</strong>", content, flags=re.MULTILINE)
    content = re.sub(r"^\*\s+(.+)$", r"<li>\1</li>", content, flags=re.MULTILINE)
    content = re.sub(r"(^- .+$\n?)+", lambda m: f"<ul>{m.group(0)}</ul>", content, flags=re.MULTILINE)
    content = re.sub(r"\n\n", "</p><p>", content)
    content = f"<p>{content}</p>"
    
    # 生成 tags
    tags_html = "".join([f'<span class="tag {t}">{t}</span>' for t in data.get("topics", [])])
    
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data["title"]} - 股票學習筆記</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <h1>📈 股票學習筆記</h1>
        <nav>
            <a href="../index.html">總覽</a>
            <a href="../knowledge.html">知識庫</a>
            <a href="../history.html">學習記錄</a>
        </nav>
    </header>

    <main class="content">
        <h1>{data["title"]}</h1>
        <p class="meta">{data.get("date", "")} {tags_html}</p>
        {content}
    </main>

    <footer>
        <p>由妖姬西打龍 🐍 自動生成</p>
        <p>最後更新：{datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
    </footer>
</body>
</html>"""
    return html


def generate_index(stats: dict) -> str:
    """生成首頁"""
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>股票學習筆記</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>📈 股票學習筆記</h1>
        <p class="subtitle">朝股票操作大師邁進中</p>
        <nav>
            <a href="index.html" class="active">總覽</a>
            <a href="knowledge.html">知識庫</a>
            <a href="history.html">學習記錄</a>
        </nav>
    </header>

    <main>
        <section class="stats">
            <div class="stat-card">
                <h3>學習回合</h3>
                <p>{stats["total_sessions"]}</p>
            </div>
            <div class="stat-card">
                <h3>涵蓋主題</h3>
                <p>{stats["total_topics"]}</p>
            </div>
            <div class="stat-card">
                <h3>最新學習</h3>
                <p>{stats["last_learn"]}</p>
            </div>
        </section>

        <section class="topics">
            <h2>📚 依主題瀏覽</h2>
            <div class="topic-grid">
                <a href="topics/technical.html" class="topic-card">
                    <h3>📊 技術分析</h3>
                    <p>K線、均線、支撐壓力</p>
                </a>
                <a href="topics/fundamental.html" class="topic-card">
                    <h3>💰 基本面分析</h3>
                    <p>財報、估值、產業</p>
                </a>
                <a href="topics/chips.html" class="topic-card">
                    <h3>🎲 籌碼面分析</h3>
                    <p>法人、主力、融資券</p>
                </a>
                <a href="topics/strategy.html" class="topic-card">
                    <h3>🎯 操作策略</h3>
                    <p>當沖、波段、價值投資</p>
                </a>
                <a href="topics/risk.html" class="topic-card">
                    <h3>⚠️ 風險管理</h3>
                    <p>停損停利、倉位控制</p>
                </a>
                <a href="topics/psychology.html" class="topic-card">
                    <h3>🧠 交易心理</h3>
                    <p>心態建設、認知偏誤</p>
                </a>
            </div>
        </section>

        <section class="recent">
            <h2>🕐 最近學習</h2>
            <ul>
                {stats["recent_list"]}
            </ul>
        </section>
    </main>

    <footer>
        <p>由妖姬西打龍 🐍 自動生成</p>
        <p>最後更新：{datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
    </footer>
</body>
</html>"""
    return html


def main():
    """主程式"""
    print("生成網站...")
    
    # 清理並建立輸出目錄
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    # 複製靜態檔案
    shutil.copy(SITE_DIR / "style.css", OUTPUT_DIR / "style.css")
    
    # 建立主題目錄
    (OUTPUT_DIR / "topics").mkdir(exist_ok=True)
    (OUTPUT_DIR / "history").mkdir(exist_ok=True)
    
    # 統計
    total_sessions = 0
    all_topics = set()
    recent_list = []
    
    # 處理學習記錄
    learning_dir = MEMORY_DIR / "stock-learning"
    if learning_dir.exists():
        for md_file in sorted(learning_dir.glob("*.md"), reverse=True):
            data = parse_markdown(md_file)
            
            # 統計
            total_sessions += 1
            all_topics.update(data["topics"])
            
            # 生成 HTML
            html = generate_html(data)
            output_file = OUTPUT_DIR / "history" / f"{data['filename']}.html"
            output_file.write_text(html, encoding="utf-8")
            
            # 最近列表
            if len(recent_list) < 10:
                recent_list.append(
                    f'<li><a href="history/{data["filename"]}.html">{data["date"]} - {data["title"][:30]}</a></li>'
                )
    
    # 處理知識庫
    knowledge_file = MEMORY_DIR / "stock-knowledge.md"
    if knowledge_file.exists():
        data = parse_markdown(knowledge_file)
        html = generate_html(data)
        (OUTPUT_DIR / "knowledge.html").write_text(html, encoding="utf-8")
    
    # 生成首頁
    stats = {
        "total_sessions": total_sessions,
        "total_topics": len(all_topics),
        "last_learn": recent_list[0].split(">")[1].split("-")[0].strip() if recent_list else "--",
        "recent_list": "\n                ".join(recent_list) if recent_list else "<li>尚無記錄</li>",
    }
    
    index_html = generate_index(stats)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    
    print(f"✅ 網站已生成到 {OUTPUT_DIR}")
    print(f"   學習回合: {total_sessions}")
    print(f"   涵蓋主題: {len(all_topics)}")
    print(f"   最後更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()