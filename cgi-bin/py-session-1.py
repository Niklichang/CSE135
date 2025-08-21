#!/usr/bin/env python3
import os, sys, json, time, secrets
from html import escape
from urllib.parse import parse_qs

STORE = "/tmp"

def get_cookie(name):
    c = os.environ.get("HTTP_COOKIE", "")
    for part in c.split(";"):
        if "=" in part:
            k, v = part.strip().split("=", 1)
            if k == name: return v
    return None

def load_session(sid):
    try:
        with open(f"{STORE}/{sid}.json", "r") as f: return json.load(f)
    except Exception:
        return {}

def save_session(sid, data):
    with open(f"{STORE}/{sid}.json", "w") as f: json.dump(data, f)

sid = get_cookie("PYSESSID")
set_cookie = ""
if not sid:
    sid = secrets.token_hex(16)
    set_cookie = f"Set-Cookie: PYSESSID={sid}; Path=/; HttpOnly"

sess = load_session(sid)

# Read POST body
length = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
body = sys.stdin.read(length) if length > 0 else ""
if body:
    params = parse_qs(body, keep_blank_values=True)
    if "username" in params:
        u = params["username"][0].strip()
        if u != "":
            sess["username"] = u
            sess["ts"] = int(time.time())
            save_session(sid, sess)

name = sess.get("username", "")

print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=utf-8")
if set_cookie: print(set_cookie)
print()
print(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Python Session Page 1</title></head>
<body>
<h1>Python Session Page 1</h1>
<p><b>Name:</b> {escape(name) if name else 'You do not have a name set'}</p>

<p style="margin-top:16px;">
  <a href="/py-cgiform.html">Python CGI Form</a>
</p>

<form action="/cgi-bin/py-destroy-session.py" method="get" style="margin-top:16px;">
  <button type="submit">Destroy Session</button>
</form>
</body></html>""")
