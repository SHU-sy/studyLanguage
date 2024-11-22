arr = sorted(list(map(int, input().split())))
a, b, c = arr

if a + b <= c:
    c = a + b - 1

print(a + b + c)