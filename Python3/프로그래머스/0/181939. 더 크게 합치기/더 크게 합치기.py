def solution(a, b):
    a, b = str(a), str(b)
    if a+b < b+a:
        answer = b+a
        return int(answer)
    else:
        answer = a+b
        return int(answer)