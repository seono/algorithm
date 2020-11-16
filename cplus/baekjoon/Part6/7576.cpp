#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int arr[1000][1000];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	int N, M;
	queue<pair<int, int>>Q;
	scanf("%d %d", &N, &M);
	int A = N * M;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] == 1)Q.push(make_pair(i, j));
			else if (arr[i][j] == -1)A--;
		}
	}
	int ans = -1;
	int one = Q.size();
	while (!Q.empty()) {
		ans++;
		int Qsize = Q.size();
		for (int i = 0; i < Qsize; i++) {
			pair<int, int>tmp = Q.front();
			Q.pop();
			for (int a = 0; a < 4; a++) {
				int tx = tmp.first + dx[a];
				int ty = tmp.second + dy[a];
				if (tx < 0 || tx >= M || ty < 0 || ty >= N)continue;
				if (arr[tx][ty] == 0) {
					arr[tx][ty] = 1;
					one++;
					Q.push(make_pair(tx, ty));
				}
			}
		}
	}
	if (one == A)printf("%d\n", ans);
	else printf("-1\n");
	return 0;
}