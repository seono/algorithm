import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline



if __name__ == "__main__":
    N = int(input())
    con_time = []
    rule_dict = defaultdict(list)
    rule_list = [0 for i in range(N)]
    start_list = []
    result = 0
    for i in range(N):
        temp = list(map(int,input().split(' ')))[:-1]
        con_time.append(temp.pop(0))
        if len(temp)>0:
            for t in temp:
                rule_dict[t-1].append(i)
            rule_list[i] = len(temp)
        else:
            heapq.heappush(start_list,[con_time[i],i])
    while start_list:
        c, n = heapq.heappop(start_list)
        result = c
        con_time[n] = result
        if n in rule_dict:
            for t in rule_dict[n]:
                rule_list[t]-=1
                if rule_list[t]==0:
                    heapq.heappush(start_list,[con_time[t]+result,t])
    for c in con_time:
        print(c)