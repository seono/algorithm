#include<iostream>

using namespace std;
int up_arr[101] = { 0, };
int down_arr[101] = { 0, };
int main() {
	int a;
	cin >> a;
	int up = a, down = 0;
	//up �� ���� ���� down �� �迭�� ���� ��
	for (int i = 1; i <= a; i++) {
		int t;
		cin >> t;
		down_arr[i] = t;
		if (up_arr[t] == 0)down++;
		up_arr[t]++;
	}
	//up�� ������ 0�� idx�� ������ -> down���� �ش� idx�κ� ����
	//->���ܵ� down�� �ش��ϴ� ���� up���� ����
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