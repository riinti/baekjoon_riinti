a = input()
if a[0]=="A":
  if a[1]=="+":
    b=4.3
  elif a[1]=="0":
    b=4.0
  else:
    b=3.7
elif a[0]=="B":
  if a[1]=="+":
    b=3.3
  elif a[1]=="0":
    b=3.0
  else:
    b=2.7
elif a[0]=="C":
  if a[1]=="+":
    b=2.3
  elif a[1]=="0":
    b=2.0
  else:
    b=1.7
elif a[0]=="D":
  if a[1]=="+":
    b=1.3
  elif a[1]=="0":
    b=1.0
  else:
    b=0.7
else:
  b=0.0
print(b)