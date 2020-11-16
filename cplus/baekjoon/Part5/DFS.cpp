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

private:
	void dfs(int curr) {
		visited[curr] = true;
		cout << "node " << curr << " visited" << endl;
		for (int next : adj[curr])
			if (!visited[next])dfs(next);
	}

};

int main() {
	Graph G(10);
	G.addEdge(0, 1);
	G.addEdge(1, 3);
	G.addEdge(3, 3);
	G.addEdge(2, 3);
	G.addEdge(4, 6);
	G.addEdge(5, 7);
	G.addEdge(5, 8);
	G.addEdge(7, 8);
	G.sortList();
	int components = G.dfsAll();
	cout << "The number of components is " << components << endl;
}