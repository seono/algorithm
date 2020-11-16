#include<iostream>
using namespace std;
typedef long long ll;
int r, c;
ll num=0;

ll pow(int n) {
	ll tmp = 1;
	while (n--)tmp *= 2;
	return tmp;
}

void dp(ll i, ll j, ll N) {
	if (i == r && j == c) {
		printf("%lld", num);
		return;
	}
	else {
		if (r < i + N / 2 ) {
			if (c < j + N / 2) {
				dp(i, j, N / 2);
			}
			else {
				num += N*N/4;
				dp(i, j + N / 2, N / 2);
			}
		}
		else {
			if (c < j + N / 2) {
				num += N*N/2;
				dp(i + N / 2, j, N / 2);
			}
			else {
				num += N*N/4* 3;
				dp(i + N / 2, j + N / 2, N / 2);
			}
		}
	}
}

int main() {
	int N;
	scanf("%d %d %d", &N, &r, &c);
	ll tmp = pow(N);
	dp(0, 0, tmp);
	return 0;
}