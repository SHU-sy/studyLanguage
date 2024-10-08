def solution(a, b):
    c = str(a)+str(b)
    answer = max(int(c), (2*a*b))
    return answer