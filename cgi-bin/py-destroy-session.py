#!/usr/bin/env python3
import os, pathlib

STORE = "/tmp"

def get_cookie(name):
    c = os.environ.get("HTTP_COOKIE", "")
    for part in c.split(";"):
        if "=" in part:
            k, v = part.strip().split("=", 1)
            if k == name: return v
    return None

sid = get_cookie("PYSESSID")
if sid:
    p = pathlib.Path(f"{STORE}/{sid}.json")
    try: p.unlink()
    except FileNotFoundError: pass

print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=utf-8")
print("Set-Cookie: PYSESSID=; Path=/; HttpOnly; Max-Age=0")
print()
print("""<!doctype html>
<html><head><meta charset="utf-8"><title>Python Session Destroyed</title></head>
<body>
<h1>Session Destroyed</h1>
<p><a href="/py-cgiform.html">Back to the Python CGI Form</a></p>
<p><a href="/cgi-bin/py-session-1.py">Back to Page 1</a></p>
</body>
</html>""")
