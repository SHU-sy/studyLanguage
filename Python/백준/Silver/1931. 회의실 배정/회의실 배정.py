import sys
input = sys.stdin.readline
n = int(input())
count = 0
meet = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
end = 0

for i in meet:
    if i[0] >= end:
        count += 1
        end = i[1]
print(count)