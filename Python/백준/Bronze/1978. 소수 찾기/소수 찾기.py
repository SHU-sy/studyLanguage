n = int(input())
number = list(map(int, input().split()))
c = 0

for num in number:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            c += 1

print(c)