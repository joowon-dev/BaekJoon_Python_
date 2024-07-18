import sys
N,M = map(int,sys.stdin.readline().split())
arr=[]
temp=[[1,1]]
temp1=[]
tempsum=[]
for i in range(N):
    arr.append(list(input()))
count=1
while(1):
    for i in temp:
        x,y=i
        for j in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
            a,b=j
            if a<=M and b<=N and a>0 and b>0:            
                if [a,b] not in tempsum:
                    if arr[b-1][a-1]=='1':
                        temp1.append([a,b])
                        tempsum.append([a,b])
    count+=1
    if [M,N] in temp1:
        break
    temp=[]
    temp=temp1.copy()
    temp1=[]
print(count)