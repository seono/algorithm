import sys
input = sys.stdin.readline

e = [[0,0] for _ in range(10001)]
a = [0]*10001
b = [0]*10001
c = [0]*10001

def sol(st):
    global N,W
    for i in range(st,N):
        a[i+1]=min(b[i]+1,c[i]+1)
        if e[i][0] + e[i][1]<=W:
            a[i+1]=min(a[i+1],a[i]+1)
        if i>0 and e[i-1][0]+e[i][0]<=W and e[i-1][1]+e[i][1]<=W:
            a[i+1]=min(a[i+1],a[i-1]+2)
        if i<N-1:
            b[i+1] = a[i+1]+1
            if e[i][0]+e[i+1][0]<=W:
                b[i+1] = min(b[i+1],c[i]+1)
            c[i+1] = a[i+1]+1
            if e[i][1]+e[i+1][1]<=W:
                c[i+1] = min(c[i+1],b[i]+1)
T = int(input())
while T:
    T-=1
    N , W = map(int,input().split())
    for i,num in enumerate(list(map(int,input().split()))):
        e[i][0]=num
    for i,num in enumerate(list(map(int,input().split()))):
        e[i][1]=num
    a[0]=0
    b[0]=1
    c[0]=1
    sol(0)
    res = min(1e9,a[N])
    if N>1 and e[0][0]+e[N-1][0]<=W:
        a[1] = 1
        b[1] = 2
        c[1] = 1 if e[0][1]+e[1][1]<=W else 2
        sol(1)
        res = min(res,c[N-1]+1)
    if N>1 and e[0][1]+e[N-1][1]<=W:
        a[1] = 1
        b[1] = 1 if e[0][0]+e[1][0]<=W else 2
        c[1] = 2
        sol(1)
        res = min(res,b[N-1]+1)
    if N>1 and e[0][0]+e[N-1][0]<=W and e[0][1]+e[N-1][1]<=W:
        a[1] = 0
        b[1], c[1] = 1,1
        sol(1)
        res = min(res,a[N-1]+2)
    print(res)
    