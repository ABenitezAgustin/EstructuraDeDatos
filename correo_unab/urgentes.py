from cola import is_empty, dequeue

class GestorUrgentes:
    def __init__(self, usuario):
        self.usuario = usuario

    def procesar_entrada(self):
        while not is_empty(self.usuario.cola_prioridad_entrada):
            mensaje = dequeue(self.usuario.cola_prioridad_entrada).dato
            self.usuario.carpeta_entrada.agregar_mensaje(mensaje)

    def procesar_salida(self):
        while not is_empty(self.usuario.cola_prioridad_salida):
            mensaje = dequeue(self.usuario.cola_prioridad_salida).dato
            self.usuario.carpeta_enviados.agregar_mensaje(mensaje)
