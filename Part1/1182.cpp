#include<iostream>
#pragma warning(disable:4996)

using namespace std;
int N, M;
int cnt = 0;
int arr[23];
void dfs(int i, int sum) {
	if (arr[i] + sum == M)cnt++;
	if (i == N - 1)return;

	dfs(i + 1, sum);
	dfs(i + 1, sum + arr[i]);
}

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	dfs(0, 0);
	printf("%d", cnt);
	return 0;
}