import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
card = input().split()
m = int(input())
count_card = input().split()
ans = []

count_dict = defaultdict(int)
for a in card:
    count_dict[a] += 1
for i in count_card:
    ans.append(count_dict[i])
print(" ".join(map(str, ans)))