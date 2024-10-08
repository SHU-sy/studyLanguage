n, k = map(int, input().split())
a = list(map(str, input().split()))
a = [x for x in a if str(k) not in x]
print(len(a))