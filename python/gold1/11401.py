import sys
input = sys.stdin.readline

N,K = map(int,input().split())
def sol(n,k):
    p = 1000000007
    global N
    def power(x,y):
        ans = 1
        while y>0:
            if y%2:
                ans*=x
                ans%=p
            x*=x
            x%=p
            y=y//2
        return ans
    F = [0]*(N+1)
    F[1]=1
    for i in range(2,N+1):
        F[i]=(F[i-1]*i)%p
    inv = [0]*(N+1)
    inv[N] = power(F[N],p-2)
    for i in range(N-1,0,-1):
        inv[i] = (inv[i+1]*(i+1))%p
    if n==k or k==0:
        return 1
    r = (F[n]*inv[n-k])%p
    r = (r*inv[k])%p
    return r
print(sol(N,K))