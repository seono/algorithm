#include<iostream>
#include<cstring>
#include<vector>
//2 5 5 4 5 6 3 7 6 6
using namespace std;
typedef long long ll;
int arr[6][2] = { 0, };
ll ans = 0;
//합, 자리수, 남은 성냥 개비 수
//성냥 최대한 쓰는 수부터 사용하여 최대한 자리수를 줄이고
//사용한 조합을 변경
//3 7 7 이용하는경우가 4 6 7 이용할 때 보다 더 크다.
//dp사용하는 걸로 변경
void dp(ll hap, int cnt) {
	if (ans > 0)return;
	if (cnt == 0) {
		ans = hap;
	}
	for (int i = 5; i >= 0; i--) {
		if (cnt >= (i + 2)) {
			dp(hap * 10 + arr[i][0], cnt - (i + 2));
		}
	}
}

int main() {
	int N;
	scanf("%d", &N);
	arr[0][0] = 1;
	arr[1][0] = 7;
	arr[2][0] = 4;
	arr[3][0] = 2;
	arr[4][0] = 0;
	arr[5][0] = 8;
	while (N--) {
		int n;
		ans = 0;
		scanf("%d", &n);
		if (n>=2 && n <= 8&&n!=6) {
			printf("%d ", arr[n - 2][0]);
		}
		if (n == 6)printf("6 ");
		if (n == 9)printf("10 ");
		if (n > 9) {
			dp(0, n);
			while (ans) {
				printf("%lld", ans % 10);
				ans = ans / 10;
			}
			printf(" ");
		}
		if(n%2==1){
			printf("7");
			n = n - 3;
		}
		while (n) {
			n = n - 2;
			printf("1");
		}
		printf("\n");
	}
	return 0;
}