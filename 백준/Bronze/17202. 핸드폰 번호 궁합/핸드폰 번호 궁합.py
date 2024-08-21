import sys 
A=sys.stdin.readline()
B=sys.stdin.readline()
arr=''
arrtemp=''
for i in range (8):
    arr+=A[i]+B[i]
while len(arr) > 2:
    for i in range(len(arr)-1):
        temp=int(arr[i])+int(arr[i+1])
        if temp>=10:
            temp=temp-10
        arrtemp+=str(temp)
    arr=''
    arr=arrtemp
    arrtemp=''
print(arr)