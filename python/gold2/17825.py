import sys
input = sys.stdin.readline
cnt_list = list(map(int, input().split()))

horse = [[0,0],[0,0],[0,0],[0,0]]
points = [[0]*21 for _ in range(5)]
left_side = [10, 13, 16, 19]
right_side = [30, 28, 27, 26]
down_side = [20, 22, 24]
up_side = [25, 30, 35, 40]
straight_side = [0]+list(range(2,42,2))
load = [straight_side, left_side, down_side, right_side, up_side]

def go(side, idx, cnt):
    if side == 0:
        if idx+cnt==20:
            return 4,3
        if idx+cnt<len(straight_side):
            if idx+cnt in [5,10,15]:
                return (idx+cnt)//5, 0
            else:
                return side, idx+cnt
        else:
            return -2, 0
    if side < 4:
        if idx+cnt<len(load[side]):
            return side, idx+cnt
        else:
            idx-=len(load[side])
            side=4
    if idx+cnt<len(load[side]):
        return side, idx+cnt
    return -2, 0
    

result = 0
def dp(idx, score):
    if idx==10:
        global result
        result = max(score,result)
        return
    cnt = cnt_list[idx]
    for j in range(4):
        side, i = horse[j]
        if side==-2:
            continue
        new_side, new_i = go(side, i,cnt)
        if new_side==-2:
            horse[j] = [-2,0]
            points[side][i]=0
            dp(idx+1,score)
            points[side][i]=1
            horse[j] = [side, i]
        else:
            if points[new_side][new_i]:
                continue
            horse[j] = [new_side, new_i]
            points[new_side][new_i]=1
            points[side][i]=0
            dp(idx+1,score+load[new_side][new_i])
            horse[j] = [side, i]
            points[new_side][new_i]=0
            points[side][i]=1
    return

dp(0,0)
print(result)