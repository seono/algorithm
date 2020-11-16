#include<iostream>
#include<cstring>
//2 5 5 4 5 6 3 7 6 6
using namespace std;
int dp_arr[101][53];
int num;
int arr[6][2] = { {0,6},{1,2},{2,5},{4,4},{7,3},{8,7} };
int arr2[6][2] = { {1,2},{2,5},{4,4},{6,6},{7,3},{8,7} };
//n개 성냥개비, k자리 수
int match(int n,int k) {
	int& ret = dp_arr[n][k];
	if (ret != -1)return ret;
	if (n == 0 && k == 0) return ret = 1;
	if (k == 0 || n == 0) return ret = 0;
	for (int i = 2; i< 8; i++) {
		if (n - i < 0)continue;
		ret = match(n - i, k - 1);
		if (ret>0)return ret;
	}
	return ret;
}

void backtrackAns(int n, int k, bool firstPos) {
	if (n==0||k == 0)return;
	if (firstPos) {
		for (int i = 0; i < 6; i++) {
			if (n - arr2[i][1] < 0)continue;
			if (match(n - arr2[i][1], k - 1)>0) {
				printf("%d", arr2[i][0]);
				backtrackAns(n - arr2[i][1], k - 1, false);
				return;
			}
		}
	}
	else {
		for (int i = 0; i < 6; i++) {
			if (n - arr[i][1] < 0)continue;
			if (match(n - arr[i][1], k - 1) > 0) {
				printf("%d", arr[i][0]);
				backtrackAns(n - arr[i][1], k - 1, false);
				return;
			}
		}
	}
}

int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		int n;
		scanf("%d", &n);
		int idx;
		memset(dp_arr, -1, sizeof(dp_arr));
		for (idx = 1; idx < 53; idx++)if (match(n, idx))break;
		backtrackAns(n, idx, true);
		printf(" ");
		if(n%2==1){
			printf("7");
			n = n - 3;
		}
		while (n) {
			n = n - 2;
			printf("1");
		}
		printf("\n");
	}
	return 0;
}