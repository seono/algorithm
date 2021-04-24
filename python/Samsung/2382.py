import sys
sys.stdin = open("input.txt", "r")

#상하좌우 y,x
d = [(-1,0),(1,0),(0,-1),(0,1)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int,input().split())
    st = {}
    for _ in range(K):
        y,x,cnt,dir = map(int,input().split())
        st[(y,x)]=(cnt,dir-1)
    for t in range(M):
        new_st = {}
        for key,value in st.items():
            y,x = key
            cnt,dir = value
            dy,dx = d[dir]
            ny,nx = y+dy,x+dx
            if ny==0 or ny==N-1 or nx==0 or nx==N-1:
                cnt>>=1
                dir^=1
                if cnt:
                    new_st[(ny,nx)]=[(cnt,dir)]
            else:
                if (ny,nx) in new_st:
                    new_st[(ny,nx)].append((cnt,dir))
                else:
                    new_st[(ny,nx)]=[(cnt,dir)]
        st = {}
        for key,value in new_st.items():
            if len(value)>1:
                nCnt,nDir = 0,0
                sumCnt = 0
                for c,dir in value:
                    if c>nCnt:
                        nDir = dir
                        nCnt = c
                    sumCnt+=c
                st[key]=(sumCnt,nDir)
            else:
                st[key]=value[0]
    ans = 0
    for v in st.values():
        ans+=v[0]
    print("#"+str(test_case),ans)