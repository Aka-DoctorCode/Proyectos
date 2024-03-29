import re
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import system
import registerKey

# Detalles de la cuenta de correo electrónico
mi_correo = registerKey.mi_correo
# Contraseña de aplicacion generada desde Gmail
mi_contraseña = registerKey.mi_contraseña
asunto = "Usuario registrado correctamente usando la aplicación register.py (Autor: Francisco)"
asuntoModificado = "Usuario modificado correctamente usando la aplicación register.py (Autor: Francisco)"
class CRUD:
    # Constructor de la clase
    def __init__(self):
        pass

    # Metodo para registrar usuario
    def registrar_usuario(self):
        correo = ""
        nombre_archivo = ("./BD/" + correo + ".txt")
        nombre = ""
        apellido = ""
        edad = ""
        pais = ""
        genero = ""
        telefono = ""
        
        # Validar el correo y si existe en la base de datos
        correoValido = False
        while(correoValido == False):
            correo = input("Ingrese el correo electrónico: ").lower()
            validar_correo = (r"[^@]+@[^@]+\.[^@]+")
            # Creación de archivo
            nombre_archivo = ("./BD/" + correo + ".txt")
            if (re.match(validar_correo, correo) and os.path.exists(nombre_archivo)):
                correoValido = False
                print("El correo ya existe")
                time.sleep(1.5)
                system("clear")
            elif (re.match(validar_correo, correo)):
                correoValido = True
                print("Correo valido")
                time.sleep(1.5)
            else:
                system("clear")
                correoValido = False
                print("Formato del correo invalido (xxx@xxx.x)")
                time.sleep(1.5)
        print("Verificando si el correo existe en la base de datos ...")
        time.sleep(1.5) 
        
        # Validar los otros datos
        nombreValido = False
        while(nombreValido == False):
            nombre = input("Nombre: ").capitalize()
            validar_nombre = (r"^[A-ZÁÉÍÓÚÑÜ]+([a-záéíóúñü]*)$")
            if (re.match(validar_nombre, nombre)):
                print("Nombre valido")
                nombreValido = True
                time.sleep(1.5)
            else:
                system("clear")
                nombreValido = False
                print("Solo use letras en el nombre")
                time.sleep(1.5)
        apellidoValido = False
        while(apellidoValido == False):
            apellido = input("Apellido: ").capitalize()
            validar_apellido = (r"^[A-ZÁÉÍÓÚÑÜ]+([a-záéíóúñü]*)$")
            if (re.match(validar_apellido, apellido)):
                print("Apellido valido")
                apellidoValido = True
                time.sleep(1.5)
            else:
                system("clear")
                apellidoValido = False
                print("Solo use letras en el apellido")
                time.sleep(1.5)
        edadValido = False
        while(edadValido == False):
            edad = input("Edad: ")
            validar_edad = (r"^([1-9]|[1-9][0-9])$")
            if (re.match(validar_edad, edad)):
                print("Edad valida")
                edadValido = True
                time.sleep(1.5)
            else:
                system("clear")
                edadValido = False
                print("Solo use números para la edad, edades mayores a 100 coloque 99")
                time.sleep(1.5)
        paisValido = False
        while(paisValido == False):
            pais = input("País: ")
            validar_pais = (r"^[a-záéíóúñüA-ZÁÉÍÓÚÑÜ]+(?:[\s-][a-záéíóúñüA-ZÁÉÍÓÚÑÜ]+)*$")
            if (re.match(validar_pais, pais)):
                print("Pais valido")
                paisValido = True
                time.sleep(1.5)
            else:
                system("clear")
                paisValido = False
                print("El pais no es valido")
                time.sleep(1.5)
        generoValido = False
        while(generoValido == False):
            genero = input("Género (M o F): ")
            validar_genero = (r"^[mfMF]$")
            if (re.match(validar_genero, genero)):
                print("Género valido")
                generoValido = True
                time.sleep(1.5)
            else:
                system("clear")
                generoValido = False
                print("Escriba M para masculino y F para femenino")
                time.sleep(1.5)
        telefonoValido = False
        while(telefonoValido == False):
            telefono = input("Teléfono: ")
            validar_telefono = (r"^\+\d{10,14}$")
            if (re.match(validar_telefono, telefono)):
                print("Teléfono valido")
                telefonoValido = True
                time.sleep(1.5)
            else:
                system("clear")
                telefonoValido = False
                print("El teléfono no es valido")
                time.sleep(1.5)

        # función creadora de archivo en modo W
        archivo = open(nombre_archivo, "w")
        archivo.write(f'Email: {correo}\n')
        archivo.write(f'Nombre: {nombre}\n')
        archivo.write(f'Apellido: {apellido}\n')
        archivo.write(f'Edad: {edad}\n')
        archivo.write(f'País: {pais}\n')
        archivo.write(f'Género: {genero}\n')
        archivo.write(f'Teléfono: {telefono}\n')
        archivo.close()

        # función para escribir la base de datos de usuarios
        archivo = open("./BD/usuarios.txt", "a")
        archivo.write(f'Email: {correo}\n')
        archivo.close()

        # Correo de confirmación
        mensaje = MIMEMultipart()
        mensaje['From'] = mi_correo
        mensaje['To'] = correo
        mensaje['Subject'] = asunto
        destinatario = [correo, "frankmolcas@gmail.com"]
        cuerpo = cuerpo =  f"¡Bienvenido!\n Gracias por resgistrarte en mi app de registros usando Python\n Usuario registrado correctamente\nCorreo Electronico: {correo}\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad} años\nPaís: {pais}\nGénero: {genero}\nTelefono: {telefono}"
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        # Iniciar sesión en el servidor SMTP de Gmail
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login(mi_correo, mi_contraseña)
        # Enviar correo electrónico
        texto = mensaje.as_string()
        servidor_smtp.sendmail(mi_correo, destinatario, texto)
        # Cerrar sesión en el servidor SMTP
        servidor_smtp.quit()
        print("Correos electrónicos enviados con éxito.")
        time.sleep(1.5)
        system("clear")

    # Función para mostrar el usuario
    def mostrar_usuario(self):
        opcion = ""
        # Loop de submenu ver usuarios
        while opcion != "1" and opcion != "2":
            opcion = input("Selecciona una opción:\n1. Ver Base de datos\n2. Ver un usuario\n")
            if opcion == "1":
                archivo = open("./BD/usuarios.txt", "r")
                contenido = archivo.read()
                print("Abrinedo Base de Datos")
                time.sleep(1.5)
                print(contenido)
                archivo.close()
                opcion = ""
                while opcion != "1":
                    opcion = input("Presione '1' para volver al menu inicial\n")
                    if opcion == "1":
                        print("Cerrando Base de Datos")
                        time.sleep(1.5)
                        system("clear")
                    else:
                        print("Opción inválida")
                        time.sleep(1.5)
                        system("clear")
            elif opcion == "2":
                Abrir_usuario = input("Ingrese el correo electrónico del usuario que desea abrir: ").lower()
                usuario_abierto = open(f"./BD/{Abrir_usuario}.txt", "r")
                print(f"Abriendo usuario {Abrir_usuario}")
                time.sleep(1.5)
                print(usuario_abierto.read())
                usuario_abierto.close()
                opcion = ""
                while opcion != "1":
                    opcion = input("Presione '1' para volver al menu inicial\n")
                    if opcion == "1":
                        print("Cerrando Base de Datos")
                        time.sleep(1.5)
                        system("clear")
                    else:
                        print("Opción inválida")
                        time.sleep(1.5)
                        system("clear")
            else:
                print("Opción inválida")
                time.sleep(1.5)
                system("clear")

    # Metodo para editar usuario
    def editar_usuario(self):
        correo = ""
        Selecionar_usuario =""
        Nuevo_correo = ""
        nombre = ""
        apellido = ""
        edad = ""
        pais = ""
        genero = ""
        telefono = ""
        lista = ""

        # Metodo para validar si existe el correo en la base de datos
        usuario_existe = False
        while(usuario_existe == False):
            Selecionar_usuario = input("Ingrese el correo electrónico del usuario que desea editar: ").lower()
            if os.path.exists(f"./BD/{Selecionar_usuario}.txt"):
                print("Verificando si el correo existe en la base de datos ...")
                time.sleep(1.5)
                print("El correo existe en la base de datos")
                usuario_existe = True
                usuario_abierto = open(f"./BD/{Selecionar_usuario}.txt", "r")
                contenido_usuario = usuario_abierto.read()
                usuario_abierto.close()
                # extraer los pares clave valor de cada linea del documento y guardarlo en un lista      
                lista = contenido_usuario.split("\n")
            else:
                system("clear")
                usuario_existe = False 
                print("El correo no existe en la base de datos")
                time.sleep(1.5)
        
        # Metodo para validar el nuevo correo
        verificarCorreo = False
        while (verificarCorreo == False):
            Nuevo_correo = input("Nuevo correo: ").lower()
            validar_correo = (r"[^@]+@[^@]+\.[^@]+")
            if (re.match(validar_correo, Nuevo_correo) and os.path.exists(f"./BD/{Nuevo_correo}.txt")):
                print("Nuevo Correo Valido")
                time.sleep(1.5)
                system("clear")
                time.sleep(1.5)
                print("El correo ya existe en la base de datos")
                verificarCorreo = False
            elif (re.match(validar_correo, Nuevo_correo)):
                print("Nuevo Correo Valido")
                correo = Nuevo_correo
                verificarCorreo = True
                time.sleep(1.5)
                print("El correo no existe en la base de datos")
                time.sleep(1.5)
                print(f"El correo se cambiara a: {Nuevo_correo}")
            elif (Nuevo_correo == ""):
                split = lista[0].split(": ")
                correo = split[1]
                verificarCorreo = True
                time.sleep(1.5)
                print(f"El correo se mantendra como: {correo}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarCorreo = False
                print("Formato del correo invalido (xxx@xxx.x)")
                time.sleep(1.5)

        # Cambio de nombre del archivo
        if (Selecionar_usuario != correo):
            os.rename(f"./BD/{Selecionar_usuario}.txt", f"./BD/{correo}.txt")
            print(f"Correo cambiado exitosamente a {Nuevo_correo}")

        # Validar los otros datos
        verificarNombre = False
        while (verificarNombre == False):
            Nuevo_nombre = input("Nuevo nombre: ").capitalize()
            validar_nombre = (r"^[A-ZÁÉÍÓÚÑÜ]+([a-záéíóúñü]*)$")
            if (re.match(validar_nombre, Nuevo_nombre)):
                print("Nuevo Nombre Valido")
                nombre = Nuevo_nombre
                verificarNombre = True
                time.sleep(1.5)
                print(f"El nombre se cambaira a: {Nuevo_nombre}")
                time.sleep(1.5)
            elif (Nuevo_nombre == ""):
                split = lista[1].split(": ")
                nombre = split[1]
                verificarNombre = True
                print(f"El nombre se mantendra como: {nombre}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarNombre = False
                print("Solo use letras en el nombre")
                time.sleep(1.5)
        
        verificarApellido = False
        while (verificarApellido == False):
            Nuevo_apellido = input("Nuevo apellido: ").capitalize()
            validar_apellido = (r"^[A-ZÁÉÍÓÚÑÜ]+([a-záéíóúñü]*)$")
            if (re.match(validar_apellido, Nuevo_apellido)):
                print("Nuevo Apellido Valido")
                apellido = Nuevo_apellido
                verificarApellido = True
                time.sleep(1.5)
                print(f"El apellido se cambaira a: {Nuevo_apellido}")
                time.sleep(1.5)
            elif (Nuevo_apellido == ""):
                split = lista[2].split(": ")
                apellido = split[1]
                verificarApellido = True
                print(f"El apellido se mantendra como: {apellido}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarApellido = False
                print("Solo use letras en el apellido")
                time.sleep(1.5)

        verificarEdad = False
        while (verificarEdad == False):
            Nueva_edad = input("Nueva edad: ")
            validar_edad = (r"^([1-9]|[1-9][0-9])$")
            if (re.match(validar_edad, Nueva_edad)):
                print("Nueva Edad Valida")
                edad = Nueva_edad
                verificarEdad = True
                time.sleep(1.5)
                print(f"La edad se cambiara a: {Nueva_edad}")
                time.sleep(1.5)
            elif (Nueva_edad == ""):
                split = lista[3].split(": ")
                edad = split[1]
                verificarEdad = True
                print(f"La edad se mantendra como: {edad}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarEdad = False
                print("Solo use numeros en la edad, si la edad es mayor a 100 escriba 99")
                time.sleep(1.5)
        
        verificarPais = False
        while (verificarPais == False):
            Nuevo_pais = input("Nuevo pais: ")
            validar_pais = (r"^[a-záéíóúñüA-ZÁÉÍÓÚÑÜ]+(?:[\s-][a-záéíóúñüA-ZÁÉÍÓÚÑÜ]+)*$")
            if (re.match(validar_pais, Nuevo_pais)):
                print("Nuevo Pais Valido")
                pais = Nuevo_pais
                verificarPais = True
                time.sleep(1.5)
                print(f"El pais se cambiara a: {Nuevo_pais}")
                time.sleep(1.5)
            elif (Nuevo_pais == ""):
                split = lista[4].split(": ")
                pais = split[1]
                verificarPais = True
                print(f"El pais se mantendra como: {pais}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarPais = False
                print("Solo use letras en el pais")
                time.sleep(1.5)
        
        verificarGenero = False
        while (verificarGenero == False):
            Nuevo_genero = input("Nuevo genero: ")
            validar_genero = (r"^[mfMF]$")
            if (re.match(validar_genero, Nuevo_genero)):
                print("Nuevo Genero Valido")
                genero = Nuevo_genero
                verificarGenero = True
                time.sleep(1.5)
                print(f"El genero se cambiara a: {Nuevo_genero}")
                time.sleep(1.5)
            elif (Nuevo_genero == ""):
                split = lista[5].split(": ")
                genero = split[1]
                verificarGenero = True
                print(f"El genero se mantendra como: {genero}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarGenero = False
                print("Solo use letras en el genero")
                time.sleep(1.5)
        
        verificarTelefono = False
        while (verificarTelefono == False):
            Nuevo_telefono = input("Nuevo telefono: ")
            validar_telefono = (r"^\+\d{10,14}$")
            if (re.match(validar_telefono, Nuevo_telefono)):
                print("Nuevo Telefono Valido")
                telefono = Nuevo_telefono
                verificarTelefono = True
                time.sleep(1.5)
                print(f"El telefono se cambiara a: {Nuevo_telefono}")
                time.sleep(1.5)
            elif (Nuevo_telefono == ""):
                split = lista[6].split(": ")
                telefono = split[1]
                verificarTelefono = True
                print(f"El telefono se mantendra como: {telefono}")
                time.sleep(1.5)
            else:
                system("clear")
                verificarTelefono = False
                print("Formato del telefono invalido (xxx@xxx.x)")
                time.sleep(1.5)

        # #función modificadora de archivo en modo w
        archivo = open(f"./BD/{correo}.txt", "w")
        archivo.write(f'Email: {correo}\n')
        archivo.write(f'Nombre: {nombre}\n')
        archivo.write(f'Apellido: {apellido}\n')
        archivo.write(f'Edad: {edad}\n')
        archivo.write(f'País: {pais}\n')
        archivo.write(f'Género: {genero}\n')
        archivo.write(f'Teléfono: {telefono}\n')
        archivo.close()

        split = lista[0].split(": ")

        # # Función para cambiar el correo electrónico en usuario.txt
        with open("./BD/usuarios.txt", "r") as usuarios:
            contenido = usuarios.readlines()
        for i, linea in enumerate(contenido):
            if lista[0] in linea:
                contenido[i] = f"Email: {Nuevo_correo} / {split[1]} \n"
        with open("./BD/usuarios.txt", "w") as usuarios:
            usuarios.writelines(contenido)
        print("Correo electrónico modificado y guardado en la base de datos")
        time.sleep(1.5)
        system("clear")

        # Correo de confirmación
        mensaje = MIMEMultipart()
        mensaje['From'] = mi_correo
        mensaje['To'] = correo
        mensaje['Subject'] = asuntoModificado
        destinatario = [correo, "frankmolcas@gmail.com"]
        cuerpo = cuerpo = f"Usuario modificado '{lista[0]}' correctamente\nCorreo Electronico: {correo}\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad} años\nPaís: {pais}\nGénero: {genero}\nTelefono: {telefono}"
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        # Iniciar sesión en el servidor SMTP de Gmail
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login(mi_correo, mi_contraseña)
        # Enviar correo electrónico
        texto = mensaje.as_string()
        servidor_smtp.sendmail(mi_correo, destinatario, texto)
        # Cerrar sesión en el servidor SMTP
        servidor_smtp.quit()
        print("Correos electrónicos enviados con éxito.")
        time.sleep(1.5)
        system("clear")
        
        opcion = ""
        while opcion != "1":
            opcion = input("Presione '1' para volver al menu inicial\n")
            if opcion == "1":
                print("Cerrando Base de Datos")
                time.sleep(1.5)
                system("clear")
            else:
                print("Opción inválida")
                time.sleep(1.5)
                system("clear")

    # Metodo para eliminar un usuario
    def eliminar_usuario(self):
        Usuario_a_elimnar = input("Ingrese el correo electrónico del usuario que desea eliminar: ").lower()
        os.remove(f"./BD/{Usuario_a_elimnar}.txt")
        with open("./BD/usuarios.txt", "r") as usuarios:
            contenido = usuarios.readlines()
        for i, linea in enumerate(contenido):
            if Usuario_a_elimnar in linea:
                contenido[i] = f"Correo eliminado: {Usuario_a_elimnar}\n"
        with open("./BD/usuarios.txt", "w") as usuarios:
            usuarios.writelines(contenido)
        print(f'Usuario {Usuario_a_elimnar} eliminado de la base de datos')
        time.sleep(1.5)
        opcion = ""
        while opcion != "1":
            opcion = input("Presione '1' para volver al menu inicial\n")
            if opcion == "1":
                print("Cerrando Base de Datos")
                time.sleep(1.5)
                system("clear")
            else:
                print("Opción inválida")
                time.sleep(1.5)
                system("clear")

    # Función lectura base de datos
    def ver_basededatos(self):
        archivo = open("./BD/usuarios.txt", "r")
        print("Abriendo base de datos")
        time.sleep(1.5)
        print(archivo.readlines())
        archivo.close()
        opcion = ""
        while opcion != "1":
            opcion = input("Presione '1' para cerrar base de datos\n")
            if opcion == "1":
                print("Cerrando Base de Datos")
                time.sleep(1.5)
                system("clear")
            else:
                print("Opción inválida")
                time.sleep(1.5)
                system("clear")
    
    # Función salir
    def salir(self):
        system("clear")
        print("Gracias por usar nuestro programa")

miCrud = CRUD()
Opciones = {
    "1": miCrud.registrar_usuario,
    "2": miCrud.mostrar_usuario,
    "3": miCrud.editar_usuario,
    "4": miCrud.eliminar_usuario,
    "5": miCrud.ver_basededatos,
    "6": miCrud.salir
}
while True:
    opcion = input("1. Registrar usuario\n2. Mostrar usuario\n3. Editar usuario\n4. Eliminar Usuario\n5. Ver base de datos de usuarios\n6. Salir\n")
    if opcion == '6':
        system("clear")
        print("Gracias por usar esta APP")
        break
    elif opcion in Opciones:
        Opciones[opcion]()
    else:
        system("clear")
        print("Opción inválida. Por favor, ingrese una opción válida.")
        time.sleep(1.5)