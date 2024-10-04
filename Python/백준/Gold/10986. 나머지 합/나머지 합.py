import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
prefix_sum = 0
c = [0] * m  # same index count
c[0] = 1
count = 0  # 구간의 개수

for i in range(n):
    prefix_sum += number[i]
    remainder = prefix_sum % m

    count += c[remainder]
    c[remainder] += 1
print(count)