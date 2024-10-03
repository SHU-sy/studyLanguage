t = int(input())
for _ in range(t):
    change = [25, 10, 5, 1]
    result = [0 for _ in range(4)]
    c = int(input())
    for i in range(4):
        result[i] += c // change[i]
        c %= change[i]
    print(" ".join(map(str, result)))