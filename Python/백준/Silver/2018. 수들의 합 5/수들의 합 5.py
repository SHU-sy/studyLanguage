n = int(input())
count = 0

for a in range(1, n+1):
    total = n - (a * (a -1)) // 2
    
    if total <= 0:
        break
    if total % a == 0:
        count += 1
print(count)