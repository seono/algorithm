#include<iostream>
using namespace std;

#define N_MAX 316

int f(int n) {
	while ((n & 3) == 0)n >>= 2;
	return(n + 1) % 8;
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N_MAX; i++)if (i * i == N) {
		puts("1"); return 0;
	}
	for (int i = 1; i <= N_MAX; i++)for (int j = i; j <= N_MAX; j++)if (i * i + j * j == N) {
		puts("2"); return 0;
	}
	if (f(N))puts("3");
	else puts("4");
	return 0;
}