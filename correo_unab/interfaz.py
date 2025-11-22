from abc import ABC, abstractmethod
class Interfaz:                  #clase abstracta, modelo de interfaz(debe ser heredada por las diferentes clases usuario)
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
    