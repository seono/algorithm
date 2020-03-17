#include<iostream>
#include<vector>
#include<queue>
using namespace std;

vector<bool>visited(100001, false);

int main() {
	int N, K;
	queue<int>Q;
	scanf("%d %d", &N, &K);
	Q.push(N);
	visited[N] = true;
	int t = -1;
	while (!Q.empty()) {
		int Qsize = Q.size();
		t++;
		for (int i = 0; i < Qsize; i++) {
			int tmp = Q.front();
			if (tmp == K) { printf("%d", t); return 0; }
			Q.pop();
			if (tmp < 100000 && !visited[tmp + 1]) {
				Q.push(tmp + 1);
				visited[tmp + 1] = true;
			}
			if (tmp > 0 && !visited[tmp - 1]) {
				Q.push(tmp - 1);
				visited[tmp - 1] = true;
			}
			if (tmp * 2 <= 100000 && !visited[tmp * 2]) {
				Q.push(tmp * 2);
				visited[tmp * 2] = true;
			}
		}
	}
	return 0;
}