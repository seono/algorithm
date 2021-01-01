import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
W = int(input())
arr = [[1,1],[N,N]]
for _ in range(W):
    arr.append(list(map(int,input().split())))
dp_arr = [[0]*(W+3) for _ in range(W+3)]
def dp(idx1,idx2):
    if idx1==W+1:
        return 0
    if dp_arr[idx1][idx2]:
        return dp_arr[idx1][idx2]
    x,y = arr[idx1+1]
    x1,y1 = arr[idx1]
    x2,y2 = arr[idx2]
    result = min(dp(idx1+1,idx2)+abs(x-x1)+abs(y-y1), dp(idx1+1,idx1)+abs(x-x2)+abs(y-y2))
    dp_arr[idx1][idx2] = result
    return result
def backtracking(idx1,idx2, one, two):
    if idx1==W+1:
        return
    x,y = arr[idx1+1]
    x1,y1 = arr[idx1]
    x2,y2 = arr[idx2]
    a1 = dp_arr[idx1+1][idx2]+abs(x-x1)+abs(y-y1)
    a2 = dp_arr[idx1+1][idx1]+abs(x-x2)+abs(y-y2)
    if a1<a2:
        output("%d\n"%one)
        backtracking(idx1+1,idx2,one,two)
    else:
        output("%d\n"%two)
        backtracking(idx1+1,idx1,two,one)
sys.setrecursionlimit(10000)
output("%d\n"%dp(1,0))
backtracking(1,0,2,1)