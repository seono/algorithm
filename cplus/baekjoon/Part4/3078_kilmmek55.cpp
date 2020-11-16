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

	//�� �̸��� ���̷� �ٲپ� ����
	for (int i = 0; i < n; ++i) {
		cin >> str;

		arr[i] = str.length();
	}
	//k������ cnt�� ī��Ʈ
	for (int i = 0; i < k; ++i)
		cnt[arr[i]]++;
	//���� k��°���� n����
	for (int i = 0; i < n; ++i) {
		if (i + k < n)
			cnt[arr[i + k]]++;
		//k�� üũ->k+i��
		cnt[arr[i]]--;
		//1�� ��ī��Ʈ->i��
		ans += cnt[arr[i]];
		//�� ������ �ջ�
	}

	cout << ans;

	return 0;
}