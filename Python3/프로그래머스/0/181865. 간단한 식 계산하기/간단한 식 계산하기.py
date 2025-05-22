def solution(binomial):
    a, cmd, b = binomial.split()
    a, b = int(a), int(b)
    if cmd == "+":
        return a+b
    elif cmd == "-":
        return a-b
    else:
        return a*b