#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;

int n;
vector<int>arr;
vector<int>v[10001];
vector<int>child[10001];
vector<int>ans;
int dp_arr[10001][2];
bool back[10001];
//st==true->현재정점선택가능
int dp(int idx, bool st) {
	int& ret = dp_arr[idx][st];
	if (ret != -1)return ret;
	int tmp=0;
	for (int next : child[idx]) {
		tmp += dp(next, true);
	}
	ret = tmp;
	if (st) {
		int tmp2=arr[idx];
		for (int next : child[idx]) {
			tmp2 += dp(next, false);
		}
		ret = max(ret, tmp2);
	}
	return ret;
}

void backtrackAns(int idx, bool st) {
	back[idx] = true;
	if (idx == n)return;
	int tmp = 0;
	for (int next : child[idx]) {
		tmp += dp(next, true);
	}
	int tmp2 = 0;
	if (st) {
		tmp2 = arr[idx];
		for (int next : child[idx]) {
			tmp2 += dp(next, false);
		}
	}
	if (tmp2 > tmp) {
		ans.push_back(idx + 1);
		for (int next : child[idx]) {
			if (!back[next]) {
				backtrackAns(next, false);
			}
		}
	}
	else {
		for (int next : child[idx]) {
			if (!back[next]) {
				backtrackAns(next, true);
			}
		}
	}
	return;
}
void dfs(int idx) {
	back[idx] = true;
	for (int next : v[idx]) {
		if (!back[next]) {
			child[idx].push_back(next);
			dfs(next);
		}
	}
}
int main() {
	cin >> n;
	arr.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < n-1; i++) {
		int edge1, edge2;
		cin >> edge1 >> edge2;
		edge1--; edge2--;
		v[edge1].push_back(edge2);
		v[edge2].push_back(edge1);
	}
	memset(dp_arr, -1, sizeof(dp_arr));
	dfs(0);
	cout << dp(0, true) << endl;
	memset(back, false, sizeof(back));
	backtrackAns(0, true);
	sort(ans.begin(), ans.end());
	for (int i = 0; i < ans.size(); i++)cout << ans[i] << " ";
	return 0;
}