#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int N;
vector<int>ans;
int arr[10001];
int dis[10001];
int dp_arr[10001][10];
//cnt ¿ÞÂÊÀ¸·Î ÃÑ µ¹·ÁÁø È½¼ö-> %10ÇØ¾ßÇÔ
int dp(int idx, int cnt) {
	int& ret = dp_arr[idx][cnt];
	if (idx == N)return ret = 0;
	if (ret != -1)return ret;
	int tmp = (arr[idx] + cnt) % 10;
	int l, r;
	if (dis[idx] > tmp) {
		l = dis[idx] - tmp;
		r = 10 - l;
	}
	else {
		r = tmp - dis[idx];
		l = 10 - r;
	}
	ret = min(dp(idx + 1, (cnt + l) % 10) + l, dp(idx + 1, cnt) + r);
	return ret;
}

void backtrackAns(int idx, int cnt) {
	if (idx == N)return;
	int tmp = (arr[idx] + cnt) % 10;
	int l, r;
	if (dis[idx] > tmp) {
		l = dis[idx] - tmp;
		r = 10 - l;
	}
	else {
		r = tmp - dis[idx];
		l = 10 - r;
	}
	if (dp(idx + 1, (cnt + l) % 10) + l < dp(idx + 1, cnt) + r) {
		cout << idx + 1 << " " << l << endl;
		backtrackAns(idx + 1, (l + cnt) % 10);
		return;
	}
	else {
		cout << idx + 1 << " " << -r << endl;
		backtrackAns(idx + 1, cnt);;
		return;
	}
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)scanf("%1d", &arr[i]);
	for (int i = 0; i < N; i++)scanf("%1d", &dis[i]);
	memset(dp_arr, -1, sizeof(dp_arr));
	cout << dp(0, 0) << endl;
	backtrackAns(0, 0);
	return 0;
}