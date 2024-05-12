import sys

input = sys.stdin.readline

word = input().rstrip()

word = word.replace("c=","_")
word = word.replace("c-","_")
word = word.replace("dz=","_")
word = word.replace("d-","_")
word = word.replace("lj","_")
word = word.replace("nj","_")
word = word.replace("s=","_")
word = word.replace("z=","_")
print(len(word))