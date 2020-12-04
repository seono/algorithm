import sys

input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int,input().split()))
C = 3000001
arr = [0]*C*2
arr1 = [0]*C*2

result = 0
def left(idx, sum, check):
    if idx==N//2:
        if check:
            arr[sum+C]+=1
        else:
            arr1[sum+C]+=1
        return
    left(idx+1,sum,check)
    left(idx+1,sum+num_list[idx],1)

def right(idx,sum,check):
    if idx<N//2:
        global S,result
        result+=arr[S+C-sum]
        if check:
            result+=arr1[S+C-sum]
        return
    right(idx-1,sum,check)
    right(idx-1,sum+num_list[idx],1)
left(0,0,0)
right(N-1,0,0)
print(result)