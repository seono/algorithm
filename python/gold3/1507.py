import sys
input = sys.stdin.readline

def sol(road_map):
    result = 0
    unuse_map = [[False for i in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(i+1,N):
            for k in range(N):
                if k==i or k==j:
                    continue
                if road_map[i][j]==road_map[i][k]+road_map[k][j]:
                    unuse_map[i][j]=True
                elif road_map[i][j]>road_map[i][k]+road_map[k][j]:
                    return -1
    for i in range(N):
        for j in range(i+1,N):
            if unuse_map[i][j]==False:
                result+=road_map[i][j]
    return result

if __name__ == "__main__":
    N = int(input())
    road_map = [[] for i in range(N)]
    
    for i in range(N):
        road_map[i] = list(map(int, input().split(' ')))
    
    print(sol(road_map))
    
