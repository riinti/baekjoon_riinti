import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  age, name = input().split()
  nlist.append([int(age), name])

nlist = sorted(nlist, key=lambda x: x[0])#람다는 함수를 한줄로 정리해줌 key뒤에 오는 기준으로 리스트를 정력
#key가 없을 떄는 알파벳도 정렬에 관여하지만 x[0]즉 나이로만 정렬하게 되면서 기존 입력받은 순서가 유지

for i in nlist:
  print(i[0], i[1])
