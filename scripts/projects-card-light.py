from pathlib import Path

WIDTH = 900
HEIGHT = 240

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

.blue {{
    fill:#0969da;
    font-weight:bold;
}}

.green {{
    fill:#1a7f37;
    font-weight:bold;
}}

.orange {{
    fill:#bc4c00;
    font-weight:bold;
}}

.white {{
    fill:#24292f;
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

<!-- Heading -->
<text x="20" y="32" class="blue">
─ Featured Projects ───────────────────────────────────────────────────────────────────────────────
</text>

<!-- Project 1 -->
<text x="20" y="70">
<tspan class="green">•</tspan>
<tspan class="orange"> Tailflow - Next-Gen Team Collaboration</tspan>
</text>

<text x="38" y="95" class="white">
High-performance platform streamlining team workflows with real-time connectivity and AI organization.
</text>

<!-- Project 2 -->
<text x="20" y="135">
<tspan class="green">•</tspan>
<tspan class="orange"> Movie Portfolio Platform</tspan>
</text>

<text x="38" y="160" class="white">
Sophisticated movie discovery interface featuring dynamic sliders, ratings, and watchlist functionality.
</text>

<!-- Project 3 -->
<text x="20" y="200">
<tspan class="green">•</tspan>
<tspan class="orange"> AI Web Scraper &amp; Research Engine</tspan>
</text>

<text x="38" y="225" class="white">
AI-driven tool to transform websites into structured knowledge via single or bulk processing.
</text>

</svg>
"""

Path("projects-card-light.svg").write_text(svg, encoding="utf-8")

print("projects-card-light.svg generated.")