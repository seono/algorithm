import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write


class Trie(object):
    def __init__(self):
        self.next = {}
        self.fail = None
        self.output = False
    
    def addWord(self,node,word):
        if len(word)==0:
            node.output = True
            return
        nx = ord(word[0])-97
        if nx not in node.next:
            node.next[nx]=Trie()
        self.addWord(node.next[nx], word[1:])
    
    
root = Trie()
for i in range(int(input())):
    root.addWord(root,input().strip())

Q = deque()
root.fail = root
Q.append(root)
while Q:
    cur = Q.popleft()
    for i in range(26):
        if i not in cur.next:
            continue
        if cur == root:cur.next[i].fail=root
        else:
            tmp = cur.fail
            while tmp!=root and i not in tmp.next:
                tmp = tmp.fail
            if i in tmp.next:
                tmp = tmp.next[i]
            cur.next[i].fail = tmp
        if cur.next[i].fail.output:
            cur.next[i].output=True
        Q.append(cur.next[i])

for i in range(int(input())):
    word = input().strip()
    cur = root
    res = False
    for c in word:
        nx = ord(c)-97
        while cur!=root and cur and nx not in cur.next:
            cur = cur.fail
        if cur and nx in cur.next:
            cur = cur.next[nx]
        if cur and cur.output:
            res = True
            break
    output("YES\n" if res else "NO\n")