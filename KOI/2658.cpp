#include <iostream>
#pragma warning(disable:4996)
using namespace std;
struct point {
	int x, y;
};
int arr[11][11];
int main() {
	point* p = new point[10];
	int size = 0;
	freopen("input.txt", "r", stdin);
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			char s;
			cin >> s;
			arr[i][j] = s - 48;
			if (arr[i][j]) {
				arr[10][j]++;
				arr[i][10]++;
				size++;
			}
		}
	}
	int yes = 0;
	for (int i = 0; i < 10; i++) {
		if (arr[10][i] == 1) {
			p[yes].x = i;
			for (int j = 0; j < 10; j++) {
				if (arr[j][i])p[yes++].y = j;
			}
		}
		if (arr[i][10] == 1) {
			p[yes].y = i;
			for (int j = 0; j < 10; j++) {
				if (arr[i][j])p[yes++].x = j;
			}
		}
	}
	int size1 = 0;
	int time = 0;
	if (yes == 3) {
		//수직방향
		if (p[0].x == p[1].x || p[0].x == p[2].x || p[1].x == p[2].x) {
			for (int i = 0; i < 10; i++) {
				if (arr[10][i] == 1) {
					size1 += arr[10][i];
					while (arr[10][i + 1] == arr[10][i] + 2) {
						size1 += arr[10][++i];
						time = 1;
					}
					if (size1 == 1) {
						while (arr[10][i - 1] == arr[10][i] + 2) {
							size1 += arr[10][--i];
							time = 1;
						}
					}
					if (time)break;
				}
			}
		}//수평방향
		else if (p[0].y == p[1].y || p[0].y == p[2].y || p[1].y == p[2].y) {
			for (int i = 0; i < 10; i++) {
				if (arr[i][10] == 1) {
					size1 += arr[i][10];
					while (arr[i + 1][10] == arr[i][10] + 2) {
						size1 += arr[++i][10];
						time = 1;
					}
					if (size1 == 1) {
						while (arr[i - 1][10] == arr[i][10] + 2) {
							size1 += arr[--i][10];
							time = 1;
						}
					}
					if (time)break;
				}
			}
		}
	}
	if (yes == 2) {
		if (arr[10][p[0].x] == 1 && arr[p[0].y][10] == arr[10][p[1].x]) {
			for (int i = 0; i < 10; i++) {
				if (arr[10][i] == 1) {
					size1 += arr[10][i++];
					while (arr[10][i] == arr[10][i-1] + 1) {
						size1 += arr[10][i++];
					}
					time = 1;
				}
				else if(arr[10][i]>1){
					size1 += arr[10][i++];
					while (arr[10][i] == arr[10][i - 1] - 1) {
						size1 += arr[10][i++];
					}
					time = 1;
				}
				if (time)break;
			}
			p[2].y = p[0].y;
			p[2].x = p[1].x;
		}
		else if (arr[10][p[1].x] == 1 && arr[p[1].y][10] == arr[10][p[0].x]) {
			for (int i = 0; i < 10; i++) {
				if (arr[10][i] == 1) {
					size1 += arr[10][i++];
					while (arr[10][i] == arr[10][i - 1] + 1) {
						size1 += arr[10][i++];
					}
					time = 1;
				}
				else if (arr[10][i] > 1) {
					size1 += arr[10][i++];
					while (arr[10][i] == arr[10][i - 1] - 1) {
						size1 += arr[10][i++];
					}
					time = 1;
				}
				if (time) break;
			}
			p[2].y = p[1].y;
			p[2].x = p[0].x;
		}
		else {
			cout << 0 << endl;
			return 0;
		}
		if (arr[p[2].y][p[2].x] == 0&&arr[p[2].x][p[2].y]==0) {
			cout << 0 << endl;
			return 0;
		}
	}
	if (size == size1) {
		int min[3] = { 0,1,2 };
		for (int j = 0; j < 3; j++) {
			int m = j;
			for (int i = m + 1; i < 3; i++) {
				if (p[min[m]].y > p[min[i]].y)m = i;
			}
			int temp = min[m];
			min[m] = min[j];
			min[j] = temp;
		}
		if (p[min[0]].y == p[min[1]].y) {
			if (p[min[0]].x > p[min[1]].x) {
				int temp = min[0];
				min[0] = min[1];
				min[1] = temp;
			}
		}
		else if (p[min[1]].y == p[min[2]].y) {
			if (p[min[1]].x > p[min[2]].x) {
				int temp = min[1];
				min[1] = min[2];
				min[2] = temp;
			}
		}
		for (int i = 0; i < 3; i++) {
			cout << p[min[i]].y + 1 << " " << p[min[i]].x + 1 << endl;
		}
	}
	else {
		cout << 0 << endl;
	}
	return 0;
}