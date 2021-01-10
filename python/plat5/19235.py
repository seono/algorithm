import sys
input = sys.stdin.readline

arr = [[0]*10 for _ in range(10)]

N = int(input())
point = 0
# move1 -> check -> done? yes-> move2 -> check -> done? -> move2 ....
#                         no-> check2 -> done? -> move2 -
#red to blue and green
def move1(x,y,mode):
    if mode==1:
        nx,ny=x,4
        while ny<10 and not arr[nx][ny]:
            ny+=1
        arr[nx][ny-1]=arr[x][y]
        nx,ny=4,y
        while nx<10 and not arr[nx][ny]:
            nx+=1
        arr[nx-1][ny]=arr[x][y]
        arr[x][y]=0
    #가로
    elif mode==2:
        nx,ny=x,4
        while ny<10 and not arr[nx][ny]:
            ny+=1
        arr[nx][ny-2]=arr[nx][ny-1]=arr[x][y]
        nx,ny=4,y
        while nx<10 and arr[nx][ny]==0 and arr[nx][ny+1]==0:
            nx+=1
        arr[nx-1][ny]=arr[nx-1][ny+1]=arr[x][y]
        arr[x][y],arr[x][y+1]=0,0
    else:
        nx,ny=x,4
        while ny<10 and arr[nx][ny]==0 and arr[nx+1][ny]==0:
            ny+=1
        arr[nx][ny-1]=arr[nx+1][ny-1]=arr[x][y]
        nx,ny=4,y
        while nx < 10 and not arr[nx][ny]:
            nx+=1
        arr[nx-2][ny]=arr[nx-1][ny]=arr[x][y]
        arr[x][y],arr[x+1][y]=0,0
# check special zone
def check2():
    ch = [0,0]
    for x in range(4,6):
        for y in range(4):
            if arr[x][y]:
                ch[x%2]=1
                break
    ch = sum(ch)
    if ch:
        for x in range(9,3,-1):
            for y in range(4):
                arr[x][y] = arr[x-ch][y]
    ch = [0,0]
    for y in range(4,6):
        for x in range(4):
            if arr[x][y]:
                ch[y%2]=1
                break
    ch = sum(ch)
    if ch:
        for y in range(9,3,-1):
            for x in range(4):
                arr[x][y] = arr[x][y-ch]

# check point
def check():
    global point
    check_done = False
    x = 6
    while x<10:
        if arr[x][0] and arr[x][1] and arr[x][2] and arr[x][3]:
            for i in range(4):
                arr[x][i] = 0
            point+=1
            check_done=True
        x+=1
    y = 6
    while y<10:
        if arr[0][y] and arr[1][y] and arr[2][y] and arr[3][y]:
            for i in range(4):
                arr[i][y] = 0
            check_done = True
            point+=1
        y+=1
    return check_done

def move2():
    for y in range(8,3,-1):
        for x in range(4):
            if arr[x][y]:
                if x<3 and arr[x][y]==arr[x+1][y]:
                    ny=y+1
                    while ny<10 and arr[x][ny]==0 and arr[x+1][ny]==0:
                        ny+=1
                    if ny-1!=y:
                        arr[x][ny-1]=arr[x+1][ny-1]=arr[x][y]
                        arr[x][y]=arr[x+1][y]=0
                elif x>0 and arr[x][y]==arr[x-1][y]:
                    ny=y+1
                    while ny<10 and arr[x][ny]==0 and arr[x-1][ny]==0:
                        ny+=1
                    if ny-1!=y:
                        arr[x][ny-1]=arr[x-1][ny-1]=arr[x][y]
                        arr[x][y]=arr[x-1][y]=0
                else:
                    ny=y+1
                    while ny<10 and arr[x][ny]==0:
                        ny+=1
                    if ny-1!=y:
                        arr[x][ny-1]=arr[x][y]
                        arr[x][y]=0
    
    for x in range(8,3,-1):
        for y in range(4):
            if arr[x][y]:
                if y<3 and arr[x][y]==arr[x][y+1]:
                    nx = x+1
                    while nx<10 and arr[nx][y]==0 and arr[nx][y+1]==0:
                        nx+=1
                    if nx-1!=x:
                        arr[nx-1][y]=arr[nx-1][y+1]=arr[x][y]
                        arr[x][y]=arr[x][y+1]=0
                elif y>0 and arr[x][y]==arr[x][y-1]:
                    nx = x+1
                    while nx<10 and arr[nx][y]==0 and arr[nx][y-1]==0:
                        nx+=1
                    if nx-1!=x:
                        arr[nx-1][y]=arr[nx][y-1]=arr[x][y]
                        arr[x][y]=arr[x][y-1]=0
                else:
                    nx=x+1
                    while nx<10 and arr[nx][y]==0:
                        nx+=1
                    if nx-1!=x:
                        arr[nx-1][y]=arr[x][y]
                        arr[x][y]=0
    

def checkLast():
    ans = 0
    for x in range(4):
        for y in range(6,10):
            if arr[x][y]:ans+=1
            if arr[y][x]:ans+=1
    return ans
def printBoard():
    for y in range(10):
        print(' '.join(map(str,arr[y])))
    print()
for i in range(1,N+1):
    t,x,y = map(int,input().split())
    if t==1:
        arr[x][y]=i
    elif t==2:
        arr[x][y]=i
        arr[x][y+1]=i
    else:
        arr[x+1][y]=i
        arr[x][y]=i
    #printBoard()
    move1(x,y,t)
    #printBoard()
    while check():
        #printBoard()
        move2()
        #printBoard()
    check2()
    #printBoard()
print(point)
print(checkLast())