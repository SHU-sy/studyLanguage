import sys
input = sys.stdin.readline
n = int(input())
lists = []

for i in range(n):
    age, name = input().split()
    lists.append((int(age), name, i))
s_lists = sorted(lists, key=lambda x: (x[0], x[2]))

for age, name, _ in s_lists:
    print(age, name)