class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
        self.subcarpetas = []

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        if mensaje in self.mensajes:
            self.mensajes.remove(mensaje)

    def agregar_subcarpeta(self, subcarpeta):
        self.subcarpetas.append(subcarpeta)

    def mostrar_mensajes(self):
        print(f"Carpeta: {self.nombre}")
        if not self.mensajes:
            print("  (Sin mensajes)")
        else:
            for mensaje in self.mensajes:
                mensaje.mostrar()



    def mover_mensaje_recursivo(self, asunto, carpeta_destino):
    # Buscar el mensaje en la carpeta actual
      for mensaje in self.mensajes:
          if mensaje.asunto.lower() == asunto.lower():
              self.eliminar_mensaje(mensaje)
              carpeta_destino.agregar_mensaje(mensaje)
              print(f"Mensaje con asunto '{asunto}' movido desde '{self.nombre}' a '{carpeta_destino.nombre}'.")
              return True  # Se encontró y movió el mensaje

         # Si no está en esta carpeta, buscar en las subcarpetas (recursivamente)
      for subcarpeta in self.subcarpetas:
          encontrado = subcarpeta.mover_mensaje_recursivo(asunto, carpeta_destino)
          if encontrado:
            return True  # Si se movió desde una subcarpeta, detenemos la búsqueda

      return False  # No se encontró el mensaje en esta rama

            
    def buscar_mensajes(self, criterio, valor):
      encontrados = []
      for mensaje in self.mensajes:
          if criterio == "asunto" and valor.lower() in mensaje.asunto.lower():
              encontrados.append(mensaje)
          elif criterio == "remitente" and valor.lower() in mensaje.remitente.lower():
              encontrados.append(mensaje)
          elif criterio == "contenido" and valor.lower() in mensaje.contenido.lower():
              encontrados.append(mensaje)

      for subcarpeta in self.subcarpetas:
          encontrados.extend(subcarpeta.buscar_mensajes(criterio, valor))

      return encontrados

    

    def buscar_subcarpeta(self, nombre):
        if self.nombre.lower() == nombre.lower():
            return self
        for sub in self.subcarpetas:
            encontrada = sub.buscar_subcarpeta(nombre)
            if encontrada:
                return encontrada
        return None
