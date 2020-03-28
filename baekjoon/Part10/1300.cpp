#include<iostream>
using namespace std;


int main() {
	int	n, k;
	scanf("%d %d", &n, &k);
	long long h = k;
	long long l = 0;
	while (l + 1 < h) {
		long long mid = (l + h) / 2;
		long long cnt = 0;
		//1행부터 구구단처럼 셈하면 갯수 알수있고 n보다큰경우만 자르면된다
		for (int i = 1; i <= n; i++)cnt = mid / i < n ? cnt + mid / i : cnt + n;
		if (cnt<k){
			l= mid;
		}
		else h = mid;
	}
	printf("%lld", h);
	return 0;
}