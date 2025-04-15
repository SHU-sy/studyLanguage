import sys
input = sys.stdin.readline

def time_to_ms(time_str):
    minute, second, ms = time_str.split(':')
    total_ms = int(minute) * 60000 + int(second) * 1000 + int(ms)
    return total_ms

peoples = [input().split() for _ in range(8)]
peoples.sort(key=lambda x: time_to_ms(x[0]))
score = [10, 8, 6, 5, 4, 3, 2, 1]
b_score = 0
r_score = 0

for i in range(8):
    if peoples[i][1] == "B":
        b_score += score[i]
    else:
        r_score += score[i]

print("Red" if r_score > b_score else "Blue")