#include<iostream>

using namespace std;
int arr[101][101] = { 0, };
int main() {
	int result = 0;
	for (int i = 0; i < 4; i++) {
		int x_1, y_1, x_2, y_2;
		cin >> x_1 >> y_1 >> x_2 >> y_2;
		for (int a = y_1; a < y_2; a++) {
			for (int b = x_1; b < x_2; b++) {
				if (arr[a][b]==0) {
					result++;
					arr[a][b]++;
				}
			}
		}
	}
	cout << result;
	return 0;
}