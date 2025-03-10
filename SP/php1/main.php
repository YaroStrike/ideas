<?php

$data = require 'data.php';

function printList($array) {
    echo '<ul>';
    foreach ($array as $key => $value) {
        echo '<li>' . htmlspecialchars($key);
        if (is_array($value)) {
            printList($value);
        } else {
            echo ': ' . htmlspecialchars($value);
        }
        echo '</li>';
    }
    echo '</ul>';
}

printList($data);
?>