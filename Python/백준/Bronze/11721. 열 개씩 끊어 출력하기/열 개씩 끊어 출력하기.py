import sys
input = sys.stdin.readline
string = list(map(str, input().strip()))
while string:
    print("".join(string[:10]))
    del string[:10]