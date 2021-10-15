import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from src import RSA_ENC

def test_rsa_p():
    answer = [1, 2, 3, 4, 5, 6, 122]
    expected = [
        RSA_ENC.RSA_ENC(1, 1).p,
        RSA_ENC.RSA_ENC(2, 1).p,
        RSA_ENC.RSA_ENC(3, 1).p,
        RSA_ENC.RSA_ENC(4, 1).p,
        RSA_ENC.RSA_ENC(5, 1).p,
        RSA_ENC.RSA_ENC(6, 1).p,
        RSA_ENC.RSA_ENC(122, 1).p
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_p")
    assert x[0]

def test_rsa_q():
    answer = [1, 2, 3, 4, 5, 6, 122]
    expected = [
        RSA_ENC.RSA_ENC(1, 1).q,
        RSA_ENC.RSA_ENC(1, 2).q,
        RSA_ENC.RSA_ENC(1, 3).q,
        RSA_ENC.RSA_ENC(1, 4).q,
        RSA_ENC.RSA_ENC(1, 5).q,
        RSA_ENC.RSA_ENC(1, 6).q,
        RSA_ENC.RSA_ENC(1, 122).q
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_q")
    assert x[0]

def test_rsa_t():
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
        printErrorIndexes(x[1], "test_rsa_t")
    assert x[0]

def test_rsa_n():
    answer = [14, 22, 38, 95, 10]
    expected = [
        RSA_ENC.RSA_ENC(2, 7).n,
        RSA_ENC.RSA_ENC(2, 11).n,
        RSA_ENC.RSA_ENC(2, 19).n,
        RSA_ENC.RSA_ENC(5, 19).n,
        RSA_ENC.RSA_ENC(2, 5).n
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_n")
    assert x[0]

def doTest(answer, expected):
    wrong = []
    noMistake = True
    for x in range(0, len(answer)):
        if expected[x] != answer[x]:
            wrong.append(x)
            noMistake = False
    return noMistake, wrong

def printErrorIndexes(errors, testName = ""):
    if testName != "":
        print("{}:\n    Error(s) at line --> ".format(testName), end='')
    else:
        print("Error(s) at line: ", end='')
    print(str(errors)[1:-1])