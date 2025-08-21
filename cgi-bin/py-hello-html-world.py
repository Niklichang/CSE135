#!/usr/bin/env python3
import os
from datetime import datetime
from html import escape

# Headers
print("Cache-Control: no-cache")
print("Content-Type: text/html\n")

# Data
now = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
ip = os.environ.get("REMOTE_ADDR", "Unknown")

# Output
print("""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Hello, Python!</title></head>
<body>
  <h1>Niklas was here writing Python - Hello, Python!</h1>
  <p>This page was generated with the Python programming language</p>
  <p>Current Time: {now}</p>
  <p>Your IP Address: {ip}</p>
</body>
</html>""".format(now=escape(now), ip=escape(ip)))
