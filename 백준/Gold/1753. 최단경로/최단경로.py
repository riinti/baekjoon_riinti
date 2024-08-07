import heapq
import sys

input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값 -> 10억

n, m = map(int, input().split())
start = int(input())

# 3가지 리스트 필요: 노드에 연결된 간선, 방문여부, 최단거리 저장(답)
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) #무한으로 초기화

for _ in range(m):
    u, v, w = map(int, input().split())#시작정점, 끝정점, 가중치
    graph[u].append((v, w))

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        #현재 노드와 연결된 인접 노드 확인
        for i in graph[now]:
            cost =dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])