import sys
input = sys.stdin.readline

def palindrome(s):
    return s == s[::-1]

def remove_string(string, index):
    new_string = string[:index] + string[index + 1:]
    return palindrome(new_string)

t = int(input())
arr = [input().strip() for _ in range(t)]
for string in arr:
    if string == string[::-1]:
        print(0)
    else:
        start = 0
        end = len(string) - 1
        palindrome_string = False

        for i in range(len(string) // 2):
            if string[start + i] != string[end - i]:
                temp1, temp2 = start+i, end-i
                if remove_string(string, temp1) or remove_string(string, temp2):
                    palindrome_string = True
                break

        if palindrome_string:
            print(1)
        else:
            print(2)