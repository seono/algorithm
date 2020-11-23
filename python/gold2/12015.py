import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]

for num in arr[1:]:
    if num>result[-1]:
        result.append(num)
    else:
        result[bisect.bisect_left(result,num)] = num
print(len(result))