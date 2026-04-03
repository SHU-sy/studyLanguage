n = int(input())
result = []
for i in range(1, 10):
    result.append(f"{n} * {i} = {n * i}")
print("\n".join(result))