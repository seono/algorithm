#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int arr[100][100];

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}
	int ans = 0;
	queue<pair<int,int>>Q;
	Q.push(make_pair(0, 0));
	while (!Q.empty()) {
		ans++;
		int qSize = Q.size();
		for (int a = 0; a < qSize; a++) {
			pair<int, int> tmp = Q.front();
			if (tmp.first == N - 1 && tmp.second == M - 1) {
				printf("%d", ans); return 0;
			}
			Q.pop();
			for (int i = 0; i < 4; i++) {
				int x = tmp.first + dx[i];
				int y = tmp.second + dy[i];
				if (x < 0 || x >= N || y < 0 || y >= M)continue;
				if (arr[x][y]) {
					arr[x][y] = 0;
					Q.push(make_pair(x, y));
				}
			}
		}
	}
	return 0;
}