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
            // captura datos
            $eliminar = $_POST['eliminar'];
            // query de busqueda
            $sql1 = "SELECT * FROM articulos where nombre = '$eliminar'";
            // ejecución de la consulta de busqueda
            $resultado1 = $conexion->query($sql1);
            // validacion si existe el producto
            if($resultado1->num_rows == 1){
                // query de eliminacion
                $sql2 = "DELETE FROM articulos WHERE nombre = '$eliminar'";
                // ejecución de la consulta de eliminacion
                $resultado2 = $conexion->query($sql2);
                // validacion si el producto fue eliminado
                if($resultado2){
                    include "../Componentes/navBar.php";
                    echo "<h1>PRODUCTO ELMINADO DE LA BASE DE DATOS</h1>";
                    echo "Volviendo a elminar...";
                header("refresh: 1; url=../Frontend/Fdelete.php");
                }else {
                    include "../Componentes/navBar.php";
                    echo "<h1> Error al elminar el producto</h1>".$conexion->error;
                    echo "Volviendo a eliminar...";
                header("refresh: 1; url=../Frontend/Fdelete.php");
                }
            }else{
                echo "<h1>Producto no encontrado</h1>";
            }
        $conexion->close();
        }
?>
</html>
