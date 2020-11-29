import sys
input = sys.stdin.readline

testcase = int(input())


class Union(object):
    def __init__(self, num):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = [x,1]
            return x
        if x==self.parent[x][0]:
            return x
        else:
            p = self.find(self.parent[x][0])
            self.parent[x][0] = p
            return p
    
    def Union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x!=y):
            self.parent[y][0] = x
            self.parent[x][1]+=self.parent[y][1]
        return self.parent[x][1]

for _ in range(testcase):
    F = int(input())
    u = Union(F)
    for _ in range(F):
        a,b = map(str, input().split())
        print(u.Union(a,b))
        
    
