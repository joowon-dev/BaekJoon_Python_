N=input()
arr=[]
for x in range(1,len(N)-1):
    for y in range(1,len(N)-x):
        for z in range(1,len(N)-x-y+1):
            if(x+y+z==len(N)):
                arr.append(N[:x][::-1]+N[x:x+y][::-1]+N[x+y:x+y+z][::-1])
arr.sort()
print(arr[0])