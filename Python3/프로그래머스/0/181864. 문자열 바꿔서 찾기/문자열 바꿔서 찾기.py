def solution(myString, pat):
    arr = ''
    for s in myString:
        if s == "A":
            arr += "B"
        else:
            arr += "A"
    return 1 if pat in arr else 0