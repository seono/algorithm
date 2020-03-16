#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

vector<vector<char>>arr(50, vector<char>(50));

int main() {
	int R, C;
	queue<pair<int, int>>Q;
	queue<pair<int, int>>W;
	scanf("%d %d", &R, &C);
	getchar();
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			scanf("%c", &arr[i][j]);
			if (arr[i][j] == 'S') {
				Q.push(make_pair(i, j));
			}
			else if (arr[i][j] == '*') {
				W.push(make_pair(i, j));
			}
		}
		getchar();
	}
	int ans = 0;
	while (!Q.empty()) {
		int Qsize=Q.size(), Wsize=W.size();
		ans++;
		for (int t = 0; t < Wsize; t++) {
			pair<int, int> tmp = W.front();
			W.pop();
			for (int a = 0; a < 4; a++) {
				int x = tmp.first + dx[a];
				int y = tmp.second + dy[a];
				if (x < 0 || x >= R || y < 0 || y >= C)continue;
				if (arr[x][y] == '.'||arr[x][y]=='S') {
					arr[x][y] = '*';
					W.push(make_pair(x, y));
				}
			}
		}
		for (int t = 0; t < Qsize; t++) {
			pair<int, int>tmp = Q.front();
			Q.pop();
			for (int a = 0; a < 4; a++) {
				int x = tmp.first + dx[a];
				int y = tmp.second + dy[a];
				if (x < 0 || x >= R || y < 0 || y >= C)continue;
				if (arr[x][y] == 'D') {
					printf("%d\n", ans);
					return 0;
				}
				if (arr[x][y] == '.') {
					arr[x][y] = 'S';
					Q.push(make_pair(x, y));
				}
			}
		}
	}
	printf("KAKTUS\n");
	return 0;
}	