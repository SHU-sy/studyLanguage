import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word1, word2 = input().split()
    s_word1, s_word2 = "".join(sorted(list(word1))), "".join(sorted(list(word2)))
    if s_word1 == s_word2:
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")