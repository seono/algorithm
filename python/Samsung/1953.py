import sys


direction = {0:[],1:[(1,0),(-1,0),(0,1),(0,-1)], 2:[(1,0),(-1,0)], 3:[(0,1),(0,-1)], 
             4:[(-1,0),(0,1)], 5:[(1,0),(0,1)], 6:[(1,0),(0,-1)], 7:[(-1,0),(0,-1)]}

state = {"r":0, "c":0, "t":0}
que = []
    
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline().strip("\n"))

for test_case in range(1, T+1):
    h = sys.stdin.readline().strip("\n").split(" ")
    N, M, R, C, L = int(h[0]), int(h[1]), int(h[2]), int(h[3]), int(h[4])
    
    maps = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for row in range(N):
        l = sys.stdin.readline().strip("\n").split(" ")
        for col in range(M):
            maps[row][col] = int(l[col])

    count = 1
    state["r"], state["c"], state["t"] = R, C, 1
    que.append(state)
    visited[R][C] = 1
    while len(que) > 0:
        curr_state = que.pop(0)
        curr_r, curr_c, curr_t = curr_state["r"], curr_state["c"], curr_state["t"]
        if curr_t >= L:
            continue
        for h, v in direction[maps[curr_r][curr_c]]:
            next_r, next_c, next_t = curr_r+h, curr_c+v, curr_t+1

            can_move = (next_r < N) and (next_r >= 0) and (next_c < M) and (next_c >= 0)
            if (can_move == True):
                is_open = False
                for h, v in direction[maps[next_r][next_c]]:
                    tmp_r, tmp_c = next_r+h, next_c+v
                    if (tmp_r==curr_r) and (tmp_c==curr_c):
                        is_open = True
                if (visited[next_r][next_c] < 1) and (is_open==True):
                    new_state = {"r":next_r, "c":next_c, "t":curr_t + 1}
                    que.append(new_state)
                    visited[next_r][next_c] = 1
                    count += 1
    print("#%d %d" %(test_case, count))