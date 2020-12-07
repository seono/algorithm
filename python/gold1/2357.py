import sys
input= sys.stdin.readline

N, M = map(int,input().split())
INF = 1e11
arr_min = [INF]*400000
arr_max = [0]*400000
num_list = []
st = 1
while st<N:
    st*=2

def get(s,e):
    num_min,num_max=INF,0
    while s<=e:
        if s%2==1:
            num_min=min(arr_min[s],num_min)
            num_max=max(arr_max[s],num_max)
        if e%2==0:
            num_min=min(arr_min[e],num_min)
            num_max=max(arr_max[e],num_max)
        s = (s+1)//2
        e = (e-1)//2
    return num_min, num_max

for i in range(N):
    n=int(input())
    arr_min[st+i]=n
    arr_max[st+i]=n
temp = st
while temp>1:
    ed = temp
    temp = temp//2
    for i in range(temp,ed):
        arr_min[i] = min(arr_min[i*2],arr_min[i*2+1])
        arr_max[i] = max(arr_max[i*2],arr_max[i*2+1])
for _ in range(M):
    i,j = map(int,input().split())
    print(' '.join(map(str,get(st+i-1,st+j-1))))