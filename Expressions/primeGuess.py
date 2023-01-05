from sympy.ntheory import factorint

def primeDisplay(calculatedNum):
    parts = factorint(calculatedNum)
    print(parts)
    bases = list(parts.keys())
    exponents = list(parts.values())
    result = ""
    for i, base in enumerate(bases):
        result += f"{str(base)} " if exponents[i] == 1 else f"{str(base)}^{str(exponents[i])} "
    return result

def primeCheck(calculatedNum):
    ans = 1
    for num in calculatedNum.split(" "):
        ans *= int(num.split("^")[0]) if not("^" in num) else pow(int(num.split("^")[0]), int(num.split("^")[1]))
    return ans