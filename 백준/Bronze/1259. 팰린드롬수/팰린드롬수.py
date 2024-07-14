while(1):
    N=input()
    if(N=='0'):
        break
    temp=N[::-1]
    if(temp == N):
        print('yes')
    else:
        print('no')