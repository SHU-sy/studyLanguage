import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
count = 0

for index in range(n):
    num = arr[index]
    s = 0
    e = len(arr) - 1

    while s < e:
        if s == index:
            s += 1
            continue
        if e == index:
            e -= 1
            continue

        num_sum = arr[s] + arr[e]

        if num_sum == num:
            count += 1
            break
        elif num_sum < num:
            s += 1
        else:
            e -= 1

print(count)