import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
alist = list(map(int, input().split()))

dq = deque()

for i in range(N): #슬라이딩 윈도우
  while dq and (dq[-1][1] > alist[i]): 
      dq.pop() # dp 리스트에 추가하려는 값이 지금 가장 큰 값보다 작다면 dp 마지막 요소 제거 
  dq.append((i + 1, alist[i])) # dp리스트에 (인덱스, 값)순으로 추가
  if dq[-1][0] - dq[0][0] >= L:
    dq.popleft() # dp리스트에 인덱스 값이 L값을 넘어가면 왼쪽(작은 값)을 제거
  print(dq[0][1], end=' ')