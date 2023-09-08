<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./Style/index.css">
    <link rel="stylesheet" href="./Style/navBar.css">
    <title>Control de Inventario</title>
</head>

<body>
    <?php
        include "Componentes/navBar.php";
    ?>
    <h1>Gestion de inventario de Tienda</h1>
    <form action="login.php">
        <label for="usuario">Usuario&nbsp;<span>(*)</span></label>
        <input type="text" name="usuario">
        <label for="password">Password&nbsp;<span>(*)</span></label>
        <input type="password" name="password">
        <input id="boton" type="submit" value="Iniciar Sesion">
    </form>

</body>
</html>