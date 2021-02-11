from cmath import exp, pi
import sys
input = sys.stdin.readline

n = int(input())
N = 1
while N<2*n:N<<=1
a = list(map(int,input().split()))+[0]*(N-n)
b = list(map(int,input().split()))
b.reverse()
b = b+[0]*(N-2*n)+b
# def fft(a):
#     N = len(a)
#     if N == 1: return a
#     A_even = fft(a[0::2])
#     A_odd = fft(a[1::2])
#     w_N = [exp(2j*pi*n/N) for n in range(N//2)]
#     return [A_even[n] + w_N[n] * A_odd[n] for n in range(N//2)] + \
#         [A_even[n] - w_N[n] * A_odd[n] for n in range(N//2)]
    
def fft(x, inverse=False):
    N, e = 1,0
    while N < len(x):
        N<<=1
        e+=1
    for i in range(N):
        tmp = i
        j = 0
        for _ in range(e):
            j=j<<1 | tmp&1
            tmp>>=1
        if i<j:x[i],x[j]=x[j],x[i]
    n=2
    while n<=N:
        unit  = exp(2j*pi/n * (1 if inverse else -1))
        for i in range(0,N,n):
            W = 1
            for k in range(i, i+n//2):
                tmp = x[k+n//2]*W
                x[k+n//2]=x[k]-tmp
                x[k]+=tmp
                W*=unit
        n<<=1
    if inverse:
        for i in range(N):x[i]/=N

fft(a)
fft(b)
s = [i*j for i, j in zip(a,b)]
fft(s,True)
print(max(int(round(x.real)) for x in s))