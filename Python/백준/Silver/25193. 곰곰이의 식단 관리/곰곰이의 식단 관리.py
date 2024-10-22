import sys
input = sys.stdin.readline
n = int(input())
foods = list(input().strip())

count_c = foods.count("C")
count_not_c = n - count_c

if not count_not_c:
    print(count_c)
elif count_not_c == 1:
    print((count_c+1) // 2)
else:
    print((count_c + count_not_c) // (count_not_c + 1))