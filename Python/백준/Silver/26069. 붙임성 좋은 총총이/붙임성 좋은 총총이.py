import sys
input = sys.stdin.readline

n = int(input())
dance = set(['ChongChong'])

for _ in range(n):
    people = input().split()
    if (people[0] in dance) or (people[1] in dance):
        dance.add(people[0])
        dance.add(people[1])
print(len(dance))