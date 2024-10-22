import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1, arr2 = [list(map(int, input().split())) for _ in range(2)]
print(" ".join(map(str, sorted(arr1 + arr2))))