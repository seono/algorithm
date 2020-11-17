import sys
import heapq
input = sys.stdin.readline

# 구간별로 val잡아서 우선순위 큐에 넣지만
# 논리상으로 모든 구간을 검사하고 최소 val을 가진 index를 집어넣어야했지만
# 앞구간부터 검사하는 방법으로 코딩되어있었다


class D(object):
    def __init__(self):
        self.start = 0
        self.end = 0
        self.isFinish = 0
        self.diff = 1e+10
        self.num = 0


def sol(num_list, N):
    v_rank = []
    for n in num_list:
        heapq.heappush(v_rank, [0, n])
    num_list.insert(0,0)
    x_list = []
    for i in range(len(num_list)-1):
        d = D()
        diff = num_list[i+1]-num_list[i]
        d.num = num_list[i]+1
        if diff==1:
            d.isFinish=1
        elif diff==2:
            heapq.heappush(v_rank, [0, num_list[i]+1])
            d.isFinish=1
        else:
            d.start = num_list[i]
            d.end = num_list[i+1]
            d.diff = diff
        x_list.append(d)
    x_list.sort(key = lambda x:x.diff)
    isChange = True
    while isChange and len(v_rank)<N:
        m_num = 1e+64
        temp_list = []
        isChange=False
        for i in range(len(num_list)-1):
            if x_list[i].isFinish == 1:
                continue
            val = (x_list[i].end - x_list[i].num)*(x_list[i].num-x_list[i].start)-1
            if val<m_num:
                temp_list = []
                temp_list.append([val, i])
                m_num = val
                isChange = True
            elif val==m_num:
                temp_list.append([val, i])
        if isChange:
            while temp_list:
                val, i = temp_list.pop()
                if x_list[i].end-x_list[i].num == (x_list[i].end - x_list[i].start)/2:
                    heapq.heappush(v_rank, [val, x_list[i].num])
                else:
                    heapq.heappush(v_rank, [val, x_list[i].num])
                    heapq.heappush(v_rank, [val, x_list[i].end-x_list[i].num+x_list[i].start])
                x_list[i].num+=1
                
                if x_list[i].num > (x_list[i].end + x_list[i].start)/2:
                    x_list[i].isFinish = 1
    if len(v_rank) < N:
        while v_rank:
            print(heapq.heappop(v_rank)[1], end=' ')
            N-=1
        n = num_list[-1]
        while N>0:
            N-=1
            n+=1
            print(n,end=' ')
    else:
        while N>0:
            print(heapq.heappop(v_rank)[1], end=' ')
            N-=1
    return
        

if __name__ == "__main__":
    L = int(input())
    if L>0:
        num_list = sorted(list(map(int, input().split(' '))))
        N = int(input())
        sol(num_list,N)
    else:
        N = int(input())
        sol([],N)
