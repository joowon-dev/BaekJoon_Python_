import sys 
for _ in range(int(sys.stdin.readline())):
    print(1 if bin(int(sys.stdin.readline())).count('1')==1 else 0)