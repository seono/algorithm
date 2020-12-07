import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0]* 4000001
st = 1
while st<N:
    st*=2
j=0
for _ in range(N):
    n = int(input())
    arr[st+j]=n
    j+=1
temp = st
def get(s,e):
    ans = 0
    while s<=e:
        if s%2==1: ans+=arr[s]
        if e%2==0: ans+=arr[e]
        s = (s+1)//2
        e = (e-1)//2
    return ans
while st>1:
    ed = st
    st = st//2
    for i in range(st,ed):
        arr[i]=arr[i*2]+arr[i*2+1]
for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a==1:
        v = arr[temp+b-1] - c
        arr[temp+b-1]-=v
        st = temp+b-1
        while st>1:
            st = st//2
            arr[st]-=v
    else:
        print(get(temp+b-1,temp+c-1))