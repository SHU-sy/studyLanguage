import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = list(map(str, input().split()))
    answer = []
    for word in s:
        word = word[::-1]
        answer.append(word)
    print(" ".join(answer))