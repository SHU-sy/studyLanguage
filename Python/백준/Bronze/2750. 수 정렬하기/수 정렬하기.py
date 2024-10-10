import sys
input = sys.stdin.readline
n = int(input())
num = sorted(int(input().strip()) for _ in range(n))
sys.stdout.write("\n".join(map(str, num)))