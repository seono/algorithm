#include<iostream>
#include<vector>
#include<stack>
using namespace std;
vector<vector<int>>arr(102, vector<int>(102, 0));
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int cnt = 0;
int main() {
	int N, M, K;
	stack<pair<int,int>> S;
	scanf("%d %d %d", &N, &M, &K);
	for (int i = 0; i < K; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		arr[a][b] = 1;
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			if (arr[i][j] == 1) {
				S.push(make_pair(i, j));
				int temp = 1;
				arr[i][j] = 0;
				while (S.size() > 0) {
					pair<int, int>tmp;
					tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (arr[tmp.first + dx[a]][tmp.second + dy[a]] == 1) {
							arr[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a])); temp++;
						}
					}
				}
				if (temp > cnt)cnt = temp;
			}
		}
	}
	printf("%d\n", cnt);
	return 0;
}