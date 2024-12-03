import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tracks = list(map(int, input().split()))
count = 0

for i in range(1, n):
	if tracks[i-1] >= tracks[i]:
		if tracks[i-1]-tracks[i] < k:
			count += 1
			tracks[i] += k

		else:
			print(-1)
			sys.exit()

print(count)