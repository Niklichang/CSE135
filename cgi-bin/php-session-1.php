#!/usr/bin/env php-cgi
<?php
session_start();
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=utf-8");

if (isset($_POST['username'])) {
    $_SESSION['username'] = $_POST['username'];   // server-side session
}
$name = $_SESSION['username'] ?? '';
?>
<!doctype html>
<html>
<head><meta charset="utf-8"><title>PHP Session Page 1</title></head>
<body>
<h1>PHP Session Page 1</h1>
<p><b>Name:</b> <?= $name !== '' ? htmlspecialchars($name) : 'You do not have a name set' ?></p>

<form method="post" action="/cgi-bin/php-session-1.php" style="margin-top:10px">
  <label>Your name: <input name="username" value="<?= htmlspecialchars($name) ?>"></label>
  <button type="submit">Save to session</button>
</form>

<p style="margin-top:16px;"><a href="/">Home</a></p>
</body>
</html>
