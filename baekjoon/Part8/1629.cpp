#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
int p;
ll pow(int a,int b,int c) {
	if (b == 1)return a;
	ll tmp;
	tmp = pow(a, b / 2, c);
	if (b % 2 == 1) {
		return (tmp * tmp) % c * a % c;
	}
	else {
		return (tmp * tmp)%c;
	}
}

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	ll result = pow(a,b,c)%c;
	cout << result;
	return 0;
}