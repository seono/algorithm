#include<iostream>

using namespace std;
int up_arr[101] = { 0, };
int down_arr[101] = { 0, };
int main() {
	int a;
	cin >> a;
	int up = a, down = 0;
	//up 은 숫자 개수 down 은 배열에 숫자 값
	for (int i = 1; i <= a; i++) {
		int t;
		cin >> t;
		down_arr[i] = t;
		if (up_arr[t] == 0)down++;
		up_arr[t]++;
	}
	//up에 개수가 0인 idx가 있을시 -> down에서 해당 idx부분 제외
	//->제외된 down에 해당하는 숫자 up에서 감소
	while (down < up) {
		down = 0, up = 0;
		for (int i = 1; i <= a; i++) {
			if (up_arr[i] == 0) {
				up_arr[down_arr[i]]--;
				down_arr[i] = 0;
			}
		}
		for (int i = 1; i <= a; i++) {
			if (up_arr[i])down++;
			if (down_arr[i])up++;
		}
	}
	cout << down << endl;
	for (int i = 1; i <= a; i++) {
		if (up_arr[i])cout << i << endl;
	}
	return 0;
}