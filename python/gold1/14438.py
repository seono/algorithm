import sys
input = sys.stdin.readline

N = int(input())
t = [sys.maxsize]*400000
st = 1
while st<N:
    st*=2

t[st:st+N] = list(map(int,input().split()))
temp = st
while temp>1:
    ed = temp
    temp = temp//2
    for i in range(temp,ed):
        t[i]=min(t[i*2:i*2+2])
M = int(input())
def get(a,b):
    ans = sys.maxsize
    while a<=b:
        if a%2==1: ans=min(ans,t[a])
        if b%2==0: ans=min(ans,t[b])
        a = (a+1)//2
        b = (b-1)//2
    return ans



for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        temp = st+b-1
        t[temp]=c
        while temp>1:
            temp=temp//2
            t[temp]=min(t[temp*2:temp*2+2])
    else:
        print(get(st+b-1,st+c-1))