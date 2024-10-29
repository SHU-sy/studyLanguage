import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    sang, sun = set(), set()
    if n ==0 and m==0:
        break
    for _ in range(n):
        sang.add(int(input()))
    for _ in range(m):
        sun.add(int(input()))

    print(len(sang.intersection(sun)))