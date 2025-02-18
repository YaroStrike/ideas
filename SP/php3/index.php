<?php
function showForm($action = "", $method = "post"){
    require 'form.html';
}
showForm("process_form.php", "post");
?>