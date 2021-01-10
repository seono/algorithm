import sys
input = sys.stdin.readline

class myDict(object):
    def __init__(self):
        self.root = {}

    def insert(self, now, word, idx):
        if len(word)==idx:
            now['*']=word
            return
        if word[idx] not in now:
            now[word[idx]]={}
        self.insert(now[word[idx]],word,idx+1)
        return

    
myD = myDict()
N = int(input())
for _ in range(N):
    row = input().strip()
    myD.insert(myD.root,row,0)
boggle = []
visited = [[False]*4 for _ in range(4)]
dy,dx = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]
word_set = set()
score_Dict = {1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
def dfs(y,x,now,length):
    global boggle,visited
    if length>8:return
    if boggle[y][x] in now:
        if '*' in now[boggle[y][x]]:
            word_set.add(now[boggle[y][x]]['*'])
        for i in range(8):
            ny,nx=y+dy[i],x+dx[i]
            if ny<0 or nx<0 or ny>=4 or nx>=4:continue
            if visited[ny][nx]:continue
            visited[ny][nx]=True
            dfs(ny,nx,now[boggle[y][x]],length+1)
            visited[ny][nx]=False
input()
M = int(input())
for i in range(M):
    boggle = [input().strip() for _ in range(4)]
    if i<M-1:
        input()
    for y in range(4):
        for x in range(4):
            visited[y][x]=True
            dfs(y,x,myD.root,0)
            visited[y][x]=False
    total_score = 0
    word_list = sorted(word_set)
    for word in word_set:
        total_score+=score_Dict[len(word)]
    print(total_score,min(word_set,key=lambda x : (-len(x),x)),len(word_set))
    word_set = set()
