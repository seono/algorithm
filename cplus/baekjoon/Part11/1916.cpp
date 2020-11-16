#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
const int MAX_V = 1000;
const int INF = 1000000000;

typedef pair<int, int> P;
int main() {
	int V, E;
	vector<P> adj[MAX_V];
	scanf("%d %d", &V, &E);
	for (int i = 0; i < E; i++) {
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		adj[u - 1].push_back(P(v - 1, w));
	}

	int dist[MAX_V];
	fill(dist, dist + MAX_V, INF);
	bool visited[MAX_V] = { 0, };
	priority_queue<P, vector<P>, greater<P>> PQ;
	int st, ed;
	scanf("%d %d", &st, &ed);
	st--; ed--;
	dist[st] = 0;
	PQ.push(P(0, st));
	while (!PQ.empty()) {
		int curr;
		do {
			curr = PQ.top().second;
			PQ.pop();
		} while (!PQ.empty()&& visited[curr]);
		if (visited[curr])break;
		visited[curr] = true;
		for (auto& p : adj[curr]) {
			int next = p.first, d = p.second;
			if (dist[next] > dist[curr] + d) {
				dist[next] = dist[curr] + d;
				PQ.push(P(dist[next], next));
			}
		}
	}
	printf("%d", dist[ed]);
	return 0;
}