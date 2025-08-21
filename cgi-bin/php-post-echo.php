#!/usr/bin/env php-cgi
<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html");

// POST data
$raw = file_get_contents('php://input');

// Use $_POST if form-encoded
$params = $_POST;
if (empty($params) && !empty($raw)) {
    parse_str($raw, $params);
}
?>
<!DOCTYPE html>
<html>
<head><title>POST Request Echo</title></head>
<body>
<h1 align="center">POST Request Echo</h1>
<hr>
<b>Message Body:</b><br />
<ul>
<?php
foreach ($params as $k => $v) {
    if (is_array($v)) {
        foreach ($v as $vv) {
            echo "<li>" . htmlspecialchars($k) . " = " . htmlspecialchars($vv) . "</li>\n";
        }
    } else {
        echo "<li>" . htmlspecialchars($k) . " = " . htmlspecialchars($v) . "</li>\n";
    }
}
?>
</ul>
</body>
</html>
