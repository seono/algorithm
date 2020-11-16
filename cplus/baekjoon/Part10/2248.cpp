#include<iostream>
#include<cstring>
using namespace std;
int dp[32][32];
char result[32];
int N;
//���� ��Ʈ n ���� 1Ƚ�� m
int bin(int n, int m) {
	int& ret = dp[n][m];
	if (ret != -1)return ret;
	if (m == 0 || n == 0)return ret = 1;

	ret = bin(n - 1, m);
	if (m > 0)ret += bin(n - 1, m - 1);
	return ret;
}
//pivot �̹��� 0���� ä��� �������� �ѱ�� ��찡 1�� ä��� �Ѿ�� ��캸�� ��
//ũ�Ƿ� pivot=bin(n-1,m)
//k�� �տ� ä�����ϴµ� k�� pivot���� ������ �̹��� 0���� ä��� 
//pivot���� ũ�� 1��ä��� k-pivot�� ������ ä��
//
void skip(int n, int m, int k, int p) {
	if (n == 0)return;
	if (m == 0) {
		for (int i = 0; i < n; i++)
			result[p + i] = '0';
		return;
	}
	int pivot = bin(n - 1, m);
	if (k < pivot) {
		result[p] = '0';
		skip(n - 1, m, k, p + 1);
	}
	else {
		result[p] = '1';
		skip(n - 1, m, k-pivot, p + 1);
	}
}


int main() {
	int l, i;
	scanf("%d %d %d", &N, &l, &i);
	memset(dp, -1, sizeof(dp));
	skip(N, l, i-1, 0);
	result[N] = '\0';
	cout << result << endl;
	return 0;
}