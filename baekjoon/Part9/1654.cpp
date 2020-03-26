#include<iostream>
using namespace std;
#define MAXN 2147483648


int main() {
	int k, n;
	scanf("%d %d", &k, &n);
	long long* arr = new long long[k];
	for (int i = 0; i < k; i++)scanf("%lld", arr + i);
	long long h = MAXN;
	long long l = 0;
	while (l + 1 < h) {
		long long mid = (h + l) / 2;
		int cnt = 0;
		for (int i = 0; i < k; i++) {
			long long tmp = arr[i];
			while (true) {
				if (tmp >= mid) {
					tmp -= mid;
					cnt++;
				}
				else {
					break;
				}
			}
		}
		if (cnt < n)h = mid;
		else l = mid;
	}
	printf("%lld", l);
	return 0;
}