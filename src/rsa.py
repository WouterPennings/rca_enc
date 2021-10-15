import math
import rsa_helper as REH

class rsa:

    def __init__(self, _p, _q):
        if self.__inputIsCorrect(_p):
            self.p = _p
        if self.__inputIsCorrect(_q):
            self.q = _q
        self.n = _p * _q
        self.t = (_p - 1) * (_q - 1)

        self.dKey = None
        self.eKey = None

    def encrypt(self, number):
        return int(math.floor(math.pow(number, self.eKey) % self.n))

    def decrypt(self, number):
        return int(math.floor(math.pow(number, self.dKey) % self.n))

    def generateKeys(self):
        self.eKey = self.__generateEncryptionKey()
        self.dKey = self.__generateDecryptionKey()

    #  |                             |
    #  |  Below are private methods  |
    #  |                             |
    # \/                            \/

    def __generateEncryptionKey(self):
        for x in range(2, self.t + 1):
            result = REH.isCoprime(x, self.t)
            if result is True:
                return x

    def __generateDecryptionKey(self):
        i = 6
        while True:
            x = (i * self.eKey) % self.t
            if x == 1:
                return i
            i = i + 1

    def __inputIsCorrect(self, number):
        x = isinstance(number, int)
        if not x:
            self.__raiseError("Number given was not of type: 'integer'")
        x = REH.isPrime(number)
        if not x:
            self.__raiseError("Number given was prime'")
        return True

    @staticmethod
    def __raiseError(message):
        raise ValueError('rsa Exception → {}'.format(message))
