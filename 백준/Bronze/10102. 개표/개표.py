import sys

x = int(sys.stdin.readline())
y = str(sys.stdin.readline())


if  y.count('A')>x/2:
    print('A')
elif y.count('A')<x/2:
    print('B')
else :
    print('Tie')