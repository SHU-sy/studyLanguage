import sys
from collections import defaultdict
input = sys.stdin.readline
alphabet = defaultdict(int)
t = int(input())

for i in range(t):
    case = input().strip()
    ans = [0]*10
    for w in case:
        alphabet[w] += 1

    while alphabet['Z'] > 0:
        for char in "ZERO":
            alphabet[char] -= 1
        ans[0] += 1
    while alphabet['W'] > 0:
        for char in "TWO":
            alphabet[char] -= 1
        ans[2] += 1
    while alphabet['U'] > 0:
        for char in "FOUR":
            alphabet[char] -= 1
        ans[4] += 1
    while alphabet['X'] > 0:
        for char in "SIX":
            alphabet[char] -= 1
        ans[6] += 1
    while alphabet['G'] > 0:
        for char in "EIGHT":
            alphabet[char] -= 1
        ans[8] += 1
    while alphabet['O'] > 0:
        for char in "ONE":
            alphabet[char] -= 1
        ans[1] += 1
    while alphabet['R'] > 0:
        for char in "THREE":
            alphabet[char] -= 1
        ans[3] += 1
    while alphabet['F'] > 0:
        for char in "FIVE":
            alphabet[char] -= 1
        ans[5] += 1
    while alphabet['S'] > 0:
        for char in "SEVEN":
            alphabet[char] -= 1
        ans[7] += 1
    while alphabet['E'] > 0:
        for char in "NINE":
            alphabet[char] -= 1
        ans[9] += 1

    res = ''.join(str(num) * ans[num] for num in range(10))
    print(f"Case #{i+1}: {res}")