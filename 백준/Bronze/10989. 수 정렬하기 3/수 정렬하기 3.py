import sys

input = sys.stdin.readline

N = int(input())
  
cou = [0] * (10000 + 1)  #0이 존재하는 리스트생성,카운트할 리스트

for _ in range(N):
  cou[int(input())] += 1 #각각의 값이 나올때마다 cou에 해당하는 인덱스에 1추가

for i in range(len(cou)):
    if cou[i] != 0: 
        for _ in range(cou[i]):
            print(i) #cou의 0이 아닌값 즉 nlist에서 존재한 값을 0부터 차례로 출력