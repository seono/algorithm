import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(input().strip().split())
arr2 = input().strip()

def getpi(p):
    m = len(p)
    j = 0
    pi = [0]*m
    for i in range(1,m):
        while j>0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i]==p[j]:
            j+=1
            pi[i]=j
    return pi

def gcd(n1,n2):
    if n1<n2:n1,n2=n2,n1
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1

pi = getpi(arr1)
if pi[-1]*2<N:
    print("{}/{}".format(1,N))
else:
    g = gcd(N,N//(N-pi[-1]))
    print("{}/{}".format(N//(N-pi[-1])//g,N//g))