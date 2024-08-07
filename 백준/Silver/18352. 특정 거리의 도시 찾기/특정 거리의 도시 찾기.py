import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, k, x= map(int, input().split())

# 3가지 리스트 필요: 노드에 연결된 간선, 방문여부, 최단거리 저장(답)
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())#시작정점, 끝정점
    graph[u].append((v, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
dijkstra(x)
rlist = []
for i in range(1, n+1):
    if distance[i] == k:
        rlist.append(i)
    else:
        continue
rlist.sort()
if len(rlist) == 0:
    print(-1)
else:
    print(*rlist, sep="\n")