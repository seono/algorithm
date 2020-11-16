#pragma warning(disable:4996)
#include<iostream>
#define eps 0.000000000001
using namespace std;

struct dot {
	double mass;
	double x;
};

int main(int argc, char** argv)
{
	int test_case;
	int T;
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int ball;
		cin >> ball;
		dot* dt;
		dt = (dot*)malloc(sizeof(dot) * ball);
		for (int i = 0; i < ball; i++) {
			cin >> dt[i].x;
		}
		for (int i = 0; i < ball; i++) {
			cin >> dt[i].mass;
		}
		cout << "#" << test_case << " ";
		double x = 0;
		double F = 0;
		double high, low;
		for (int m = 0; m < ball - 1; m++) {
			high = dt[m+1].x;
			low = dt[m].x;
			while (1) {
				x = (high + low) / 2;
				F = 0;
				for (int j = 0; j < ball; j++) {
					if (j <= m) {
						F -= dt[j].mass / (x - dt[j].x) / (x - dt[j].x);
					}
					else {
						F += dt[j].mass / (dt[j].x - x) / (dt[j].x - x);
					}
				}
				if (F < 0) {
					low = x;
				}
				else {
					high = x;
				}
				if (high - low < eps)break;
			}
			if (F > -5 && F < 5) {
				cout.setf(ios::fixed);
				cout.precision(10);
				cout << x << " ";
			}
		}
		cout << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}