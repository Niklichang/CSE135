#!/usr/bin/env python3
import os
from html import escape

# Headers
print("Cache-Control: no-cache")
print("Content-Type: text/html\n")

# HTML top
print("""<!DOCTYPE html>
<html><head><title>Environment Variables</title></head>
<body><h1 align="center">Environment Variables</h1>
<hr>""")

# env vars
for key in sorted(os.environ.keys()):
    print(f"<b>{escape(key)}:</b> {escape(os.environ[key])}<br />")

# HTML bottom
print("</body></html>")
