import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)

    return max_sum
print(kadane(arr))