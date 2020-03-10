#include<iostream>

using namespace std;

int main() {
	int N, arr[3] = { 1,1,2 };
	scanf("%d", &N);
	for (int i = 3; i <= N % 47244; i++) {
		arr[i % 3] = (arr[(i - 2) % 3] + arr[(i - 1) % 3]) % 15746;
	}
	printf("%d", arr[N % 3]);
	return 0;
}