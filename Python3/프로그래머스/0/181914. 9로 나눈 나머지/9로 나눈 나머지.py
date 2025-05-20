def solution(number):
    answer = 0
    number = list(number)
    for n in number:
        answer += int(n)
    return answer%9