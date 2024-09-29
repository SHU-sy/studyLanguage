import sys
mapping = {
    'c=': 1, 'c-': 1, 'dz=': 1,
    'd-': 1, 'lj': 1, 'nj': 1,
    's=': 1, 'z=': 1
}
a = sys.stdin.readline().strip()

for i in mapping.keys():
    a = a.replace(i, '1')
print(len(a))