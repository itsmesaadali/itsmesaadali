from pathlib import Path

WIDTH = 600
HEIGHT = 520

svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<style>

text {{
    font-family: monospace;
    font-size:15px;
    fill:#24292f;
}}

.title {{
    fill:#57606a;
    font-size:14px;
}}

.green {{
    fill:#1a7f37;
    font-weight:bold;
}}

.yellow {{
    fill:#9a6700;
}}

.orange {{
    fill:#bc4c00;
    font-weight:bold;
}}

.blue {{
    fill:#0969da;
    font-weight:bold;
}}

.white {{
    fill:#24292f;
}}

.bold {{
    font-weight:bold;
}}

.link {{
    fill:#0969da;
}}

</style>

<!-- Background -->
<rect
x="0"
y="0"
width="{WIDTH}"
height="{HEIGHT}"
fill="#ffffff"
stroke="#d0d7de"/>

<!-- Title -->
<text x="20" y="30" class="title">
TERMINAL - D:\\itsmesaadali
</text>

<line
x1="15"
y1="42"
x2="585"
y2="42"
stroke="#d8dee4"/>

<!-- Prompt -->
<text x="20" y="70">
<tspan class="green">PS D:\\itsmesaadali&gt;</tspan>
<tspan class="white bold"> whoami</tspan>
</text>

<!-- Name -->
<text x="35" y="105">
<tspan class="white bold">Saad Ali</tspan><tspan class="title"> | Software Developer &amp; Student</tspan>
</text>

<!-- Info -->
<text x="20" y="145">
<tspan class="orange">Now</tspan>
<tspan class="white" dx="35">Full-Stack Developer &amp; BSSE Student</tspan>
</text>

<text x="20" y="170">
<tspan class="orange">Focus</tspan>
<tspan class="white" dx="23">Web &amp; Backend Development</tspan>
</text>

<!-- Stack -->
<text x="20" y="215" class="blue">
─ Stack ─────────────────────────────────────────────────────
</text>

<text x="20" y="245">
<tspan class="orange">Frontend</tspan>
<tspan class="white" dx="15">Next.js, React, TanStack, TypeScript</tspan>
</text>

<text x="20" y="270">
<tspan class="orange">Backend</tspan>
<tspan class="white" dx="20">Node.js, NestJS, Python, C++</tspan>
</text>

<text x="20" y="295">
<tspan class="orange">Cloud</tspan>
<tspan class="white" dx="40">Vercel, Docker, Git, Prisma</tspan>
</text>

<!-- Links -->
<text x="20" y="340" class="blue">
─ Links &amp; Contact ───────────────────────────────────────────────
</text>

<text x="20" y="370">
<tspan class="orange">Portfolio</tspan>
<tspan class="link" dx="15">devsaad.vercel.app</tspan>
</text>

<text x="20" y="395">
<tspan class="orange">Email</tspan>
<tspan class="link" dx="48">itmesaad@gmail.com</tspan>
</text>

<text x="20" y="420">
<tspan class="orange">GitHub</tspan>
<tspan class="link" dx="35">github.com/itsmesaadali</tspan>
</text>

<!-- Footer -->
<text x="20" y="475">
<tspan class="green">PS D:\\itsmesaadali&gt;</tspan>
<tspan class="yellow"> coming soon...</tspan>
<tspan class="green"> █</tspan>
</text>

</svg>
"""

Path("info-card-light.svg").write_text(svg, encoding="utf-8")

print("✅ info-card-light.svg generated.")