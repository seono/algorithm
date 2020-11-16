#include<iostream>
#include<stack>
using namespace std;

stack<pair<int,int>> S;
int N;
int cnt = 0;
int m = 0;
int arr[100][100];
bool visited[100][100];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

void dfs(int h) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)visited[i][j] = false;
	}
	cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j])continue;
			visited[i][j] = true;
			if (arr[i][j] > h) {
				cnt++;
				S.push(make_pair(i, j));
				while (S.size() > 0) {
					pair<int, int>tmp = S.top();
					S.pop();
					for (int a = 0; a < 4; a++) {
						if (tmp.first + dx[a] < 0 || tmp.first + dx[a] >= N ||
							tmp.second + dy[a] < 0 || tmp.second + dy[a] >= N)continue;
						if (!visited[tmp.first+dx[a]][tmp.second+dy[a]]
							&&arr[tmp.first + dx[a]][tmp.second + dy[a]] > h) {
							S.push(make_pair(tmp.first + dx[a], tmp.second + dy[a]));
							visited[tmp.first + dx[a]][tmp.second + dy[a]] = true;
						}
					}
				}
			}
		}
	}
	if (cnt > m)m = cnt;
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	for (int a = 1; a <= 100; a++)dfs(a);
	printf("%d", m);
	return 0;
}