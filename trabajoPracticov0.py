from abc import ABC, abstractmethod
import re
class Interfaz:                  #clase abtracta, modelo de interfaz(debe ser heredada por las diferentes clases usuario)
    @abstractmethod              
    def enviar_mensaje(self, destinatario, asunto, contenido): 
        pass
    
    @abstractmethod
    def recibir_mensaje(self, mensaje): 
        pass
    
    @abstractmethod
    def mostrar_bandeja_entrada(self):
        pass
    
    @abstractmethod
    def mostrar_bandeja_(self):
        pass
    
    
    
    
class Mensaje: #Definimos la clase mensaje 
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido

    def mostrar(self):
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Contenido: {self.contenido}")
        print("-" * 30)

# class Carpeta:
#     def __init__(self, bandeja_entrada, bandeja_salida):
#         self.bandeja_entrada = bandeja_entrada
#         self.bandeja_salidad = bandeja_salida

# class Servidor:
#     def __init__(self, usuarios):
#         self.usuarios = []
    
#     def agregar_usuario():
#         usuario = Usuario(self.nombre, self.correo)
        


class Usuario(Interfaz): #Clase usuario heredamos los metodos de interfaz, encapsulamos propiedades que consideramos privadas de cada usuario
    def __init__(self, nombre, correo, contraseña):
        self.__nombre = nombre
        self.__correo = correo                    
        self.__contraseña = contraseña
        self.bandeja_recibidos = []
        self.bandeja_enviados = []
    
    @property                             #Utilizamos decoradores getters y setters para acceder y/o modificar los atributos privados de la clase usuario
    def nombre(self):
        return self.__nombre  
    
    @nombre.setter
    def nombre(self, nuevo__nombre):
        self.__nombre = nuevo__nombre 
     
    @property
    def correo(self):
        return self.__correo  
    
    @correo.setter
    def correo(self, nuevo__nombre):
        self.__correo = nuevo__nombre
    
    @property
    def contraseña(self):
        return self.__contraseña  
    
    @contraseña.setter
    def contraseña(self, nueva__contraseña):
        self.__contraseña = nueva__contraseña           

    
    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        self.bandeja_enviados.append(mensaje)  
        destinatario.recibir_mensaje(mensaje)  

    
    def recibir_mensaje(self, mensaje):
        self.bandeja_recibidos.append(mensaje)

    
    def mostrar_bandeja_entrada(self):
        print(f"\nBandeja de entrada de {self.nombre}:")
        if not self.bandeja_recibidos:
            print("No hay mensajes.")
        for mensaje in self.bandeja_recibidos:
            mensaje.mostrar()

    
    def mostrar_bandeja_salida(self):
        print(f"\nBandeja de salida de {self.nombre}:")
        if not self.bandeja_enviados:
            print("No hay mensajes enviados.")
        for mensaje in self.bandeja_enviados:
            mensaje.mostrar()
    
    def __str__(self):
        return f"El usuario se llama {self.nombre} y su correo elecectronico es {self.correo}"
        

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
              destinatario_correo = input("Ingrese la direccion correo electronico de el destinatario")
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
              nombre = input("Decime tu nombre: ") ##esto lo puedo hacer con una funcion e invocarla como hare con ingresar usuario
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
        
def main(): #Funcion Main, pone en marcha el programa al ejecutarlo
    servidor = Servidor() 
    servidor.Menu() 
   
if __name__ == "__main__":
    main()     


