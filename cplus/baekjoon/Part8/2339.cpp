#include<iostream>
#include<vector>
using namespace std;

int dp(vector<vector<int>> v, int y, int x, bool stat) {
	//°¡·Î ÄÆ
	int cnt = 0;
	if (stat) {
		bool c = false;
		for (int i = 1; i < y-1; i++) {
			for (int j = 0; j < x; j++) {
				if (v[i][j] == 1) {
					bool p = true;
					for (int a = 0; a < x; a++) {
						if (v[i][a] == 2)p = false;
					}
					if (p) {
						c = true;
						vector<vector<int>>tmp(i, vector<int>(x));
						for (int ti = 0; ti < i; ti++) {
							for (int tj = 0; tj < x; tj++)tmp[ti][tj] = v[ti][tj];
						}
						int t1 = dp(tmp, i, x, false);
						vector<vector<int>>tmp2(y - i - 1, vector<int>(x));
						for (int ti = i + 1, a = 0; ti < y;a++, ti++) {
							for (int tj = 0; tj < x; tj++)tmp2[a][tj] = v[ti][tj];
						}
						int t2 = dp(tmp2, y - i - 1, x, false);
						cnt += t1 * t2;
					}
				}
			}
		}
		if (c)return cnt;
		else {
			int tmp = 0;
			for (int i = 0; i < y; i++) {
				for (int j = 0; j < x; j++)if (v[i][j] == 2)tmp++;
			}
			if (tmp == 0 || tmp > 1)return 0;
			else return 1;
		}
	}
	//¼¼·Î ÄÆ
	else {
		bool c = false;
		for (int i = 0; i < y; i++) {
			for (int j = 1; j < x-1; j++) {
				if (v[i][j] == 1) {
					bool p = true;
					for (int a = 0; a < y; a++) {
						if (v[a][j] == 2)p = false;
					}
					if (p) {
						c = true;
						vector<vector<int>>tmp(y, vector<int>(j));
						for (int ti = 0; ti < y; ti++) {
							for (int tj = 0; tj < j; tj++)tmp[ti][tj] = v[ti][tj];
						}
						int t1 = dp(tmp, y, j, true);
						vector<vector<int>>tmp2(y, vector<int>(x-j-1));
						for (int ti = 0; ti < y; ti++) {
							for (int tj = j+1,a=0; tj < x;a++, tj++)tmp2[ti][a] = v[ti][tj];
						}
						int t2 = dp(tmp2, y, x-j-1, true);
						cnt += t1 * t2;
					}
				}
			}
		}
		if (c)return cnt;
		else {
			int tmp = 0;
			for (int i = 0; i < y; i++) {
				for (int j = 0; j < x; j++)if (v[i][j] == 2)tmp++;
			}
			if (tmp == 0 || tmp > 1)return 0;
			else return 1;
		}
	}
}

int main() {
	int N;
	scanf("%d", &N);
	vector<vector<int>>arr(N, vector<int>(N));
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	int ans = dp(arr, N, N, true) + dp(arr, N, N, false);
	if (ans == 0)printf("-1");
	else printf("%d", ans);
	return 0;
}