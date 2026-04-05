import sys
n = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(len(n)):
    result += n[i]*n[i]
print(result%10)