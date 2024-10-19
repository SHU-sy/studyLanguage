import sys
from collections import deque
input = sys.stdin.readline

def conveyor_belt(n, k, belt):
    robot = deque([False] * n)
    step = 0
    zero_count = belt.count(0)

    while True:
        step += 1

        belt.rotate(1)
        robot.rotate(1)
        robot[-1] = False

        for i in range(n-2, -1, -1):
            if robot[i] and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    zero_count += 1

        robot[-1] = False

        if belt[0] > 0 and not robot[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                zero_count += 1

        if zero_count >= k:
            break

    return step

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
answer = conveyor_belt(n, k, belt)
print(answer)