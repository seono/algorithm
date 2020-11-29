import sys
input = sys.stdin.readline

N = int(input())
root = [[] for _ in range(N+1)]
node_list = set(range(1,N+1))
for _ in range(N):
    x, l, r = map(int, input().split())
    root[x] = ([l,r])
    if l in node_list:
        node_list.remove(l)
    if r in node_list:
        node_list.remove(r)
n = list(node_list)[0]
inorder,st = {},[]
temp = 1
now = n
while now>0 or st:
    if now>0:
        st.append(now)
        now = root[now][0]
    else:
        now = st.pop()
        inorder[now] = temp
        temp+=1
        now = root[now][1]
result = 1
max_lv = 1
idx = 1
next_lv = []
if root[n][0]>0:
    next_lv.append(root[n][0])
if root[n][1]>0:
    next_lv.append(root[n][1])
while next_lv:
    l,r = next_lv[0],next_lv[-1]
    width = inorder[r]-inorder[l]+1
    idx+=1
    if width>result:
        result = width
        max_lv = idx
    l = len(next_lv)
    while l>0:
        l-=1
        n = next_lv.pop(0)
        if root[n][0]>0:
            next_lv.append(root[n][0])
        if root[n][1]>0:
            next_lv.append(root[n][1])
print(max_lv,result)