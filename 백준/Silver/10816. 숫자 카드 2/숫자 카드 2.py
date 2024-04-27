import sys

input = sys.stdin.readline

N = int(input())
nlist = list(map(int,input().split()))
M =int(input())
mlist = list(map(int,input().split()))

hash = {} #딕셔너리(사전형)생성 인덱스 접근시 key값으로 접근

for i in nlist:
    if i in hash:
        hash[i] += 1 # i라는 key값에 접근 후 value값에 1을 더한다
    else:
        hash[i] = 1 # i라는 key값에 접근 후 value값에 1을 저장한다

for i in mlist:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
      