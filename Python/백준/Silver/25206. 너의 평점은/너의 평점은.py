import sys
score_map = {
    'A+' : 4.5, 'A0' : 4.0,
    'B+' : 3.5, 'B0' : 3.0,
    'C+' : 2.5, 'C0' : 2.0,
    'D+' : 1.5, 'D0' : 1.0,
    'F' : 0.0
}
total_credit = 0
sum_cs = 0
for i in range(20):
    sub, credit, score = sys.stdin.readline().split()

    if score == "P":
        continue

    total_credit += float(credit)
    sum_cs += float(credit) * score_map[score]
print(sum_cs / total_credit)