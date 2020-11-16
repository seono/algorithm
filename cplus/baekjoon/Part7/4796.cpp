#include<iostream>
using namespace std;

int main() {
	int c = 1;
	while (true) {
		int l, p, v;
		scanf("%d %d %d", &l, &p, &v);
		if (l == 0 && p == 0 && v == 0)break;
		int ans = 0;
		while (v >= p) {
			v -= p;
			ans += l;
		}
		if (v > l)ans += l;
		else ans += v;
		printf("Case %d: %d\n",c++, ans);
	}
}