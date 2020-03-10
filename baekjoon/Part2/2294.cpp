#include<iostream>
#pragma warning(disable:4996)
using namespace std;
#include<algorithm>
const int MAX_N = 103;
const int MAX_K = 10003;
const int IMPOSSIBLE = 10000000;


int main() {
	int N, K, arr[MAX_N] = { 0, }, dp[MAX_N][MAX_K];
	scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++) {
		scanf("%d", arr+i);
	}
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= K; j++)
			dp[i][j] = IMPOSSIBLE;
	}
	for (int i = 0; i <= N; i++) {
		dp[i][0] = 0;
		for (int j = 0; j <= K; j++) {
			dp[i + 1][j] = min(dp[i + 1][j], dp[i][j]);
			int jj = j + arr[i];
			if (jj <= K)dp[i][jj] = min(dp[i][jj], dp[i][j] + 1);
		}
	}
	if (dp[N-1][K] == IMPOSSIBLE)puts("-1");
	else printf("%d\n", dp[N-1][K]);
	return 0;
}