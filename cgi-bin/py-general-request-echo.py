#!/usr/bin/env python3
import os, sys
from html import escape

# Headers
print("Cache-Control: no-cache")
print("Content-Type: text/html\n")

# Get the env vars
protocol = os.environ.get("SERVER_PROTOCOL", "")
method   = os.environ.get("REQUEST_METHOD", "")
query    = os.environ.get("QUERY_STRING", "")

# Read raw body
length = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
body = sys.stdin.read(length) if length > 0 else ""

# Output HTML
print(f"""<!DOCTYPE html>
<html><head><title>General Request Echo</title></head>
<body><h1 align="center">General Request Echo</h1>
<hr>
<p><b>HTTP Protocol:</b> {escape(protocol)}</p>
<p><b>HTTP Method:</b> {escape(method)}</p>
<p><b>Query String:</b> {escape(query)}</p>
<p><b>Message Body:</b> {escape(body)}</p>
</body></html>""")
