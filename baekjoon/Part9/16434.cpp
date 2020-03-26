#include<iostream>
using namespace std;
#define MAXN 1.2345588e+17+1
typedef long long ll;
struct room {
	bool type=true;
	int atk;
	int HP;
};

int main() {
	int N, H_atk;
	scanf("%d %d", &N, &H_atk);
	room* arr = new room[N];
	for (int i = 0; i < N; i++) {
		room tmp;
		int t;
		scanf("%d %d %d", &t, &tmp.atk, &tmp.HP);
		if (t == 1)tmp.type = false;
		arr[i] = tmp;
	}
	ll h = MAXN;
	ll l = 0;
	while (l + 1 < h) {
		ll mid = (h + l) / 2;
		ll tmp_hp = mid;
		bool die = false;
		ll tmp_atk = H_atk;
		for (int i = 0; i < N; i++) {
			if (!arr[i].type) {
				ll t = (arr[i].HP-1) / tmp_atk;
				if (tmp_hp <= t * arr[i].atk) {
					die = true;
					break;
				}
				tmp_hp -= t * arr[i].atk;
			}
			else {
				tmp_hp = tmp_hp + arr[i].HP >= mid ? mid : tmp_hp + arr[i].HP;
				tmp_atk += arr[i].atk;
			}
		}
		if (die) {
			l = mid;
		}
		else {
			h = mid;
		}
	}
	printf("%lld", h);
	return 0;
}