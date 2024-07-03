n = int(input())
arr = list(map(int,input().split()))
arr_set = set(arr)
goal = int(input())
 
count = 0
for i in arr:
    if i<goal :
        if goal-i in arr_set :
            count += 1
print(count//2)