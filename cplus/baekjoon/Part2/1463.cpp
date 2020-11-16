#include<iostream>
#pragma warning(disable:4996)
#include<algorithm>
const int MAX = 10001;
using namespace std;
int main(){
	int N, dp[MAX];

	scanf("%d", &N);

	fill(dp, dp + MAX,10000);
	dp[1] = 0;
	for (int i = 1; i < N; i++) {
		dp[i + 1] = min(dp[i] + 1, dp[i + 1]);
		if (i*2<MAX)dp[i * 2] = min(dp[i] + 1,dp[i*2]);
		if (i*3<MAX)dp[i * 3] = min(dp[i] + 1,dp[i*3]);
	}
	printf("%d", dp[N]);
	return 0;
}