import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
ans = set()

m_word = [w for w in arr if len(w)>=m]
counts = Counter(m_word)
word = sorted(counts.keys(), key=lambda x: (-counts[x], -len(x), x))
print("\n".join(word))