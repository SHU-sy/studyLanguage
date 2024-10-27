import sys
input = sys.stdin.readline

n, p = map(int, input().split())
w, l, g = map(int, input().split())
win, lose = set(), set()
score = 0

for _ in range(p):
    name, wl = input().split()
    if wl == 'W':
        win.add(name)
    else:
        lose.add(name)

for _ in range(n):
    name = input().strip()
    if name in win:
        score += w
    else:
        score = max(score - l, 0)

    if score >= g:
        print("I AM NOT IRONMAN!!")
        break
else:
    print("I AM IRONMAN!!")