#include<iostream>
#include<algorithm>

using namespace std;
#define ffor(i,x)for(int (i)=0;(i)<(x);(i)++)
#define fffor(i,x)for(int (i)=1;(i)<=(x);(i)++)

int arr[3];
int sol(int x) {
	int temp = x;
	ffor(i, 3) {
		x = x % 1000 * 10 + x / 1000;
		if (temp > x)temp = x;
	}
	return temp;
}

int main() {
	int input=0;
	int i;
	cin >> i;
	input += i * 1000;
	cin >> i;
	input += i * 100;
	cin >> i;
	input += i * 10;
	cin >> i;
	input += i;
	input = sol(input);
	int res = 0;
	for (int i = 1111; i <= 9999; i++) {
		if (sol(i) == i)res++;
		if (sol(i) == input) {
			cout << res << endl;
			break;
		}
	}
	return 0;
}