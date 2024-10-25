import sys
input = sys.stdin.readline

def palindrome(string):
    str_len = len(string)
    start = 0
    end = str_len -1

    while start < end:
        if string[start] != string[end]:
            left = True
            left_s = start+1
            left_e = end
            while left_s < left_e:
                if string[left_s] != string[left_e]:
                    left = False
                    break
                left_s += 1
                left_e -= 1

            right = True
            right_s = start
            right_e = end - 1
            while right_s < right_e:
                if string[right_s] != string[right_e]:
                    right = False
                    break
                right_s += 1
                right_e -= 1

            return 1 if left or right else 2
        start += 1
        end -= 1
    return 0

t = int(input())
arr = [input().strip() for _ in range(t)]
for string in arr:
    print(palindrome(string))