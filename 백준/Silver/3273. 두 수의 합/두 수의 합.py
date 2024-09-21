import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))
K = int(input())

count = {}
cnt = 0

for num in n_list:
  count[num] = 0

for i in n_list:
  result = K - i
  if result in count:
    cnt += 1
     
print(cnt // 2)