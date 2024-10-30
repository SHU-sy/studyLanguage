import sys
from collections import defaultdict
input = sys.stdin.readline
trees = defaultdict(int)
total_tree = 0

while True:
    tree = input().strip()
    if tree == "":
        break
    trees[tree] += 1
    total_tree += 1

for tree, count in sorted(trees.items()):
    print(f"{tree} {((trees[tree]/total_tree)*100):.4f}")