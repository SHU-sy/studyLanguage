import sys
input = sys.stdin.readline

arr = sorted([int(input().strip()) for _ in range(9)])

two = sum(arr) - 100
s = 0
e = 8

while s < e:
    current_sum = arr[s] + arr[e]
    if current_sum == two:
        break

    elif current_sum > two:
        e -= 1

    else:
        s += 1

ans = [arr[i] for i in range(9) if i != s and i != e]

print("\n".join(map(str, ans)))