import sys
import bisect
import copy
input = sys.stdin.readline

M = int(input())
num_list = list(map(int,input().split()))

st = [num_list[0]]
temp = [None]*M

for idx in range(M):
    num = num_list[idx]
    if num>st[-1]:
        st.append(num)
        temp[idx]=len(st)-1
    else:
        i = bisect.bisect_left(st,num)
        st[i]=num
        temp[idx]=i
l = len(st)
print(l)
l-=1
temp2 = []
for i in range(M-1,-1,-1):
    if l<0:
        break
    if temp[i]==l:
        temp2.append(num_list[i])
        l-=1
print(' '.join(map(str, temp2[::-1])))