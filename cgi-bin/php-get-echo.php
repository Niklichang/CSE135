<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html");
?>
<!DOCTYPE html>
<html>
<head><title>GET Request Echo</title></head>
<body>
<h1 align="center">GET Request Echo</h1>
<hr>
<?php

$query = $_SERVER['QUERY_STRING'] ?? '';
echo "<b>Query String:</b> " . htmlspecialchars($query) . "<br />\n";

// Parse parameters
if (!empty($_GET)) {
    foreach ($_GET as $key => $value) {
        echo htmlspecialchars($key) . " = " . htmlspecialchars($value) . "<br />\n";
    }
}
?>
</body>
</html>
