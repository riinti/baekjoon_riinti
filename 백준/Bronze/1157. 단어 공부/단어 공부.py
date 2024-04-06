word = str(input())
word = word.upper() #입력단어 대문자로 저장
nlist = list(set(word)) #입력단어 알파벳 리스트로 변환
mlist = []

if len(word)==1:
  print(word)
else:
  for i in nlist:
      mlist.append(word.count(i)) #리스트에 각 알파벳 갯수 저장
    
  if mlist.count(max(mlist)) != 1:
    print("?") #최빈값이 여러개일때
  else:
    print(nlist[mlist.index(max(mlist))]) #최빈값이 여러개가 아닐때