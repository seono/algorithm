#include<iostream>
using namespace std;

int arr[6400][6400];
int mns = 0, zero = 0, one = 0;

void dp(int i, int j, int s) {
	int t = arr[i][j];
	int worked = 0;
	for (int a = 0; a < s; a++) {
		for (int b = 0; b < s; b++) {
			if (arr[i+a][j+b] != t) {
				worked = 1;
				break;
			}
		}
		if (worked)break;
	}
	if (worked) {
		for (int a = 0; a < 3; a++) {
			for (int b = 0; b < 3; b++) {
				dp(i + s / 3 * a, j + s / 3 * b, s / 3);
			}
		}
	}
	else {
		if (t == 0)zero++;
		if (t == 1)one++;
		if (t == -1)mns++;
	}
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	dp(0, 0, N);
	printf("%d\n%d\n%d", mns, zero, one);
	return 0;
}