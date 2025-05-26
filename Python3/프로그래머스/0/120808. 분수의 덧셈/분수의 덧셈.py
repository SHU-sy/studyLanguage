import math
def solution(a, b, c, d):
    numer = a * d + c * b
    denom = b * d

    gcd = math.gcd(numer, denom)
    return [numer//gcd, denom//gcd]