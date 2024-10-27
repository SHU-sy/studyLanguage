import sys
input = sys.stdin.readline

n = int(input())
people = {}

for _ in range(n):
    s, w, d, p = input().split()
    w, d, p = int(w), int(d), int(p)
    people[s] = [w, d, p]

for _ in range(n):
    name, money = input().split()
    if people[name][2] > int(money):
        del people[name]

s_people = sorted(people.values(), key=lambda x: (x[0], x[1]))

if not s_people:
    print(0)
elif len(s_people) == 1:
    print(1)
else:
    count = 1
    max_count = 0
    current_p = s_people[0]
    for val in s_people[1:]:
        if (val[0] == current_p[0] and current_p[1]+1 == val[1]) or (current_p[1] == 6 and val[1] == 0 and current_p[0]+1 == val[0]):
            count += 1

        elif val[0] == current_p[0] and val[1] == current_p[1]:
            continue

        else:
            max_count = max(max_count, count)
            count = 1

        current_p = val
    max_count = max(max_count, count)
    print(max_count)