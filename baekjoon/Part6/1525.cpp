#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<string>
using namespace std;
//3x3배열을 int로 받아 string형태로
//map이용하여 string을저장-> 해당 string count되면 visited

int d[4] = { -3,3,-1,1 };
int main() {
	int n = 0;
	int idx;
	map<string, int>M;
	for (int i = 0; i < 9; i++) {
		int tmp;
		scanf("%d", &tmp);
		if (tmp == 0)idx = i;
		n = n * 10 + tmp;
	}
	queue<string> Q;
	Q.push(to_string(n));
	int ans = -1;
	while (!Q.empty()) {
		ans++;
		int Qsize = Q.size();
		for (int i = 0; i < Qsize; i++) {
			string str = Q.front(); Q.pop();
			if (str == "123456780") {
				cout << ans << endl;
				return 0;
			}
			string st;
			int zero = str.find('0');
			for (int j = 0; j < 4; j++) {
				if (zero % 3 == 2 && j==3)continue;
				if (zero % 3 == 0 && j==2)continue;
				int t = zero + d[j];
				if (t < 0 || t>8)continue;
				st = str;
				swap(st[t], st[zero]);
				if (M.count(st))continue;
				M[st] = 1;
				Q.push(st);
			}
		}
	}
	cout << "-1" << endl;
	return 0;
}