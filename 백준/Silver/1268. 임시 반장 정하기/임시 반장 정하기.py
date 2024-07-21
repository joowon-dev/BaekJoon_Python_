import sys

n = int(sys.stdin.readline().strip())
arr1 = [[0 for j in range(5)] for i in range(n)]
arr4 = [0 for j in range(n)]
for i in range(n):
  arr1[i] = list(map(int, input().split()))

for i in range (n):
  for j in range(n):
    for x in range (5):
     if(arr1[i][x]==arr1[j][x]):   
       arr4[i]+=1
       break

print(arr4.index(max(arr4)) + 1) 