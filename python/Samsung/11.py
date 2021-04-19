import sys

sys.stdin = open("input.txt", "r")

d = [-2,-1,1,2]

def sol():
    global ans
    visited = [False]*width
    for idx,num in new_arr:
        if visited[idx]:continue
        if num==0:continue
        m = 0
        for dx in d:
            n = arr[idx+dx]
            visited[idx+dx]=True
            m = max(n,m)
        if m>=num:
            continue
        ans+=num-m
        


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = 0
    width = int(input())
    arr = list(map(int,input().split()))
    new_arr = [(idx,num) for idx,num in enumerate(arr)]
    new_arr.sort(key=lambda x : x[1], reverse=True)
    sol()
    print("#"+str(test_case),ans)