#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int a[20];

int main() {
	long long w = 0;
	int t, x, y, z, r = 0;
	int i, n, u, v;
	scanf("%d%d%d%d", &x, &y, &z, &n);
	for (i = 0; i < n; i++) {
		scanf("%d%d", &u, &v);
		a[u] += v;
	}
	for (i = 19; i >= 0; i--) {
		w <<= 3; //이미 공간 차지한 부분 갯수 8배 늘리기
		t = min((long long)a[i], (long long)(x >> i)* (y >> i)* (z >> i) - w);
		w += t; // 새롭게 공간 차지한 부분 더해주기
		r += t; // 총갯수
	}
	printf("%d", w == (long long)x * y * z ? r : -1);
	//부피 딱 되면 -1
}
