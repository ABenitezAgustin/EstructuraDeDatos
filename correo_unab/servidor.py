from usuario import Usuario
import re
class Servidor:                     #La clase servidor se encarga de articular las clases Mensaje y Usuario.Nos provee de un Menu para crear los usuarios  
    def __init__(self):             #Los guarda en una lista para luego poder acceder a ellos y utilizar sus correspondientes atributos      
        self.usuarios = []
    
    def iniciar_sesion(self): #Menu para inicio de sesion
      if not self.usuarios:
          print("No hay usuarios registrados")
          return #return vacio = a return None    
    
      correo = input("ingrese su correo electronico: ")
      contraseña = input("Ingrese su contraseña: ") 
      Usuario_actual = next((usuario for usuario in self.usuarios if usuario.correo == correo and usuario.contraseña == contraseña), None) ##next devuleve el primer elemento que cumple con esta condicion
      if Usuario_actual:
          print(f"Bienvenido {Usuario_actual.nombre}!")
      while True:
          opciones = int(input("""¿Qué deseas hacer?
          (1) Enviar un mensaje
          (2) Ver bandeja de entrada
          (3) Ver bandeja de salida
          (4)Salir
          """))
        
          if opciones == 1:
              destinatario_correo = input("Ingrese la direccion correo electronico de el destinatario: ")
              destinatario = next((usuario for usuario in self.usuarios if usuario.correo == destinatario_correo), None)
              if destinatario:
                  asunto = input("Ingrese el asunto de el mensaje: ")
                  contenido = input("Ingrese el contenido de el mensaje: ")
                  Usuario_actual.enviar_mensaje(destinatario,asunto,contenido)
              else:
                  print("Destinatario no encontrado")
          elif opciones == 2:
              Usuario_actual.mostrar_bandeja_entrada()
          elif opciones == 3:
              Usuario_actual.mostrar_bandeja_salida()
          elif opciones == 4:
              break
          else: 
              print("Opcion invalida")                    
                     
    def Menu(self): #Menu principal
      while True:
          opciones = int(input("""Bienvenido a correos Unab
          (1)Crear usuario
          (2) iniciar sesion
          (3)Salir
          """))
          if opciones == 3:
              break
          elif opciones == 1:
              nombre = input("Decime tu nombre: ") 
              correo = input("Decime tu correo: ")
              while True:
                  contraseña = input("Contraseña (debe tener al menos 6 caracteres, un numero, mayusculas y minusculas )")
                  if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$", contraseña): ##la contraseña solo sera aceptada si se cumplen los requisitos
                      break                                                           ## La funcion re del modulo re sirve para buscar patrones en una cadena de texto
                  else:
                      print("La contraseña no cumple con los requisitos. Intente nuevamente")
              nuevo_usuario = Usuario(nombre, correo, contraseña)
              self.usuarios.append(nuevo_usuario)
              print("\nEl usuario fue agregado correctamente.\n")
          elif opciones == 2:
              self.iniciar_sesion()
 
    def mostrar_usuarios(usuarios):
        for i, usuario in enumerate(usuarios, start=1):
            print(f"\nUsuario {i}:")
            print(usuario)   