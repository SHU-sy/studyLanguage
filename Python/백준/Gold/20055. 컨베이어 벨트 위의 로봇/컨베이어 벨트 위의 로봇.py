import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)
step = 0

while True:
    step += 1

    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(n-1, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1

    robot[-1] = 0

    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= k:
        break
print(step)