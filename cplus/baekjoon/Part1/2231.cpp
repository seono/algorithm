#include<iostream>
#pragma warning(disable:4996)
#include<algorithm>
using namespace std;

int main(){
	int N;
	scanf("%d", &N);
	int arr[54] = { 0, };
	int num = 0;
	int i = N - 54;
	if (i < 0)i = 0;
	for (; i < N; i++) {
		int temp = i;
		//printf("%d\n", temp);
		temp += temp / 100000 % 10 + temp / 10000 % 10 + temp / 1000 % 10 + temp / 100 % 10 + temp / 10 % 10 + temp % 10;
		//printf("%d\n", temp);
		if (temp == N) {
			arr[num++] = i;
		}
	}
	sort(arr, arr + num);
	printf("%d", arr[0]);
	return 0;
}