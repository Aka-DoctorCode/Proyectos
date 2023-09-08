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
    require "../Componentes/conexionBD.php";
    if ($conexion->connect_error){
        die ("La conexion fallo: " . $conexion->connect_error);
    } else {
        echo "<script>console.log('Conexion exitosa')</script>";
        

        // Capturamos la información
        $nombre = $_POST['producto'];
        $descripcionNuevo = $_POST['descripcionNuevo'];
        $precioNuevo = $_POST['precioNuevo'];
        $coloresNuevo = $_POST['coloresNuevo'];
        $stockNuevo = $_POST['stockNuevo'];
        $promocionNuevo = $_POST['promocionNuevo'];
        // consulta
        $sql = "UPDATE articulos 
            SET descripcion = '$descripcionNuevo', precio = '$precioNuevo', colores = '$coloresNuevo', stock = '$stockNuevo', promocion = '$promocionNuevo'
            WHERE nombre = '$nombre'"
        ;
        // ejecutamos consulta
        $resultado = $conexion->query($sql);
        // Guardamos el total de filas afectadas.
        $filasAfectadas = $conexion->affected_rows;
        // Verificamos si se afecto una fila
        if ($filasAfectadas > 0) {
            echo "<script>alert('Producto modificado correctamente');</script>";
            echo "Volviendo a Modificar...";
            header("refresh: 1; url=../Frontend/FputGet.php");
            $conexion->close();
        }else{
            echo "<p>Ocurrio un evento inesperado al actualizar el usuario o no se pudo actualizar.</p>";
            echo "Volviendo a Modificar...";
            header("refresh: 1; url=../Frontend/FputGet.php");
            $conexion->close();
        }
    }
?>
</html>
