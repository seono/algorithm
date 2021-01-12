#include <bits/stdc++.h>
using namespace std;

struct Edge{
	int v, c, dual;
	Edge(){}
	Edge(int v, int c, int dual) : v(v), c(c), dual(dual) {}
};

vector<Edge> g[10101];
int k, n;
const int s = 1 * 2 + 1;
const int t = 2 * 2;

void addEdge(int s, int e, int x){
	g[s].emplace_back(e, 1, g[e].size());
	g[e].emplace_back(s, 0, g[s].size()-1);
}

void init(){
	for(int i=0; i<10101; i++) g[i].clear();
}

bool flow(){
	int path[10101] = {0};
	int par[10101]; memset(par, -1, sizeof par);
	queue<int> q; q.push(s);
	while(q.size()){
		int now = q.front(); q.pop();
		for(int x=0; x<g[now].size(); x++){
			auto i = g[now][x];
			int nxt = i.v;
			int cap = i.c;
			int dual = i.dual;
			if(par[nxt] == -1 && cap > 0){
				par[nxt] = now;
				path[nxt] = x;
				q.push(nxt);
			}
		}
	}
	if(par[t] == -1) return 0;

	for(int i=t; i!=s; i=par[i]){
		int a = par[i], b = i;
		g[a][path[b]].c --;
		int dual = g[a][path[b]].dual;
		g[b][dual].c ++;
	}
	return 1;
}

void print(){
	int prv = -2, now = s;
	while(now/2 != 2){
		if(now & 1) printf("%d ", now/2);
		prv = now;
		if(now % 2 == 0){
			now = now + 1; continue;
		}
		for(int i=0; i<g[now].size(); i++){
			int nxt = g[now][i].v;
			if(nxt/2 == now/2) continue;
			if(g[now][i].c == 0){
				g[now][i].c = 1;
				now = nxt;
				break;
			}
		}
	}
	printf("%d\n", 2);
}

void solve(int tc){
	init();
	for(int i=1; i<=n; i++){
		addEdge(i*2, i*2+1, 1);
		int j; char c;
		while(1){
			scanf("%d%c", &j, &c);
			addEdge(i*2+1, j*2, 1);
			if(c == '\n') break;
		}
	}

	printf("Case %d:\n", tc);
	for(int i=0; i<k; i++){
		if(!flow()){
			printf("Impossible\n\n"); return;
		}
	}

	for(int i=0; i<k; i++) print();
	printf("\n");
}

int main(){
	int asdf = 1;
	while(1){
		scanf("%d %d", &k, &n);
		if(!k && !n) break;
		solve(asdf++);
	}
}