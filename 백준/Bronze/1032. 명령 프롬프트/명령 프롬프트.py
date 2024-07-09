N = int(input())
arr=[]
count =N
temp=0
ans=[]
for i in range(N):
    arr.append(input())
for i in range(len(arr[0])):
    count =N
    temp=0
    for j in range(len(arr)):
        if(temp!=arr[j][i]):
            temp=arr[j][i]
        else:
            count-=1
    if(count ==1):
        ans.append(temp)
    else:
        ans.append('?')
for i in ans:
    print(i,end='')  