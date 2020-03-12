#include<iostream>
#include<vector>
#include<stack>
using namespace std;
int N;
int arr[100][100];
bool visited[100];
stack<int> S;

int check(int st, int to) {
	fill(visited, visited + 100, false);
	while (S.size() > 0)S.pop();
	for (int i = 0; i < N; i++) {
		if (arr[st][i] == 1) {
			if (i == to)return 1;
			S.push(i);
			visited[i] = true;
		}
	}
	while (S.size() > 0) {
		int tmp = S.top();
		S.pop();
		for (int j = 0; j < N; j++) {
			if (arr[tmp][j] == 1) {
				if (j == to)return 1;
				if (!visited[j])S.push(j);
				visited[j] = true;
			}
		}
	}
	return 0;
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%d ", check(i, j));
		}
		printf("\n");
	}
	return 0;
}