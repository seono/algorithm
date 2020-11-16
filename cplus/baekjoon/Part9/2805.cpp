#include<iostream>
using namespace std;

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	int* arr = new int[N];
	for (int i = 0; i < N; i++)scanf("%d", arr + i);
	int h = 1000000000;
	int l = 0;
	while (l + 1 < h) {
		int mid = (l + h) / 2;
		long long sum = 0;
		for (int i = 0; i < N; i++) {
			if (arr[i] > mid)sum += arr[i] - mid;
		}
		if (sum >= M)l = mid;
		else h = mid;
	}
	printf("%d", l);
	return 0;
}