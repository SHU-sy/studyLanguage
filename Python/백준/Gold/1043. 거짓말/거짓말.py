import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1


data = sys.stdin.read().split()
idx = 0

n, m = int(data[idx]), int(data[idx+1])
idx += 2

true_num = int(data[idx])
idx += 1
if true_num == 0:
    print(m)
    sys.exit()

true_people = list(map(int, data[idx:idx+true_num]))
idx += true_num

parent = [i for i in range(n+1)]
rank = [0] * (n+1)

for i in range(1, true_num):
    union(true_people[i], true_people[i-1])

party_list = []
for _ in range(m):
    party_size = int(data[idx])
    idx += 1
    party_people = list(map(int, data[idx:idx+party_size]))
    idx += party_size
    party_list.append(party_people)
    for i in range(1, party_size):
        union(party_people[i], party_people[i-1])

if true_people:
    root_true = find(true_people[0])

count = 0
for party in party_list:
    if all(find(person) != root_true for person in party):
        count += 1

print(count)