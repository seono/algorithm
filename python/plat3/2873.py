import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = ""
def findminyx():
    m_list = []
    for y,t in enumerate(arr,1):
        for x,num in enumerate(t,1):
            m_list.append([num,y,x])
    for _,y,x in sorted(m_list):
        if (y%2)^(x%2):
            return y,x
if N%2:
    for i in range(N-1):
        if i%2==0:
            ans+='R'*(M-1)
        else:
            ans+='L'*(M-1)
        ans+="D"
    ans+='R'*(M-1)
elif M%2:
    for i in range(M-1):
        if i%2==0:
            ans+='D'*(N-1)
        else:
            ans+='U'*(N-1)
        ans+="R"
    ans+="D"*(N-1)
else:
    y,x = findminyx()
    if y%2==0:
        #1~x-1까지
        for i in range(x-1):
            if i%2==0:
                ans+='D'*(N-1)+'R'
            else:
                ans+='U'*(N-1)+'R'
        #현재 1,x
        #1~y-1까지
        for i in range(y-2):
            if i%2==0:
                ans+='R'*(M-x)+'D'
            else:
                ans+='L'*(M-x)+'D'
        if y==N:
            for i in range(M-x):
                if i%2==0:ans+='RD'
                else:ans+='RU'
        else:
            ans+='R'*(M-x)+'D'+'L'*(M-x-1)+'D'
            for i in range(N-y-1):
                if i%2==0:ans+="LD"
                else:ans+="RD"
            ans+='R'
            for i in range(M-x-1):
                if i%2==0:ans+='R'+'U'*(N-y-1)
                else:ans+='R'+'D'*(N-y-1)
    #x가 짝
    else:
        #print('hi')
        for i in range(y-1):
            if i%2==0:ans+='R'*(M-1)+'D'
            else:ans+='L'*(M-1)+'D'
        for i in range(x-2):
            if i%2==0:ans+='D'*(N-y)+'R'
            else:ans+='U'*(N-y)+'R'
        if x==M:
            for i in range(N-y):
                if i%2==0:ans+='DR'
                else:ans+='DL'
        else:
            ans+='D'*(N-y)+'R'+'U'*(N-y-1)+'R'
            for i in range(M-x-1):
                if i%2==0:ans+='UR'
                else:ans+='DR'
            ans+='D'
            for i in range(N-y-1):
                if i%2==0:ans+='D'+'L'*(M-x-1)
                else:ans+='D'+'R'*(M-x-1)
print(ans)

# def check(s):
#     y,x=0,0
#     visited = [[0]*M for _ in range(N)]
#     visited[0][0]=1
#     res = arr[y][x]
#     for c in s:
#         if c=='R':x+=1
#         elif c=='L':x-=1
#         elif c=='U':y-=1
#         else:y+=1
#         res+=arr[y][x]
#         visited[y][x]=1
#     print('\n'.join(map(str,visited)))
# check(ans)