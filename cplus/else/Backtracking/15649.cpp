#include<iostream>
#pragma warning(disable:4996)
#include<vector>

using namespace std;
vector<int> arr;
vector<int> usi(1000,0);
void backtr(int M, int N) {
	if (arr.size() == N) {
		for (int i = 0; i < N; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 1; i <= M; i++) {
		if (usi[i] == 1)continue;
		arr.push_back(i);
		usi[i] = 1;
		backtr(M, N);
		arr.pop_back();
		usi[i] = 0;
	}
	return;
}

int main() {
	int M, N;
	scanf("%d %d", &M, &N);
	backtr(M, N);
	return 0;
}