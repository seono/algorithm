import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[0],-x[1]))
result = 1
x,y = arr[0]
tx,ty = x,y
idx = 0
while arr[idx][0]==x:
    idx+=1
ex = arr[-1][0]
h = -1e9
tidx = idx
while x<ex:
    while idx<N:
        nx,ny = arr[idx]
        if nx!=x:
            if (ny-y)/(nx-x)>=h:
                h = (ny-y)/(nx-x)
                tidx = idx
                tx,ty = nx,ny
        idx+=1
    x,y = tx,ty
    result+=1
    idx = tidx
    h = -1e9
idx = N-1
while arr[idx][0]==x:
    idx-=1
if idx==N-2:
    result-=1
x,y = arr[-1]
result+=1
ex = arr[0][0]
tidx = idx
h = -1e9
while x>ex:
    while idx>=0:
        nx,ny = arr[idx]
        if nx!=x:
            if (ny-y)/(nx-x)>=h:
                h = (ny-y)/(nx-x)
                tidx = idx
                tx,ty = nx,ny
        idx-=1
    x,y = tx,ty
    idx = tidx
    result+=1
    h = -1e9
if [x,y]==arr[0]:
    result-=1
print(result)