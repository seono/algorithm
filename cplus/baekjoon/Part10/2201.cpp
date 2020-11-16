#include<iostream>
#include<cstring>
using namespace std;
typedef long long ll;

ll k;

ll dp_arr[100][2];

//idx�ڸ���, st�� 1�� ���ü� �ֳ�
ll dp(int idx, bool st) {
	if (idx < 0)return 0;
	ll& ret = dp_arr[idx][st];
	if (idx == 0)return ret = 1;
	if (ret != -1)return ret;
	//st=true->1���ü��ִ�.
	if (st) {
		return ret = dp(idx - 1, false) + dp(idx - 1, true);
	}
	else {
		return ret = dp(idx - 1, true);
	}
}

void backtrackAns(int idx, bool st) {
	if (idx == 0)return;
	//������ 0�� ��������
	if (st) {
		//���� 0���� �־����� ����Ǽ�
		ll tmp2 = dp(idx - 1, true);
		//k��°�� �� ������ 0���� ��� ���ߴ� �ϰ� idx-1,false�� ��� 
		if (k > tmp2) {
			printf("1");
			k -= tmp2;
			backtrackAns(idx - 1, false);
		}
		//���ų� ������ 0������� �� ���ϰ� idx-1,true�� ���
		else {
			printf("0");
			backtrackAns(idx - 1, true);
		}
	}
	//1�� ��������
	else {
		printf("0");
		backtrackAns(idx - 1, true);
	}
	return;
}

int main() {
	scanf("%lld", &k);
	int i = 1;
	memset(dp_arr, -1, sizeof(dp_arr));
	ll tmp;
	//i�ڸ���
	for (; i < 100; i++) {
		//1�ν����ϴ� i�ڸ� ��ģ��
		tmp = dp(i-1, false);
		if (k > tmp) {
			k -= tmp;
		}
		else {
			break;
		}
	}
	printf("1");
	backtrackAns(i-1, false);
	return 0;
}