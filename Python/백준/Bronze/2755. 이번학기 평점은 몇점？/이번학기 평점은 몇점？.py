import sys
import decimal
input = sys.stdin.readline
score_dict = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}
n = int(input())
score = 0
total_grade = 0
for _ in range(n):
    sub = input().split()
    score += int(sub[1]) * score_dict[sub[2]]
    total_grade += int(sub[1])
print(f'{round(decimal.Decimal(score)/decimal.Decimal(total_grade),2):.2f}')