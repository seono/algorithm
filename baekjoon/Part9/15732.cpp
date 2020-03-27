#include<iostream>
using namespace std;

struct box {
	int st, ed;
	int rule;
};

int main() {
	int N, K, D;
	scanf("%d %d %d", &N, &K, &D);
	box* arr = new box[K];
	for (int i = 0; i < K; i++) {
		scanf("%d %d %d", &arr[i].st, &arr[i].ed, &arr[i].rule);
	}
	int h = 1000001;
	int l = 0;
	while (l + 1 < h) {
		int mid = (h + l) / 2;
		long long cnt = 0;
		for (int i = 0; i < K; i++) {
			if (arr[i].st <= mid) {
				int tmp = mid<=arr[i].ed?mid - arr[i].st:arr[i].ed-arr[i].st;
				cnt += tmp / arr[i].rule + 1;
			}
		}
		if (cnt < D)l = mid;
		else h = mid;
	}
	printf("%d", h);
	return 0;
}