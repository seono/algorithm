import sys
import bisect
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

arr = [num_list.pop(0)]
for n in num_list:
    if n>arr[-1]:
        arr.append(n)
    else:
        idx = bisect.bisect_left(arr,n)
        arr[idx] = n
print(len(arr))