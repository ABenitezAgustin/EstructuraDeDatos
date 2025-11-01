import unittest
from usuario import Usuario
from mensaje import Mensaje

class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.agustin = Usuario("agustin", "agustin@unab.edu", "Agustin1")
        self.jennifer = Usuario("jennifer", "jennifer@unab.edu", "Jennifer1")
        # Crear subcarpeta de prueba
        self.agustin.crear_subcarpeta("Principal", "Proyectos")

    def test_enviar_recibir_mensaje(self):
        self.agustin.enviar_mensaje(self.jennifer, "Hola", "Contenido")
        self.assertEqual(len(self.agustin.carpeta_enviados.mensajes), 1)
        self.assertEqual(len(self.jennifer.carpeta_entrada.mensajes), 1)

    def test_busqueda_recursiva_usuario(self):
        self.agustin.enviar_mensaje(self.bob, "Test", "Contenido")
        resultados = self.jennifer.buscar_mensajes("asunto", "Test")
        # Debe encontrar el mensaje en la bandeja de entrada
        self.assertEqual(len(resultados), 1)

    def test_mover_mensaje(self):
        # Enviar mensaje a la bandeja de entrada
        self.jennifer.recibir_mensaje(Mensaje("agustin@unab.edu", "jennifer@unab.edu", "Mover", "Contenido"))
        self.jennifer.crear_subcarpeta("Principal", "Archivo")
        self.jennifer.mover_mensaje("Mover", "Bandeja de Entrada", "Archivo")
        carpeta_destino = self.jennifer.carpeta_principal.buscar_subcarpeta("Archivo")
        self.assertEqual(len(carpeta_destino.mensajes), 1)

    def test_crear_subcarpeta_en_carpeta_inexistente(self):
        # Debe manejar el error sin fallar
        try:
            self.agustin.crear_subcarpeta("NoExiste", "Nueva")
        except Exception as e:
            self.fail(f"crear_subcarpeta lanzó una excepción inesperada: {e}")

    def test_mover_mensaje_inexistente(self):
        try:
            self.agustin.mover_mensaje("NoExiste", "Bandeja de Entrada", "Proyectos")
        except Exception as e:
            self.fail(f"mover_mensaje lanzó una excepción inesperada: {e}")

if __name__ == "__main__":
    unittest.main()
