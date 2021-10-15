import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from src import rsa

def test_rsa_p():
    answer = [2, 3, 5, 7, 11, 409]
    expected = [
        rsa.rsa(2, 3).p,
        rsa.rsa(3, 3).p,
        rsa.rsa(5, 3).p,
        rsa.rsa(7, 3).p,
        rsa.rsa(11, 3).p,
        rsa.rsa(409, 3).p
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_p")
    assert x[0]

def test_rsa_q():
    answer = [2, 3, 5, 7, 11, 409]
    expected = [
        rsa.rsa(3, 2).q,
        rsa.rsa(3, 3).q,
        rsa.rsa(3, 5).q,
        rsa.rsa(3, 7).q,
        rsa.rsa(3, 11).q,
        rsa.rsa(3, 409).q
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_q")
    assert x[0]

def test_rsa_t():
    answer = [6, 10, 12, 32, 72]
    expected = [
        rsa.rsa(2, 7).t,
        rsa.rsa(2, 11).t,
        rsa.rsa(2, 13).t,
        rsa.rsa(3, 17).t,
        rsa.rsa(5, 19).t
    ]
    x = doTest(answer, expected)
    if x[0] is False:
        printErrorIndexes(x[1], "test_rsa_t")
    assert x[0]

def test_rsa_n():
    answer = [14, 22, 38, 95, 10]
    expected = [
        rsa.rsa(2, 7).n,
        rsa.rsa(2, 11).n,
        rsa.rsa(2, 19).n,
        rsa.rsa(5, 19).n,
        rsa.rsa(2, 5).n
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
