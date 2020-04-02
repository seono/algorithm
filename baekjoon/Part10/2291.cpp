#include<iostream>
#include<cstring>
#include<vector>
using namespace std;
typedef long long ll;
int n, m;
ll k;
ll dp_arr[12][231];

vector<int>ans;

ll dp(int idx, int hap, int st) {
	ll& ret = dp_arr[idx][hap];
	if (idx > n || hap > m)return ret = 0;
	if (ret != 0)return ret;
	if (idx == n && hap == m) {
		return ret = 1;
	}
	for (int i = st; i <= m - hap; i++) {
		ret += dp(idx + 1, hap + i, i);
	}
	return ret;
}

void backtrackAns(int idx, int hap, int st) {
	if (idx > n || hap > m)return;
	for (int i = st; i <= m - hap; i++) {
		ll tmp = dp(idx + 1, hap + i, i);
		if (k > tmp) {
			k -= tmp;
		}
		else {
			ans.push_back(i);
			backtrackAns(idx + 1, hap + i, i);
			return;
		}
	}
	return;
}

int main() {
	scanf("%d %d %lld", &n, &m, &k);
	memset(dp_arr, 0, sizeof(dp_arr));
	backtrackAns(0, 0, 1);
	if (ans.size()) {
		for (int i = 0; i < n - 1; i++)printf("%d ", ans[i]);
		printf("%d", ans[n - 1]);
	}
	return 0;
}