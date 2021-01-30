import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
output = sys.stdout.write
N, L = map(int,input().split())
p = [num for num in range(L+1)]

def find(idx):
    if p[idx]!=idx:
        p[idx]=find(p[idx])
    return p[idx]

def Union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        p[x]=y

for i in range(N):
    a,b = map(int,input().split())
    f_a,f_b = find(a),find(b)
    if f_a:
        if f_a!=f_b:
            p[f_a]=f_b
        else:
            p[f_a]=0
        output("LADICA\n")
    elif f_b:
        p[f_b]=0
        output("LADICA\n")
    else:
        output("SMECE\n")
