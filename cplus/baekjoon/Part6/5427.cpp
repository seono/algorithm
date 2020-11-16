#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;

int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		int x, y;
		queue<pair<int, int>> F;
		queue<pair<int, int>> Q;
		scanf("%d %d", &x, &y);
		vector<vector<char>>building(y, vector<char>(x));
		getchar();
		for (int i = 0; i < y; i++) {
			for (int j = 0; j < x; j++) {
				scanf("%c", &building[i][j]);
				if (building[i][j] == '@') {
					Q.push(make_pair(j, i));
				}
				else if (building[i][j] == '*') {
					F.push(make_pair(j, i));
				}
			}
			getchar();
		}
		int ans = 0;
		int worked = 0;
		while (!Q.empty()) {
			ans++;
			int Qsize = Q.size();
			int Fsize = F.size();
			for (int t = 0; t < Fsize; t++) {
				pair<int, int>tmp = F.front();
				F.pop();
				for (int a = 0; a < 4; a++) {
					int fx = tmp.first + dx[a];
					int fy = tmp.second + dy[a];
					if (fx < 0 || fx >= x || fy < 0 || fy >= y)continue;
					if (building[fy][fx] == '.'||building[fy][fx]=='@') {
						building[fy][fx] = '#';
						F.push(make_pair(fx, fy));
					}
				}
			}
			for (int t = 0; t < Qsize; t++) {
				pair<int, int>temp = Q.front();
				Q.pop();
				if (temp.first == 0 || temp.first == x - 1 || temp.second == 0 || temp.second == y - 1) {
					while (!Q.empty())Q.pop();
					worked = 1;
					printf("%d\n", ans);
					break;
				}
				for (int a = 0; a < 4; a++) {
					int tx = temp.first + dx[a];
					int ty = temp.second + dy[a];
					if (tx < 0 || tx >= x || ty < 0 || ty >= y)continue;
					if (building[ty][tx] == '.') {
						building[ty][tx] = '#';
						Q.push(make_pair(tx, ty));
					}
				}
			}
			if (worked)break;
		}
		while (!F.empty())F.pop();
		while (!Q.empty())Q.pop();
		if (worked)continue;
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}