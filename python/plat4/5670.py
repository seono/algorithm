import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self):
        self.next = {}
        self.cnt = 0
class Trie(object):
    def __init__(self):
        self.root = Node()
        self.cnt = 0
        self.ans = 0

    def addWord(self,node,word):
        if len(word)==0:
            node.next['*']={}
            return
        if word[0] not in node.next:
            node.next[word[0]]= Node()
        node.cnt+=1
        self.addWord(node.next[word[0]],word[1:])


    def bfs(self):
        st = []
        for v in self.root.next.values():
            st.append([v,1])
        while st:
            n,cnt = st.pop()
            while True:
                if len(n.next)>1 or '*' in n.next:break
                n=list(n.next.values())[0]
            for k,v in n.next.items():
                if k=='*':
                    self.cnt+=1
                    self.ans+=cnt
                else:
                    st.append([v,cnt+1])
        return round(self.ans/self.cnt)
def round(num):
    st = str(num)
    i,f = st.split('.')
    if len(f)<3:
        while len(f)<2:
            f+="0"
        return float(i+'.'+f)
    if int(f[2])<5:
        return float(i+'.'+f[:2])
    else:
        return float(i+'.'+f[:2])+0.01
    
while True:
    try:
        n = int(input())
    except:
        break
    t = Trie()
    for _ in range(n):
        word = input().strip()
        t.addWord(t.root,word)
    print(format(t.bfs(),".2f"))