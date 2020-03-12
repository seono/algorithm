#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Graph {
public:
	int N;
	vector<vector<int>>adj;
	vector<bool>visited;

	Graph():N(0){}
	Graph(int n) :N(n) {
		adj.resize(N);
		visited.resize(N);
	}

	void addEdge(int u, int v) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	void sortList() {
		for (int j = 0; j < N; j++)sort(adj[j].begin(), adj[j].end());
	}

	void dfs() {
		fill(visited.begin(), visited.end(), false);
		dfs(0);
	}
	int dfsAll() {
		int components = 0;
		fill(visited.begin(), visited.end(), false);
		for (int i = 0; i < N; i++) {
			if (!visited[i]) {
				dfs(i);
				components++;
			}
		}
		return components;
	}

private:
	void dfs(int curr) {
		visited[curr] = true;
		for (int next : adj[curr])
			if (!visited[next])dfs(next);
	}
};

int main() {
	int N, M;
	scanf("%d %d", &N,&M);
	Graph G(N);
	for (int i = 0; i < M; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		G.addEdge(x-1, y-1);
	}
	printf("%d\n", G.dfsAll());
	return 0;
}