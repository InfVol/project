<?php
// Параметри підключення до бази даних
$servername = "";
$username = "";
$password = "";
$dbname = "";

// Встановлення з'єднання з базою даних
$conn = new mysqli($servername, $username, $password, $dbname);

// Перевірка з'єднання
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Запит для отримання останнього запису з таблиці
$sql = "SELECT * FROM table1 ORDER BY datetime DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Отримання даних з останнього запису
    $row = $result->fetch_assoc();

    // Перевірка умови для визначення, чи потрібен полив рослини
    $humidity_threshold = 60; // Поріг вологості, нижче якого потрібен полив
    $temperature_day_threshold = 30; // Поріг денної температури
    $light_intensity_threshold = 5000; // Поріг інтенсивності світла

    if ($row['humidity'] < $humidity_threshold &&
        $row['temperature_day'] > $temperature_day_threshold &&
        $row['light_intensity'] < $light_intensity_threshold) {
        // Потрібен полив
        echo "1";
    } else {
        // Полив не потрібен
        echo "0";
    }
} else {
    // У таблиці немає даних
    echo "No data in the table";
}

// Закриття з'єднання з базою даних
$conn->close();
?>