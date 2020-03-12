#include<iostream>
#include<stack>
using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	int A;
	stack<pair<int,int>> S;
	scanf("%d", &A);
	while (A--) {
		int N, M, K;
		int arr[52][52] = { {0,}, };
		int ans = 0;
		scanf("%d %d %d", &N, &M, &K);
		while (K--) {
			int n, m;
			scanf("%d %d", &n, &m);
			arr[n+1][m+1] = 1;
		}
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				if (arr[i][j]==1) {
					ans++;
					S.push(make_pair(i, j));
					while (S.size() > 0) {
						//cout << S.size() << endl;
						pair<int, int> tmp = S.top();
						S.pop();
						for (int a = 0; a < 4; a++) {
							if (arr[tmp.first + dx[a]][tmp.second + dy[a]]==1) {
								arr[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
								S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							}
						}
					}
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}