#include<iostream>
#include<cstdlib>
using namespace std;
int arr[27][27] = { 0, };
//방문여부
int ar[312];
int result;
void finding(int y, int x, int num) {
	if (arr[y][x] == 1) {
		arr[y][x] = 0;
		result++;
		finding(y + 1, x, num);
		finding(y, x + 1, num);
		finding(y - 1, x, num);
		finding(y, x - 1, num);
	}
	else {
		return;
	}
}
int compare(const void* a, const void* b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 < num2)return -1;
	if (num1 > num2)return 1;
	return 0;
}
int main() {
	int size;
	cin >> size;
	for (int i = 1; i <= size; i++) {
		for (int j = 1; j <= size; j++) {
			char a;
			cin >> a;
			arr[i][j]=(int)a-48;
		}
	}
	int num = 1;
	for (int i = 1; i <= size; i++) {
		for (int j = 1; j <= size; j++) {
			if (arr[i][j] == 1) {
				num++;
				result = 0;
				finding(i, j, num);
				ar[num - 2] = result;
			}
		}
	}
	cout << num-1 << endl;
	qsort(ar, num - 1, sizeof(int), compare);
	for (int i = 0; i < num - 1; i++) {
		cout << ar[i] << endl;
	}
	return 0;
}