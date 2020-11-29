import sys
import bisect
input = sys.stdin.readline

N = int(input())
a,b,c,d = [0 for _ in range(N)],[0 for _ in range(N)],[0 for _ in range(N)],[0 for _ in range(N)]
for i in range(N):
    a[i],b[i],c[i],d[i] = map(int, input().split())
result = 0
ab = []
cd = []
for i in a:
    for j in b:
        ab.append(i+j)
for i in c:
    for j in d:
        cd.append(i+j)
ab.sort()
cd.sort()
p = ab[0]
r = N*N
for ab_ in ab:
    l,r = bisect.bisect_left(cd,-ab_), bisect.bisect_right(cd,-ab_)
    result+=r-l
print(result)