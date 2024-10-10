scale = list(map(int, input().split()))
ascending = [i for i in range(1, 9)]
result = ''
if scale == ascending:
    print("ascending")
elif scale == sorted(ascending, reverse=True):
    print("descending")
else:
    print("mixed")