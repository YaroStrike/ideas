<?php
$handle = fopen("test.txt", "rt");
if ($handle) {
    $contents = '';
    while (!feof($handle)) { // пока (!прочитан($файл)) 
        $contents .= fread($handle, 4096); // буфер содержимого файла
    }
    fclose($handle);
    echo $contents;
} else {
    echo "Ошибка открытия файла, проверь путь";
}
?>