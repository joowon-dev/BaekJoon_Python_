N = int(input())
for i in range(N):
    print(" "*(N-i-1),end="")
    print("*"*(1+2*i),end="")
    print("")