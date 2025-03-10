<?php
// Заголовок (head)
$headBgColor = isset($_GET['bgcolor']) ? $_GET['bgcolor'] : 'fuchsia';
$headFontColor = isset($_GET['color']) ? $_GET['color'] : 'cyan';
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
echo "Красотка";
echo "</div>";

echo "<div style='color: $mainFontColor; font-size: $mainFontSize; background-color: $mainBgColor;'>";
echo "ИП Прокудин Кирилл Даватович ИНН: ";
echo "</div>";

echo "<div style='font-size: $headFontSize; background-color: $whiteBgColor;'>";
echo "союз нерушимый:";
echo "</div>";

echo "<div style='color: $whiteFontColor; font-size: $headFontSize; background-color: $blueBgColor;'>";
echo "республик свободных";
echo "</div>";

echo "<div style='color: $whiteFontColor; font-size: $headFontSize; background-color: $redBgColor;'>";
echo "всплотилась на веки великая русь";
?>