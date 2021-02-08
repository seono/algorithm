import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
arr = [0]+list(map(int,input().split()))
cnt = [0]*1000001
N_SQRT = int(N**(1/2))
an = 0

q = [tuple(map(int,input().split()))+(idx,) for idx in range(int(input()))]
q.sort(key=lambda x:(x[0]//N_SQRT,x[1]))
ans = [0]*len(q)
l,r = 0,-1
for i,j,idx in q:
    if r==-1:
        for k in range(i,j+1):
            an+=not cnt[arr[k]]
            cnt[arr[k]]+=1
        l,r = i,j
        ans[idx]=an
        continue
    for k in range(i,l):
        an+=not cnt[arr[k]]
        cnt[arr[k]]+=1
    for k in range(r+1,j+1):
        an+=not cnt[arr[k]]
        cnt[arr[k]]+=1
    for k in range(l,i):
        cnt[arr[k]]-=1
        an-=not cnt[arr[k]]
    for k in range(j+1,r+1):
        cnt[arr[k]]-=1
        an-=not cnt[arr[k]]
    l,r=i,j
    ans[idx]=an
for i in range(len(q)):
    output("%d\n"%ans[i])