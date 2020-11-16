#include<iostream>
using namespace std;

int K, arr[100001], cnt;
bool visited[100001], finished[100001];

void dfs(int curr) {
	visited[curr] = true;
	int next = arr[curr];
	if (visited[next]) {
		if (!finished[next]) {
			for (int tmp = next; tmp != curr; tmp = arr[tmp])cnt++;
			cnt++;
		}
	}
	else dfs(next);
	finished[curr] = true;
}

int main() {
	int N;
	scanf("%d", &N);
	while (N--) {
		scanf("%d", &K);
		cnt = 0;
		fill(visited, visited + K, 0);
		fill(finished, finished + K, 0);
		for (int i = 0; i < K; i++) {
			scanf("%d", &arr[i]); arr[i]--;
		}
		for (int i = 0; i < K; i++) {
			if (!visited[i])dfs(i);
		}
		printf("%d\n", K - cnt);
	}
	return 0;
}