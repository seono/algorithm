import sys
input = sys.stdin.readline
R, C = map(int,input().split())
arr = []
arr = [list(input().strip()) for _ in range(R)]
for y in range(R):
    for x in range(C):
        arr[y][x]=int(arr[y][x])
visited = [[False]*C for _ in range(R)]
ans = 0

def checkdia2(y,x,size):
    while size>0:
        y+=1
        size-=1
        if arr[y][x-size] & arr[y][x+size]:continue
        return False
    return True

def checkdia(y,x):
    size = 1
    global ans
    if ans==0:ans=1
    max_size = min(C-x,x+1,(R-y+1)//2)
    if max_size<ans:return
    while size<max_size:
        y+=1
        if arr[y][x-size] & arr[y][x+size]:
            if size>=ans:
                if checkdia2(y,x,size):
                    ans = size+1
            size+=1
        else:
            break

for y in range(R):
    for x in range(C):
        if arr[y][x]:
            checkdia(y,x)
print(ans)