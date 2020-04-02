#include<iostream>
#include<cstring>
using namespace std;
typedef long long ll;

ll k;

ll dp_arr[100][2];

//idx자리수, st는 1이 들어올수 있나
ll dp(int idx, bool st) {
	if (idx < 0)return 0;
	ll& ret = dp_arr[idx][st];
	if (idx == 0)return ret = 1;
	if (ret != -1)return ret;
	//st=true->1들어올수있다.
	if (st) {
		return ret = dp(idx - 1, false) + dp(idx - 1, true);
	}
	else {
		return ret = dp(idx - 1, true);
	}
}

void backtrackAns(int idx, bool st) {
	if (idx == 0)return;
	//이전에 0이 들어왔을때
	if (st) {
		//현재 0으로 넣었을때 경우의수
		ll tmp2 = dp(idx - 1, true);
		//k번째가 더 높을때 0넣은 경우 셈했다 하고 idx-1,false로 재귀 
		if (k > tmp2) {
			printf("1");
			k -= tmp2;
			backtrackAns(idx - 1, false);
		}
		//낮거나 같을때 0넣은경우 셈 안하고 idx-1,true로 재귀
		else {
			printf("0");
			backtrackAns(idx - 1, true);
		}
	}
	//1이 들어왔을때
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
	//i자리수
	for (; i < 100; i++) {
		//1로시작하는 i자리 이친수
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