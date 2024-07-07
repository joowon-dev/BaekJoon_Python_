T=int(input())
for i in range(T):
    N,M = map(int,input().split())
    factorial1, factorial2 = 1,1
    while(N>0):
        factorial1=N*factorial1
        factorial2=M*factorial2
        N-=1
        M-=1
    print(factorial2//factorial1)