import sys 
A=sys.stdin.readline().strip().split('.')
ans=''
for i in A:
    x=len(str(i))
    if(x%2==1):
        ans='-1.'
        break
    elif(x%4==0):
        ans+='A'*x
    else:
        ans+='A'*(x-2)+'B'*2
    ans+='.'
print (ans[0:-1])