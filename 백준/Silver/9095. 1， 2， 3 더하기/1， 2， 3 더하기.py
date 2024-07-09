import sys
a=[1,1,2,4] 
x = int(sys.stdin.readline())
for i in range (x):
    y = int(sys.stdin.readline())
    if y<len(a):
        print(a[y])
    else:
        for i in range (len(a),y+1):
            a.append(a[i-1]+a[i-2]+a[i-3])
        print(a[y])