import sys
arr, word = (sys.stdin.readline().strip() for _ in range(2))
count = 0
p = 0
word_length = len(word)

while p <= len(arr) - word_length:
    if arr[p:p+word_length] == word:
        count += 1
        p += word_length
    else:
        p += 1
print(count)