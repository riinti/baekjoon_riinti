import sys

input = sys.stdin.readline

arr=[]

for _ in range(5):
    arr.append(int(input()))

arr.sort()#중앙값을 구하기 위해 정렬

print(round(sum(arr)/len(arr)))#1) 산술평균
print(arr[len(arr)//2])#2) 중앙값