import sys
input = sys.stdin.readline
count = 0

n = int(input())
cute = [int(input()) for i in range(n)]
for c in cute:
    if c == 1:
        count += 1
    else:
        count -= 1
print("Junhee is not cute!" if count < 0 else "Junhee is cute!")