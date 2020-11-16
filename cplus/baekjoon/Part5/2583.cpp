#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
using namespace std;

int arr[102][102] = { {0,}, };
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int cnt = 0;

int main() {
	int M, N, K;
	int comp;
	stack<pair<int, int>> S;
	scanf("%d %d %d", &M, &N, &K);
	vector<int> ans;
	for (int i = 0; i < K; i++) {
		int x1, x2, y1, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int y = y1; y < y2; y++) {
			for (int x = x1; x < x2; x++) {
				arr[y][x] = 1;
			}
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j] == 0) {
				comp = 1;
				cnt++;
				S.push(make_pair(i, j));
				arr[i][j] = 1;
				while (S.size() > 0) {
					pair<int, int>tmp;
					tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= M ||
							tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr[tmp.first + dx[a]][tmp.second + dy[a]] == 0) {
							arr[tmp.first + dx[a]][tmp.second + dy[a]] = 1;
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							comp++;
						}
					}
				}
				ans.push_back(comp);
			}
		}
	}
	printf("%d\n", cnt);
	sort(ans.begin(), ans.end());
	for (int i = 0; i < cnt; i++) {
		printf("%d ", ans[i]);
	}
}