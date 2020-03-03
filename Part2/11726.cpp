#include<iostream>

#define MOD 10007

using namespace std;

int main() {
	int N, arr[3] = { 1,1,2 };
	scanf("%d", &N);
	for (int i = 3; i <= N ; i++) {
		arr[i % 3] = (arr[(i - 2) % 3] + arr[(i - 1) % 3]) % MOD;
	}
	printf("%d", arr[N % 3]);
	return 0;
}