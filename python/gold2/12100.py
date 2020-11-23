import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
b = []
result = 0
for _ in range(N):
    b.append(list(map(int, input().split())))
def move_board(b, d):
    board = deepcopy(b)
    n = len(board)
    if d==0:
        #up
        for x in range(n):
            y = 0
            temp = []
            check = False
            while y<n:
                if board[y][x]>0:
                    if check and temp[-1]==board[y][x]:
                        temp[-1]*=2
                        check = False
                    else:
                        temp.append(board[y][x])
                        check=True
                y+=1
            for i in range(n):
                if i<len(temp):
                    board[i][x]=temp[i]
                else:
                    board[i][x]=0
    elif d==1:
        #down
        for x in range(n):
            y = n-1
            temp = []
            check = False
            while y>=0:
                if board[y][x]>0:
                    if check and temp[-1]==board[y][x]:
                        temp[-1]*=2
                        check = False
                    else:
                        temp.append(board[y][x])
                        check=True
                y-=1
            for i in range(n):
                if i<len(temp):
                    board[n-1-i][x]=temp[i]
                else:
                    board[n-1-i][x]=0
    elif d==2:
        #left
        for y in range(n):
            x = 0
            temp = []
            check = False
            while x<n:
                if board[y][x]>0:
                    if check and temp[-1]==board[y][x]:
                        temp[-1]*=2
                        check = False
                    else:
                        temp.append(board[y][x])
                        check=True
                x+=1
            for i in range(n):
                if i < len(temp):
                    board[y][i]=temp[i]
                else:
                    board[y][i]=0
    else:
        #right
        for y in range(n):
            x = n-1
            temp=[]
            check = False
            while x>=0:
                if board[y][x]>0:
                    if check and temp[-1]==board[y][x]:
                        temp[-1]*=2
                        check = False
                    else:
                        temp.append(board[y][x])
                        check=True
                x-=1
            for i in range(n):
                if i<len(temp):
                    board[y][n-1-i]=temp[i]
                else:
                    board[y][n-1-i]=0            
    return board

def sol(b, cnt):
    global result
    if cnt==0:
        m = max(map(max,b))
        if m>result:
            result=m
    else:
        for n in range(4):
            sol(move_board(b,n),cnt-1)

sol(b,5)
print(result)