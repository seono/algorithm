import sys
input = sys.stdin.readline

T = int(input())

dy,dx = [-1,-1,0],[-1,1,-1]
def check(y,x):
    global N, M
    if arr[y][x]=='x':
        return False
    for i in range(3):
        ny,nx = y+dy[i],x+dx[i]
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx]=='0':
                return False
    return True

def dp(bit,idx):
    global N, M, limit_bit,ed
    if idx == ed:return 0
    if dp_arr[idx][bit]!=-1:
        return dp_arr[idx][bit]
    y = idx//M
    x = idx%M
    res = 0
    if check(y,x):
        arr[y][x]='0'
        d1 = dp(((bit<<1)|1)&limit_bit,idx+1)+1
        arr[y][x]='.'
        d2 = dp((bit<<1)&limit_bit,idx+1)
        res = max(d1,d2)
    else:
        res = dp((bit<<1)&limit_bit,idx+1)
    dp_arr[idx][bit]=res
    return res

while T:
    T-=1
    N, M = map(int,input().split())
    ed = N*M
    #최근 M+1개 비트
    #현재 idx(Y*M+X)
    #dp
    dp_arr = [[-1]*(1<<M+1) for _ in range(N*M+1)]
    limit_bit = (1<<(M+1))-1
    arr = [list(input().strip()) for _ in range(N)]
    print(dp(0,0))