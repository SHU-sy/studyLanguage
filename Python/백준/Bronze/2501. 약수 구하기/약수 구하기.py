n, k = map(int, input().split())
result = []
a = 0
while a <= n:
    a += 1
    if n % a == 0:
        result.append(a)
    if len(result) == k:
        print(result[k-1])
        break
if len(result) < k:
    print("0")