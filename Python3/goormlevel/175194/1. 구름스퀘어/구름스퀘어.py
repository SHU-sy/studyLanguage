n = int(input())
s, e = zip(*[map(int, input().split()) for _ in range(n)])
s, e = list(s), list(e)

count = 0
event = sorted(zip(s, e), key=lambda x: x[1])
end = 0

for i in event:
    if i[0] > end:
        count += 1
        end = i[1]
print(count)