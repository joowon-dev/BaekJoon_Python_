import sys 
N,M=map(int,sys.stdin.readline().strip().split())
A=1000
B=1000
for i in range(M):
    tempA,tempB=map(int,sys.stdin.readline().strip().split())
    if tempA>tempB*6 :
        tempA=tempB*6
    if tempA<A:
        A=tempA
    if tempB<B:
        B=tempB
if(A>B*6):
    A=B*6
ans = divmod(N,6)
print(ans[0]*A+ans[1]*B if (ans[0]+1)*A>ans[0]*A+ans[1]*B else (ans[0]+1)*A)