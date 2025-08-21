<?php
session_start();
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=utf-8");

// Accept name if posted from the form
if (isset($_POST['username'])) {
    $_SESSION['username'] = $_POST['username'];
}
$name = $_SESSION['username'] ?? '';
?>
<!doctype html>
<html>
<head><meta charset="utf-8"><title>PHP Session Page 1</title></head>
<body>
<h1>PHP Session Page 1</h1>
<p><b>Name:</b> <?= $name !== '' ? htmlspecialchars($name) : 'You do not have a name set' ?></p>

<p style="margin-top:16px;">
  <a href="/php-cgiform.html">PHP CGI Form</a>
</p>

<form action="/cgi-bin/php-destroy-session.php" method="get" style="margin-top:16px">
  <button type="submit">Destroy Session</button>
</form>
</body>
</html>
