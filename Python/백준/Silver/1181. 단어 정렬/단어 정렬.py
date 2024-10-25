import sys
input = sys.stdin.readline

n = int(input())
word = set(input().strip() for _ in range(n))
word = sorted(word, key=lambda x: (len(x), x))
print("\n".join(word))