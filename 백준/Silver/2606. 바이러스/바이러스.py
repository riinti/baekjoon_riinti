import sys

input = sys.stdin.readline

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)

com = int(input())
n = int(input())

visited = [0] * (com+1)
graph = [[] for i in range(com+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(1)

count = 0
for i in visited:
    if i == 1:
        count+=1
print(count-1)