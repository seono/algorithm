import sys
input = sys.stdin.readline

T = int(input())

def c(plane):
    #6 3 0 7 4 1 8 5 2
    temp = []
    for i in range(3):
        for j in range(2,-1,-1):
            temp.append(cube[plane][j*3+i])
    cube[plane]=temp
    return

def uc(plane):
    #2 5 8 1 4 7 0 3 6
    temp = []
    for i in range(2,-1,-1):
        for j in range(3):
            temp.append(cube[plane][j*3+i])
    cube[plane]=temp
    return

def change(p1,p2,t1,t2):
    for i,j in zip(t1,t2):
        cube[p1][i]=cube[p2][j]
    return

def change2(p1,temp,t1,t2):
    for i,j in zip(t1,t2):
        cube[p1][i]=temp[j]
    return

def command(cmd):
    p,m = cmd
    if m=='+':
        c(p)
    else:
        uc(p)
    if p=='L':
        if m=='+':
            temp = cube['U'][:]
            change('U','B',[0,3,6],[8,5,2])
            change('B','D',[8,5,2],[0,3,6])
            change('D','F',[0,3,6],[0,3,6])
            change2('F',temp,[0,3,6],[0,3,6])
        else:
            temp = cube['B'][:]
            change('B','U',[8,5,2],[0,3,6])
            change('U','F',[0,3,6],[0,3,6])
            change('F','D',[0,3,6],[0,3,6])
            change2('D',temp,[0,3,6],[8,5,2])
    elif p=='R':
        if m=='+':
            temp=cube['U'][:]
            change('U','F',[2,5,8],[2,5,8])
            change('F','D',[2,5,8],[2,5,8])
            change('D','B',[2,5,8],[6,3,0])
            change2('B',temp,[6,3,0],[2,5,8])
        else:
            temp=cube['U'][:]
            change('U','B',[2,5,8],[6,3,0])
            change('B','D',[6,3,0],[2,5,8])
            change('D','F',[2,5,8],[2,5,8])
            change2('F',temp,[2,5,8],[2,5,8])
    elif p=='F':
        if m=='+':
            temp=cube['U'][:]
            change('U','L',[6,7,8],[8,5,2])
            change('L','D',[2,5,8],[0,1,2])
            change('D','R',[0,1,2],[6,3,0])
            change2('R',temp,[0,3,6],[6,7,8])
        else:
            temp=cube['U'][:]
            change('U','R',[6,7,8],[0,3,6])
            change('R','D',[6,3,0],[0,1,2])
            change('D','L',[0,1,2],[2,5,8])
            change2('L',temp,[8,5,2],[6,7,8])
    elif p=='B':
        if m=='+':
            temp=cube['U'][:]
            change('U','R',[2,1,0],[8,5,2])
            change('R','D',[8,5,2],[6,7,8])
            change('D','L',[6,7,8],[0,3,6])
            change2('L',temp,[0,3,6],[2,1,0])
        else:
            temp=cube['U'][:]
            change('U','L',[2,1,0],[0,3,6])
            change('L','D',[0,3,6],[6,7,8])
            change('D','R',[6,7,8],[8,5,2])
            change2('R',temp,[8,5,2],[2,1,0])
    elif p=='D':
        if m=='+':
            temp=cube['F'][:]
            change('F','L',[6,7,8],[6,7,8])
            change('L','B',[6,7,8],[6,7,8])
            change('B','R',[6,7,8],[6,7,8])
            change2('R',temp,[6,7,8],[6,7,8])
        else:
            temp=cube['F'][:]
            change('F','R',[6,7,8],[6,7,8])
            change('R','B',[6,7,8],[6,7,8])
            change('B','L',[6,7,8],[6,7,8])
            change2('L',temp,[6,7,8],[6,7,8])
    elif p=='U':
        if m=='+':
            temp=cube['F'][:]
            change('F','R',[0,1,2],[0,1,2])
            change('R','B',[0,1,2],[0,1,2])
            change('B','L',[0,1,2],[0,1,2])
            change2('L',temp,[0,1,2],[0,1,2])
        else:
            temp=cube['F'][:]
            change('F','L',[0,1,2],[0,1,2])
            change('L','B',[0,1,2],[0,1,2])
            change('B','R',[0,1,2],[0,1,2])
            change2('R',temp,[0,1,2],[0,1,2])
def printT(plane):
    p=0
    for i in range(3,10,3):
        temp = ""
        for j in range(p,i):
            temp+=color[cube[plane][j]]
        print(temp)
        p=i
    return

def printA():
    for i in 'ULFRBD':
        print(i)
        printT(i)

color = "wyrogb"
for _ in range(T):
    #U D F B L R
    cube={'U':[0]*9,'D':[1]*9,'F':[2]*9,'B':[3]*9,'L':[4]*9,'R':[5]*9}
    m = int(input())
    cmd_list = list(map(str,input().split()))
    for cmd in cmd_list:
        command(cmd)
    printT('U')


