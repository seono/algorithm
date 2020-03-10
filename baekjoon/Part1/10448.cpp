#include<iostream>
#pragma warning(disable:4996)

using namespace std;
int arr[50];
int num = 0;

int findidx(int t_num) {
	int t = 0;
	while (arr[t] < t_num)t++;
	return t;
}
void check(int t_num) {
	int idx = findidx(t_num);
	for (int i = 0; i < idx; i++) {
		for (int j = 0; j < idx; j++) {
			for (int k = 0; k < idx; k++) {
				if (arr[i] + arr[j] + arr[k] == t_num) {
					printf("1\n"); return;
				}
			}
		}
	}
	printf("0\n");
	return;
}
void pac(int pac_num) {
	if (pac_num == 0) {
		num++;
		return;
	}
	else {
		arr[num] += pac_num--;
		pac(pac_num);
	}
}
int main() {
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= 50; i++) {
		pac(i);
	}
	for (int i = 0; i < N; i++) {
		int t_num;
		scanf("%d", &t_num);
		check(t_num);
	}
	return 0;
}