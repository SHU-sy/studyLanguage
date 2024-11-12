import sys
input = sys.stdin.readline
a, b = input().split()
a_rev = int(''.join(reversed(a)))
b_rev = int(''.join(reversed(b)))
sum_num = a_rev + b_rev
print(int(''.join(reversed(str(sum_num)))))