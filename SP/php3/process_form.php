<?php
$headBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'fuchsia';
$headFontColor = isset($_GET['color']) ? $_GET['color'] : 'cyan';
$fuchFontColor = isset($_GET['color']) ? $_GET['color'] : 'fuchsia';
$headFontSize = isset($_GET['size']) ? $_GET['size'] : '64px';
// Подзаголовок (main)
$mainBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'black';
$mainFontColor = isset($_GET['color']) ? $_GET['color'] : 'yellow';
$mainFontSize = isset($_GET['size']) ? $_GET['size'] : '48px';
// триколор
$whiteBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'white';
$blueBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'blue';
$redBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'red';
$whiteFontColor = isset($_GET['color']) ? $_GET['color'] : 'white';

echo "<div style='color: $headFontColor; font-size: $headFontSize; background-color: $headBgColor;'>";
echo "        *  Красотка  * ";
echo "</div>";

echo "<div style='color: $mainFontColor; font-size: $mainFontSize; background-color: $mainBgColor;'>";
echo "ИП Прокудин Кирилл Даватович ИНН: 2204433777";
echo "</div>";

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $name = $_POST['name'];
    $family = $_POST['family'];
    $email = $_POST['email'];
    $passw = $_POST['passw'];
    $hashPassw = password_hash($passw, PASSWORD_DEFAULT); 
    echo "<div style='color: $headFontColor; font-size: $mainFontSize; background-color: $mainBgColor;'>";
    echo "Добро пожаловать на сайт красотки " . htmlspecialchars($name) . " " . htmlspecialchars($family) . "!!" . "<br>";
    echo "</div>";
    echo "<div style='color: $fuchFontColor; font-size: $mainFontSize; background-color: $mainBgColor;'>";
    echo "Вы будете получать от нас очень полезные уведомления об акциях и скидках на вашу почту - " . htmlspecialchars($email) . " по утрам!!" . "<br>";
    echo "И пожалуйста, запишите ваш пароль на листочек: ". htmlspecialchars($hashPassw);
}
?>