import sys
input = sys.stdin.readline
def solution(sales, links):
    adj = [[] for _ in range(len(sales))]
    for a,b in links:
        adj[a-1].append(b-1)
    dp_arr = [[-1,-1] for _ in range(len(sales))]
    def dp(now,check):
        if len(adj[now])==0:
            return 0
        if dp_arr[now][check]!=-1:return dp_arr[now][check]
        #check True -> 팀원들 맘대로
        #check False -> 팀원이 다안가면 팀중에 최소매출인원 무조건 보냄
        res = 0
        if check:
            for nx in adj[now]:
                res+=min(dp(nx,False),dp(nx,True)+sales[nx])
        else:
            flag = False
            tmp = sales[now]
            for nx in adj[now]:
                m1 = dp(nx,False)
                m2 = dp(nx,True)+sales[nx]
                if m2<=m1:
                    flag=True
                    res+=m2
                else:
                    if m2-m1<tmp:
                        tmp = m2-m1
                    res+=m1
            if not flag:
                res+=tmp
        dp_arr[now][check]=res
        return res
    answer = dp(0,False)
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