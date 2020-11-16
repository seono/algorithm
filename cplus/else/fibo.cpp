#include<iostream>
#pragma warning(disable:4996)
#include<vector>
using namespace std;

vector<int> dp;
vector<int> call;
vector<int> n_call;

int fibo(int N) {
	call[N]++;
	if (N == 0)return 0;
	if (N == 1)return 1;
	return fibo(N - 1) + fibo(N - 2);
}

int n_fibo(int N) {
	n_call[N]++;
	if (N == 0) return 0;
	if (N == 1) return 1;
	if (dp[N] != -1) return dp[N];
	dp[N] = n_fibo(N - 1) + n_fibo(N - 2);
	return dp[N];
}

int main() {
	int N=0;
	scanf("%d", &N);
	dp.resize(N + 1, -1);
	call.resize(N + 1,0);
	n_call.resize(N + 1,0);
	if(fibo(N)==n_fibo(N)){
		for (int i = 0; i <= N; i++) {
			printf("fibo(%d) : %d회 호출 n_fibo(%d) : %d회 호출\n", i, call[i], i, n_call[i]);
		}
	}
	return 0;
}