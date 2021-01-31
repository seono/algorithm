import sys
from collections import defaultdict
input = sys.stdin.readline
output = sys.stdout.write
s = sys.stdin.readline().strip()

n = len(s)
suffix = [i for i in range(n)]
g = [0] * (n + 1) #순위
ng = [0] * (n + 1) #새로운 순위(순위를 갱신할 때 이용할 배열)

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
ng[suffix[0]] = 0
ng[n] = -1
t = 1

while t < n:
    suffix.sort(key=lambda x:(g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = suffix[i - 1], suffix[i]
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]
            
    if ng[n - 1] == n - 1:
        break
        
    t = t * 2
    g = ng[:]
tmp = [0]*n
lcp = [0]*n
for i in range(n):
    tmp[suffix[i]]=i
l = 0
total_len = len(s)
for i in range(n):
    if tmp[i]:
        j=suffix[tmp[i]-1]
        while i+l<total_len and j+l<total_len and s[j+l]==s[i+l]:l+=1
        lcp[tmp[i]]=l
        if l:l-=1
for i in range(n):
    suffix[i]+=1
print(' '.join(map(str,suffix)))
print('x '+' '.join(map(str,lcp[1:])))