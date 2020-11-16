#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Graph {
public:
	int N;
	vector<vector<int>>adj;
	vector<bool>visited;

	Graph() :N(0) {}
	Graph(int n) :N(n) {
		adj.resize(N);
		visited.resize(N);
	}

	void addEdge(int u, int v) {
		adj[u].push_back(v);
	}

	void sortList() {
		for (int i = 0; i < N; i++) {
			sort(adj[i].begin(), adj[i].end());
		}
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
				cout << "== new DFS begins ==" << endl;
				dfs(i);
				components++;
			}
		}
		return components;
	}

	int Gdfs() {
		int components = 0;
		for (int i = 1; i < N; i++) {
			fill(visited.begin(), visited.end(), false);
			components += Newdfs(i,i);
		}
		return components;
	}

private:
	int Newdfs(int curr, int idx) {
		visited[curr] = true;
		if (adj[curr][0] == idx) return 1;
		if (!visited[adj[curr][0]]) return Newdfs(adj[curr][0], idx);
		else return 0;
	}
	void dfs(int curr) {
		visited[curr] = true;
		cout << "node " << curr << " visited" << endl;
		for (int next : adj[curr])
			if (!visited[next])dfs(next);
	}

};
int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		int c;
		scanf("%d", &c);
		Graph G(c+1);
		for (int i = 1; i <= c; i++) {
			int n;
			scanf("%d", &n); G.addEdge(i, n);
		}
		printf("%d\n", c - G.Gdfs());
	}
	return 0;
}