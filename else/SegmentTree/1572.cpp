#include<iostream>
#pragma warning(disable:4996)
#include<vector>
#include<algorithm>
#include<cmath>
//시간 복잡도 O(MN)-> 시간초과
//세그먼트 트리-> O(MlogN)
#define MAXN 66666
using namespace std;

typedef long long ll;


void update(vector<ll>& tree, int node, int start, int end, int index, ll diff) {
	if (!(start <= index && index <= end))
		return;
	tree[node] += diff;
	if (start != end) {
		int mid = (start + end) / 2;
		update(tree, node * 2, start, mid, index, diff);
		update(tree, node * 2 + 1, mid + 1, end, index, diff);
		tree[node] = tree[node * 2] + tree[node * 2 + 1];
	}
}

int finding(vector<ll>& tree, int node, int start, int end, int pos) {
	if (start == end)
		return start;
	else {
		if (pos <= tree[node * 2])return finding(tree, node * 2, start, (start + end) / 2, pos);
		else return finding(tree, node * 2 + 1, (start + end) / 2 + 1, end, pos-tree[node*2]);
	}
}
int main() {
	int N, K;
	ll r = 0;
	scanf("%d %d", &N, &K);
	vector<int> arr1(N+1,0);
	int s = (int)ceil(log2(MAXN+1));
	s = (1 << (s + 1));
	vector<ll> tree(s,0);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &arr1[i]);
		update(tree, 1, 0, MAXN, arr1[i], 1);
		if (i >= K) {
			if (i != K)update(tree, 1, 0, MAXN, arr1[i - K], -1);
			r+=(ll)finding(tree, 1, 0, MAXN, (K+1)/2);
		}
	}
	printf("%lld", r);
	return 0;
}