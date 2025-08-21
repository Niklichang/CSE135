#!/usr/bin/env python3
import os, sys
from urllib.parse import parse_qs
from html import escape

# Headers
print("Cache-Control: no-cache")
print("Content-Type: text/html\n")

# Read POST body
length = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
body = sys.stdin.read(length) if length > 0 else ""

# Parse key=value
params = parse_qs(body, keep_blank_values=True)

# HTML output
print("""<!DOCTYPE html>
<html><head><title>POST Request Echo</title></head>
<body><h1 align="center">POST Request Echo</h1>
<hr>
<b>Message Body:</b><br />
<ul>""")

for key, values in params.items():
    for v in values:
        print(f"<li>{escape(key)} = {escape(v)}</li>")

print("""</ul>
</body></html>""")
