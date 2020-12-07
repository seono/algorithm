import sys
input = sys.stdin.readline


def getpi(s):
    m = len(s)
    pi = [0]*m
    j = 0
    for i in range(1,m):
        while j>0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i]==s[j]:
            j+=1
            pi[i]=j
    return pi

def kmp(s,p):
    ans = []
    pi = getpi(p)
    n,m,j = len(s),len(p),0
    for i in range(0,n):
        while j>0 and s[i]!=p[j]:
            j=pi[j-1]
        if s[i]==p[j]:
            if j==m-1:
                ans.append(i-m+2)
                j=pi[j]
            else:
                j+=1
    return ans

a = input()[:-1]
b = input()[:-1]
result = kmp(a,b)
print(len(result))
print(' '.join(map(str,result)))