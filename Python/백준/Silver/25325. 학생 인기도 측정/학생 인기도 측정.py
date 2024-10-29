import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
name = input().split()
student = defaultdict(int)
ans = []

for n in name:
    arr = input().split()
    for a in arr:
        student[a] += 1

for name in name:
    if name not in student:
        student[name] = 0

sort_stu = sorted(student.items(), key=lambda x: (-x[1], x[0]))
for n, c in sort_stu:
    print(n, c)