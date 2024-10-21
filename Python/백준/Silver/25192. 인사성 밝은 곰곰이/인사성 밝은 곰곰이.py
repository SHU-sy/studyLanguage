import sys
input = sys.stdin.readline
n = int(input())
new_chat = set()
count = 0

for i in range(n):
    chat = input().strip()
    if chat == "ENTER":
        new_chat.clear()
    elif chat not in new_chat:
        new_chat.add(chat)
        count += 1

print(count)