#include<iostream>
#include<cstring>

using namespace std;
string S;
int n;
string A[101];
int work = 0;
void f(int idx) {
	if (idx == S.size()) { work = 1; return ; }
	for (int i = 0; i < n; i++) {
		if (A[i].size() + idx - 1 > S.size())continue;
		if (S.compare(idx, A[i].size(), A[i]) == 0) {
			f(idx + A[i].size());
		}
	}
	return ;
}
int main() {
	cin >> S;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}
	f(0);
	cout << work << endl;
	return 0;
}