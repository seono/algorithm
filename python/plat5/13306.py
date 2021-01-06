import sys
input = sys.stdin.readline
output = sys.stdout.write
N, Q = map(int,input().split())
p = [i for i in range(0,N+1)]
nodes = [0,1]+[int(input()) for _ in range(2,N+1)]
ans = []
row_list = [list(map(int,input().split())) for _ in range(N+Q-1)]
def find(x):
    t = x
    temp = []
    while p[t]!=t:
        temp.append(t)
        t=p[t]
    for tx in temp:
        p[tx]=t
    return t

def Union(x):
    p[x]=nodes[x]
    find(x)

for row in row_list[::-1]:
    if len(row)==3:
        a, b = row[1],row[2]
        ans.append(True if find(a)==find(b) else False)
    else:
        Union(row[1])
for i in ans[::-1]:
    if i:output("YES\n")
    else:output("NO\n")