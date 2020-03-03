#include<iostream>
#pragma warning(disable:4996)

using namespace std;

// B 66 W 87
int arr[50][50] = { {0,}, };
int test_arr1[8][8], test_arr2[8][8];

int m = 100;
int N, M;
void check(int i, int j) {
	int temp_min = 0;
	for (int a = 0; a < 8; a++) {
		for (int b = 0; b <  8; b++) {
			if (arr[i + a][j + b] != test_arr1[a][b])temp_min++;
		}
	}
	if (temp_min > 32)temp_min = 64 - temp_min;
	if (m > temp_min)m = temp_min;
}
int main() {
	scanf("%d %d", &N, &M);
	int temp = 1;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (temp % 2 == 0) {
				test_arr1[i][j] = 87;
				test_arr2[i][j] = 66;
			}
			else {
				test_arr1[i][j] = 66;
				test_arr2[i][j] = 87;
			}
			temp++;
		}
		temp--;
	}
	getchar();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			char c;
			scanf("%c", &c);
			arr[i][j] = c;
		}
		getchar();
	}
	for (int i = 0; i < N-7; i++) {
		for (int j = 0; j < M-7; j++) {
			check(i, j);
		}
	}
	printf("%d", m);
	return 0;
}