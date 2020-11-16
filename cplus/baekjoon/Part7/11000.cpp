#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

int main() {
	int N;
	scanf("%d", &N);
	vector<pair<int,int>> v;
	for (int i = 0; i < N; i++) {
		int s, f;
		scanf("%d %d", &s, &f);
		v.push_back(make_pair(s, f));
	}
	sort(v.begin(), v.end());
	multiset<int>T;
	T.insert(v[0].second);
	for (int i = 1; i < N; i++) {
		if(*T.begin()<=v[i].first)T.erase(T.begin());
		T.insert(v[i].second);
	}
	printf("%u", T.size());
	return 0;
}