import sys
input = sys.stdin.readline
group_dict = {}

n, m = map(int, input().split())
for _ in range(n):
    group = input().strip()
    count = int(input())
    name = [input().strip() for _ in range(count)]
    group_dict[group] = list(map(str, name))
for i in range(m):
    quiz = input().strip()
    type = input().strip()

    if type == "0":
        print("\n".join(sorted(group_dict[quiz])))
    else:
        for key, val in group_dict.items():
            if quiz in val:
                print(key)