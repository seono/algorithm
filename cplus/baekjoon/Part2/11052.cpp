#include<iostream>
using namespace std;
int dp[1001], arr[1001];

int Bigger(int A, int B) { if (A > B)return A; return B; }

int main() {
	int N,r=0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &arr[i]);
	}
	dp[0] = arr[0] = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i] = Bigger(dp[i], dp[i - j] + arr[j]);
		}
	}
	printf("%d", dp[N]);
	return 0;
}