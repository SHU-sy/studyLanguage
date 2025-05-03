import sys
input = sys.stdin.readline

f = input().split()
m = input().split()
colors = set(f+m)

birds = []
for body in colors:
    for tail in colors:
        birds.append(f"{body} {tail}")
print("\n".join(sorted(birds)))