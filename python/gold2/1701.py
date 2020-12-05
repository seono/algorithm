import sys
input = sys.stdin.readline

st = input()[:-1]
def sol():
    def getpi(s):
        j=0
        pi = [0 for _ in range(len(s))]
        for i in range(1,len(s)):
            while j>0 and s[i] != s[j]:
                j = pi[j-1]
            if s[i]==s[j]:
                j+=1
                pi[i]=j
        return pi
    r = 0
    for i in range(len(st)):
        r = max(r,max(getpi(st[i:])))
    return r

print(sol())