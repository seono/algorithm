import sys
import bisect
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
tree = [0]*(N+1)
arr = []
def update(idx,diff):
    while idx<=N:
        tree[idx]+=diff
        idx+=(idx&-idx)
def get(idx):
    ret = 0
    while idx>0:
        ret+=tree[idx]
        idx-=(idx&-idx)
    return ret
arr = [int(input())for _ in range(N)]
n_dict = {}
for new_num,num in enumerate(sorted(arr),1):
    n_dict[num]=new_num
arr = [n_dict[num] for num in arr]
for n in arr:
    update(n,1)
    print("%d\n"%(get(N)-get(n-1)))