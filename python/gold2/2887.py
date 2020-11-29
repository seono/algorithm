import sys
input = sys.stdin.readline

def Find(x):
    if p[x]==x:
        return x
    else:
        y=Find(p[x])
        p[x]=y
        return y

def Union(x,y):
    x=Find(x)
    y=Find(y)
    if x!=y:
        p[y]=x

n = int(input())
l = []
p = [i for i in range(n)]
for i in range(n):
    x,y,z = map(int,input().split())
    l.append([x,y,z,i])

edge = []

for i in range(3):
    l.sort(key = lambda x: x[i])
    before = l[0][3]
    for j in range(1,n):
        now = l[j][3]
        edge.append([l[j][i]-l[j-1][i],before,now])
        before = now

edge.sort(key=lambda x: x[0])

cnt = 0
result = 0
for dis, st, ed in edge:
    if Find(st)!=Find(ed):
        result+=dis
        cnt+=1
        Union(st,ed)
    if cnt==n-1:
        break
print(result)
