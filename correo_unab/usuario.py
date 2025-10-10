from interfaz import Interfaz
from mensaje import Mensaje

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

    
    def enviar_mensaje(self, destinatario, asunto, contenido): #Enviar mensaje es un metodo que instancia la clase Mensaje y guarda estos objetos en una lista que sera la namdeja de salida 
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido) ## a su ves que guarda una copia de el mismo objeto dentro de la bandeja de entrada de el destinatario 
        self.bandeja_enviados.append(mensaje)  
        destinatario.recibir_mensaje(mensaje)  

    
    def recibir_mensaje(self, mensaje):
        self.bandeja_recibidos.append(mensaje)

    
    def mostrar_bandeja_entrada(self):
        print(f"\nBandeja de entrada de {self.nombre}:") #este metodo recorre la lista Bandeja de entrada y nos muestra en pantalla cada objeto
        if not self.bandeja_recibidos:                    #En caso de no encontrar nada imprime "No hay mensajes"
            print("No hay mensajes.")
        for mensaje in self.bandeja_recibidos:
            mensaje.mostrar()

    
    def mostrar_bandeja_salida(self):                     #similar al metodo anterior pero con la bandeja de salida
        print(f"\nBandeja de salida de {self.nombre}:")
        if not self.bandeja_enviados:
            print("No hay mensajes enviados.")
        for mensaje in self.bandeja_enviados:
            mensaje.mostrar()
    
    def __str__(self):
        return f"El usuario se llama {self.nombre} y su correo elecectronico es {self.correo}"