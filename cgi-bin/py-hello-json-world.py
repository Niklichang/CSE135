#!/usr/bin/env python3
import os
import json
from datetime import datetime

# Headers
print("Cache-Control: no-cache")
print("Content-Type: application/json\n")

# Data
now = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
ip = os.environ.get("REMOTE_ADDR", "Unknown")

message = {
    "title": "Hello, Python! Niklas here writing Python!",
    "heading": "Hello, Python!",
    "message": "This page was generated with the Python programming language",
    "time": now,
    "IP": ip
}

# Output JSON
print(json.dumps(message))
