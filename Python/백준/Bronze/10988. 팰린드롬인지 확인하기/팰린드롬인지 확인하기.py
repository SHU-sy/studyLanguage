import sys
w = sys.stdin.readline().strip()

if w[:len(w)] == w[-len(w):][::-1]:
    print("1")
else:
    print("0")