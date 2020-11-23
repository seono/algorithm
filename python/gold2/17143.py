import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
arr = {}
m_r = int((R-1)*2)
m_c = int((C-1)*2)
result = 0
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    arr[(r-1,c-1)]=[s,d,z]


def next_arr(arr, p):
    new_fish_index = {}
    global m_r, m_c, R, result
    for i in range(R):
        if (i,p) in arr:
            result+=arr[(i,p)][2]
            del arr[(i,p)]
            break
    for key, value in arr.items():
        if value[1]<3:
            d = 2
            idx = 0
            if m_r>0:
                if value[1] == 2:
                    idx = (key[0] + value[0]) % m_r
                else:
                    idx = (m_r + value[0] - key[0]) % m_r
                if idx>m_r-idx:
                    d = 1
                    idx = m_r - idx
            new_idx = (idx,key[1])
            value[1] = d
            if new_idx in new_fish_index:
                if value[2]>new_fish_index[new_idx][2]:
                    new_fish_index[new_idx] = value
            else:
                new_fish_index[new_idx] = value
        else:
            d = 3
            idx = 0
            if m_c>0:
                if value[1] == 3:
                    idx = (key[1] + value[0]) % m_c
                else:
                    idx = (m_c + value[0] - key[1]) % m_c
                if idx>m_c-idx:
                    d = 4
                    idx = m_c - idx
            new_idx = (key[0],idx)
            value[1] = d
            if new_idx in new_fish_index:
                if value[2]>new_fish_index[new_idx][2]:
                    new_fish_index[new_idx] = value
            else:
                new_fish_index[new_idx] = value
    #print_data(new_fish_index)
    return new_fish_index

def print_data(fish_data):
    global R,C
    arr = [[0]*C for i in range(R)]
    for key,value in fish_data.items():
        arr[key[0]][key[1]] = value[2]
    for _ in arr:
        print(_)
    print()

for i in range(C):
    arr = next_arr(arr,i)
print(result)