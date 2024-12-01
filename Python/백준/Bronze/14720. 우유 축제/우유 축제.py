import sys
input = sys.stdin.readline

n = int(input())
milks = list(map(int, input().split()))
count = 0
temp = ''

for	milk in milks:
	if milk == 0 and temp == "b":
		temp = "s"
		count += 1

	if milk == 1 and temp == "s":
		temp = "c"
		count += 1

	if milk == 2 and temp == "c":
		temp = "b"
		count += 1

	if count == 0 and milk == 0:
		temp = "s"
		count += 1

	else :
		continue
print(count)