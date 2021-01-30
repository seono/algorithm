#include <stdio.h>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAX_V = 401;
int N, P, visit[MAX_V], c[MAX_V][MAX_V], f[MAX_V][MAX_V], parent[MAX_V];
vector<int> adj[MAX_V];
 
int maxFlow(int source, int sink) {
    int ret = 0;
    while (1) {
        memset(parent, -1, sizeof(parent));
        queue<int> q;
        q.push(source);
        while (!q.empty() && parent[sink]==-1){
            int cur = q.front();
            q.pop();
            for (int next : adj[cur]) {
                if (!visit[next] && c[cur][next] - f[cur][next] > 0 && parent[next] == -1) {
                    parent[next] = cur;
                    q.push(next);
                }
            }
        }
        if (parent[sink] == -1) break;
        int tmpFlow = 987654321;
        for (int i = sink; i != source; i = parent[i]) {
            tmpFlow = min(tmpFlow, c[parent[i]][i] - f[parent[i]][i]);
            if (i != sink && i != source) visit[i] = true;
        }
        for (int i = sink; i != source; i = parent[i]) {
            f[parent[i]][i] += tmpFlow;
            f[i][parent[i]] -= tmpFlow;
        }
        ret += tmpFlow;
    }
    return ret;
}
 
int main() {
    scanf("%d %d", &N, &P);
    for (int i = 0; i < P; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
        c[a][b] = 1;
        c[b][a] = 1;
    }
    printf("%d", maxFlow(1, 2));
    return 0;
}