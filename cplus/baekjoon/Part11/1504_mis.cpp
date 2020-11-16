//문제-> 정점 st,ed(마지막입력)을 지나는 1,N 최단경로
//코드-> st,ed를 잇는 간선을 지나는 1,N최단경로
//st,ed간선체크후-> 1~st+ed~N과 1~ed+st~N비교
#include<iostream>
#include<vector>
#include<cstring>
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
		adj[v - 1].push_back(P(u - 1, w));
	}
	int *dist_st = new int[V];
	fill(dist_st, dist_st + V, INF);
	bool visited[MAX_V] = { 0, };
	priority_queue<P, vector<P>, greater<P>> PQ;
	int st, ed;
	scanf("%d %d", &st, &ed);
	st--; ed--;
	bool check = false;
	int ans;
	for (auto& p : adj[st]) {
		int next = p.first;
		if (next == ed) {
			ans = p.second;
			check = true; break;
		}
	}
	if (!check) {
		printf("-1"); return 0;
	}
	dist_st[0] = 0;
	PQ.push(P(0, 0));
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
			int next = p.first, d = p.second;
			if (dist_st[next] > dist_st[curr] + d) {
				dist_st[next] = dist_st[curr] + d;
				//주변 edge크기, 정점idx
				PQ.push(P(dist_st[next], next));
			}
		}
	}
	while (!PQ.empty())PQ.pop();
	int *dist_ed=new int[V];
	fill(dist_ed, dist_ed + V, INF);
	dist_ed[V-1] = 0;
	PQ.push(P(0, V-1));
	fill(visited, visited + MAX_V, false);
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
			int next = p.first, d = p.second;
			if (dist_ed[next] > dist_ed[curr] + d) {
				dist_ed[next] = dist_ed[curr] + d;
				//주변 edge크기, 정점idx
				PQ.push(P(dist_ed[next], next));
			}
		}
	}
	ans = dist_st[st] + dist_ed[ed] < dist_st[ed] + dist_ed[st] ?
		ans+dist_st[st] + dist_ed[ed] : ans+dist_st[ed] + dist_ed[st];
	if (ans > INF)printf("-1");
	else printf("%d", ans);
	return 0;
}