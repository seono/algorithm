#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;

int N;
vector<ll> v;
ll func(int st, int en) {
	if (st == en) return v[st] * v[st];
	if (st + 1 == en) {
		ll min_val = v[st] < v[en] ? v[st] : v[en];
		ll min_v = max(v[st] * v[st], v[en] * v[en]);
		min_v =  min_v > (v[en] + v[st])* min_val ? min_v : (v[en] + v[st]) * min_val;
		return min_v;
	}
	int idx = (en + st) / 2;
	//좌우구간중에 큰것
	ll result = max(func(st, idx), func(idx, en));
	int l = idx, r = idx;
	ll m_ans = v[idx] * v[idx];
	ll sum = v[idx];
	ll min_val = v[idx];
	while (r - l < en - st) {
		ll left = l > st ? sum+v[l-1] : -1;
		ll right = r < en? sum+v[r+1] : -1;
		if (left > right) {
			if (v[l - 1] < min_val)min_val = v[l - 1];
			m_ans = max(m_ans, left*min_val);
			sum += v[l - 1];
			l--;
		}
		else {
			if (v[r + 1] < min_val)min_val = v[r + 1];
			m_ans = max(m_ans, right * min_val);
			sum += v[r + 1];
			r++;
		}
	}
	result = max(m_ans, result);
	return result;
}

int main() {
	scanf("%d", &N);
	v.resize(N);
	for (int i = 0; i < N; i++)scanf("%lld", &v[i]);
	printf("%lld", func(0, N - 1));
	return 0;
}