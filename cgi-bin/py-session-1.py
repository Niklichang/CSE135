#!/usr/bin/env python3
import os, sys, json, time, secrets
from html import escape

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
        with open(f"{STORE}/{sid}.json", "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_session(sid, data):
    with open(f"{STORE}/{sid}.json", "w") as f:
        json.dump(data, f)

sid = get_cookie("PYSESSID")
set_cookie = ""
if not sid:
    sid = secrets.token_hex(16)
    set_cookie = f"Set-Cookie: PYSESSID={sid}; Path=/; HttpOnly"

sess = load_session(sid)

# read POST body
length = int(os.environ.get("CONTENT_LENGTH", "0") or "0")
body = sys.stdin.read(length) if length > 0 else ""

name = sess.get("username", "")
if body:
    # key=value&... parser
    for kv in body.split("&"):
        if "=" in kv:
            k, v = kv.split("=", 1)
            if k == "username":
                v = v.replace("+", " ")
                try:
                    v = bytes(v.replace("%", r"\x"), "utf-8").decode("unicode_escape")
                except Exception:
                    pass
                name = v
                break
    sess["username"] = name
    sess["ts"] = int(time.time())
    save_session(sid, sess)

print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=utf-8")
if set_cookie: print(set_cookie)
print()
print(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Python Session Page 1</title></head>
<body>
<h1>Python Session Page 1</h1>
<p><b>Name:</b> {escape(name) if name else 'You do not have a name set'}</p>

<form method="post" action="/cgi-bin/py-session-1.py" style="margin-top:10px">
  <label>Your name: <input name="username" value="{escape(name)}"></label>
  <button type="submit">Save to session</button>
</form>

<p style="margin-top:16px;"><a href="/">Home</a></p>
</body></html>""")
