import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    arr = list(map(str, input().split()))
    arr.reverse()
    print(f"Case #{i+1}: {' '.join(arr)}")