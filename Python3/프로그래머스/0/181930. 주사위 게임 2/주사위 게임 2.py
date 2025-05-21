def solution(a, b, c):
    def cal(s, e):
        ans = 1
        for i in range(s, e+1):
            ans *= (a**i + b**i + c**i)
        return ans
    
    if a != b and b != c and c != a:
        return a+b+c
    elif a == b and b == c:
        return cal(1, 3)
    else:
        return cal(1, 2)
        