<?php
// Headers
header("Cache-Control: no-cache");
header("Content-Type: application/json");

// Data
$date = date("r");
$ip   = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';

// Message
$message = [
    "title"   => "Hello, PHP! Niklas here writing PHP!",
    "heading" => "Hello, PHP!",
    "message" => "This page was generated with the PHP programming language",
    "time"    => $date,
    "IP"      => $ip
];

// Output JSON
echo json_encode($message);
