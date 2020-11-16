#include<iostream>

using namespace std;


int main() {
	int N;
	long long dp[99][2];
	dp[1][0] = 1;
	dp[1][1] = 1;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j < 2; j++) {
			dp[i + 1][0] = dp[i][0] + dp[i][1];
			dp[i + 1][1] = dp[i][0];
		}
	}
	printf("%lld", dp[N][1]);
	return 0;
}