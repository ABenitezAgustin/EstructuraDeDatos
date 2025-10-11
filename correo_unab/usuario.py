from interfaz import Interfaz
from mensaje import Mensaje
from carpeta import Carpeta

class Usuario(Interfaz):
    def __init__(self, nombre, correo, contraseña):
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña

        # Carpeta raíz que contiene todas las subcarpetas
        self.carpeta_principal = Carpeta("Principal")            #Utilizamos una estructura de arbol para organizar carpetas y subcarpetas 
        # Carpetas básicas dentro de la raíz
        self.carpeta_entrada = Carpeta("Bandeja de Entrada")
        self.carpeta_enviados = Carpeta("Bandeja de Salida")

        # Agregar subcarpetas a la carpeta principal
        self.carpeta_principal.agregar_subcarpeta(self.carpeta_entrada)
        self.carpeta_principal.agregar_subcarpeta(self.carpeta_enviados)

    # Getters y setters usando decoradores
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    # Métodos para enviar y recibir mensajes
    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        self.carpeta_enviados.agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.carpeta_entrada.agregar_mensaje(mensaje)

    # Mostrar bandejas
    def mostrar_bandeja_entrada(self):
        print(f"\nBandeja de entrada de {self.nombre}:")
        self.carpeta_entrada.mostrar_mensajes()

    def mostrar_bandeja_salida(self):
        print(f"\nBandeja de salida de {self.nombre}:")
        self.carpeta_enviados.mostrar_mensajes()

    

    # Búsqueda recursiva
    def buscar_mensajes(self, criterio, valor):              
        
        if criterio not in ['asunto', 'remitente', 'contenido']:
            print(f"Criterio inválido: '{criterio}'. Usa 'asunto', 'remitente' o 'contenido'.")
            return

        resultados = self.carpeta_principal.buscar_mensajes(criterio, valor) #Utilizamos el metodo buscar mensaje que definimos en la clase carpeta para hacer la busqueda recursiva
        if resultados:
            print(f"\nSe encontraron {len(resultados)} mensajes con {criterio} que contiene '{valor}':")
            for mensaje in resultados:
                mensaje.mostrar()
        else:
            print(f"\nNo se encontraron mensajes con {criterio} que contenga '{valor}'.")

    # Mover mensaje entre carpetas
    def mover_mensaje(self, asunto, nombre_carpeta_origen, nombre_carpeta_destino): # Buscar las carpetas por nombre
        origen = self.carpeta_principal.buscar_subcarpeta(nombre_carpeta_origen)     #Mueve el primer mensaje que coincida con el asunto desde una carpeta a otra.  
        destino = self.carpeta_principal.buscar_subcarpeta(nombre_carpeta_destino)

        if not origen:
            print(f"La carpeta de origen '{nombre_carpeta_origen}' no existe.")
            return
        if not destino:
            print(f"La carpeta de destino '{nombre_carpeta_destino}' no existe.")
            return

        # Buscar mensaje por asunto en la carpeta de origen
        for mensaje in origen.mensajes:
            if mensaje.asunto.lower() == asunto.lower():
                origen.eliminar_mensaje(mensaje)
                destino.agregar_mensaje(mensaje)
                print(f"Mensaje con asunto '{asunto}' movido de '{nombre_carpeta_origen}' a '{nombre_carpeta_destino}'.")
                return

        print(f"No se encontró mensaje con asunto '{asunto}' en la carpeta '{nombre_carpeta_origen}'.")

    # String para imprimir
    def __str__(self):
        return f"El usuario se llama {self.nombre} y su correo electrónico es {self.correo}"

        
