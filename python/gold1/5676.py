import sys
input = sys.stdin.readline


def get2(a,b):
    b_ans = get(b)
    a_ans = get(a-1)
    for i in range(2):
        b_ans[i]-=a_ans[i]
    if b_ans[1]>0:
        return 0
    else:
        if b_ans[0]%2==0:
            return 1
        return -1

def get(a):
    ans = [0,0]
    while a>0:
        for i in range(2):
            ans[i]+=tree[a][i]
        a = a & (a-1)
    return ans

def update(a,b):
    global N
    while a<N+1:
        for i in range(2):
            tree[a][i]+=b[i]
        a += (a & -a)

for line in sys.stdin:
    N, K = map(int,line.strip().split())
    tree = [[0,0] for _ in range(N+1)]
    arr = [0]+list(map(int,input().strip().split()))
    idx = 1
    while idx<N+1:
        t = arr[idx]
        if t==0:
            update(idx,[0,1])
        elif t<0:
            update(idx,[1,0])
        idx+=1
    ans = ""
    for _ in range(K):
        cmd, a, b = input().split()
        a = int(a);b=int(b)
        if cmd=='C':
            if b>0:
                c=[0,0]
            elif b<0:
                c=[1,0]
            else:
                c=[0,1]
            if arr[a]==0:
                c[1]-=1
            elif arr[a]<0:
                c[0]-=1
            arr[a]=b
            update(a,c)
        else:
            t = get2(a,b)
            if t>0:
                ans+='+'
            elif t<0:
                ans+='-'
            else:
                ans+='0'
    print(ans)