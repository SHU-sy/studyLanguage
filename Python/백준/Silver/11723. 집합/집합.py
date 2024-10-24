import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    command = input().split()
    if len(command) > 1:
        c = int(command[1])
    match command[0]:
        case "add":
            s.add(c)

        case "remove":
            s.discard(c)

        case "check":
            print(1 if c in s else 0)

        case "toggle":
            if c in s:
                s.remove(c)
            else:
                s.add(c)

        case "all":
            s = set(range(1, 21))

        case "empty":
            s.clear()