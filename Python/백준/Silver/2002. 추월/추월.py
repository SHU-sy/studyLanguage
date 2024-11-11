import sys
from collections import OrderedDict
input = sys.stdin.readline

n = int(input())

D_list = OrderedDict()
for i in range(n):
    D_list[input().strip()] = i

Y_list = []
for i in range(n):
    Y_list.append(input().strip())

count = 0

for i in range(n - 1):
    for j in range(i+1, n):
        if D_list[Y_list[i]] > D_list[Y_list[j]]:
            count += 1
            break

print(count)