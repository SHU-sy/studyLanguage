import sys
w = sys.stdin.readline().strip()
s = [0] * 26
for i in w:
    if 'A' <= i <= 'Z':
        index = ord(i) - 65
        s[index] += 1
    if 'a' <= i <= 'z':
        index = ord(i) - 97
        s[index] += 1
maxCount = max(s)
maxWord = [index for index, count in enumerate(s) if count == maxCount]

if len(maxWord) > 1:
    print("?")
else:
    print(chr(maxWord[0] + 65))