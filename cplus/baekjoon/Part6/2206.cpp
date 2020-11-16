#include<iostream>
#include<queue>
using namespace std;

int arr[1001][1001];
int cache[1001][1001][2];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

//�� bfsŽ������ ���ؼ� �� ���� Ƚ�� �߰��� ����-> 1�Ѱ��� ��� ����


int main() {
	int N, M;
	vector<int>ans;
	scanf("%d %d",&N,&M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}
	queue<pair<pair<int,int>,int>> Q;
	Q.push(make_pair(make_pair(0,0),1));
	cache[0][0][1] = 1;
	while (!Q.empty()) {
		int x = Q.front().first.first;
		int y = Q.front().first.second;
		int block = Q.front().second;
		Q.pop();

		if (x == N - 1 && y == M - 1) {
			printf("%d", cache[x][y][block]); return 0;
		}
		for (int i = 0; i < 4; i++) {
			int tx = x + dx[i];
			int ty = y + dy[i];
			if (tx < 0 || tx >= N || ty < 0 || ty >= M)continue;
			//���� �ְ� ���ձⰡ �����ִ� ���
			if (arr[tx][ty] == 1 && block) {
				cache[tx][ty][block - 1] = cache[x][y][block] + 1;
				Q.push(make_pair(make_pair(tx, ty), block - 1));
			}
			//���� ���� ó�� �湮�Ͽ��� ��
			else if (arr[tx][ty] == 0 && cache[tx][ty][block] == 0) {
				cache[tx][ty][block] = cache[x][y][block] + 1;
				Q.push(make_pair(make_pair(tx, ty), block));
			}
		}
	}
	printf("-1");
	return 0;
}