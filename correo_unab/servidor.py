from usuario import Usuario
import re

class Servidor:                     #La clase servidor se encarga de articular las clases Mensaje y Usuario.Nos provee de un Menu para crear los usuarios
    def __init__(self):              #Los guarda en una lista para luego poder acceder a ellos y utilizar sus correspondientes atributos
        self.usuarios = []

    def iniciar_sesion(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        
        usuario_actual = next((u for u in self.usuarios if u.correo == correo and u.contraseña == contraseña), None)

        if not usuario_actual:
            print("usuario incorrecto.")
            return
        
        print(f"\n¡Bienvenido/a {usuario_actual.nombre}!")

        while True:
            try:
                opcion = int(input("""
¿Qué deseas hacer?
(1) Enviar un mensaje
(2) Ver bandeja de entrada
(3) Ver bandeja de salida
(4) Mover mensaje entre carpetas
(5) Buscar mensaje
(6) Agregar subcarpetas
(7) Salir
Opción: """))

                if opcion == 1:
                    destinatario_correo = input("Correo del destinatario: ")
                    destinatario = next((u for u in self.usuarios if u.correo == destinatario_correo), None)
                    
                    if not destinatario:
                        print("Destinatario no encontrado.")
                        continue #

                    asunto = input("Asunto del mensaje: ")
                    contenido = input("Contenido del mensaje: ")
                    usuario_actual.enviar_mensaje(destinatario, asunto, contenido)

                elif opcion == 2:
                    usuario_actual.mostrar_bandeja_entrada()

                elif opcion == 3:
                    usuario_actual.mostrar_bandeja_salida()

                elif opcion == 4:
                    asunto = input("Asunto del mensaje a mover: ")
                    origen = input("Nombre de la carpeta de origen: ")
                    destino = input("Nombre de la carpeta de destino: ")
                    usuario_actual.mover_mensaje(asunto, origen, destino)

                elif opcion == 5:
                    criterio = input("Buscar por (asunto/remitente/contenido): ")
                    valor = input("Texto a buscar: ")
                    usuario_actual.buscar_mensajes(criterio, valor)
                    
                elif opcion == 6:
                  carpeta_padre = input("Nombre de la carpeta donde crear la subcarpeta: ")
                  nombre_subcarpeta = input("Nombre de la nueva subcarpeta: ")
                  usuario_actual.crear_subcarpeta(carpeta_padre, nombre_subcarpeta)

                elif opcion == 7:
                  print("Sesión finalizada.")
                  break


                else:
                    print("Opción inválida.")

            except ValueError:
                print("Por favor ingresa un número válido.")

    def Menu(self):
        while True:
            try:
                opcion = int(input("""
Bienvenido a Correos UNAB
(1) Crear usuario
(2) Iniciar sesión
(3) Salir
Opción: """))

                if opcion == 1:
                    nombre = input("Nombre: ")
                    correo = input("Correo: ")

                    while True:
                        contraseña = input("Contraseña (mínimo 6 caracteres, con al menos una mayúscula, una minúscula y un número): ")
                        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$", contraseña):
                            break
                        else:
                            print("Contraseña inválida. Intente nuevamente.")

                    nuevo_usuario = Usuario(nombre, correo, contraseña)
                    self.usuarios.append(nuevo_usuario)
                    print("Usuario creado exitosamente.\n")

                elif opcion == 2:
                    self.iniciar_sesion()

                elif opcion == 3:
                    print("Gracias por usar Correos UNAB.")
                    break

                else:
                    print("Opción inválida.")

            except ValueError:
                print("Por favor ingrese un número válido.")
