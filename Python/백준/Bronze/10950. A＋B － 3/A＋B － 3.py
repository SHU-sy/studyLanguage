import sys
input = sys.stdin.readline

n = int(input())
print("\n".join((str(sum(map(int, input().split())))) for _ in range(n)))