#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

class Graph {
public:
	int N;
	vector<vector<int>> adj;

	Graph():N(0){}
	Graph(int n) :N(n) { adj.resize(N); }

	void addEdge(int u, int v) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	void sortList() {
		for (int i = 0; i < N; i++) {
			sort(adj[i].begin(), adj[i].end());
		}
	}

	void bfs() {
		vector<bool> visited(N, false);
		queue<int> Q;
		Q.push(0);
		visited[0] = true;
		while (!Q.empty()) {
			int curr = Q.front();
			Q.pop();
			if(curr)
			for (int next : adj[curr]) {
				if (!visited[next]) {
					visited[next] = true;
					Q.push(next);
				}
			}
		}
	}

	int A_bfs(int x,int y) {
		vector<bool> visited(N, false);
		queue<int> Q;
		int ans = -1;
		int worked = -1;
		Q.push(x);
		visited[x] = true;
		while (!Q.empty()) {
			ans++;
			int qSize = Q.size();
			int curr;
			for (int i = 0; i < qSize; i++) {
				curr = Q.front();
				if (curr == y) return ans;
				Q.pop();
				for (int next : adj[curr]) {
					if (!visited[next]) {
						visited[next] = true;
						Q.push(next);
					}
				}
			}
		}
		return -1;
	}
};

int main() {
	int N;
	scanf("%d", &N);
	int x, y;
	scanf("%d %d", &x, &y);
	Graph G(N+1);
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		G.addEdge(a, b);
	}
	int ans = G.A_bfs(x, y);
	printf("%d", ans);
	return 0;
}