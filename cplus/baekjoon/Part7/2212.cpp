#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int N, K;
	scanf("%d %d", &N, &K);
	vector<int>v;
	vector<int>dis;
	for (int i = 0; i < N; i++) {
		int n;
		scanf("%d", &n);
		v.push_back(n);
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < N-1; i++) {
		int a = v[i];
		int b = v[i + 1];
		if (a == b)continue;
		else {
			dis.push_back(b - a);
		}
	}
	sort(dis.begin(), dis.end());
	int ans = 0;
	for (int i = 0; dis.size()+1>=K&& i < dis.size() - K + 1; i++) {
		ans += dis[i];
	}
	cout << ans;
	return 0;
}