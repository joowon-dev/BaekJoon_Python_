import sys 

n,d = map(int,sys.stdin.readline().split())
temp=''
count = 0
for i in range(n):
    temp+=str(i+1)
for i in temp:
    if i==str(d):
        count+=1
print(count)