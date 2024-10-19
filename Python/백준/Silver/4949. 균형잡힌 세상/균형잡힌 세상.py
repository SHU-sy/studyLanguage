import sys
from collections import deque
input = sys.stdin.readline

while True:
    data = input().rstrip()
    if data == ".":
        break

    s = deque()
    val = True

    for temp in data:
        if temp in "([":
            s.append(temp)
        elif temp in ")]":
            if not s:
                val = False
                break
            t = s.pop()
            if (temp == ")" and t != "(") or (temp == "]" and t != "["):
                val = False
                break
    if s:
        val = False

    print("yes" if val else "no")