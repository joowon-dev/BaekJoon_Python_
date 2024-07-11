import sys
while(1):
    arr = list(map(int,sys.stdin.readline().split()))
    if(arr[0]==-1):
        break
    count= 0
    for i in arr:
        if i==0:
            break
        if i*2 in arr : 
            count+=1
    print(count)