t = int(input())
for _ in range(t):
    a = int(input())
    total = 0
    for i in range(1, a+1):
        if i%2!=0:
            total += i
    print(total)