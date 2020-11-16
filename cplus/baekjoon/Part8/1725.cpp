#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> v(100001);


int dp(int st, int en) {
	if (st == en) return v[st];
	if (st + 1 == en) {
		int r;
		if (v[st] < v[en]) {
			r = v[st] * 2;
			if (v[en] > r)return v[en];
			else return r;
		}
		else {
			r = v[en] * 2;
			if (v[st] > r)return v[st];
			else return r;
		}
	}
	int mid = (st + en) / 2;
	int result = max(dp(st, mid), dp(mid, en));
	int l = mid, r = mid;
	int hap = v[mid];
	int width = 1;
	int min_val = v[mid];
	while (r - l< en - st) {
		int left = l > st ? min(v[l - 1],min_val) : -1;
		int right = r < en  ? min(v[r + 1],min_val) : -1;
		width++;
		if (left > right) {
			min_val = left;
			hap = max(hap, min_val * width);
			l--;
		}
		else {
			min_val = right;
			hap = max(hap, min_val * width);
			r++;
		}
	}
	result = max(hap, result);
	return result;
}

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &v[i]);
	}
	printf("%d", dp(0, N - 1));
	return 0;
}