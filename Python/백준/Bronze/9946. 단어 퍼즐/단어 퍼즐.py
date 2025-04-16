import sys
input = sys.stdin.readline

count = 0

while True:
    word1, word2 = [input().strip() for _ in range(2)]
    if word1 == "END" and word2 == "END":
        break

    count += 1

    if "".join(sorted(list(word1))) == "".join(sorted(list(word2))):
        print(f"Case {count}: same")
    else:
        print(f"Case {count}: different")