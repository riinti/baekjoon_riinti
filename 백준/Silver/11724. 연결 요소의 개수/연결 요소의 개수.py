import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

point, line = map(int, input().split())


visited = [0] * (point+1)
graph = [[] for i in range(point+1)]

for _ in range(line):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

count = 0 # 연결 노드의 수
visited = [0] * (point+1)
for i in range(1, point+1):
    if visited[i] == 0:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1
        
print(count)