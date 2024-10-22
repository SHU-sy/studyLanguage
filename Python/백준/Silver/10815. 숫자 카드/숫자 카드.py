import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
num_card = map(int, input().split())
count_card = defaultdict(int)

for card in num_card:
    count_card[card] += 1

m = int(input())
my_card = map(int, input().split())
ans = []

for mc in my_card:
    ans.append(count_card[mc])
print(" ".join(map(str, ans)))