N,M = map(int,input().split())
blist=[]
lst=[]
count=0
chess = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]
# chess=[["WBWBWBWB"],["BWBWBWBW"],["WBWBWBWB"],["BWBWBWBW"],["WBWBWBWB"],["BWBWBWBW"],["WBWBWBWB"],["BWBWBWBW"]]

for _ in range(N):
  blist.append(input())
  
for a in range(N-7):
  for b in range(M-7):
    w_index=0 
    b_index=0 
    for i in range(a,a+8):
      for j in range(b,b+8):
        if (i+j)%2==0:#짝수인 경우
          if blist[i][j]!=chess[i-a][j-b]:#B일 때
            w_index+=1
          else:#W일 때
            b_index+=1
        else:#홀수인 경우
          if blist[i][j]!=chess[i-a][j-b]:#B일 때
            w_index+=1
          else:#W일 때
            b_index+=1

    lst.append(b_index)
    lst.append(w_index)
print(min(lst))