import sys
import heapq
input = sys.stdin.readline
n = int(input())
num_heapq = []

def push_abs_heap(heap, value):
    heapq.heappush(heap, (abs(value), value))

def pop_abs_heap(heap):
    return heapq.heappop(heap)[1]

for _ in range(n):
    num = int(input())
    if num == 0:
        if not num_heapq:
            print("0")
        else:
            print(pop_abs_heap(num_heapq))
    else:
        push_abs_heap(num_heapq, num)