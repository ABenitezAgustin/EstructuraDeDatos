class Mensaje: #Definimos la clase mensaje 
    def __init__(self, remitente, destinatario, asunto, contenido, prioridad = 0):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.prioridad = prioridad # 0 = normal/ 1 = urgente

    def mostrar(self):                       #definimos el formato como queremos que se muestren los mensajes en pantalla
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Contenido: {self.contenido}")
        if self.prioridad == 1:
            print("(MENSAJE URGENTE)")
        print("-" * 30)
