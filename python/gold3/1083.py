import sys
input = sys.stdin.readline


def sol(num_list, S, target):
    if S==0 or len(num_list)==0:
        return num_list
    if target<0:
        return sol(num_list, S, 0)
    if target==len(num_list)-1:
        return num_list
    m_idx = num_list.index(max(num_list[:S+1]))
    if m_idx<=S:
        return [num_list.pop(m_idx)] + sol(num_list,S-m_idx,0)
    if num_list[target]<num_list[target+1]:
        num_list[target], num_list[target+1] = num_list[target+1], num_list[target]
        return sol(num_list, S-1, target-1)
    return sol(num_list, S, target+1)


if __name__ == "__main__":
    N = int(input())
    sys.setrecursionlimit(3000)
    num_list = list(map(int,input().split(' ')))
    S = int(input())
    if len(num_list)==1:
        print(num_list[0])
    elif S == 0:
        for x in num_list:
            print(x, end=' ')
    else:
        for x in sol(num_list,S,0):
            print(x, end=' ')