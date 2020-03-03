#include<iostream>
#pragma warning(disable:4996)
#include<algorithm>

const int MAXN = 100001;

using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int a = 1; a <= T; a++) {
		int n;
		scanf("%d", &n);
		int arr[2][MAXN];
		int dp[MAXN][3] = { 0 };
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &arr[i][j]);
			}
		}
		for (int i = 0; i < n; i++) {
			dp[i+1][0] = max(dp[i + 1][0], max(dp[i][0], max(dp[i][1], dp[i][2])));
			dp[i+1][1] = max(dp[i + 1][1], max(dp[i][0], dp[i][2]) + arr[0][i]);
			dp[i+1][2] = max(dp[i + 1][2], max(dp[i][0], dp[i][1]) + arr[1][i]);
		}
		printf("%d\n", max(dp[n][0],max(dp[n][1],dp[n][2])));
	}
	return 0;
}