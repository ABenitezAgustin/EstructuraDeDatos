class GestorFiltros:
    def __init__(self, usuario):
        self.usuario = usuario

    def aplicar(self, mensaje):
        filtros = self.usuario.filtros
        carpeta_principal = self.usuario.carpeta_principal
        for texto, carpeta_destino in filtros["asunto"]:
            if texto in mensaje.asunto.lower():
                return carpeta_principal.buscar_subcarpeta(carpeta_destino)
        for texto, carpeta_destino in filtros["remitente"]:
            if texto in mensaje.remitente.lower():
                return carpeta_principal.buscar_subcarpeta(carpeta_destino)
        for texto, carpeta_destino in filtros["contenido"]:
            if texto in mensaje.contenido.lower():
                return carpeta_principal.buscar_subcarpeta(carpeta_destino)
        return None

    def agregar(self, criterio, texto, carpeta_destino):
        carpeta = self.usuario.carpeta_principal.buscar_subcarpeta(carpeta_destino)
        if not carpeta:
            print(f"Carpeta '{carpeta_destino}' no encontrada")
            return
        self.usuario.filtros[criterio].append((texto.lower(), carpeta_destino))
