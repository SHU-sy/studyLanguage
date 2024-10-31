import math
n, k = map(int, input().split())
print(1%10007 if n==k or k==0 else math.comb(n, k) % 10007)