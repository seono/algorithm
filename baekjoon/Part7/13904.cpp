#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int N;
	scanf("%d", &N);
	int arr[1001] = { 0, };
	vector<pair<int,int>>v(N);
	for (int i = 0; i < N; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		v[i].first = b;
		v[i].second = a;
	}
	sort(v.begin(), v.end());
	int ans = 0;
	for (int i = N-1; i >= 0; i--) {
		for (int j = v[i].second; j > 0; j--) {
			if (arr[j-1] == 0 ) {
				ans += v[i].first;
				arr[j-1] = v[i].first;
				break;
			}
		}
	}
	printf("%d", ans);
	return 0;
}