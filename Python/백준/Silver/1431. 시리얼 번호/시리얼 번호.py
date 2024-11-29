import sys
input = sys.stdin.readline

def digit_sum(s):
    return sum(int(c) for c in s if c.isdigit())

n = int(input())
serial = [input().strip() for i in range(n)]
answer = sorted(serial, key=lambda x: (len(x), digit_sum(x), x))
print("\n".join(answer))