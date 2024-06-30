import sys

A = int(sys.stdin.readline())
arr =list((map(int,sys.stdin.readline().split())))

dp=[1]*A

for i in range (1,A):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
dp_arr=[]
x=max(dp)
for i in range(A-1,-1,-1):
    if dp[i] == x:
        dp_arr.append(arr[i])
        x-=1
print(max(dp)) 
dp_arr.reverse()    
for i in dp_arr:
    print(i,end=' ')