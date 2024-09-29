import sys
w = sys.stdin.readline().strip()
for i in range(ord('a'), ord('z')+1):
    print(w.find(chr(i)), end=' ')