#include<iostream>
typedef long long ll;
#define MOD 10007
using namespace std;
int main() {
	int N;
	ll dp[10];
	scanf("%d", &N);
	for (int i = 0; i < 10; i++)dp[i] = 1;
	for (int t = 2; t <= N; t++) {
		for (int i = 9; i > 0; i--) {
			for (int j = i-1; j > 0; j--) {
				dp[i] += dp[j]%MOD;
			}
			dp[i] += 1;
		}
	}
	ll r = 0;
	for (int i = 0; i < 10; i++) {
		r += dp[i];
		r %= MOD;
	}
	printf("%lld", r);
	return 0;
}