#include<iostream>
#include<algorithm>
#include<stack>
#include<cstring>
using namespace std;
typedef long long ll;
int n;
ll k;
ll dp_arr[51][101];

ll pow(int num) {
	ll tmp = 1;
	while (num--)tmp *= 2;
	return tmp;
}

ll dp(int idx, int st) {
	ll &ret = dp_arr[idx][st+50];
	if (idx == n && st == 0)return ret = 0;
	if (idx == n)return ret = 1;
	if (ret != -1)return ret;
	if (st == 0)ret = dp(idx + 1, st + 1) + pow(n - idx - 1);
	else ret = dp(idx + 1, st + 1) + dp(idx + 1, st-1);
	return ret;
}

//(로시작 l 보다크면 )집어넣고 
void backtrackAns(int idx, int st) {
	if (idx == n)return;
	ll l = dp(idx + 1, st + 1);
	if (k<=l) {
		printf("(");
		backtrackAns(idx + 1, st + 1);
	}else{
		printf(")");
		k -= l;
		backtrackAns(idx + 1, st-1);
	}
	return;
}

int main() {
	scanf("%d %lld", &n, &k);
	memset(dp_arr, -1, sizeof(dp_arr));
	backtrackAns(0, 0);
	return 0;
}