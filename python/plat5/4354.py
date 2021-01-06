import sys
input = sys.stdin.readline

def getpi(p):
    m = len(p)
    pi = [0]*m
    j = 0
    for i in range(1,m):
        while j>0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i]==p[j]:
            j+=1
            pi[i]=j
    return pi

while True:
    st = input().strip()
    if len(st)==1 and st[0]=='.':
        break
    pi = getpi(st)
    if pi[-1]==0 or pi[-1] % (len(st)- pi[-1]):
        print(1)
    else:
        print(len(st)//(len(st)-pi[-1]))