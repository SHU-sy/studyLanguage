import sys
a = [list(map(int, sys.stdin.readline().split()))for _ in range(9)]
max_val = -1
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if a[i][j] > max_val:
            max_val = a[i][j]
            row, col = i+1, j+1
print(max_val)
print(row, col)