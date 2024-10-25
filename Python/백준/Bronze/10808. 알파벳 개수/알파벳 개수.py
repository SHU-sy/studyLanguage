import sys
from collections import Counter
s = sys.stdin.readline().strip()
counter = Counter(s)
for char in 'abcdefghijklmnopqrstuvwxyz':
    print(counter[char], end=' ')