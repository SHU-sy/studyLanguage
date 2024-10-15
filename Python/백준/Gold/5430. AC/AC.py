import sys
from collections import deque
input = sys.stdin.readline
testcase = int(input())

for _ in range(testcase):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1]

    if arr:
        nums = deque(map(int, arr.split(',')))
    else:
        nums = deque()

    reverse = False

    for functions in p:
        if functions == 'R':
            reverse = not reverse
        elif functions == 'D':
            if not nums:
                print("error")
                break
            if reverse:
                nums.pop()
            else:
                nums.popleft()
    else:
        if reverse:
            nums.reverse()
        print("[" + ",".join(map(str, nums)) + "]")