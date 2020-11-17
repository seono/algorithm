import sys
from collections import defaultdict
import heapq

def solution(construct, rule_dict, rule_list, D):
    start_list = []
    for i in range(len(construct)):
        if i not in rule_list:
            if i == D-1:
                return construct[i]
            heapq.heappush(start_list,[construct[i], i])
    con_max_time = 0
    while start_list:
        con_max_time, idx =heapq.heappop(start_list)
        if idx in rule_dict:
            for r in rule_dict[idx]:
                rule_list[r]-=1
                if rule_list[r]==0:
                    if r==D-1:
                        return construct[r]+con_max_time
                    heapq.heappush(start_list,[construct[r]+con_max_time,r])
            del rule_dict[idx]
    return con_max_time

if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for t in range(testcase):
        K = int(sys.stdin.readline().split(' ')[1])
        construct = list(map(int, sys.stdin.readline().split(' ')))
        rule_dict = defaultdict(list)
        rule_list = defaultdict(int)
        for i in range(K):
            l, r = map(int,sys.stdin.readline().split(' '))
            rule_dict[l-1].append(r-1)
            rule_list[r-1]+=1
        D = int(sys.stdin.readline())
        print(solution(construct,rule_dict,rule_list, D))