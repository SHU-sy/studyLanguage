from collections import deque
import sys

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, sys.stdin.readline().split())
    paper = deque(map(int, sys.stdin.readline().split()))
    paper_index = deque([i for i in range(n)])
    count = 0

    while paper:
        current_importance = paper[0]
        current_index = paper_index[0]

        if current_importance == max(paper):
            count += 1
            if current_index == m:
                print(count)
                break
            paper.popleft()
            paper_index.popleft()
        else:
            paper.rotate(-1)
            paper_index.rotate(-1)