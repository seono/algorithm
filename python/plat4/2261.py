import sys
input = sys.stdin.readline

N = int(input())
def dist(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1]) ** 2


def sol(left, right):
    if right-left==2:return dist(arr[left],arr[left+1])
    elif right-left==3:
        return min(dist(arr[left],arr[left+1]),dist(arr[left+1],arr[left+2]),dist(arr[left],arr[left+2]))
    
    mid = (right+left)//2
    d = min(sol(left,mid),sol(mid,right))
    tmp = []
    mid = arr[mid][0]
    for i in range(left,right):
        xdist = arr[i][0]-mid
        xdist*=xdist
        if xdist>d:continue
        tmp.append(arr[i])
    tmp.sort(key=lambda x:x[1])
    tmp_len = len(tmp)
    if tmp_len>1:
        for i in range(tmp_len-1):
            for j in range(i+1,tmp_len):
                if (tmp[i][1] - tmp[j][1]) **2 > d:
                    break
                d = min(d, dist(tmp[i],tmp[j]))
    return d

arr = [list(map(int,input().split())) for _ in range(N)]
arr = list(set(map(tuple,arr)))
if len(arr)!=N:
    print(0)
else:
    arr.sort()
    print(sol(0,len(arr)))