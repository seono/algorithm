import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split(' ')))

def getDownArrToRight(idx):
    p = [arr[idx]]
    for num in arr[idx+1:]:
        if num < p[-1]:
            p.append(num)
        else:
            l = len(p)-1
            while l>-1 and num>=p[l]:
                l-=1
            p[l+1]=num
    return len(p)

def getDownArrToLeft(idx):
    p = [arr[idx]]
    for num in reversed(arr[:idx]):
        if num < p[-1]:
            p.append(num)
        else:
            l = len(p)-1
            while l>-1 and num>=p[l]:
                l-=1
            p[l+1]=num
    return len(p)
def sol(num): return getDownArrToLeft(num)+getDownArrToRight(num)-1
ans = 0
for i in range(N):
    if sol(i)>ans:
        ans=sol(i)
print(ans)