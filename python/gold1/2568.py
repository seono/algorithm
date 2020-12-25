import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
temp = [0]*(n+1)
arr.sort()

ans = [arr[0][1]]

for idx,ab in enumerate(arr[1:],1):
    a,b=ab
    if b>ans[-1]:
        ans.append(b)
        temp[idx]=len(ans)-1
    else:
        i = bisect.bisect_left(ans,b)
        temp[idx]=i
        ans[i]=b
print(n-len(ans))
x = []
p = len(ans)-1
while n>0:
    n-=1
    if temp[n]==p:
        p-=1
    else:
        x.append(arr[n][0])
print('\n'.join(map(str,sorted(x))))