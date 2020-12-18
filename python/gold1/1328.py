import sys
input = sys.stdin.readline


def sol():
    N, L, R = map(int, input().split())
    arr = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for n in range(1,N+1):
        arr[n][n][1]=1
        arr[n][1][n]=1
    for n in range(2,N+1):
        for l in range(1,L+1):
            for r in range(1,R+1):
                arr[n][l][r] = arr[n-1][l][r]*(n-2) + arr[n-1][l-1][r] + arr[n-1][l][r-1]
    print(arr[N][L][R] % 1000000007)
    return
sol() 
