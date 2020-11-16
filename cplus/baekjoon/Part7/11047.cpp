#include<iostream>
using namespace std;

int main() {
	int N, K;
	int arr[11];
	scanf("%d %d", &N, &K);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &arr[i]);
	}
	int ans = 0;
	while (K != 0) {
		if (arr[N] <= K) {
			int temp = K / arr[N];
			ans += temp;
			K -= temp * arr[N];
		}
		N--;
	}
	printf("%d", ans);
	return 0;
}