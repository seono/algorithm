import sys
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

def get(a,b):
    ans_min = 1e9
    ans_max = 0
    while a<=b:
        if a%2==1:
            ans_min = min(ans_min,tree[a][0])
            ans_max = max(ans_max,tree[a][1])
        if b%2==0:
            ans_min = min(ans_min,tree[b][0])
            ans_max = max(ans_max,tree[b][1])
        a=(a+1)>>1
        b=(b-1)>>1
    return ans_min,ans_max

def update(idx,diff):
    tree[idx]=(diff,diff)
    while idx>1:
        idx>>=1
        tree[idx][0]=min(tree[idx<<1][0],tree[idx<<1|1][0])
        tree[idx][1]=max(tree[idx<<1][1],tree[idx<<1|1][1])

while T:
    T-=1
    N, K = map(int,input().split())
    st = 1
    while st<N:
        st*=2
    tree = [[0,0] for _ in range(st*2)]
    for i in range(st,st+N):
        tree[i]=[i-st+1,i-st+1]
    tmp = st
    while tmp>1:
        ed = tmp
        tmp = tmp>>1
        for i in range(tmp,ed):
            tree[i][0]=min(tree[i<<1][0],tree[i<<1|1][0])
            tree[i][1]=max(tree[1<<1][1],tree[i<<1|1][1])
    
    for i in range(K):
        q,a,b=map(int,input().split())
        if q:
            min_num,max_num = get(st+a,st+b)
            #print(min_num,max_num)
            if min_num==a+1 and max_num==b+1:
                output("YES\n")
            else:
                output("NO\n")
        else:
            tmp = tree[st+a][0]
            update(st+a,tree[st+b][0])
            update(st+b,tmp)