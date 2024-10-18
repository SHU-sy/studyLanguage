import sys
input = sys.stdin.readline
n,m = map(int, input().split())
see_set = set()
listen_set = set()

listen_set.update([input().strip() for _ in range(n)])
see_set.update([input().strip() for _ in range(m)])
ls = listen_set.intersection(see_set)
print(len(ls))
print("\n".join(sorted(ls)))