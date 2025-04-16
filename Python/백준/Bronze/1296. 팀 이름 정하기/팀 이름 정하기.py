import sys
input = sys.stdin.readline

def find_alpha(name):
    name = list(name)
    find = [0, 0, 0, 0]
    for n in name:
        if n == "L":
            find[0] += 1
        elif n == "O":
            find[1] += 1
        elif n == "V":
            find[2] += 1
        elif n == "E":
            find[3] += 1
    return find

y_name = find_alpha(input().strip())
percent = []

t = int(input())
for _ in range(t):
    t_name = input().strip()
    team_name = find_alpha(t_name)
    L = y_name[0] + team_name[0]
    O = y_name[1] + team_name[1]
    V = y_name[2] + team_name[2]
    E = y_name[3] + team_name[3]
    percent.append((((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100, t_name))

print(sorted(percent, key=lambda x: (-x[0], x[1]))[0][1])