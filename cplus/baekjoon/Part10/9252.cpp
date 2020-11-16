#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;


string ar1;
string ar2;

int arr_dp[1001][1001];

//idx는 현재 ar1의 위치, st는 이전 ar2에 대조된 위치다음
int dp(int idx, int st) {
	int& ret = arr_dp[idx][st];
	if (idx == ar1.length())return ret = 0;
	if (st == ar2.length())return ret = 0;
	if (ret != -1)return ret;
	ret = dp(idx + 1, st);
	for (int i = st; i < ar2.length(); i++) {
		if (ar2[i] == ar1[idx]) {
			ret = max(dp(idx + 1, i+1) + 1, ret);
		}
	}
	return ret;
}

void backtrackans(int idx, int st) {
	if (idx == ar1.length() || st == ar2.length())return;
	for (int i = st; i < ar2.length(); i++) {
		if (ar2[i] == ar1[idx] && dp(idx + 1, i+1) + 1 > dp(idx + 1, st)) {
			cout << ar1[idx];
			backtrackans(idx + 1, i+1);
			return;
		}
	}
	backtrackans(idx + 1, st);
	return;
}

int main() {
	cin >> ar1;
	cin >> ar2;
	memset(arr_dp, -1, sizeof(arr_dp));
	int ans = dp(0, 0);
	if (ans == 0) cout << 0;
	else {
		cout << ans << endl;
		backtrackans(0, 0);
	}
	return 0;
}