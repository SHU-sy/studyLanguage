import sys
arr = sys.stdin.readline()
ans = []
for string in arr:
    if string.isdigit():
        ans.append(string)

    elif 'a' <= string <= 'z':
        string = ord(string) + 13
        if string > ord('z'):
            string -= 26
        ans.append(chr(string))

    elif 'A' <= string <= 'Z':
        string = ord(string) + 13
        if string > ord('Z'):
            string -= 26
        ans.append(chr(string))

    else:
        ans.append(string)
print("".join(ans))