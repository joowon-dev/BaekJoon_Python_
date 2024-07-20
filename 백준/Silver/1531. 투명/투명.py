import sys
N,M = map (int, sys.stdin.readline().split())
arr=[[0] * 100 for i in range(100)]
count=0
for _ in range(N):
    x1,y1,x2,y2 =  map (int, sys.stdin.readline().split())
    for i in range(y1-1,y2):
        for j in range(x1-1,x2):
            arr[i][j] +=1
for i in range(100):
    for j in range(100):
        if arr[i][j] > M:
            count +=1
print(count)