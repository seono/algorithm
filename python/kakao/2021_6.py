import sys
input = sys.stdin.readline
import heapq
d = [(0,-1),(0,1),(-1,0),(1,0)]
INF = 1e9
dp_arr = [[[-1]*(1<<7) for _ in range(4)] for _ in range(4)]
    
def solution(board, r, c):
    board_dict = {}
    
    def dfs(y,x,y1,x1,n):
        st = [(0,y,x)]
        visited = [[False]*4 for _ in range(4)]
        visited[y][x]=True
        while st:
            cnt,y,x = heapq.heappop(st)
            if y==y1 and x==x1:
                return cnt
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                if 0<=ny<4 and 0<=nx<4:
                    if not visited[ny][nx]:
                        visited[ny][nx]=True
                        heapq.heappush(st,(cnt+1,ny,nx))
                    if board[ny][nx] and (1<<board[ny][nx])&n:continue
                else:continue
                ny,nx = ny+dy,nx+dx
                if 0<=ny<4 and 0<=nx<4:
                    if board[ny][nx] and (1<<board[ny][nx])&n:
                        if not visited[ny][nx]:
                            visited[ny][nx]=True
                            heapq.heappush(st,(cnt+1,ny,nx))
                    else:
                        ny,nx=ny+dy,nx+dx
                        if 0<=ny<4 and 0<=nx<4:
                            if not visited[ny][nx]:
                                visited[ny][nx]=True
                                heapq.heappush(st,(cnt+1,ny,nx))
                        else:
                            heapq.heappush(st,(cnt+1,ny-dy,nx-dx))
    answer = 0
    def dp(y,x,n):
        if n==0:
            return 0
        if dp_arr[y][x][n]!=-1:
            return dp_arr[y][x][n]
        res = INF
        for k,v in board_dict.items():
            if (1<<k) & n:
                y1,x1,y2,x2=v
                res = min(res,dp(y1,x1,n^(1<<k))+dfs(y,x,y2,x2,n)+dfs(y2,x2,y1,x1,n),dp(y2,x2,n^(1<<k))+dfs(y,x,y1,x1,n)+dfs(y1,x1,y2,x2,n))
        dp_arr[y][x][n]=res
        return res
    n=0
    for y,b in enumerate(board):
        for x,num in enumerate(b):
            if num:
                n=n|(1<<num)
                if num in board_dict:
                    board_dict[num].extend([y,x])
                else:
                    board_dict[num]=[y,x]
    answer = dp(r,c,n)
    answer += len(board_dict)*2
    return answer

r,c=map(int,input().split())

board = []
tmp = []
for idx,row in enumerate(list(map(str,input().split(',')))):
    row = row.replace("[","").replace("[","")
    row = row.replace("]","").replace("]","")
    if idx>1 and idx%4==0:
        board.append(tmp)
        tmp = [int(row)]
    else:
        tmp.append(int(row))
board.append(tmp)
print(solution(board,r,c))