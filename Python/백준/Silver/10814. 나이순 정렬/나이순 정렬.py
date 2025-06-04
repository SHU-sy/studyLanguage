import sys
input = sys.stdin.readline

n = int(input())
people = {}

for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age not in people:
        people[age] = []
    people[age].append(name)

for age in sorted(people.keys()):
    for name in people[age]:
        print(age, name)