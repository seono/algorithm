#include<iostream>
using namespace std;

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	int* arr = new int[n];
	for (int i = 0; i < n; i++)scanf("%d", arr + i);
	int h = 1000000000;
	int l = 0;
	while (l + 1 < h) {
		int mid = (l + h) / 2;
		int tmp = mid;
		int cnt = 1;
		for (int i = 0; i < n; i++) {
			if (arr[i] > mid) {
				l = mid;
				break;
			}
			if (arr[i] > tmp) {
				tmp = mid;
				cnt++;
			}
			tmp -= arr[i];
		}
		if (l == mid) {
			continue;
		}
		if (cnt > m)l = mid;
		else h = mid;
	}
	printf("%d", h);
	return 0;
}