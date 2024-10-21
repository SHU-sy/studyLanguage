import sys
from collections import OrderedDict
input = sys.stdin.readline
lists = OrderedDict()

k, l = map(int, input().split())

for _ in range(l):
    std_num = input().strip()
    if std_num in lists:
        del lists[std_num]
    lists[std_num] = True
print("\n".join(list(lists.keys())[:k]))