import sys
input = sys.stdin.readline

def count_pointer(n, arr, x):
    arr.sort()
    s = 0
    e = len(arr) - 1
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
    return count

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(count_pointer(n, arr, x))