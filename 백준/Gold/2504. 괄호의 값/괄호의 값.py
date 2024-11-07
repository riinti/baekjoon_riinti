import sys

input = sys.stdin.readline

arr=input().rstrip()
stack=[]

answer=0
tmp=1
for i in range(len(arr)):
    if arr[i] =='(':
        stack.append(arr[i])
        tmp *=2
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *=3
    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if arr[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2 
    else:
        if not stack or stack[-1] == "(":
            answer=0
            break
        if arr[i-1] =='[':
            answer+=tmp
        stack.pop()
        tmp //=3

if stack:
    print(0)
else:
    print(answer)