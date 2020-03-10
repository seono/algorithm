#include<iostream>
typedef long long ll;
#define MOD 1000000000
using namespace std;
int main() {
	int N;
	ll dp[2][10];
	scanf("%d", &N);
	for (int i = 0; i < 10; i++)dp[0][i] = 1;
	dp[0][0] = 0;
	for (int t = 2; t <= N; t++) {
		for (int i = 0; i < 10; i++) {
			ll l = 0;
			ll r = 0;
			if (i > 0)l = dp[t % 2][i - 1] % MOD;
			if (i < 9)r = dp[t % 2][i + 1] % MOD;
			dp[(t + 1) % 2][i] = (l + r) % MOD;
		}
	}
	ll r = 0;
	for (int i = 0; i < 10; i++) {
		r += dp[(N + 1) % 2][i];
		r %= MOD;
	}
	printf("%lld", r);
	return 0;
}