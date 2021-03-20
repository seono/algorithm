import sys
input = sys.stdin.readline

N = int(input())
a,b,c,d = [0]*N,[0]*N,[0]*N,[0]*N
for i in range(N):
    a[i],b[i],c[i],d[i] = map(int, input().split())

ab = []
cd = {}
for i in range(N):
    for j in range(N):
        ab.append(a[i]+b[j])
        _cd = c[i]+d[j]
        cd[_cd] = cd.get(_cd,0)+1
ans = 0
for num in ab:
    ans+=cd.get(-num,0)
print(ans)