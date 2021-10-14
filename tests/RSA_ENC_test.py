import os
import sys
import unittest

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from src import RSA_ENC

class TestRCA_ENC(unittest.TestCase):

    def test_enc(self):
        answer = 6
        rsa = RSA_ENC.RSA_ENC(2, 7)
        self.assertEqual(rsa.t, answer, "{} did not equal to {}".format(rsa.t, answer))
