import sys
input = sys.stdin.readline


def gcd(n1,n2):
    while n2!=0:
        if n1<n2:
            n1,n2=n2,n1
        n1,n2=n2,n1%n2
    return n1

def extension_gcd(n1,n2):
    tmp = n1
    t,t1,t2=0,0,1
    while n2!=0:
        q = n1//n2
        r = n1%n2
        t = t1 - q*t2
        n1 = n2
        n2 = r
        t1 = t2
        t2 = t
    while t1<0:t1+=tmp
    return t1

T = int(input())
while T:
    T-=1
    a,b=map(int,input().split())
    if b==1:
        if a+1>1e9:print("IMPOSSIBLE")
        else:print(a+1)
    elif a==1:
        print(1)
    elif gcd(a,b)!=1:print("IMPOSSIBLE")
    else:
        ans = extension_gcd(a,b)
        if ans>1e9:print("IMPOSSIBLE")
        else:print(ans)