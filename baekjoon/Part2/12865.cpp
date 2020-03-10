#pragma GCC optimize("O3")
#pragma GCC target("arch=skylake")
#include <cstdio>

int main() {
	int d[100001] = {};
	int N, K, W, V, i;
	scanf("%d %d", &N, &K);
	while (N--) {
		scanf("%d %d", &W, &V);
		for (i = K; i >= W; i--)if (d[i] < d[i - W] + V)d[i] = d[i - W] + V;
	}
	printf("%d", d[K]);
	return 0;
}