import random
import sympy as sp
from latex2sympy2 import latex2sympy

def getPrime(limit):
    primes = []
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def randNum(cmdInput):
    cmdArray = [int(i) for i in cmdInput.split()]
    returnNum = 0
    if len(cmdArray) == 2:
        returnNum = round(random.uniform(cmdArray[0], cmdArray[1]), 2)
    else:
        returnNum = random.randint(cmdArray[1], cmdArray[2]) if cmdArray[0] == 0 else round(random.uniform(cmdArray[1], cmdArray[2]), 2)

    return returnNum

def determinant(cmdInput):
    iteration = len(cmdInput[0].split(" "))
    A = []
    for i in range(0, iteration):
        A.append(cmdInput[i].split(" "))
    A = sp.Matrix(A)
    answer = sp.latex(A).replace("\left[", "").replace("\\right]", "").replace("matrix", "vmatrix") + " = " + str(A.det())
    return answer

def eigenvalue(cmdInput):
    print(cmdInput)
    I = sp.Symbol("I")
    iteration = len(cmdInput[0].split(" "))
    A = []
    for i in range(0, iteration):
        A.append(cmdInput[i].split(" "))
    A = sp.Matrix(A)
    eigenvalList = []
    for i in str(A.eigenvals()).lstrip("{").rstrip("}").split(", "):
        print(i)
        eigenvalList.append(sp.latex(eval(i.split(": ").pop(0).replace("sqrt", "sp.sqrt"))))
        print(sp.latex((i.split(": ").pop(0))))
    answer = sp.latex(A).replace("\left[", "").replace("\\right]", "").replace("matrix", "vmatrix") + "\quad \lambda = " + ", ".join(eigenvalList)
    return answer

def integrate(cmdInput):
    x = sp.Symbol("x")
    eq = latex2sympy(cmdInput)
    answer = sp.latex(sp.simplify(sp.integrate(eq, x)))
    return "\int" + cmdInput + "dx = " + answer + "+C"

def differential(cmdInput):
    x = sp.Symbol("x")
    eq = latex2sympy(cmdInput)
    answer = sp.latex(sp.simplify(sp.diff(eq, x)))
    return "\\frac{d}{dx}" + cmdInput + " = " + answer