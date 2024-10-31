m, n = map(int, input().split())
noPrime = [False for i in range(0, n+1)]
result = []
for i in range(2, n+1):
    if noPrime[i]:
        continue
    result.append(i)
    for j in range(i, n+1, i):
        noPrime[j] = True
for i in result:
    if m<=i and i <=n:
        print(i)