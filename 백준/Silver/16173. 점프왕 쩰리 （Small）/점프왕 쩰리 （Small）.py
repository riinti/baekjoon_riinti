import sys

input = sys.stdin.readline

n = int(input()) #범위 생성
graph = [list(map(int, input().split())) for _ in range(n)] #게임판 생성
dx = [1, 0] 
dy = [0, 1]#오른쪽과 아래 방향 설정

visited = [[0] * n for _ in range(n)] #방문여부 판단 리스트

def dfs(x, y):
    if x >= n or x <= -1 or y >= n or y <= -1: 
        return False #범위 밖으로 나가면 패배
    if visited[x][y] == 1:
        return False #이미 방문해서 실패한곳

    if graph[x][y] == -1:
        print('HaruHaru')
        exit() #도착지 도착

    visited[x][y] = 1 #방문한 곳 1로 채우기

    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y] #좌표이동
        dfs(nx, ny)#재귀

if not dfs(0, 0):
    print('Hing')