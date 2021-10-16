import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from src import rsa_helper
from src import tokens

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

    def encrypt(self, x):
        text = str(x).lower()
        result = ""
        for c in text:
            key = tokens.getKeyByValue(c)
            result += tokens.charToken[self.__encryptNumber(key)]
        return result

    def decrypt(self, x):
        text = str(x).lower()
        result = ""
        for c in text:
            key = tokens.getKeyByValue(c)
            result += tokens.charToken[self.__decryptNumber(key)]
        return result


    def generateKeys(self):
        self.eKey = self.__generateEncryptionKey()
        self.dKey = self.__generateDecryptionKey()

    #  |                             |
    #  |  Below are private methods  |
    #  |                             |
    # \/                            \/

    def __encryptNumber(self, x):
        return int(round(rsa_helper.pow(x, self.eKey) % self.n, 0))

    def __decryptNumber(self, x):
        return int(round(rsa_helper.pow(x, self.dKey) % self.n, 0))

    def __generateEncryptionKey(self):
        for x in range(2, self.t + 1):
            result = rsa_helper.isCoprime(x, self.t)
            if result is True:
                return x

    def __generateDecryptionKey(self):
        i = 6
        while True:
            x = (i * self.eKey) % self.t
            if x == 1:
                return i
            i += + 1

    def __inputIsCorrect(self, number):
        x = isinstance(number, int)
        if not x:
            self.__raiseError("Number given was not of type: 'integer'")
        x = rsa_helper.isPrime(number)
        if not x:
            self.__raiseError("Number given was prime'")
        return True

    @staticmethod
    def __raiseError(message):
        raise ValueError('rsa Exception → {}'.format(message))
