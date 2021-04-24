import sys
sys.stdin = open("input.txt", "r")

def getTime(stair,t):
    # sorted stair
    inStair = []
    idx = 0
    ret = 0
    while idx<len(stair):
        nowP = stair[idx]
        if len(inStair)<3:
            inStair.append(nowP+t)
            ret = nowP+t
        else:
            if inStair[0]<=nowP:
                inStair.pop(0)
                inStair.append(nowP+t)
                ret = nowP+t
            else:
                tmp = inStair.pop(0)
                inStair.append(tmp+t)
                ret = tmp+t
        idx+=1
    return ret

def distanse(py,px,num):
    y,x = stairs[num]
    return abs(py-y)+abs(px-x)

def check():
    global bit,L
    ch = [[],[]]
    for idx in range(L):
        py,px = p[idx]
        c = (bit>>idx)&1
        dis = distanse(py,px,c)
        ch[c].append(dis+1)    
    return max(getTime(sorted(ch[0]),time[0]),getTime(sorted(ch[1]),time[1]))

def sol(idx):
    global L, bit
    if idx==L:
        return check()
    ret = 1e10
    temp = bit
    ret = min(sol(idx+1),ret)
    bit |= 1<<idx
    ret = min(sol(idx+1),ret)
    bit = temp
    return ret

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    p = []
    stairs = []
    time = []
    arr = [list(map(int,input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                if arr[y][x]>1:
                    stairs.append((y,x))
                    time.append(arr[y][x])
                else:
                    p.append((y,x))
    L = len(p)
    bit = 0
    print("#"+str(test_case),sol(0))