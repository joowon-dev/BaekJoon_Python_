import sys 
for _ in range(int(sys.stdin.readline())):
    arr= sorted(list(map(int,sys.stdin.readline().split())))
    print(arr[-3])