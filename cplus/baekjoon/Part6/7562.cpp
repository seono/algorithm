#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;
bool visited[300][300];
int dx[8] = { 2,2,1,1,-1,-1,-2,-2 };
int dy[8] = { 1,-1,2,-2,2,-2,1,-1 };
int main() {
	int N;
	scanf("%d", &N);
	queue<pair<int, int>>Q;
	while (N--) {
		memset(visited, false, sizeof(visited));
		int L;
		scanf("%d", &L);
		int x, y;
		scanf("%d %d", &x, &y);
		int x1, y1;
		int worked = 0;
		scanf("%d %d", &x1, &y1);
		if (x == x1 && y == y1) {
			printf("0\n"); continue;
		}
		while (!Q.empty())Q.pop();
		Q.push(make_pair(x, y));
		int ans = 0;
		while (!Q.empty()) {
			ans++;
			int Qsize = Q.size();
			for (int i = 0; i < Qsize; i++) {
				pair<int, int>tmp = Q.front();
				Q.pop();
				if (tmp.first == x1 && tmp.second == y1)break;
				for (int a = 0; a < 8; a++) {
					int tx = tmp.first + dx[a];
					int ty = tmp.second + dy[a];
					if (tx == x1 && ty == y1) {
						printf("%d\n", ans);
						worked = 1; break;
					}
					if (tx < 0 || tx >= L || ty < 0 || ty >= L)continue;
					if (visited[tx][ty])continue;
					else {
						visited[tx][ty] = true;
						Q.push(make_pair(tx, ty));
					}
				}
				if (worked)break;
			}
			if (worked)break;
		}
	}
	return 0;
}