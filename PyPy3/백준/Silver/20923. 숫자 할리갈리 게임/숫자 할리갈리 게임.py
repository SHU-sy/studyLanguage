import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
do_card = deque()
su_card = deque()

for _ in range(n):
    d, s = map(int, input().split())
    do_card.append(d)
    su_card.append(s)

ground_do = deque()
ground_su = deque()
current_do = 0
current_su = 0

for i in range(m):
    if i % 2 == 0:
        current_do = do_card.pop()
        ground_do.append(current_do)
    else:
        current_su = su_card.pop()
        ground_su.append(current_su)

    if not do_card:
        print("su")
        break
    elif not su_card:
        print("do")
        break

    if current_do == 5 or current_su == 5:
        if ground_su:
            do_card.extendleft(ground_su)
        if ground_do:
            do_card.extendleft(ground_do)
        ground_do.clear()
        ground_su.clear()
        current_do = 0
        current_su = 0

    elif current_do + current_su == 5 and ground_do and ground_su:
        su_card.extendleft(ground_do)
        su_card.extendleft(ground_su)
        ground_do.clear()
        ground_su.clear()
        current_do = 0
        current_su = 0

else:
    do_len = len(do_card)
    su_len = len(su_card)

    if do_len > su_len:
        print("do")
    elif do_len < su_len:
        print("su")
    elif do_len == su_len:
        print("dosu")