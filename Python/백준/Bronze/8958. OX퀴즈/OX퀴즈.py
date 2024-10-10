import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    a = input().strip()
    count = 0
    score = 0
    for i in a:
        if i == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)