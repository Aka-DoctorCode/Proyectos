<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Style/index.css">
    <link rel="stylesheet" href="../Style/navBar.css">
    <title>Document</title>
</head>
<?php
    include "../Componentes/navBar.php";
    // componente de conexion
    require '../Componentes/conexionBD.php';
    // if else
    if ($conexion->connect_error) {
        die("Conexion fallida: ".$conexion->connect_error);
    } else {
        echo "<script>console.log('Conexion exitosa')</script>";
        // variable de busqueda
        $buscar = $_POST['buscar'];
        // definir consulta SQL
        $sql = "SELECT * FROM articulos WHERE nombre='$buscar'";
        // almacenar datos de la consulta
        $resultado = $conexion->query($sql);
        // verificamos si hay resultados
        if ($resultado->num_rows >= 1) {
            while ($campo = $resultado->fetch_assoc()){
                //  Variblaes para el DOM
                    $id = $campo['id'];
                    $nombre = $campo['nombre'];
                    $descripcion = $campo['descripcion'];
                    $precio = $campo['precio'];
                    $colores = $campo['colores'];
                    $stock = $campo['stock'];
                    $promocion = $campo['promocion'];
                    $resgistrado = $campo['registrado'];
            }}else{
                echo "No exite el producto";
            }
        // Liberamos la memoria de cualquier dato valioso obtenido.
        $resultado->free();
        // Cerramos la conexion
        $conexion->close();  
    }
?>
<h1><?php echo $nombre?></h1>
<form id="agregar" action="./Bput.php" method="POST">
        <label for="descripcionNuevo">Descripcion&nbsp;<span>(*)</span></label>
        <input type="text" name="descripcionNuevo" value="<?php echo $descripcion ?>" required pattern="[\w\s]{10,255}">
        <label for="precioNuevo">Precio&nbsp;<span>(*)</span></label>
        <input type="number" name="precioNuevo" value="<?php echo $precio ?>" required pattern="[0-9]{1,6}.[0-9]{,2}">
        <label for="coloresNuevo">Colores&nbsp;<span>(*)</span></label>
        <input type="text" name="coloresNuevo" value="<?php echo $colores ?>" required pattern="[A-Za-z]{3,20}">
        <label for="stockNuevo">Stock&nbsp;<span>(*)</span></label>
        <input type="number" name="stockNuevo" value="<?php echo $stock ?>" required pattern="[0-9]{1,6}">
        <label for="promocionNuevo">Promoción&nbsp;<span>(*)</span></label>
        <input type="number" name="promocionNuevo" value="<?php echo $promocion ?>" required pattern="[0-9]{1,6}.[0-9]{,2}">
        <input id="ocultar" type="text" name="producto" value="<?php echo $nombre ?>">
        <input id="boton" type="submit" value="Registrar">
</form>
</html>
