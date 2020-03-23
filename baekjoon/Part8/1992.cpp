#include<iostream>
using namespace std;

int arr[64][64];

void dp(int i, int j, int s) {
	int t = arr[i][j];
	int worked = 0;
	for (int a = 0; a < s; a++) {
		for (int b = 0; b < s; b++) {
			if (arr[i + a][j + b] != t) {
				worked = 1;
				break;
			}
		}
		if (worked)break;
	}
	if (worked) {
		printf("(");
		for (int a = 0; a < 2; a++) {
			for (int b = 0; b < 2; b++) {
				dp(i + s / 2 * a, j + s / 2 * b, s / 2);
			}
		}
		printf(")");
	}
	else {
		printf("%d", t);
	}
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}
	dp(0, 0, N);
	return 0;
}