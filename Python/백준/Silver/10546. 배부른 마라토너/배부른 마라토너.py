import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
participate = []
complete = []

for _ in range(n):
    participate.append(input().strip())

for _ in range(n-1) :
    complete.append(input().strip())

print("".join(list(Counter(participate) - Counter(complete))))