import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1
    return True


n, m = map(int, input().split())
true_list = list(map(int, input().split()))
true_num = true_list[0]

parent = [i for i in range(n+1)]
rank = [0] * (n+1)
count = 0
party_list = []

if true_num == 0:
    print(m)
    sys.exit()
else:
    true_people = true_list[1:]
    for i in range(1, true_num):
        union(true_people[i], true_people[i - 1])

for _ in range(m):
    party_num, *party_people = map(int, input().split())
    party_list.append(party_people)
    for i in range(1, party_num):
        union(party_people[i], party_people[i-1])

true_root = set(find(p) for p in true_people)
for party in party_list:
    if any(find(person) in true_root for person in party):
        continue
    count += 1
print(count)