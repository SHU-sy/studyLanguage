import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while True:
        less = heapq.heappop(scoville)
        
        if less >= K:
            return count
        if not scoville:
            return -1
        s = less + (heapq.heappop(scoville)*2)
        count += 1
        heapq.heappush(scoville, s)