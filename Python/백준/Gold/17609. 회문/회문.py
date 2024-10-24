import sys
input = sys.stdin.readline

t = int(input())
arr = [input().strip() for _ in range(t)]
for string in arr:
    if string == string[::-1]:
        print(0)
    else:
        start = 0
        end = len(string) - 1
        p = False

        for i in range(len(string)//2):
            if string[start+i] != string[end-i]:
                left = True
                left_s = start + i + 1
                left_e = end - i
                while left_s < left_e:
                    if string[left_s] != string[left_e]:
                        left = False
                        break
                    left_s += 1
                    left_e -= 1

                right = True
                right_s = start+i
                right_e = end-i-1
                while right_s < right_e:
                    if string[right_s] != string[right_e]:
                        right = False
                        break
                    right_s += 1
                    right_e -= 1

                if left or right:
                    p = True
                break

        if p:
            print(1)
        else:
            print(2)