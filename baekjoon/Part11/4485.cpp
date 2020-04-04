#include<iostream>
#include<cstring>
#include<queue>
using namespace std;
const int MAX_V = 16000;
const int MAX_N = 126;
const int INF = 200000;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

typedef pair<int, int>P;

int main() {
	int num = 0;
	while (true) {
		num++;
		int n;
		scanf("%d", &n);
		vector<P>adj[MAX_V];
		if (!n)break;
		int arr[MAX_N][MAX_N];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)scanf("%d", &arr[i][j]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int a = 0; a < 4; a++) {
					int tx = j + dx[a];
					int ty = i + dy[a];
					if (tx < 0 || tx >= n || ty < 0 || ty >= n)continue;
					adj[i * n + j].push_back(P(ty * n + tx, arr[ty][tx]));
				}
			}
		}
		int dist[MAX_V];
		fill(dist, dist + MAX_V, INF);
		bool visited[MAX_V] = { 0, };
		priority_queue<P, vector<P>, greater<P>> PQ;
		dist[0] = 0;
		PQ.push(P(0, 0));
		while (!PQ.empty()) {
			int curr;
			do {
				curr = PQ.top().second;
				PQ.pop();
			} while (!PQ.empty() && visited[curr]);
			if (visited[curr])break;
			visited[curr] = true;
			for (const auto& p : adj[curr]) {
				int next = p.first, d = p.second;
				if (dist[next] > dist[curr] + d) {
					dist[next] = dist[curr] + d;
					PQ.push(P(dist[next], next));
				}
			}
		}
		printf("Problem %d: %d\n",num, dist[n * n - 1]+arr[0][0]);
	}
}