while True:
    n = int(input())

    if n == -1:
        break

    number = []
    s = 0
    for i in range(1, n):
        if n % i == 0:
            number.append(i)
            s += i

    if s == n:
        print(f"{n} = {' + '.join(str(i) for i in number)}")
    else:
        print(f"{n} is NOT perfect.")