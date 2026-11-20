import unittest
from procesador import contar_palabras, frecuencia_palabras, resumen

class TestProcesador(unittest.TestCase):
    def test_contar_palabras(self):
        self.assertEqual(contar_palabras("hola mundo"), 2)
        self.assertEqual(contar_palabras(""), 0)
        self.assertEqual(contar_palabras("una sola"), 2)

    def test_frecuencia_palabras(self):
        resultado = frecuencia_palabras("hola mundo hola", top=2)
        self.assertEqual(resultado["hola"], 2)
        self.assertEqual(resultado["mundo"], 1)

    def test_resumen_texto_corto(self):
        self.assertEqual(resumen("hola", 100), "hola")

    def test_resumen_texto_largo(self):
        texto = "palabra " * 20
        r = resumen(texto, 50)
        self.assertTrue(r.endswith("..."))
        self.assertTrue(len(r) <= 53)

if __name__ == "__main__":
    unittest.main()
