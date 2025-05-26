def solution(hp):
    count = 0
    attacks = [5, 3, 1]
    for attack in attacks:
        temp = hp//attack
        count += temp
        hp -= temp * attack
        if hp == 0:
            return count