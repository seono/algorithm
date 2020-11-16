#include<iostream>

using namespace std;
#define MOD 10007;
int main() {
	int dp[1001][1001];
	int N, K;
	scanf("%d %d", &N, &K);
	dp[0][0] = 0;
	dp[1][0] = 1, dp[1][1] = 1;
	for (int n = 2; n <= N; n++) {
		dp[n][n] = 1;
		dp[n][0] = 1;
		for (int k = 1; k < n; k++) {
			dp[n][k] = (dp[n - 1][k] + dp[n - 1][k - 1])%MOD;
		}
	}
	printf("%d", dp[N][K]);
	return 0;
}