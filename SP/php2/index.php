<?php
$handle = fopen("test.txt", "rt");
if ($handle) {
    $contents = '';
    while (!feof($handle)) {
        $contents .= fread($handle, 4096);
    }
    fclose($handle);
    echo $contents;
} else {
    echo "Ошибка открытия файла, проверь путь";
}
?>