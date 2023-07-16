class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b != 0:
            return a / b

    @staticmethod
    def ildiz(a):
        return a ** 0.5

    @staticmethod
    def kvtop(a):
        return a * a

    @staticmethod
    def bin(a):
        return a + 1
