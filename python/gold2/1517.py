import sys
import copy
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
new_list = copy.deepcopy(n_list)
result = 0

def merge_sort(temp):
    global n, result
    size = 1
    while size<n:
        left_start, right_start = 0, size
        k=0
        while right_start<=n:
            left, right = left_start,right_start
            k = left
            while left<right_start and right<right_start+size and right<n:
                if n_list[left]<=n_list[right]:
                    new_list[k]=n_list[left]
                    k+=1
                    left+=1
                else:
                    new_list[k]=n_list[right]
                    k+=1
                    right+=1
                    result+=right_start-left
            while left<right_start and left<n:
                new_list[k]=n_list[left]
                k+=1
                left+=1
            while right<right_start+size and right<n:
                new_list[k]=n_list[right]
                k+=1
                right+=1

            left_start+=(2*size)
            right_start+=(2*size)
        for i in range(n):
            n_list[i]=new_list[i]
        size=size*2

merge_sort(n_list)
print(result)