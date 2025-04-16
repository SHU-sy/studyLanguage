import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    best_word = input().strip()
    for _ in range(n-1):
        word = input().strip()
        if best_word.upper() > word.upper():
            best_word = word
    print(best_word)