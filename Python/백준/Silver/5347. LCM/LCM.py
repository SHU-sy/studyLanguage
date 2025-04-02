import sys
import math
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    print(math.lcm(nums[0], nums[1]))