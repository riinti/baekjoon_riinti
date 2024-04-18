N = int(input())
nlist = list(map(int, input().split()))
count = 0

for j in nlist:
  b_count = 0
  if j > 1:
      for i in range(2, j):
          if j % i == 0:
            b_count += 1

      if b_count == 0:
        count += 1
  else:
    continue
      
print(count)