import sys
N,x,y=map(int,sys.stdin.readline().split())
round =1
a=[0]*N
while (1):
    count = 0
    group = 0
    for i in range(N):
        if (2**round>count):
            a[i]=group
            count +=1
        else:
            group += 1
            a[i]=group
            count=1
    if(a[x-1]==a[y-1]):
        print(round)
        break
    else:
        round +=1