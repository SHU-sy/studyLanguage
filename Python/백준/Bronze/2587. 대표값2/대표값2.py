import sys
num = [int(sys.stdin.readline().strip()) for _ in range(5)]
print(sum(num)//5)
print(sorted(num)[2])