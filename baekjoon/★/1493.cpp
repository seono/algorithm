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
		w <<= 3; //�̹� ���� ������ �κ� ���� 8�� �ø���
		t = min((long long)a[i], (long long)(x >> i)* (y >> i)* (z >> i) - w);
		w += t; // ���Ӱ� ���� ������ �κ� �����ֱ�
		r += t; // �Ѱ���
	}
	printf("%d", w == (long long)x * y * z ? r : -1);
	//���� �� �Ǹ� -1
}
