import sys 
A,B = map (int , sys.stdin.readline().split())
print(int(str(int(str(A)[::-1]) + int(str(B)[::-1]))[::-1]))