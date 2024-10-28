import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())

connect = []
for i in range(num):
    connect.append(list(map(int, sys.stdin.readline().split())))

result = [1]
tmp = 0
while tmp != len(result):
    tmp = len(result)
    for i in connect:
        if i[0] in result and i[1] not in result:
            result.append(i[1])
        elif i[1] in result and i[0] not in result:
            result.append(i[0])

print(tmp-1)