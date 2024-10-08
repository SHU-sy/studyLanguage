a, b, v = map(int, input().split())
day = (v-b-1) // (a-b) + 1  # 가야하는거리 // 하루에 가는 거리 + 마지막날
print(day)