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
		//1����� ������ó�� ���ϸ� ���� �˼��ְ� n����ū��츸 �ڸ���ȴ�
		for (int i = 1; i <= n; i++)cnt = mid / i < n ? cnt + mid / i : cnt + n;
		if (cnt<k){
			l= mid;
		}
		else h = mid;
	}
	printf("%lld", h);
	return 0;
}