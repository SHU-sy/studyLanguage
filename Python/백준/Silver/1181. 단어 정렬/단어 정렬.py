import sys
input = sys.stdin.readline

n = int(input())
w = list(set([input().strip() for _ in range(n)]))
w.sort(key=lambda x: (len(x), x))

print("\n".join(w))