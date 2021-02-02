import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
num1,num2 = [0]*110,[0]*110
for i,num in enumerate(input().strip()):
    num1[i]=int(num)
for i,num in enumerate(input().strip()):
    num2[i]=int(num)
dp_arr = [[[[[1e9]*2 for l in range(10)] for k in range(10)] for j in range(10)] for i in range(110)]


def dp(now,x,y,z,w):
    if now>=N: return 0
    if dp_arr[now][x][y][z][w]!=1e9:
        return dp_arr[now][x][y][z][w]
    if x==num2[now]:
        dp_arr[now][x][y][z][w]=min(dp(now+1,y,z,num1[now+3],0),dp(now+1,y,z,num1[now+3],1))
        return dp_arr[now][x][y][z][w]
    tmp = 1 if w else -1
    for i in range(1,4):
        i = i*tmp
        dp_arr[now][x][y][z][w] = min(dp_arr[now][x][y][z][w],1+dp(now,(x+i)%10,y,z,w))
        dp_arr[now][x][y][z][w] = min(dp_arr[now][x][y][z][w],1+dp(now,(x+i)%10,(y+i)%10,z,w))
        dp_arr[now][x][y][z][w] = min(dp_arr[now][x][y][z][w],1+dp(now,(x+i)%10,(y+i)%10,(z+i)%10,w))
    return dp_arr[now][x][y][z][w]
print(min(dp(0,num1[0],num1[1],num1[2],0),dp(0,num1[0],num1[1],num1[2],1)))