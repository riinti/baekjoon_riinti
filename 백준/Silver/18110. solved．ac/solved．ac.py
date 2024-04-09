import sys

input = sys.stdin.readline

def ban(num):
  if num - int(num) >= 0.5:
    return int(num) + 1
  else:
    return int(num)

N = int(input())

if N != 0:
  n = int(ban(N*0.15))
  nlist = []

  for _ in range(N):
    nlist.append(int(input()))
  
  nlist = sorted(nlist)
  
  if n!=0:
    del nlist[0:n]
    del nlist[-n:]

  dif = ban(sum(nlist)/len(nlist))
  print(dif)

else:
  print("0")

#round함수의 특징
#5 미만의 숫자는 내림, 5 초과의 숫자는 올림
#만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림