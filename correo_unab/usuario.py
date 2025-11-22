from interfaz import Interfaz
from mensaje import Mensaje
from carpeta import Carpeta
from cola import Cola, enqueue, dequeue, is_empty
from filtros import GestorFiltros
from urgentes import GestorUrgentes

class Usuario(Interfaz):
    def __init__(self, nombre, correo, contraseña):
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña

        # Carpeta raíz y subcarpetas básicas 
        self.carpeta_principal = Carpeta("Principal")
        self.carpeta_entrada = Carpeta("Bandeja de Entrada")
        self.carpeta_enviados = Carpeta("Bandeja de Salida")
        self.carpeta_principal.agregar_subcarpeta(self.carpeta_entrada)
        self.carpeta_principal.agregar_subcarpeta(self.carpeta_enviados)

        # Colas para mensajes con prioridad
        self.cola_prioridad_entrada = Cola()
        self.cola_prioridad_salida = Cola()

        # Filtros
        self.filtros = {"asunto": [], "remitente": [], "contenido": []}

        # Gestores
        self.gestor_filtros = GestorFiltros(self)
        self.gestor_urgentes = GestorUrgentes(self)

    # --- Getters y setters ---
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def contraseña(self):
        return self.__contraseña

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    # --- Métodos de envío y recepción ---
    def enviar_mensaje(self, destinatario, asunto, contenido, urgente=False):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        if urgente:
            enqueue(self.cola_prioridad_salida, mensaje)
        else:
            self.carpeta_enviados.agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje, urgente)

    def recibir_mensaje(self, mensaje, urgente=False):
        if urgente:
            enqueue(self.cola_prioridad_entrada, mensaje)
            return

        carpeta_destino = self.gestor_filtros.aplicar(mensaje)
        if carpeta_destino:
            carpeta_destino.agregar_mensaje(mensaje)
        else:
            self.carpeta_entrada.agregar_mensaje(mensaje)

    # --- Procesar mensajes urgentes ---
    def procesar_mensajes_urgentes_entrada(self):
        self.gestor_urgentes.procesar_entrada()

    def procesar_mensajes_urgentes_salida(self):
        self.gestor_urgentes.procesar_salida()

    # --- Mostrar bandejas ---
    def mostrar_bandeja_entrada(self):
        self.procesar_mensajes_urgentes_entrada()
        print(f"\nBandeja de entrada de {self.nombre}:")
        self.carpeta_entrada.mostrar_mensajes()

    def mostrar_bandeja_salida(self):
        self.procesar_mensajes_urgentes_salida()
        print(f"\nBandeja de salida de {self.nombre}:")
        self.carpeta_enviados.mostrar_mensajes()

    # --- Filtros ---
    def agregar_filtro(self, criterio, texto, carpeta_destino):
        self.gestor_filtros.agregar(criterio, texto, carpeta_destino)

    # --- Crear subcarpeta ---
    def crear_subcarpeta(self, nombre_carpeta_padre, nombre_subcarpeta):
        carpeta_padre = self.carpeta_principal.buscar_subcarpeta(nombre_carpeta_padre)
        if carpeta_padre:
            carpeta_padre.agregar_subcarpeta(Carpeta(nombre_subcarpeta))
        else:
            print(f"No se encontró la carpeta '{nombre_carpeta_padre}'")

    # --- Buscar y mover mensajes ---
    def buscar_mensajes(self, criterio, valor):
        resultados = self.carpeta_principal.buscar_mensajes(criterio, valor)
        return resultados

    def mover_mensaje(self, asunto, nombre_carpeta_origen, nombre_carpeta_destino):
        origen = self.carpeta_principal.buscar_subcarpeta(nombre_carpeta_origen)
        destino = self.carpeta_principal.buscar_subcarpeta(nombre_carpeta_destino)
        if origen and destino:
            movido = origen.mover_mensaje_recursivo(asunto, destino)
            if not movido:
                print(f"No se encontró mensaje con asunto '{asunto}' en '{nombre_carpeta_origen}'")
        else:
            print("Carpeta origen o destino no encontrada")

    # --- String ---
    def __str__(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}"
