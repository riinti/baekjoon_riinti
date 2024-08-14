import sys

input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n + 1) # 부모 테이블

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i


edges = [] # 모든 간선을 담을 리스트
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges = sorted(edges,key=lambda x:(x[2]))


for i in edges:
    a, b, cost = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)