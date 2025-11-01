import unittest
from carpeta import Carpeta
from mensaje import Mensaje

class TestCarpeta(unittest.TestCase):
    def setUp(self):
        self.carpeta = Carpeta("Principal")
        self.subcarpeta = Carpeta("Sub")
        self.carpeta.agregar_subcarpeta(self.subcarpeta)
        self.mensaje = Mensaje("agustin@unab.edu", "jennifer@unab.edu", "Asunto1", "Texto")
        self.subcarpeta.agregar_mensaje(self.mensaje)

    def test_agregar_eliminar_mensaje(self):
        m2 = Mensaje("x", "y", "Asunto2", "Texto2")
        self.carpeta.agregar_mensaje(m2)
        self.assertIn(m2, self.carpeta.mensajes)
        self.carpeta.eliminar_mensaje(m2)
        self.assertNotIn(m2, self.carpeta.mensajes)

    def test_busqueda_recursiva(self):
        resultados = self.carpeta.buscar_mensajes("asunto", "Asunto1")
        self.assertIn(self.mensaje, resultados)

    def test_mover_mensaje_recursivo(self):
        destino = Carpeta("Destino")
        movido = self.carpeta.mover_mensaje_recursivo("Asunto1", destino)
        self.assertTrue(movido)
        self.assertIn(self.mensaje, destino.mensajes)
        self.assertNotIn(self.mensaje, self.subcarpeta.mensajes)

    def test_buscar_subcarpeta(self):
        encontrada = self.carpeta.buscar_subcarpeta("Sub")
        self.assertEqual(encontrada, self.subcarpeta)
        no_encontrada = self.carpeta.buscar_subcarpeta("NoExiste")
        self.assertIsNone(no_encontrada)

if __name__ == "__main__":
    unittest.main()
