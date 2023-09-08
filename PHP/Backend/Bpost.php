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
    // conexion
    require '../Componentes/conexionBD.php';
    // if else
    if ($conexion->connect_error) {
        die("Conexion fallida: ".$conexion->connect_error);
    } else {
        echo "<script>console.log('Conexion exitosa')</script>";

        // DATOS DEL INPUT
        $nombre = $_POST['nombre'];
        $descripcion = $_POST['descripcion'];
        $precio = $_POST['precio'];
        $colores = $_POST['colores'];
        $stock = $_POST['stock'];
        $promocion = $_POST['promocion'];

        
        $query = "INSERT INTO articulos (nombre, descripcion, precio, colores, stock, promocion) VALUES ('$nombre', '$descripcion', '$precio', '$colores', '$stock', '$promocion') ";

        $consulta = $conexion->query($query);

        if ($consulta) {
            echo "<script>alert('Producto ingresado correctamente');</script>";
            echo "Volviendo al registro...";
            header("refresh: 1; url=../Frontend/Fpost.php");
        } else {
            echo "<script>alert('Error al ingresar producto');</script>";
            echo "Volviendo al registro...";
            header("refresh: 1; url=../Frontend/Fpost.php");
        }

        $conexion->close();
    } 
    // datos conexion (else)
?>
</html>
