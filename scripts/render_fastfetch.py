"""Regenerate the GitHub-safe terminal card: python scripts/render_fastfetch.py."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
art = (ROOT / "assets/ascii-art.txt").read_text(encoding="utf-8-sig").splitlines()
while art and not art[-1].strip():
    art.pop()

BG = "#0d1117"
FG = "#c9d8eb"
BLUE = "#89b4fa"
YELLOW = "#f9c873"
MUTED = "#56677d"
GREEN = "#a6da95"
rows = [
    ("title", "paifln@github"),
    ("rule", ""),
    ("Name", "Alibi Kabessov"),
    ("Role", "Software Developer"),
    ("Also", "Computer Science Educator"),
    ("Focus", "Products, tools & systems"),
    ("", ""),
    ("section", "Stack"),
    ("Languages", "Python, TypeScript, JavaScript, Luau"),
    ("Frontend", "React, Next.js, Tailwind CSS"),
    ("Backend", "FastAPI, aiogram, SQLAlchemy"),
    ("Data", "PostgreSQL, SQLite, Redis, S3"),
    ("Desktop", "Electron, Blockly, Arduino"),
    ("Delivery", "Docker, GitHub Actions, Vercel"),
    ("", ""),
    ("section", "Projects"),
    ("CodeArena", "Self-hosted programming contests"),
    ("DOCUMENTOR", "Academic document review"),
    ("Noctune", "Personal music library & player"),
    ("ZiyatAI", "Teaching workspace [in development]"),
    ("JECTIVE", "Robotics studio [in development]"),
    ("", ""),
    ("section", "Contact"),
    ("Email", "kabessovalibi007@gmail.com"),
    ("GitHub", "github.com/paifln"),
    ("LinkedIn", "alibi-kabessov-60b97b43a"),
    ("", ""),
    ("Status", "Open to roles & collaboration"),
]

parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="650" viewBox="0 0 1120 650" role="img" aria-labelledby="title desc">
  <title id="title">paifln — Alibi Kabessov · fastfetch</title>
  <desc id="desc">Terminal profile with supplied ASCII portrait on the left and software development stack, projects and contacts on the right. Full links are available in the README.</desc>
  <rect x="1" y="1" width="1118" height="648" rx="12" fill="{BG}" stroke="#303d4b"/>
  <g font-family="Consolas, 'Liberation Mono', Menlo, monospace" font-size="16" fill="{FG}">
    <text x="30" y="35" fill="{BLUE}">paifln<tspan fill="{FG}"> / </tspan><tspan fill="{YELLOW}">README.md</tspan></text>
    <text x="1090" y="35" text-anchor="end" fill="{MUTED}">bash</text>
    <text x="30" y="68" fill="{GREEN}">paifln@github<tspan fill="{FG}">:~$ fastfetch</tspan></text>
  </g>
  <rect x="12" y="88" width="1096" height="548" rx="10" fill="#151b23"/>
  <g font-family="Consolas, 'Liberation Mono', Menlo, monospace" font-size="14" style="white-space:pre" xml:space="preserve">''']

for i, line in enumerate(art):
    parts.append(f'<text x="24" y="{116 + i * 17}" font-size="13" textLength="{len(line) * 7.5}" lengthAdjust="spacingAndGlyphs" fill="{BLUE}">{escape(line)}</text>')

for i, (key, value) in enumerate(rows):
    y = 116 + i * 17
    if not key:
        continue
    if key == "title":
        content = f'<tspan fill="{BLUE}">{value}</tspan>'
    elif key in ("rule", "section"):
        label = "─" * 65 if key == "rule" else f'─ {value} ' + "─" * (62 - len(value))
        content = f'<tspan fill="{MUTED}">{label}</tspan>'
    else:
        dots = "." * max(2, 15 - len(key))
        content = f'<tspan fill="{YELLOW}">{key}</tspan><tspan fill="{MUTED}"> {dots} </tspan><tspan fill="{GREEN if key == "Status" else FG}">{escape(value)}</tspan>'
    parts.append(f'<text x="536" y="{y}">{content}</text>')

for i, color in enumerate(["#242d3a", "#ed8796", GREEN, YELLOW, BLUE, "#c6a0f6", "#8bd5ca", FG]):
    parts.append(f'<rect x="{536 + i * 25}" y="608" width="25" height="14" fill="{color}"/>')
parts.append('</g></svg>')
(ROOT / "assets/fastfetch.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
