import sys 
A,B = map (int , sys.stdin.readline().split())
print(len(set(map(int, sys.stdin.readline().split()))^set(map(int, sys.stdin.readline().split()))))