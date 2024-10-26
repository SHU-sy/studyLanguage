arr = input().strip()
count = 10
pre_bowl = arr[0]
for bowl in arr[1:]:
    if bowl == pre_bowl:
        count += 5
    else:
        count += 10
    pre_bowl = bowl
print(count)