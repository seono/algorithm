#include<iostream>
#include<cstring>
using namespace std;
int dp[32][32];
char result[32];
int N;
//남은 비트 n 남은 1횟수 m
int bin(int n, int m) {
	int& ret = dp[n][m];
	if (ret != -1)return ret;
	if (m == 0 || n == 0)return ret = 1;

	ret = bin(n - 1, m);
	if (m > 0)ret += bin(n - 1, m - 1);
	return ret;
}
//pivot 이번에 0으로 채우고 다음으로 넘기는 경우가 1로 채우고 넘어가는 경우보다 더
//크므로 pivot=bin(n-1,m)
//k개 앞에 채워야하는데 k가 pivot보다 작으면 이번에 0으로 채우고 
//pivot보다 크면 1로채우고 k-pivot을 다음에 채움
//
void skip(int n, int m, int k, int p) {
	if (n == 0)return;
	if (m == 0) {
		for (int i = 0; i < n; i++)
			result[p + i] = '0';
		return;
	}
	int pivot = bin(n - 1, m);
	if (k < pivot) {
		result[p] = '0';
		skip(n - 1, m, k, p + 1);
	}
	else {
		result[p] = '1';
		skip(n - 1, m, k-pivot, p + 1);
	}
}


int main() {
	int l, i;
	scanf("%d %d %d", &N, &l, &i);
	memset(dp, -1, sizeof(dp));
	skip(N, l, i-1, 0);
	result[N] = '\0';
	cout << result << endl;
	return 0;
}