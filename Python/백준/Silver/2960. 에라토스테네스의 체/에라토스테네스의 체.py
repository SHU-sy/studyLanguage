import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in reversed(range(2, n+1))]
result = []
while arr:
    p = arr.pop()
    result.append(p)
    nums = [i for i in range(p, n+1, p)]
    for num in nums:
        if num in arr:
            arr.remove(num)
            result.append(num)
print(result[k-1])