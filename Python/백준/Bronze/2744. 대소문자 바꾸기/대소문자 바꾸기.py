import sys
a = sys.stdin.readline().strip()
r = []
for i in range(len(a)):
    if 65 <= ord(a[i]) <= 90:
        r.append(a[i].lower())
    else:
        r.append(a[i].upper())
print(''.join(r))