#include<iostream>
#include<vector>
#include<cstring>
#include<queue>
#include<algorithm>
using namespace std;
struct NODE {
	int next;
	int cycle = 0;
	int cycleCnt = 0;
	int varCnt = 0;
};
bool visited[1001];
bool chked[1001];
vector<pair<int, int>> comp;
// cycle크기, cycle크기포함 최대 component
int k, n;
int dp[1001][1001];
NODE node[1001];
queue<int> Q;

int dfs(int idx) {
	visited[idx] = true;
	int next = node[idx].next;
	int cycle = 0;
	if (!chked[next]) {
		if (visited[next]) {
			int cnt = 1;
			node[idx].cycle = idx;
			while (next != idx) {
				cnt++;
				node[next].cycle = idx;
				next = node[next].next;
			}
			node[idx].cycleCnt = cnt;
			node[idx].varCnt = -cnt;
			Q.push(idx);
			cycle = idx;
		}
		else cycle = dfs(next);
	}
	else {
		cycle = node[next].cycle;
	}
	chked[idx] = true;
	node[idx].cycle = cycle;
	node[cycle].varCnt++;
	return cycle;
}

int main() {
	int w, v;
	int ans = 0;
	scanf("%d %d", &k, &n);
	for (int i = 1; i <= k; i++) {
		scanf("%d", &node[i].next);
	}
	for (int i = 1; i <= k; i++) {
		if (chked[i])continue;
		dfs(i);
	}
	int c = 0;
	while (!Q.empty()) {
		c = Q.front(); Q.pop();
		if (node[c].cycleCnt > n)continue;
		comp.push_back(make_pair(node[c].cycleCnt, node[c].varCnt));
	}
	comp.push_back(make_pair(0, 0));
	sort(comp.begin(), comp.end());
	int l_size = comp.size();
	memset(dp, -1, sizeof(dp));
	//dp[i][cycle]에 가변값 저장
	//dp[i][j]는 j가 cycle보다 작을땐 dp[i-1]에서 가져옴
	//j가 cycle보다 크거나 같을땐 dp[i-1][j-w]가 있다면 그 값에 가변값 더한것과 dp[i-1][j]중 큰값
	//없다면 그냥 i-1에서 가져옴
	for (int i = 1; i < l_size; i++) {
		w = comp[i].first;
		v = comp[i].second;
		dp[i][w] = v;
		for (int j = 1; j <= n; j++) {
			if (j > w) {
				if (dp[i - 1][j - w] >= 0) {
					dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j]);
				}
				else {
					dp[i][j] = max(dp[i][j], dp[i - 1][j]);
				}
			}
			else {
				dp[i][j] = max(dp[i][j], dp[i - 1][j]);
			}
		}
	}
	//dp i = n까지 검사
	//dp값이 존재하고 i->cycle dp값은 가변값
	/*cout << endl;
	for (int i = 0; i < l_size; i++) {
		for (int j = 0; j <= n; j++) {
			cout << dp[i][j] << " ";
		}
		cout << endl;
	}*/
	for (int i = 1; i <= n; i++) {
		if (dp[l_size - 1][i] >= 0) {
			ans = max(ans, i + dp[l_size - 1][i]);
		}
	}
	//ans가 n이상이되었다는것은-> cycle은 n이전까지만 검사했고 가변값을 더한것이므로
	//n이하의값부터 ans까지 모든 경우의 수가 가능하다는것
	if (ans > n)printf("%d\n", n);
	//ans가 n 이하라면 그것이 최대
	else printf("%d\n", ans);
	return 0;
}