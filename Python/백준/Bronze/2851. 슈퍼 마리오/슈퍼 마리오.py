import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(10)]
score = 0

for num in nums:
    if score + num <= 100:
        score += num
    else:
        if abs(100-(score+num)) <= abs(100-score):
            score += num
        break
print(score)