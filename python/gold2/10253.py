import sys
input = sys.stdin.readline

T = int(input())
def gcd(n1,n2):
    while n2!=0:
        if n1<n2:
            n1,n2=n2,n1
        t = n1 % n2
        n1,n2=n2,t
    return n1
while T>0:
    T-=1
    a,b = map(int, input().split())
    while a!=1:
        n = b//a + 1
        a = a*n-b
        b = n*b
        t = gcd(a,b)
        a //=t
        b //=t
    print(b)