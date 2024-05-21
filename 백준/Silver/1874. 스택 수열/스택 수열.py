import sys

input = sys.stdin.readline

n=int(input())
mlist = [] #스택수열 생성
num = 1 #스택수열에 들어갈 정수값
rlist = [] #출력 리스트

for i in range(n):
    inp_num = int(input())
    while num <= inp_num:
        rlist.append("+")
        mlist.append(num) #스택수열에 정수값 추가
        num += 1
    if inp_num == mlist[-1]:
        rlist.append("-")
        mlist.pop() #스택수열의 마지막값이 주어진 수와 같아질때
    else:
        rlist.append("NO")
        break
            
if "NO" in rlist:
    print("NO")
else:
    print(*rlist, sep= "\n")