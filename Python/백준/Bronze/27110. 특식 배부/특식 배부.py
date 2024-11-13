n = int(input())
people = list(map(int, input().split()))
max_peo = 0

for p in people:
    max_peo += min(n, p)
print(max_peo)