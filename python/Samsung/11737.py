Order = 1
y,x = 0,0
# U     ㄷ     n     >
# 1 4   3 4   3 2   1 2
# 2 3   2 1   4 1   4 3
rot = 0
d = [[(0,0),(1,0),(1,1),(0,1)],
    [(1,1),(1,0),(0,0),(0,1)],
    [(1,1),(0,1),(0,0),(1,0)],
    [(0,0),(0,1),(1,1),(1,0)]]

def getYX(num):
    global y,x,Order,rot
    Order-=1
    #print(y,x,num)
    if(Order<0): return
    now = 1<<Order
    size = now<<Order
    zone = (num-1)>>(Order*2)
    nextnum = (num)%size
    #print(rot,zone)
    dy,dx = d[rot][zone]
    x+=dx*now
    y+=dy*now
    if (zone==0 and rot%2==0) or (zone==3 and rot%2==1):
        #좌회전
        rot=(rot-1)%4
    elif (zone==3 and rot%2==0) or (zone==0 and rot%2==1):
        #우회전
        rot=(rot+1)%4
    getYX(nextnum)

def test():
    global Order, rot,y,x
    temp1,temp2 = Order, rot
    visited = [[0]*(2**Order) for _ in range(2**Order)]
    def printTable():
        for i in range(2**temp1):
            print(visited[i])
    for i in range(1,65):
        Order = temp1
        rot = temp2
        y,x = 0,0
        getYX(i)
        visited[y][x]=1
        printTable()
        print()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,a,b = input().split()
    Order = int(n)
    rot = 3
    y,x = 0,0
    getYX(int(a))
    # print("================\n",y,x)
    # print("================")
    y1,x1 = y,x
    Order = int(n)
    rot = 3 
    y,x = 0,0
    getYX(int(b))
    #print(y,x)
    print("#"+str(test_case)+" "+str(round((((y-y1)*10)**2+((x-x1)*10)**2)**0.5)))

