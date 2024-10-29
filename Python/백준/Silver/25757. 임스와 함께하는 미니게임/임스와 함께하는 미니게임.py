import sys
input = sys.stdin.readline
n, game = input().split()

count = 0
game_dict = {'Y': 2, 'F': 3, 'O': 4}
people = set(input().strip() for _ in range(int(n)))

print(len(people)//(game_dict[game]-1))