import sys

input = sys.stdin.readline

while True:
  graph = list(map(int, input().split()))

  if graph[0] == 0:
    break

  stack = []
  max_result = 0

  for i, height in enumerate(graph):
    if i == 0: 
      continue
      
    if stack and stack[-1][1] > height: # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작으면
      while stack: 
        stack_i, stack_height = stack.pop()
        width_start = 1
        if stack:
          width_start = stack[-1][0]+1
        result = (i - width_start) * stack_height
        max_result = max(result, max_result)
        # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
        if not stack or stack[-1][1] <= height:
          break

    
    if not stack or stack[-1][1] <= height: # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
      stack.append((i, height))

  
  while stack: # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산
      stack_i, stack_height = stack.pop()
      width_start = 1
      if stack:
        width_start = stack[-1][0]+1
      result = (graph[0]+1 - width_start) * stack_height
      max_result = max(result, max_result)

  print(max_result)