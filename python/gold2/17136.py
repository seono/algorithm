import sys
import copy
input = sys.stdin.readline

paper = []
result = 100
total = 0
chosen=[0,5,5,5,5,5]
d = 10
for _ in range(10):
    temp = list(map(int, input().split()))
    total += sum(temp)
    paper.append(temp)

def check_paper(i,j,k):
    if i+k>10 or j+k>10:
        return False
    for y in range(i,i+k):
        for x in range(j,j+k):
            if paper[y][x]==0:
                return False

    return True

def sol(depth):
    global total, result, d
    if result>0 and depth>=result:
        return
    if total==0:
        result = min(result, depth)
        return
    for y in range(d):
        for x in range(d):
            if paper[y][x]:
                break
        if paper[y][x]:
            break
    if paper[y][x]:
        recover_list = []
        for i in range(1,6):
            if chosen[i]>0:
                if check_paper(y,x,i):
                    for y1 in range(i):
                        for x1 in range(i):
                            paper[y+y1][x+x1]=0
                            recover_list.append((y+y1,x+x1))
                    chosen[i]-=1
                    total-=i*i
                    sol(depth+1)
                    total+=i*i
                    chosen[i]+=1
                    for y2,x2 in recover_list:
                        paper[y2][x2]=1
sol(0)
if result == 100:
    print(-1)
else:
    print(result)