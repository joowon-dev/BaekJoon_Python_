N,M=map(int,input().split())
arr=[[]*M]*N
start1='W'
start2='B'
count1=0
count2=0
count=[]
for i in range(N):
  arr[i]=input()
for i in range(N+1-8):
  for x in range (M+1-8): 
    for j in range(i,8+i):
      start1, start2 = start2, start1
      comp1, comp2 =start1, start2
      for y in range(x,8+x):
        comp1, comp2 =comp2, comp1
        if(comp1 !=arr[j][y]):
          count1+=1
        elif(comp2 !=arr[j][y]
             ):
          count2+=1
    count.append(count1)
    count.append(count2)
    count1=0
    count2=0
print(min(count)) 