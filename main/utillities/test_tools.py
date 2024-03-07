import random

class Archfee:
    @staticmethod
    def m2generator(m2,rango=1000):
        delta = random.randint(1,rango)
        delta*-1 if (random.randint(1,rango)==1) else delta
        return m2+delta