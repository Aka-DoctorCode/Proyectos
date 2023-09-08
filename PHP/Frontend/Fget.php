<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../Style/index.css">
        <link rel="stylesheet" href="../Style/navBar.css">
        <title>Productos</title>
    </head>
    <body>
        <?php include "../Componentes/navBar.php";?>
        <h1>Productos de la tienda</h1>
        <section>
        <?php
            // conexion
            require '../Componentes/conexionBD.php';
            // if else
            if ($conexion->connect_error) {
                die("Conexion fallida: ".$conexion->connect_error);
            } else {
                echo "<script>console.log('Conexion exitosa')</script>";
                // consulta de busqueda
                $sql = "SELECT * FROM articulos";
                // ejecución de la consulta
                $resultado = $conexion->query($sql);
                // validadcion de resulados
                if($resultado->num_rows > 0){
                    // extraccion de datos
                    echo "<div class='table'>";
                        echo "<table>";
                            echo "<tr>";
                                echo "<th>ID</th>";
                                echo "<th>Nombre</th>";
                                echo "<th>Descripcion</th>";
                                echo "<th>Precio</th>";
                                echo "<th>Colores</th>";
                                echo "<th>Stock</th>";
                                echo "<th>Promocion</th>";
                                echo "<th>Registrado</th>";
                            echo "</tr>";
                            while($fila = $resultado->fetch_assoc()){
                                $id = $fila['id'];
                                $nombre = $fila['nombre'];
                                $descripcion = $fila['descripcion'];
                                $precio = $fila['precio'];
                                $colores = $fila['colores'];
                                $stock = $fila['stock'];
                                $promocion = $fila['promocion'];
                                $resgistrado = $fila['registrado'];

                                echo "<tr>";
                                    echo "<td>".$id."</td>";
                                    echo "<td>".$nombre."</td>";
                                    echo "<td>".$descripcion."</td>";
                                    echo "<td>$ ".$precio."</td>";
                                    echo "<td>".$colores."</td>";
                                    echo "<td>".$stock."</td>";
                                    echo "<td>$ ".$promocion."</td>";
                                    echo "<td>".$resgistrado."</td>";
                                echo "</tr>"; 
                        }
                        echo "</table>";
                    echo "</div>";
                }else{
                    echo "<h1>No hay productos</h1>";
                }

                $resultado->free();
                $conexion->close();
            }
        ?>
        </section>
    </body>
</html>
