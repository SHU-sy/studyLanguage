n = int(input())
number = list(map(int, input().split()))
num = sum(number)
print(oct(num)[2:])