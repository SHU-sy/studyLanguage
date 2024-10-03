import sys
word = [sys.stdin.readline().strip() for _ in range(5)]
line = []
for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            line.append(word[j][i])
print("".join(line))