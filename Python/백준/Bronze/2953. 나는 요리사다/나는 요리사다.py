import sys
input = sys.stdin.readline
arr = [sum(list(map(int, input().split()))) for _ in range(5)]
max_arr = max(arr)
print(arr.index(max_arr)+1, max_arr)