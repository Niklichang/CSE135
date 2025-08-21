#!/usr/bin/env php-cgi
<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html");
?>
<!DOCTYPE html>
<html>
<head><title>Environment Variables</title></head>
<body>
<h1 align="center">Environment Variables</h1>
<hr>
<?php

foreach ($_SERVER as $key => $value) {
    echo "<b>" . htmlspecialchars($key) . ":</b> " . htmlspecialchars($value) . "<br />\n";
}
?>
</body>
</html>
