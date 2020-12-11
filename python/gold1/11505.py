import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

p = 1000000007

arr = [1]*4000000

st = 1

def get(s,e):
    ans = 1
    while s<=e:
        if s%2==1:ans=(ans*arr[s])%p
        if e%2==0:ans=(ans*arr[e])%p
        s = (s+1)//2
        e = (e-1)//2
    return ans

while st<N:
    st*=2

for i in range(N):
    arr[st+i]=int(input())

temp = st
while temp>1:
    ed = temp
    temp = temp//2
    for i in range(temp,ed):
        arr[i] = (arr[i*2]*arr[i*2+1])%p

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a==1:
        temp = st+b-1
        x = arr[temp]
        arr[temp]= c
        while temp>1:
            temp = temp//2
            arr[temp]=(arr[temp*2]*arr[temp*2+1])%p
            
    elif a==2:
        print(get(st+b-1,st+c-1))