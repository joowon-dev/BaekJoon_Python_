import sys

A = int(sys.stdin.readline())
arr = []
temp =[]
for _ in range(A):
    B=input()
    if len(temp)==0 : 
        temp.append(B)
    else : 
        sum = B+B 
        count = 0 
        for i in temp :       
            if i  not in sum :
                count+=1
            elif len(i)!=len(B):
                count+=1
            if count == len(temp):
                temp.append(B)
                break
print(len(temp))