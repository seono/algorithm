import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
h_arr = [[[] for _ in range(N)] for _ in range(N)]
horse = []
dx, dy = [1,-1,0,0],[0,0,-1,1]

for idx in range(K):
    y,x,m = map(int,input().split())
    h_arr[y-1][x-1].append(idx)
    horse.append([y-1,x-1,m-1])

def sol():
    turn = 0
    while turn<=1000:
        i=0
        while i<K:
            y,x,move = horse[i]
            ty,tx = y+dy[move], x+dx[move]
            if ty<0 or ty>=N or tx<0 or tx>=N or arr[ty][tx]==2:
                move=move+1 if move%2==0 else move-1
                horse[i][2]=move
                ty,tx = y+dy[move],x+dx[move]
                if ty<0 or ty>=N or tx<0 or tx>=N or arr[ty][tx]==2:
                    i+=1
                    continue 
            idx = h_arr[y][x].index(i)
            horses = h_arr[y][x][idx:]
            horse[i][2]=move
            for h in horses:
                horse[h][0],horse[h][1]=ty,tx
            h_arr[y][x] = h_arr[y][x][:idx]
            if arr[ty][tx]:
                h_arr[ty][tx].extend(horses[::-1])
            else:
                h_arr[ty][tx].extend(horses)
            if len(h_arr[ty][tx])>3:
                return turn+1
            i+=1
        turn+=1
    return -1

print(sol())

