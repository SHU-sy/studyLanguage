def solution(n):
    for i in range(1, n):
        num = i*i
        if num == n:
            return 1
        if num > n:
            return 2