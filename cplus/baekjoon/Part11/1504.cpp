#include<iostream>
#include<vector>
#include<cstring>
#include<queue>
#include<algorithm>
using namespace std;
typedef long long ll;
const int MAX_V = 1000;
const ll INF = 200000000;

typedef pair<int, int> P;
int main() {
	int V, E;
	vector<P> adj[MAX_V];
	scanf("%d %d", &V, &E);
	for (int i = 0; i < E; i++) {
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		adj[u - 1].push_back(P(v - 1, w));
		adj[v - 1].push_back(P(u - 1, w));
	}
	ll** dist = new ll* [V];
	for (int i = 0; i < V; i++) {
		dist[i] = new ll[V];
		memset(dist[i], 0, sizeof(ll) * V);
	}
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++)dist[i][j] = INF;
	}
	priority_queue<P, vector<P>, greater<P>> PQ;
	int st, ed;
	scanf("%d %d", &st, &ed);
	st--; ed--;
	PQ.push(P(0, 0));
	for (int i = 0; i < V; i++) {
		dist[i][i] = 0;
		PQ.push(P(0, i));
		bool visited[MAX_V] = { 0, };
		while (!PQ.empty()) {
			int curr;
			do {
				curr = PQ.top().second;
				PQ.pop();
			} while (!PQ.empty() && visited[curr]);
			if (visited[curr])break;
			visited[curr] = true;
			//시작점에서 주변 edge이동
			for (const auto& p : adj[curr]) {
				int next = p.first;
				ll d = p.second;
				if (dist[i][next] > dist[i][curr] + d) {
					dist[i][next] = dist[i][curr] + d;
					//주변 edge크기, 정점idx
					PQ.push(P(dist[i][next], next));
				}
			}
		}
		while (!PQ.empty())PQ.pop();
	}
	ll ans1 = dist[0][st] + dist[st][ed] + dist[ed][V - 1];
	ll ans2 = dist[0][ed] + dist[ed][st] + dist[st][V - 1];
	if (ans1 >= INF && ans2 >= INF) {
		puts("-1"); return 0;
	}
	if (ans1 < ans2)printf("%lld", ans1);
	else printf("%lld", ans2);
	return 0;
}