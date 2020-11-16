#include<iostream>
#include<stack>
using namespace std;

char arr[100][100] = { {0,}, };
char arr2[100][100] = { {0,}, };
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	int N, cnt=0;
	scanf("%d", &N);
	getchar();
	stack<pair<int, int>>S;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%c", &arr[i][j]);
			arr2[i][j] = arr[i][j];
		}
		getchar();
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j] == 'R') {
				S.push(make_pair(i, j));
				cnt++;
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N || tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr[tmp.first + dx[a]][tmp.second + dy[a]] == 'R') {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							arr[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
						}
					}
				}
			}
			else if (arr[i][j] == 'G') {
				S.push(make_pair(i, j));
				cnt++;
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N || tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr[tmp.first + dx[a]][tmp.second + dy[a]] == 'G') {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							arr[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
						}
					}
				}
			}
			else if (arr[i][j] == 'B') {
				S.push(make_pair(i, j));
				cnt++;
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N || tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr[tmp.first + dx[a]][tmp.second + dy[a]] == 'B') {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							arr[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
						}
					}
				}
			}
		}
	}
	printf("%d ", cnt);
	cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr2[i][j] == 'R'||arr2[i][j]=='G') {
				S.push(make_pair(i, j));
				cnt++;
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N || tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr2[tmp.first + dx[a]][tmp.second + dy[a]] == 'R'|| arr2[tmp.first + dx[a]][tmp.second + dy[a]] == 'G') {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							arr2[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
						}
					}
				}
			}
			else if (arr2[i][j] == 'B') {
				S.push(make_pair(i, j));
				cnt++;
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N || tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (arr2[tmp.first + dx[a]][tmp.second + dy[a]] == 'B') {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							arr2[tmp.first + dx[a]][tmp.second + dy[a]] = 0;
						}
					}
				}
			}
		}
	}
	printf("%d\n", cnt);
	return 0;
}