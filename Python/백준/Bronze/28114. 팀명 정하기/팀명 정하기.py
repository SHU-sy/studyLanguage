import sys
input = sys.stdin.readline

members = []
ans_year = []

for _ in range(3):
    solve, year, name = input().split()
    solve, year = int(solve), int(year)
    ans_year.append(year%100)
    members.append([solve, name])

members.sort(key=lambda x: (-x[0]))
ans_name = "".join(member[1][0] for member in members)

print(''.join(map(str, sorted(ans_year))))
print(ans_name)