#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
using namespace std;

const int MAX_V = 1001;
const int INF = 20000000;

typedef pair<int, int> P;

int main() {
	int N, M, X;
	scanf("%d %d %d", &N, &M, &X);
	vector<P>adj[MAX_V];
	for (int i = 0; i < M; i++) {
		int v, u, w;
		scanf("%d %d %d", &v, &u, &w);
		adj[v - 1].push_back(P(u - 1, w));
	}
	int dist[MAX_V][MAX_V] = { 0 };
	for (int i = 0; i < MAX_V; i++) {
		for (int j = 0; j < MAX_V; j++)dist[i][j] = INF;
	}
	priority_queue<P, vector<P>, greater<P>> PQ;
	for (int i = 0; i < N; i++) {
		bool visited[MAX_V] = { 0, };
		dist[i][i] = 0;
		PQ.push(P(0, i));
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
				if (dist[i][next] > dist[i][curr] + d) {
					dist[i][next] = dist[i][curr] + d;
					PQ.push(P(dist[i][next], next));
				}
			}
		}
		while (!PQ.empty())PQ.pop();
	}
	int max=0;
	X--;
	for (int i = 0; i < N; i++) {
		if(dist[i][X] + dist[X][i] > max)max = dist[i][X] + dist[X][i];
	}
	printf("%d", max);
	return 0;
}