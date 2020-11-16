#include<iostream>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	int* arr = new int[n];
	int a = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", arr + i);
		if (arr[i] > a)a = arr[i];
	}
	int m; scanf("%d", &m);
	int h = 100000;
	int l = 0;
	while (l + 1 < h) {
		long long sum=0;
		int mid = (l + h) / 2;
		if(mid)
		for (int i = 0; i < n; i++) {
			if (arr[i] <= mid)sum += arr[i];
			else sum += mid;
		}
		if (sum > m)h = mid;
		else l = mid;
	}
	if (l > a)printf("%d", a);
	else printf("%d", l);
	return 0;
}