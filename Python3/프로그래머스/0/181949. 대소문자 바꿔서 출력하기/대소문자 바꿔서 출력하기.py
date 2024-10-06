import sys

str = sys.stdin.readline().strip()
result = []
for i in range(len(str)):
    if ord('A') <= ord(str[i]) <= ord('Z'):
        result.append(str[i].lower())
    else:
        result.append(str[i].upper())
print("".join(result))