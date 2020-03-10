#include<iostream>
using namespace std;

int arr[300000];
long long cnt[21];

int main() {
	int n, k;
	long long ans = 0;
	string str;

	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> k;

	//각 이름을 길이로 바꾸어 저장
	for (int i = 0; i < n; ++i) {
		cin >> str;

		arr[i] = str.length();
	}
	//k값까지 cnt에 카운트
	for (int i = 0; i < k; ++i)
		cnt[arr[i]]++;
	//이후 k번째부터 n까지
	for (int i = 0; i < n; ++i) {
		if (i + k < n)
			cnt[arr[i + k]]++;
		//k등 체크->k+i등
		cnt[arr[i]]--;
		//1등 디스카운트->i등
		ans += cnt[arr[i]];
		//총 개수에 합산
	}

	cout << ans;

	return 0;
}