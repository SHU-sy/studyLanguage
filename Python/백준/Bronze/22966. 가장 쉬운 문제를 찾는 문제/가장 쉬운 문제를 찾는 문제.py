import sys
input = sys.stdin.readline

n = int(input().strip())
res, num = input().split()
num = int(num)

for _ in range(n-1):
    q, nums = input().split()
    nums = int(nums)
    
    if nums < num:
        res = q
        num = nums
print(res)