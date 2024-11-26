import sys
input = sys.stdin.readline

def rounding(value):
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)

n = int(input())

if n == 0:
    print(0)
else:
    score = sorted([int(input()) for _ in range(n)])
    exception = rounding(n*0.15)
    exception_score = score[exception:n-exception]
    print(rounding(sum(exception_score) / len(exception_score)))