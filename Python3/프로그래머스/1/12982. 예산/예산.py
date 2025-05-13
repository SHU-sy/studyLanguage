import heapq
def solution(d, budget):
    heapq.heapify(d)
    count = 0

    while d:
        if d[0] <= budget:
            budget -= heapq.heappop(d)
            count += 1
        else:
            break
    return count