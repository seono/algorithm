#include<iostream>
#include<queue>
#include<vector>
using namespace std;

vector<bool>visited(100001, false);

int f(int n) {
	int t = 1;
	while (n / t>=10) {
		t *= 10;
	}
	return (n / t - 1) * t + n % t;
}

int main() {
	int N, T, G;
	scanf("%d %d %d", &N, &T, &G);
	if (N > G) {
		printf("ANG"); return 0;
	}
	queue<int> Q;
	Q.push(N);
	visited[N] = true;
	int ans = -1;
	while (!Q.empty()) {
		ans++;
		int Qsize = Q.size();
		if (ans > T) {
			printf("ANG"); return 0;
		}
		for (int i = 0; i < Qsize; i++) {
			int tmp = Q.front();
			int temp = f(tmp * 2);
			Q.pop();
			if (tmp == G) {
				printf("%d\n", ans); return 0;
			}
			if (tmp + 1 < 100000 && !visited[tmp+1]) {
				Q.push(tmp + 1);
				visited[tmp + 1] = true;
			}
			if (tmp!=0&&tmp * 2 < 100000 && !visited[temp]) {
				Q.push(temp);
				visited[temp] = true;
			}
		}
	}
}