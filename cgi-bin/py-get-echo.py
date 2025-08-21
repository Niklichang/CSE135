#!/usr/bin/env python3
import os
from html import escape
from urllib.parse import parse_qs

# Headers
print("Cache-Control: no-cache")
print("Content-Type: text/html\n")

# Query string
query = os.environ.get("QUERY_STRING", "")

# Parse into dictionary
params = parse_qs(query)

# HTML top
print("""<!DOCTYPE html>
<html><head><title>GET Request Echo</title></head>
<body><h1 align="center">GET Request Echo</h1>
<hr>""")

# Show query string
print(f"<b>Query String:</b> {escape(query)}<br />")

# Show parsed parameters
for key, values in params.items():
    for v in values:
        print(f"{escape(key)} = {escape(v)}<br />")

# HTML bottom
print("</body></html>")
