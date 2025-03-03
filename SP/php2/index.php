<?php
$priv = isset($_GET['priv']) ? $_GET['priv'] : 'приветствие';
$name = isset($_GET['name']) ? $_GET['name'] : 'Имя';
$color = isset($_GET['color']) ? $_GET['color'] : 'black';
$title = "сайт привет герман";
?>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title><?= $title ?></title>
</head>
<body style="display: flex; flex-direction: column;align-items: center; width: 100vw">
<form action="" method="GET" style="display: flex; flex-direction: column; width: 50%">
    <h1 style="color: <?= $color ?>"><?= $priv ?> <?= $name ?></h1>
    <select name="name">
        <option value="Герман!">Герман</option>
        <option value="Кирилл!">Кирилл</option>
        <option value="Лёня!">Лёня</option>
    </select>
    <label for="priv">Приветствие:</label>
    <input type="text" id="priv" name="priv" required><br><br>
    <input type="radio" name="color" id="color1" value="red">
    <label for="color1">Красный</label>
    <input type="radio" checked name="color" id="color2" value="black">
    <label for="color2">Черный</label>
    <input type="radio" name="color" id="color3" value="green">
    <label for="color3">Зеленый</label>
    <input type="submit" value="Отправить">
</form>
</body>
</html>