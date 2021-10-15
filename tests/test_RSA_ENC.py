import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from src import RSA_ENC

def test_enc_t():
    answer = [6, 10, 12, 32, 72]
    expected = [
        RSA_ENC.RSA_ENC(2, 7).t,
        RSA_ENC.RSA_ENC(2, 11).t,
        RSA_ENC.RSA_ENC(2, 13).t,
        RSA_ENC.RSA_ENC(3, 17).t,
        RSA_ENC.RSA_ENC(5, 19).t
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        print("Error(s) at line: ", end='')
        print(str(x[1])[1:-1])
    assert x[0]

def doTest(answer, expected):
    wrong = []
    noMistake = True
    for x in range(0, len(answer)):
        if expected[x] != answer[x]:
            wrong.append(x)
            noMistake = False
    return noMistake, wrong
