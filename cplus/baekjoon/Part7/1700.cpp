#include<iostream>
#include<vector>
#include<set>
using namespace std;

int main() {
	int N, K;
	int C_size = 0;
	scanf("%d %d", &N, &K);
	vector<int> arr(K);
	//-1�� ���»���
	vector<int> C(K + 1, -1);
	//������ ���� Ƚ��
	int cnt[101] = { 0, };
	for (int i = 0; i < K; i++) {
		scanf("%d", &arr[i]);
		cnt[arr[i]]++;
	}
	int i;
	for (i = 0; C_size < N; i++) {
		cnt[arr[i]]--;
		//�ڸ��� �����ִ°��
		if (C[arr[i]] == -1) {
			C[arr[i]] = cnt[arr[i]];
			C_size++;
		}
		//���� �ִ°��
		else {
			C[arr[i]]--;
		}
	}
	int ans = 0;
	for (; i < K; i++) {
		//���� �ִ°��
		cnt[arr[i]]--;
		if (C[arr[i]] > -1) {
			C[arr[i]]--;//���� Ƚ�� ����
		}
		//�����ϴ� ���
		else {
			bool er = true;
			ans++;
			//���� Ƚ���� 0�̸� �ٷ� ����
			for (int a = 0; a < K; a++) {
				if (C[arr[a]] == 0) {
					er = false;
					C[arr[a]]--;//0���� -1�Ǵϱ� ����
					break;
				}
			}
			//�ƴϸ� ���� ���߿� ��Ÿ���� ������� ����
			if (er) {
				set<int> plug;
				int j;
				for (j = i + 1; plug.size() < N; j++) {
					if (C[arr[j]]>-1 && !plug.count(arr[j])) {
						plug.insert(arr[j]);
					}
				}
				j--;
				C[arr[j]] = -1;//-1�ιٷ� �����ؼ� ����
			}
			C[arr[i]] = cnt[arr[i]];
		}
	}
	printf("%d", ans);
	return 0;
}