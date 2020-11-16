#include<iostream>
#include<cstring>
#include<algorithm>
const long long MAXN = 1000000002;
using namespace std;
typedef long long ll;
int n, m;
ll k;
ll dp_arr[101][101];

//idx=문자열 idx, a 남은 횟수, z 남은 횟수
ll dp(int a, int z) {
	ll& ret = dp_arr[a][z];
	if (a == 0 || z == 0)return ret = 1;
	if (ret != -1)return ret;
	ret = dp(a - 1, z) + dp(a, z - 1);
	ret = min(ret, MAXN);
	return ret;
}
//z를 쓴다는 것은 a를 현재 쓰고 뒤에 오는 모든 경우를 다 포함해도 n번쨰가 더 클 경우
//z를 썼을 때는 n - a에서 다시 연산
void backtrackAns(int a, int z) {
	if (a == -1 || z == -1)return;
	if (a == 0 && z == 0)return;
	ll cnt_a = dp(a - 1, z);
	ll cnt_z = dp(a, z - 1);
	if (cnt_a == k) {
		printf("a"); a--;
		while (z--)printf("z");
		while (a--)printf("a");
		return;
	}
	if (cnt_a<0||cnt_a > k) {
		printf("a");
		backtrackAns(a - 1, z);
	}
	else {
		k -= cnt_a;
		printf("z");
		backtrackAns(a, z - 1);
	}
	return;
}

int main() {
	scanf("%d %d %lld", &n, &m, &k);
	memset(dp_arr, -1, sizeof(dp_arr));
	if (k > dp(n-1,m)+ dp(n,m-1)) {
		printf("-1"); return 0;
	}
	backtrackAns(n, m);
	return 0;
}