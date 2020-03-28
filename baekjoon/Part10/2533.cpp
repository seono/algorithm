#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
const int INF = 1000000000;

vector<int>arr[1000000], child[1000000];
int dp[1000001][2];
bool visited[1000000];
int n;

void dfs(int curr) {
	visited[curr] = true;
	for (int next : arr[curr]) {
		if (!visited[next]) {
			child[curr].push_back(next);
			dfs(next);
		}
	}
	return;
}

int g(int idx, bool st) {
	int& ret = dp[idx][st];
	if (ret != -1)return ret;
	int notpick = INF, pick = 1;
	for (int next : child[idx])
		pick += g(next, true);
	if (st) {
		notpick = 0;
		for (int next : child[idx])notpick += g(next, false);
	}
	return ret = min(pick, notpick);
}

void trackAns(int idx, bool st) {
	int notpick = INF, pick=1;
	for (int next : child[idx])
		pick += g(next, true);
	if (st) {
		notpick = 0;
		for (int next : child[idx])
			notpick += g(next, false);
	}
	if (pick < notpick) {
		printf("%dth man is EA\n", idx + 1);
		for (int next : child[idx])
			trackAns(next, true);
	}
	else {
		for (int next : child[idx])
			trackAns(next, false);
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n-1; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		u--; v--;
		arr[u].push_back(v);
		arr[v].push_back(u);
	}
	dfs(0);
	memset(dp, -1, sizeof(dp));
	printf("%d", g(0, true));
	return 0;
}