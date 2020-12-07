import sys
input = sys.stdin.readline
prime_num = []

st, ed = map(int,input().split())
visit = [1]*(1000001)
num = 2
while num*num<=ed:
    n = num*num
    if st%n==0:
        s = st
    else:
        s = (st//n+1)*n
    for i in range(s,ed+1,n):
        visit[i-st]=0
    num+=1
print(sum(visit[0:ed-st+1]))