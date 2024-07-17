import sys 

n,d = map(int,sys.stdin.readline().split())
temp=''
for i in range(n):
    temp+=str(i+1)
print(temp.count(str(d)))