<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Style/index.css">
    <link rel="stylesheet" href="../Style/navBar.css">
    <title>Modificar Producto</title>
</head>
<body>
    <?php include "../Componentes/navBar.php";?>
    <h1>Modificar Producto</h1>
    <form action="../Backend/BputGet.php" method="post">
        <label for="buscar">Nombre&nbsp;<span>(*)</span></label>
        <input type="text" name="buscar" requiered pattern="[\w\s]{10,255}">
        <input id="boton" type="submit" value="Buscar Producto">
    </form>
</body>
</html>