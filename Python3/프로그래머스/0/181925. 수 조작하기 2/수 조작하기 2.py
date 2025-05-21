def solution(numLog):
    answer = ''
    res = 0
    for i in range(1, len(numLog)):
        res = numLog[i] - numLog[i-1]
        
        if res == 1:
            answer += 'w'
        elif res == -1:
            answer += 's'
        elif res == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer