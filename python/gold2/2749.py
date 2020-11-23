import sys
input = sys.stdin.readline

num = int(input())
idx = 1
arr = [0,1]
while True:
    idx+=1
    arr.append((arr[-1]+arr[-2])%1000000)
    if arr[-2]==0:
        if arr[-1]==1:
            break
print(arr[num%(idx-1)])
