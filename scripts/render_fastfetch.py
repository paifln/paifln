"""Render README artwork. Requires playwright and Microsoft Edge."""
from html import escape
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
W, H = 1200, 980
BG, FG, BLUE, GOLD, MUTED = '#0c1117', '#bdc9d2', '#83a1b5', '#c0a465', '#586975'
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">PAIFLN | Alibi Kabessov</title>
<desc id="desc">Linux terminal profile with a large PAIFLN ASCII logo, profile, technology stack and projects. Midnight blue, steel and muted gold palette.</desc>
<rect width="1200" height="980" rx="12" fill="{BG}"/>
<rect x="0.5" y="0.5" width="1199" height="979" rx="12" fill="none" stroke="#2b3741"/>
<path d="M0 52H1200" stroke="#2b3741"/>
<g font-family="Consolas, monospace" font-variant-ligatures="none" fill="{FG}">''']

def text(x,y,value,color=FG,size=21):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" xml:space="preserve" style="white-space:pre">{escape(value)}</text>')

def prompt(y,command):
    parts.append(f'<text x="44" y="{y}" font-size="20"><tspan fill="{BLUE}">paifln@github</tspan><tspan fill="{MUTED}"> ~ </tspan><tspan fill="{GOLD}">$ </tspan><tspan>{escape(command)}</tspan></text>')

text(28,33,'TERMINAL',MUTED,15)
text(506,33,'paifln@github: ~',BLUE,15)
text(1105,33,'bash',MUTED,15)
prompt(101,'whoami')
art=(ROOT/'assets/ascii-wordmark.txt').read_text(encoding='utf-8').splitlines()
for i,line in enumerate(art):
    text(58,153+i*35,line,FG if i<3 else BLUE,29)
text(46,353,'Alibi Kabessov',FG,28)
text(46,389,'Software Developer  /  Computer Science Educator',BLUE,21)
parts.append('<path d="M44 421H1156" stroke="#2b3741"/>')
prompt(466,'cat stack.conf')
rows=[
('Languages','Python / TypeScript / JavaScript / Luau'),
('Frontend','React / Next.js / Tailwind CSS'),
('Backend','FastAPI / aiogram / SQLAlchemy'),
('Data','PostgreSQL / SQLite / Redis / S3'),
('Desktop','Electron / Blockly / Arduino'),
('Delivery','Docker / GitHub Actions / Vercel'),
]
for i,(key,value) in enumerate(rows):
    text(46,510+i*33,key,BLUE)
    text(234,510+i*33,value)
prompt(752,'ls projects/')
projects=[('CodeArena','Self-hosted programming contests'),('DOCUMENTOR','Academic document review'),('Noctune','Personal music library & player'),('ZiyatAI','Teaching workspace',True),('JECTIVE','Robotics studio',True)]
for i,row in enumerate(projects):
    y=796+i*30
    text(46,y,row[0],GOLD,20)
    text(234,y,row[1],FG,20)
    if len(row)>2: text(940,y,'in development',MUTED,18)
parts.append('<path d="M44 938H1156" stroke="#2b3741"/>')
text(46,965,'Open to roles & collaboration',BLUE,17)
for i,color in enumerate([MUTED,BLUE,FG,'#74765a',GOLD,'#d3bd88']):
    parts.append(f'<rect x="{1012+i*24}" y="952" width="24" height="12" fill="{color}"/>')
parts.append('</g></svg>')
(ROOT/'assets/fastfetch.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    page=browser.new_page(viewport={'width':W,'height':H},device_scale_factor=2)
    page.goto((ROOT/'assets/fastfetch.svg').as_uri())
    page.locator('svg').screenshot(path=str(ROOT/'assets/fastfetch.png'))
    preview=browser.new_page(viewport={'width':900,'height':735},device_scale_factor=1)
    preview.set_content('<style>body{margin:0}svg{width:900px;height:auto;display:block}</style>'+''.join(parts))
    preview.screenshot(path=str(ROOT/'assets/preview.png'))
    browser.close()
