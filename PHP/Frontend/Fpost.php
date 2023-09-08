<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Style/index.css">
    <link rel="stylesheet" href="../Style/navBar.css">
    <title>Ingresar Producto</title>
</head>
<body>
    <?php include "../Componentes/navBar.php";?>
    <h1>Ingresar Producto</h1>
    <form id="agregar" action="../Backend/Bpost.php" method="POST">
        <label for="nombre">Nombre&nbsp;<span>(*)</span></label>
        <input type="text" name="nombre" requiered pattern="[\w\s]{10,255}+">
        
        <label for="descripcion">Descripcion</label>
        <textarea type="text" name="descripcion" pattern="[\w\s]{10,255}"></textarea>
        
        <label for="precio">Precio&nbsp;<span>(*)</span></label>
        <input type="number" name="precio" required pattern="[0-9]{1,6}.[0-9]{,2}">
        
        <label for="colores">Colores</label>
        <input type="text" name="colores" pattern="[A-Za-z]{3,20}">

        <label for="stock">Stock&nbsp;<span>(*)</span></label>
        <input type="number" name="stock" required pattern="[0-9]{1,6}">

        <label for="promocion">Promoción</label>
        <input type="number" name="promocion" pattern="[0-9]{1,6}.[0-9]{,2}">

        <input id="boton" type="submit" value="Registrar">
    </form>
</body>
</html>