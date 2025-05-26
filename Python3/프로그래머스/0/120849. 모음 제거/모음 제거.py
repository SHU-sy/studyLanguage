def solution(my_string):
    arr = ["a", "e", "i", "o", "u"]
    answer = ''
    for string in my_string:
        if string not in arr:
            answer += string
    return answer