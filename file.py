import unittest

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return f"error: bo'luvchi 0 ga teng bo'la olmaydi"

class TestCalculator(unittest.TestCase):

    def test_add(self):
        '''Test case function for addition'''
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test case function for subtraction'''
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    @unittest.skip('Some reason')
    def test_mul(self):
        '''Test case function for multiplication'''
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        self.calc = Calculator()
        result = self.calc.div(10, 2)
        expected = 5
        self.assertEqual(result, expected)
#unittest.main(argv=[''], verbosity=2, exit=False)

class TestCalcDiv(unittest.TestCase):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_div(self):
        '''Test case function for division'''
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)
        self.assertEqual(self.calc.mul(7, 3), 21)
        self.assertEqual(self.calc.add(5, 9), 14)
        self.assertEqual(self.calc.sub(10, 5), 5)
class TestCalcDiv(unittest.TestCase):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_div(self):
        '''Test case function for division'''
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)

    def test_div_error(self):
        '''Make sure ZeroDivisionError is raised when necessary'''
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)

unittest.main(argv=[''], defaultTest='TestCalcDiv', verbosity=2, exit=False)