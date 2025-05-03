import sys
from collections import Counter

do = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]
works = []

line = sys.stdin.readlines()
for i in line:
    works.extend(i.split())

total = len(works)
works = Counter(works)

for todo in do:
    print(f"{todo} {works[todo]} {works[todo]/total:.2f}")
print(f"Total {total} 1.00")