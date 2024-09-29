import sys
for i in range(100):
    try:
        a = sys.stdin.readline().strip()
        if a:
            print(a)
    except EOFError:
        break