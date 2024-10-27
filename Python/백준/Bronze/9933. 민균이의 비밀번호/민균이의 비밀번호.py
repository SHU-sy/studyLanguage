import sys
input = sys.stdin.readline
n = int(input())
password = set(input().strip() for _ in range(n))

for pasw in password:
    if pasw[::-1] in password:
        len_p = len(pasw)
        print(len_p, pasw[len_p//2])
        break