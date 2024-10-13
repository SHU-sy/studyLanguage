import sys
input = sys.stdin.readline
num = [int(input().strip()) for _ in range(3)]
s_num = sum(num)
c = 0
for i in range(3):
    if num[i] == 60:
        c +=1
if c == 3:
    print("Equilateral")

elif s_num == 180:
    if num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")