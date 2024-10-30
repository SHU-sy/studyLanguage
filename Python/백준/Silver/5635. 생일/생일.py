import sys
input = sys.stdin.readline
n = int(input())
stu = []

for _ in range(n):
    arr = input().split()
    name = arr[0]
    d, m, y = int(arr[1]), int(arr[2]), int(arr[3])

    stu.append((name, y, m, d))

stu.sort(key=lambda x: (x[1], x[2], x[3]))

print(stu[-1][0])
print(stu[0][0])
