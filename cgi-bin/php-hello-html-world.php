#!/usr/bin/env php-cgi
<?php
// Headers
header("Cache-Control: no-cache");
header("Content-Type: text/html");

// Data
$date = date("r");
$ip   = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';

// Output
?>
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Hello, PHP!</title></head>
<body>
  <h1>Niklas was here writing PHP - Hello, PHP!</h1>
  <p>This page was generated with the PHP programming language</p>
  <p>Current Time: <?= htmlspecialchars($date, ENT_QUOTES, 'UTF-8') ?></p>
  <p>Your IP Address: <?= htmlspecialchars($ip, ENT_QUOTES, 'UTF-8') ?></p>
</body>
</html>
