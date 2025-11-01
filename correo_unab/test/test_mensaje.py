import unittest
from mensaje import Mensaje

class TestMensaje(unittest.TestCase):
    def setUp(self):
        self.mensaje = Mensaje("agustin@unab.edu", "jennifer@unab.edu", "Hola", "Contenido del mensaje")

    def test_creacion_mensaje(self):
        self.assertEqual(self.mensaje.remitente, "agustin@unab.edu")
        self.assertEqual(self.mensaje.destinatario, "jennifer@unab.edu")
        self.assertEqual(self.mensaje.asunto, "Hola")
        self.assertEqual(self.mensaje.contenido, "Contenido del mensaje")

    def test_mostrar_mensaje(self):
        # Solo probamos que el método no falle al ejecutarse
        try:
            self.mensaje.mostrar()
        except Exception as e:
            self.fail(f"mostrar() lanzó una excepción inesperada: {e}")

if __name__ == "__main__":
    unittest.main()
