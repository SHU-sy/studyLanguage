import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
s = 0
e = len(arr)-1
count = 0

while s < e:
    current_sum = arr[s] + arr[e]
    if current_sum == x:
        count += 1
        s += 1
        e -= 1

    elif current_sum < x:
        s += 1

    else:
        e -= 1
print(count)