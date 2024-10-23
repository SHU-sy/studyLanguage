def solution(n, m):
    result = []
    isvis = [False for i in range(0, n)]
    def back(p, m):
        temp = p
        if len(p.replace(" ",""))== m:
            result.append(temp)
        else:
            for i in range(0, n):
                if isvis[i] == False:
                    isvis[i] = True
                    back(p+str(i + 1)+" ", m)
                    isvis[i] = False

    for i in range(0, n):
        isvis[i] = True
        back(str(i + 1)+" ", m)
        isvis[i] = False
    for i in result:
        print(i)


n, m = map(int, input().split())
solution(n, m)