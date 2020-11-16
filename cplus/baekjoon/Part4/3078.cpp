#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

vector<vector<int>>v(21, vector<int>(0));

int N, K;

int check(int name, int idx) {
	while (v[name].size() != 0&&idx - v[name][0] > K) {
		v[name].erase(v[name].begin());
	}
	v[name].push_back(idx);
	return v[name].size()-1;
}

int main() {
	long long ans = 0;
	scanf("%d %d", &N, &K);
	int i = 0;
	while(i<N){
		char str[22];
		scanf("%s", &str);
		ans += check(strlen(str), i);
		i++;
	}
	printf("%lld", ans);
	return 0;
}