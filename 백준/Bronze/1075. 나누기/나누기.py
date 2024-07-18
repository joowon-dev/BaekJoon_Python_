import sys
N=int(sys.stdin.readline())
F=int(sys.stdin.readline())
num=(N-100)-(N-100)%F
while(int((str(N))[:len(str(N))-2]+'00')>num):
    num+=F
print(('0'+str(num))[-2:])