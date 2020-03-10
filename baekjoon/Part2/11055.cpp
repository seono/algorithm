#include<iostream>

using namespace std;

int main() {
	int a[1001];
	int dp[1001];
	long m = 0, ans=0;
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &a[i]); dp[i] = 0;
	}
	for (int i = 1; i <= N; i++) {
		m = 0;
		for (int j = 1; j < i; j++) {
			if (a[i] <= a[j])continue;
			if (dp[j] > m)m = dp[j];
		}
		dp[i] = a[i] + m;
		if (dp[i] > ans) ans = dp[i];
	}
	printf("%ld", ans);
	return 0;
}