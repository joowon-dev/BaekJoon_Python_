import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
arr=[1]
temp = [[0 for j in range(2)] for i in range(y)]
for i in range (y):
    temp[i] = list(map(int,sys.stdin.readline().split()))
    if temp[i][0] in arr:
        arr.append(temp[i][1])
    elif temp[i][1] in arr:
        arr.append(temp[i][0])
while(1):
    count=0
    for i in range(y):
        if temp[i][0] in arr:
            arr.append(temp[i][1])
            temp[i][0]=0
            temp[i][1]=0
            count+=1
        elif temp[i][1] in arr:
            arr.append(temp[i][0])
            temp[i][0]=0
            temp[i][1]=0
            count+=1
    if(count==0):
        break
print(len(list(set(arr)))-1)