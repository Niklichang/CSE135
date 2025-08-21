#!/usr/bin/env php-cgi
<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html");

// Raw request body
$raw = file_get_contents("php://input");
?>
<!DOCTYPE html>
<html>
<head><title>General Request Echo</title></head>
<body>
<h1 align="center">General Request Echo</h1>
<hr>
<p><b>HTTP Protocol:</b> <?= htmlspecialchars($_SERVER['SERVER_PROTOCOL'] ?? '') ?></p>
<p><b>HTTP Method:</b> <?= htmlspecialchars($_SERVER['REQUEST_METHOD'] ?? '') ?></p>
<p><b>Query String:</b> <?= htmlspecialchars($_SERVER['QUERY_STRING'] ?? '') ?></p>
<p><b>Message Body:</b> <?= htmlspecialchars($raw) ?></p>
</body>
</html>
