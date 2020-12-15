import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

arr = [0]*400000

def get(s,e):
    ans = 0
    while s<=e:
        if s%2==1:ans+=arr[s]
        if e%2==0:ans+=arr[e]
        s=(s+1)//2
        e=(e-1)//2
    return ans

st = 1
while st<N:
    st=st*2
arr[st:st+N]=list(map(int,input().split()))

temp = st
while temp>1:
    ed = temp
    temp=temp//2
    for i in range(temp,ed):
        arr[i]=arr[i*2]+arr[i*2+1]

for _ in range(Q):
    x,y,a,b = map(int, input().split())
    if x>y:
        x,y = y,x
    print(get(st+x-1,st+y-1))
    temp = st+a-1
    c = b-arr[temp]
    arr[temp] = b
    while temp>1:
        temp=temp//2
        arr[temp]+=c