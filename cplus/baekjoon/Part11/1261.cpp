#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
using namespace std;
const int MAX_V = 101;
const int MAX_N = 10001;
const int INF = 10001;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

typedef pair<int,pair<int, int>>P;

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	int arr[MAX_V][MAX_V];
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}
	vector<P>adj[MAX_V][MAX_V];
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			for (int a = 0; a < 4; a++) {
				int tx = j + dx[a];
				int ty = i + dy[a];
				if (tx < 0 || tx >= n || ty < 0 || ty >= m)continue;
				adj[i][j].push_back(P(arr[ty][tx], pair<int,int>(ty,tx)));
			}
		}
	}
	int dist[MAX_N];
	fill(dist, dist + MAX_N, INF);
	bool visited[MAX_V][MAX_V] = { 0, };
	priority_queue<P, vector<P>, greater<P>>PQ;
	dist[0] = 0;
	PQ.push(P(0,pair<int,int>(0, 0)));
	while (!PQ.empty()) {
		pair<int,int> curr;
		do {
			curr = PQ.top().second;
			PQ.pop();
		} while (!PQ.empty() && visited[curr.first][curr.second]);
		if (visited[curr.first][curr.second])break;
		visited[curr.first][curr.second] = true;
		for (const auto& p : adj[curr.first][curr.second]) {
			pair<int, int>next = p.second;
			int d = p.first;
			if (dist[next.first * n + next.second] > dist[curr.first * n + curr.second] + d) {
				dist[next.first * n + next.second] = dist[curr.first * n + curr.second] + d;
				PQ.push(P(dist[next.first*n+next.second], next));
			}
		}
	}
	printf("%d", dist[n * m - 1]);
	return 0;
}