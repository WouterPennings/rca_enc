import math


class RSA_ENC:

    def __init__(self, _p, _q):
        self.q = _q
        self.p = _p
        self.n = _p * _q
        self.t = (_p - 1) * (_q - 1)

        self.dKey = None
        self.eKey = None
        self.__generateKeys()

    def encrypt(self, number):
        return int(math.floor(math.pow(number, self.eKey) % self.n))

    def decrypt(self, number):
        return int(math.floor(math.pow(number, self.dKey) % self.n))

    def __generateKeys(self):
        self.eKey = self.__generateEncryptionKey()
        self.dKey = self.__generateDecryptionKey()

    def __generateEncryptionKey(self):
        for x in range(2, self.t + 1):
            result = self.__isCoprime(x, self.t)
            if result is True:
                return x

    def __generateDecryptionKey(self):
        i = 6
        while True:
            x = (i * self.eKey) % self.t
            if x == 1:
                return i
            i = i + 1

    # Credit: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
    @staticmethod
    def __gcd(p, q):
        while q != 0:
            p, q = q, p % q
        return p

    # Credit: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
    def __isCoprime(self, x, y):
        return self.__gcd(x, y) == 1
