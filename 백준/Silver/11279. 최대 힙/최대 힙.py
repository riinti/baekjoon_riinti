import heapq
import sys

input = sys.stdin.readline

n = int(input())
m_heap = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        if len(m_heap) != 0:
            print(heapq.heappop(m_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(m_heap, (-temp, temp))