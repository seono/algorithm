#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int n, c;
	scanf("%d %d", &n, &c);
	int* arr = new int[n];
	for (int i = 0; i < n; i++)scanf("%d", arr + i);
	sort(arr, arr + n);
	int h = arr[n-1]-arr[0]+1;
	int l = 0;
	while (l + 1 < h) {
		int mid = (h + l) / 2;
		int s = arr[0];
		int cnt = 1;
		for (int i = 1; i < n; i++) {
			if (arr[i] - s >= mid) {
				s = arr[i];
				cnt++;
			}
		}
		if (cnt < c)h = mid;
		else l = mid;
	}
	printf("%d", l);
	return 0;
}