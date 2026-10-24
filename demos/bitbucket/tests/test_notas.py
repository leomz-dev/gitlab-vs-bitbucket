"""Pruebas unitarias del módulo NotasApp (ejecutables con unittest)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.notas import (
    NotaInvalidaError,
    aprobo,
    promedio,
    promedio_ponderado,
    validar_nota,
)


class TestValidarNota(unittest.TestCase):
    def test_acepta_nota_en_rango(self):
        self.assertEqual(validar_nota(4.5), 4.5)

    def test_acepta_limites_del_rango(self):
        self.assertEqual(validar_nota(0.0), 0.0)
        self.assertEqual(validar_nota(5.0), 5.0)

    def test_rechaza_nota_mayor_a_cinco(self):
        with self.assertRaises(NotaInvalidaError):
            validar_nota(5.1)

    def test_rechaza_nota_negativa(self):
        with self.assertRaises(NotaInvalidaError):
            validar_nota(-1.0)

    def test_rechaza_valor_no_numerico(self):
        with self.assertRaises(NotaInvalidaError):
            validar_nota("cuatro")


class TestPromedio(unittest.TestCase):
    def test_promedio_aritmetico(self):
        self.assertEqual(promedio([3.0, 4.0, 5.0]), 4.0)

    def test_promedio_redondea_a_dos_decimales(self):
        self.assertEqual(promedio([3.0, 3.5]), 3.25)

    def test_promedio_lista_vacia(self):
        with self.assertRaises(NotaInvalidaError):
            promedio([])

    def test_promedio_con_nota_invalida(self):
        with self.assertRaises(NotaInvalidaError):
            promedio([3.0, 6.0])


class TestAprobo(unittest.TestCase):
    def test_aprueba_por_encima_del_umbral(self):
        self.assertTrue(aprobo([4.0, 4.5]))

    def test_reprueba_por_debajo_del_umbral(self):
        self.assertFalse(aprobo([2.0, 2.5]))

    def test_respeta_umbral_personalizado(self):
        self.assertTrue(aprobo([3.2, 3.4], umbral=3.0))


class TestPromedioPonderado(unittest.TestCase):
    def test_promedio_ponderado_basico(self):
        self.assertEqual(promedio_ponderado([3.0, 4.0], [30, 70]), 3.7)

    def test_promedio_ponderado_redondea_a_dos_decimales(self):
        self.assertEqual(promedio_ponderado([3.0, 4.0, 3.4], [1, 1, 1]), 3.47)

    def test_rechaza_longitudes_distintas(self):
        with self.assertRaises(NotaInvalidaError):
            promedio_ponderado([3.0], [50, 50])

    def test_rechaza_suma_de_pesos_en_cero(self):
        with self.assertRaises(NotaInvalidaError):
            promedio_ponderado([3.0], [0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
