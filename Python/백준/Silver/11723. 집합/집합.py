import sys
input = sys.stdin.readline

m = int(input())
mask = 0
for _ in range(m):
    command = input().split()
    if len(command) > 1:
        c = 1 << int(command[1])
    match command[0]:
        case "add":
            mask |= c

        case "remove":
            mask &= ~c

        case "check":
            print(1 if (mask & c) else 0)

        case "toggle":
            mask ^= c

        case "all":
            mask = ~0

        case "empty":
            mask = 0