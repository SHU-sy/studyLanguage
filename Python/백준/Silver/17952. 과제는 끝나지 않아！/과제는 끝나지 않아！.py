import sys
input = sys.stdin.readline

n = int(input())
project_list = []
score = 0

for _ in range(n):
    project = list(map(int, input().split()))

    if project[0] == 1:
        project_list.append(project)

    if project_list:
        project = project_list.pop()
        project[2] -= 1

        if project[2] == 0:
            score += project[1]
        else:
            project_list.append(project)

print(score)