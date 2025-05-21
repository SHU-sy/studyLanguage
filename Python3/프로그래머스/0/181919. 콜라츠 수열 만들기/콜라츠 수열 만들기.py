def solution(x):
    answer = []
    while True:
        answer.append(x)
        if x == 1:
            return answer
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x+1