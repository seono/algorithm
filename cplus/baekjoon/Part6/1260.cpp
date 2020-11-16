#include<iostream>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;


class Graph {
public:
	int N;
	vector<vector<int>> adj;
	vector<bool>visited;

	Graph():N(0){}
	Graph(int n) :N(n) { adj.resize(N); visited.resize(N); }

	void addEdge(int v, int u) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	void sortList() {
		for (int i = 0; i < N; i++)sort(adj[i].begin(), adj[i].end());
	}

	void bfs(int idx) {
		fill(visited.begin(), visited.end(), false);
		queue<int> Q;
		Q.push(idx);
		visited[idx] = true;
		while (!Q.empty()) {
			int curr = Q.front();
			cout << curr << " ";
			Q.pop();
			for (int next : adj[curr]) {
				if (!visited[next]) {
					visited[next] = true;
					Q.push(next);
				}
			}
		}
	}
	void dfs(int idx) {
		fill(visited.begin(), visited.end(), false);
		Rdfs(idx);
	}

private:
	void Rdfs(int idx) {
		visited[idx] = true;
		cout << idx << " ";
		for (int next : adj[idx]) {
			if (!visited[next])Rdfs(next);
		}
	}
};

int main() {
	int N, M, V;
	scanf("%d %d %d", &N, &M, &V);
	Graph G(N + 1);
	for (int i = 0; i < M; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		G.addEdge(x, y);
	}
	G.sortList();
	G.dfs(V);
	cout << endl;
	G.bfs(V);
	cout << endl;
	return 0;
}