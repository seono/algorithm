#include<iostream>
#include<algorithm>
#include<stack>
#include<cstring>
using namespace std;
typedef long long ll;
ll k;
ll dp_arr[51][51];

ll pow(int num) {
	ll tmp = 1;
	if (num < 0)return -1;
	while (num--)tmp *= 2;
	return tmp;
}

ll dp(int idx, int st) {
	ll &ret = dp_arr[idx][st];
	if (ret != -1)return ret;
	if (idx == 0 && st == 0)return ret = 0;
	if (idx == 0)return ret = 1;
	if (st == 0)ret = dp(idx - 1, st + 1) + pow(idx - 1);
	else ret = dp(idx - 1, st + 1) + dp(idx - 1, st - 1);
	return ret;
}

//(로시작 l 보다크면 )집어넣고 
void backtrackAns(int idx, int st) {
	if (idx == 0)return;
	ll l = dp(idx - 1, st + 1);
	if (k<=l) {
		printf("(");
		backtrackAns(idx - 1, st + 1);
	}else{
		printf(")");
		k -= l;
		if(st>0)backtrackAns(idx - 1, st - 1);
		else {
			k -= 1;
			ll tmp = pow(idx - 2);
			if (tmp < 0)return;
			while (tmp) {
				if (k >= tmp) {
					k -= tmp; printf(")");
				}
				else printf("(");
				tmp = tmp >> 1;
			}
			return;
		}
	}
	return;
}

int main() {
	int n;
	scanf("%d %lld", &n, &k);
	k++;
	memset(dp_arr, -1, sizeof(dp_arr));
	if (k > dp(n, 0)) {
		printf("-1"); return 0;
	}
	backtrackAns(n, 0);
	return 0;
}