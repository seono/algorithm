#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	vector<pair<int,int>>v;
	for (int i = 0; i < n; i++) {
		int s, f;
		scanf("%d %d", &s, &f);
		v.push_back(make_pair(f, s));
	}
	sort(v.begin(), v.end());
	int end = v[0].first;
	int ans = 1;
	for (int i = 1; i < n; i++) {
		if (v[i].second >= end) {
			ans++;
			end = v[i].first;
		}
	}
	printf("%d", ans);
	return 0;
}