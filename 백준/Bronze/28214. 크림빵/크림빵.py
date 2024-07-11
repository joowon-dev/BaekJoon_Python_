import sys
N,K,P = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
count =0 
temp=0
ans=0
for i in arr :
    temp+=1
    if i == 0:
        count+=1    
    if temp == K:
        if count <P :
            ans +=1
        temp=0
        count=0
print(ans)