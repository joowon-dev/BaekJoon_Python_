import sys
import math
n = int(sys.stdin.readline())
S,M,L,XL,XXL,XXXL=map(int,sys.stdin.readline().split())
T,P =map(int,sys.stdin.readline().split())
count=0
for i in S,M,L,XL,XXL,XXXL:
    count+=math.ceil(i/T) 
print(count)
print(math.floor(n/P),n % P)