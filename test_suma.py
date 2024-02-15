import unittest
from suma import sumar

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(-6, 6), 1)
        self.assertEqual(dividir(10, 0), None)

if __name__ == '__main__':
     unittest.main()
