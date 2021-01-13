import sys
input = sys.stdin.readline
T = int(input())

def update(idx):
    idx+=size//2
    while idx>0:
        tree[idx]+=1
        idx=idx//2

def sum(s,e,node,ns,ne):
    if(e<=ns or ne<=s):return 0
    if(s<=ns and ne<=e):return tree[node]
    mid = (ns+ne)//2
    return sum(s,e,node*2,ns,mid)+sum(s,e,node*2+1,mid,ne)

while T:
    T-=1
    n = int(input())
    size = 1<<18
    arr = [list(map(int,input().split())) for _ in range(n)]
    tree = [0]*size
    arr.sort(key = lambda x : (x[1]))
    r = 0
    newY = [0]*n
    for i in range(n):
        if i>0 and arr[i][1]!=arr[i-1][1]:r+=1
        newY[i]=r
    
    for i in range(n):
        arr[i][1]=newY[i]
    arr.sort(key = lambda x:(x[0],-x[1]))
    ans = 0

    for i in range(n):
        ans+=sum(arr[i][1],size//2,1,0,size//2)
        update(arr[i][1])
    
    print(ans)