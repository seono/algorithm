#include<iostream>
#include<vector>
using namespace std;
vector<vector<char>>arr(2200, vector<char>(2200,'*'));

void dp(int i, int j, int s) {
	if (s == 0) {
		return;
	}
	else {
		for (int a = 0; a < s; a++) {
			for (int b = 0; b < s; b++) {
				arr[i + s + a][j + s + b] = ' ';
			}
		}
		for (int a = 0; a < 3; a++) {
			for (int b = 0; b < 3; b++) {
				if (a == 1 && b == 1)continue;
				dp(i + s * a, j + s * b, s / 3);
			}
		}
	}
}

int main(){
	int N;
	scanf("%d", &N);
	dp(0, 0, N/3);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%c", arr[i][j]);
		}
		printf("\n");
	}
	return 0;
}