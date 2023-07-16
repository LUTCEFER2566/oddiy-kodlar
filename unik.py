import unittest
from kalkulyator import Calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_sub(self):
        result = Calculator.sub(10, 5)
        self.assertEqual(result, 5)
    def test_kvtop(self):
        result=Calculator.kvtop(6)
        self.assertEqual(result,36)

    def test_bulinma(self):
        result=Calculator.div(100,2)
        self.assertEqual(result,50)

    def test_kopaytma(self):
        result = Calculator.mul(10, 2)
        self.assertEqual(result, 20)

    def test_ildiz(self):
        result = Calculator.ildiz(49)
        self.assertEqual(result, 7)
    def test_bin(self):
        result = Calculator.bin(49)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
