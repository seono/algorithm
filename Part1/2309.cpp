#include<iostream>
#pragma warning(disable:4996)
#include<vector>
#include<cstdlib>

int compare(const void* a, const void* b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 > num2)return 1;
	if (num1 < num2)return -1;
	return 0;
}
using namespace std;
int main() {
	int N=0;
	int arr[9];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
		N += arr[i];
	}
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (N - arr[i] - arr[j] == 100) {
				arr[i]=999;
				arr[j]=998;
				break;
			}
		}
		if (arr[i] == 999)break;
	}
	qsort(arr, 9, sizeof(int), compare);
	for (int i = 0; i < 7; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}