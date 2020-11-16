#include<iostream>
#include<algorithm>
using namespace std;
const int INF = 10000000;

int N;
int arr[1000][3], dp[1001][4];

int RGB(int pos, int prev = 3) {
	int& ret = dp[pos][prev];
	if (ret != -1)return ret;
	if (pos == N)return ret = 0;
	ret = INF;
	for (int i = 0; i < 3; i++) {
		if (prev != i)ret = min(ret, RGB(pos + 1, i) + arr[pos][i]);
	}
	return ret;
}

void trackAns(int pos, int prev = 3) {
	if (pos == N)return;
	
	for (int i = 0; i < 3; i++) {
		if (prev != i && RGB(pos + 1, i) + arr[pos][i] == RGB(pos, prev)) {
			printf("%dth town color: %d\n", pos + 1, i);
			trackAns(pos + 1, i);
			return;
		}
	}
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++)scanf("%d", &arr[i][j]);
	}
	memset(dp, -1, sizeof(dp));
	printf("min cost: %d\n", RGB(0));
	//trackAns(0);
	return 0;
}