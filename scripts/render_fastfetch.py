"""Regenerate the GitHub terminal card: python scripts/render_fastfetch.py."""
from html import escape
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BG, PANEL = "#080e14", "#0d1720"
FG, BLUE, GOLD, MUTED = "#b4c4d1", "#7897ae", "#b59a52", "#465e70"

# Editable ASCII source, rendered as text to keep every slash crisp.
GLYPHS = [
    [" ______ ", r"/\  == \ ", r"\ \  _-/", r" \ \_\  ", r"  \/_/  "],
    [" ______ ", r"/\  __ \ ", r"\ \  __ \ ", r" \ \_\ \_\ ", r"  \/_/\/_/"],
    [" __ ", r"/\ \ ", r"\ \ \ ", r" \ \_\ ", r"  \/_/"],
    [" ______ ", r"/\  ___\ ", r"\ \  __\ ", r" \ \_\  ", r"  \/_/  "],
    [" __     ", r"/\ \    ", r"\ \ \___", r" \ \_____\ ", r"  \/_____/"],
    [" __   __ ", r"/\ \-./  \ ", r"\ \ \-./\ \ ", r" \ \_\ \ \_\ ", r"  \/_/  \/_/"],
]
art = ["  ".join(g[i].ljust(max(map(len, g))) for g in GLYPHS).rstrip() for i in range(5)]
(ROOT / "assets/ascii-wordmark.txt").write_text("\n".join(art) + "\n", encoding="utf-8")
columns = [
    ("01 / PROFILE", [
        ("Name", "Alibi Kabessov"), ("Role", "Software Developer"),
        ("Also", "Computer Science Educator"), ("Focus", "Products, tools & systems"),
        ("", ""), ("CONTACT", ""),
        ("Email", "kabessovalibi007@gmail.com"), ("GitHub", "github.com/paifln"),
        ("LinkedIn", "alibi-kabessov-60b97b43a"),
    ]),
    ("02 / STACK", [
        ("Languages", "Python / TypeScript / JavaScript"), ("", "Luau"),
        ("Frontend", "React / Next.js / Tailwind CSS"),
        ("Backend", "FastAPI / aiogram / SQLAlchemy"),
        ("Data", "PostgreSQL / SQLite / Redis / S3"),
        ("Desktop", "Electron / Blockly / Arduino"),
        ("Delivery", "Docker / GitHub Actions / Vercel"),
    ]),
    ("03 / PROJECTS", [
        ("CodeArena", "Programming contests"), ("DOCUMENTOR", "Academic document review"),
        ("Noctune", "Music library & player"),
        ("ZiyatAI", "Teaching workspace [dev]"), ("JECTIVE", "Robotics studio [dev]"),
    ]),
]
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
<title id="title">paifln вЂ” Alibi Kabessov В· terminal profile</title>
<desc id="desc">Large PAIFLN ASCII wordmark in a dark blue and muted gold Linux terminal, followed by profile, stack, projects and contacts.</desc>
<rect x="1" y="1" width="1598" height="898" rx="14" fill="{BG}" stroke="{MUTED}"/>
<path d="M1 57H1599" stroke="{MUTED}"/>
<g font-family="Consolas, 'Liberation Mono', monospace" fill="{FG}">
<g font-size="16"><text x="32" y="35" fill="{BLUE}">paifln / <tspan fill="{GOLD}">README.md</tspan></text>
<text x="1568" y="35" text-anchor="end" fill="{MUTED}">bash вЂ” 160 Г— 48</text>
<text x="40" y="102" fill="{GOLD}">paifln@github<tspan fill="{FG}">:~$ fastfetch --logo paifln</tspan></text></g>
<rect x="24" y="125" width="1552" height="270" rx="8" fill="{PANEL}"/>
<g font-size="48" xml:space="preserve" style="white-space:pre">''']
for i, line in enumerate(art):
    parts.append(f'<text x="65" y="{176 + i * 44}" fill="{FG if i < 3 else BLUE}">{escape(line)}</text>')
parts.append('</g>')
for col, (heading, rows) in enumerate(columns):
    x = 40 + col * 520
    parts.append(f'<text x="{x}" y="447" font-size="17" fill="{GOLD}">{heading}</text>')
    parts.append(f'<path d="M{x} 464h480" stroke="{MUTED}"/>')
    for i, (key, value) in enumerate(rows):
        y = 500 + i * 32
        if key:
            parts.append(f'<text x="{x}" y="{y}" font-size="15" fill="{BLUE}">{escape(key)}</text>')
        if value:
            parts.append(f'<text x="{x + 109}" y="{y}" font-size="15">{escape(value)}</text>')
parts.append(f'<path d="M40 811h1520" stroke="{MUTED}"/><text x="40" y="850" font-size="16" fill="{GOLD}">в—Џ Open to roles &amp; collaboration</text>')
for i, color in enumerate([BG, MUTED, BLUE, FG, "#686c52", GOLD, "#d1bb7a", "#dce2df"]):
    parts.append(f'<rect x="{1320+i*30}" y="835" width="30" height="17" fill="{color}"/>')
parts.append('</g></svg>')
(ROOT / "assets/fastfetch.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.goto((ROOT / "assets/fastfetch.svg").as_uri())
    page.locator("svg").screenshot(path=str(ROOT / "assets/fastfetch.png"))
    browser.close()

