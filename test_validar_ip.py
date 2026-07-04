import unittest
from validar_ip import validar_ip


class TestValidarIP(unittest.TestCase):

    def test_ip_valida(self):
        self.assertTrue(validar_ip("192.168.1.1"))

    def test_octeto_mayor_255(self):
        self.assertFalse(validar_ip("256.100.50.25"))

    def test_con_letras(self):
        self.assertFalse(validar_ip("192.abc.1.1"))

    def test_menos_partes(self):
        self.assertFalse(validar_ip("192.168.1"))

    def test_mas_partes(self):
        self.assertFalse(validar_ip("192.168.1.1.10"))


if __name__ == "__main__":
    unittest.main()