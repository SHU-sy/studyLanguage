import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
b_len = len(b)
result = []

for i in a:
    result.append(i)

    if len(result) >= b_len and result[-b_len:] == list(b):
        for _ in range(b_len):
            result.pop()

if result:
    print(''.join(result))
else:
    print("FRULA")