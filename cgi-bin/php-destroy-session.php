<?php
session_start();
$_SESSION = [];
if (ini_get("session.use_cookies")) {
  $p = session_get_cookie_params();
  setcookie(session_name(), '', time()-42000, $p["path"], $p["domain"], $p["secure"], $p["httponly"]);
}
session_destroy();

header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=utf-8");
?>
<!doctype html>
<html>
<head><meta charset="utf-8"><title>PHP Session Destroyed</title></head>
<body>
<h1>Session Destroyed</h1>
<p><a href="/php-cgiform.html">Back to the PHP CGI Form</a></p>
<p><a href="/cgi-bin/php-session-1.php">Back to Page 1</a></p>
</body>
</html>
